import enchant
import re
import requests
from . import config


custom_en_dict = [
    'savlon',
    'aci',
    'handsanitizer',
    'handwash',
    'corona',
    'covid',
    'covid19',
    'coronavirus',
    'handrub',
    'shinex',
    'tfm',
    'mrp',
    'taka',
    'cant',
    'dont',
    'whats',
    'im'
]


def get_rasa_path(in_text):
    option = get_language(in_text)
    if option == 'BNL':
        port = config.RASA_BNL_PORT
    elif option == 'EN':
        port = config.RASA_EN_PORT
    else:
        port = config.RASA_BN_PORT
    path = config.RASA_ROOT + ':' + str(port) + '/webhooks/rest/webhook'
    return path


def clean_text(text):
    custom_punctuation = r"""!"#$%&()*+,-./:;<=>?@[\]^_`{|}~"""
    # single quote needs to be extracted for apostrophe
    translator = re.compile(
        '[%s]' % re.escape(custom_punctuation)
    )
    text = translator.sub(' ', text)
    text = text.lower()
    text = " ".join(text.split())
    return text


def is_banglish(text):
    dict_en = enchant.Dict("en_US")
    words = text.split()
    for word in words:
        if word in custom_en_dict:
            continue
        if not dict_en.check(word):
            return True
    return False


def get_language(text):
    if re.search("^[A-Za-z0-9.,:;!?'()\s]+$", text):
        if is_banglish(text):
            return "BNL"
        else:
            if re.search("^[0-9.,:;!?'()\s]+$", text):
                return "NUM"
            else:
                return "EN"
    else:
        return "BN"


def get_rasa_message(sender, message):
    if get_language(message) == 'NUM':
        return config.ERR_TXT
    path = get_rasa_path(message)
    # print(path)

    data = {
        "sender": sender,
        "message": message
    }
    try:
        response = requests.post(path, json=data)
        # print(response)
        rasa_text = response.json()[0]['text']
    except Exception as e:
        print(str(e))
        rasa_text = config.ERR_TXT
    return rasa_text
