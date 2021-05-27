import re
import string
import enchant
import json

def generate_dictionary(file_name):
    re_punc = re.compile('[%s]' % re.escape(string.punctuation+"।"))
    dict_en = enchant.Dict("en_US")
    all_words = []
    yml_file = open(file_name).read()
    intents = yml_file.split('nlu:')[1].split('- intent:')[1:]
    for intent in intents:
        intent = (intent.split('examples: |')[1]).split('\n')
        for i in range(1,len(intent)):
            if (intent[i]!=''):
                try:
                    line = intent[i].split('-')[1].strip()
                    words = line.split(' ')
                    for word in words:
                        word = re_punc.sub('', word)
                        if (word != ''):
                            if (dict_en.check(word) == False):
                                all_words.append(word)
                except:
                    pass
    dictionary = list(set(all_words))
    return dictionary

def main():
    dictionary = generate_dictionary("nlu.yml")
    json_object = json.dumps(dictionary, ensure_ascii=False)
    with open("data/dictionary.json", "w",encoding="utf-8") as outfile:
        outfile.write(json_object)

if __name__ == "__main__":
    main()