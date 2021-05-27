import enchant
import string
import re
import sys
from profanity import profanity
import json

def check_presence_in_dict(chat, dictionary):
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    chat_words = chat.split(' ')
    for cw in chat_words:
        cw = re_punc.sub('', cw)
        dict = enchant.Dict("en_US")

        if (cw in dictionary) or dict.check(cw):
            continue
        else:
            return False
    return True

def check_banglish(text):
    dict_en = enchant.Dict("en_US")
    translator = re.compile(
        '[%s]' % re.escape(string.punctuation)
    )
    text = translator.sub(' ', text)
    words = text.split()
    for word in words:
        if not dict_en.check(word):
            return True
    return False

def detect_language(s):
    if re.search('^[A-Za-z0-9.,:;!?()\s]+$', s):
        if (check_banglish(s)):
            return "BANGLISH"
        else:
            if re.search('^[0-9.,:;!?()\s]+$', s):
                return "Number"
            else:
                return "ENGLISH"
    else:
        return "BANGLA"

def parse_and_detect_lang(text, bangla_dictionary, banglish_dictionary):
    words = text.split()
    prev_class = ""
    word_no = 0
    for word in words:
        current_class = detect_language(word)
        if current_class == "Number":
            return "Sorry i can't understand your question. Can you please rephrase it?"
        if current_class == "BANGLISH" or prev_class == "BANGLISH":
            if check_presence_in_dict(text.lower(), banglish_dictionary):
                return "BANGLISH"
            else:
                return "Sorry i can't understand your question. Can you please rephrase it?"
        if word_no > 0:
            if (current_class == "BANGLA" or prev_class == "BANGLA") and prev_class != current_class:
                return "Please use either Bangla or English"
        prev_class = current_class
        word_no = word_no + 1
    if current_class == "ENGLISH":
        if profanity.contains_profanity(text) == False:
            pass
        else:
            return "Please don't use profane words"
    if current_class == "BANGLA":
        if check_presence_in_dict(text.lower(), bangla_dictionary):
            pass
        else:
            return "Sorry i can't understand your question. Can you please rephrase it?"
    return current_class

def main(chat):
    f = open('data/banglish_dictionary.json')
    banglish_dictionary = json.load(f)
    f = open('data/bangla_dictionary.json')
    bangla_dictionary = json.load(f)
    resp = parse_and_detect_lang(chat, bangla_dictionary, banglish_dictionary)
    print(resp)

if __name__ == "__main__":
    main(sys.argv[1])