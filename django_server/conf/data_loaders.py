import re


def clean_question(question):
    pattern = r'\(.*?\)'
    question = re.sub(pattern, '', question)
    punctuations = '''[]'''
    cleaned_questions = ""
    for char in question:
        if char not in punctuations:
            cleaned_questions = cleaned_questions + char

    return cleaned_questions


def all_question_dict():
    laguages = ['BN', 'BNL']
    locations = {
        'BN': '../chatbot-main/bangla/data/nlu.yml',
        'BNL': '../chatbot-main/banglish/data/nlu.yml'
    }
    question_dict = dict()
    start = 7

    for language in laguages:
        if language == 'BNL':
            start = 8

        location = locations[language]
        all_question = []
        yml_file = open(location).read()
        intents = yml_file.split('nlu:')[1]
        intents = intents.split('- intent:')[1:]
        for intent in intents[start:]:

            questions = (intent.split('examples: |')[-1]).split('\n')
            for i in range(1, len(questions)):
                if questions[i] != '':
                    try:
                        all_question.append(clean_question((questions[i].split('-')[-1]).strip()))
                    except Exception as e:
                        print(e)
                        pass
        question_dict.update({language: all_question})
    return question_dict
