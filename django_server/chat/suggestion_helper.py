from fuzzywuzzy import fuzz

from django.conf import settings


def check_above(x, ratios):
    for r in ratios:
        if x >= r:
            ratios.remove(r)
            ratios.append(x)
            return ratios, True
    return ratios, False


def sort_score(val):
    return val[1]


def auto_complete(input_text, language='BNL', limit=3):
    ratios = [0, 0, 0]
    result = []
    input_text = input_text.strip()
    questions = settings.Q_DICT[language]
    result_test = []
    for question in questions:
        ratio = fuzz.partial_ratio(question, input_text)
        # ratio = fuzz.token_set_ratio(question, input_text)
        ratios, flag = check_above(ratio, ratios)
        if flag:
            result.append((question, ratio))
            result.sort(key=sort_score, reverse=True)
            if len(result) > limit:
                result = result[0:limit]

    for r, _ in result:
        result_test.append(r)


    return result_test

