import os
from django.db.models import Q
from django.core.management.base import BaseCommand, CommandError

from nlu_data.models import Intent, SubIntent, Question, Response

PATH_BN = "../chatbot-main/bangla/data-new/"
PATH_EN = "../chatbot-main/english/data-new/"
PATH_BNL = "../chatbot-main/banglish/data-new/"


def create_domain_yml(responses, intents, path):
    full_path = os.path.join(path, "domain.yml")
    with open(full_path, 'w+') as domain_file:
        domain_file.write("version: \"2.0\"\n\n")
        domain_file.write("intents:\n")
        for intent in intents:
            domain_file.write("\t- " + intent + "\n")
        domain_file.write("\nresponses:\n")
        for train_sample in responses:
            line_text = "\tutter_" + train_sample["intent"]
            if len(train_sample["sub_intent"]):
                line_text += "/" + train_sample["sub_intent"]
            line_text += ":\n"
            domain_file.write(line_text)
            domain_file.write("\t- text: " + train_sample["response"] + "\n\n")


def create_nlu_yml(response_list, path):
    full_path = os.path.join(path, "nlu.yml")
    with open(full_path, 'w+') as nlu_file:
        nlu_file.write("version: \"2.0\"\n\n")
        nlu_file.write("nlu:\n")
        for train_sample in response_list:
            intent_text = "- intent: " + train_sample["intent"]
            if len(train_sample["sub_intent"]):
                intent_text += "/" + train_sample["sub_intent"]
            intent_text += "\n"
            nlu_file.write(intent_text)
            nlu_file.write("\texamples: |\n")
            for each_example in train_sample["examples"]:
                nlu_file.write("\t- " + each_example + "\n")
            nlu_file.write("\n")


# - rule: respond to FAQs
#   steps:
#   - intent: chitchat
#   - action: utter_chitchat
def create_rule_yml(intent_list, path):
    full_path = os.path.join(path, "rules.yml")
    with open(full_path, 'w+') as rules_file:
        rules_file.write("version: \"2.0\"\n\n")
        for intent in intent_list:
            rules_file.write(
                "- rule: respond to" + intent + "\n"
                "\tsteps:\n"
            )
            rules_file.write(
                "\t- intent: " + intent + "\n" +
                "\t- action: utter_" + intent + "\n\n"
            )


def get_text(obj, lang='en'):
    if lang == 'en':
        return getattr(obj, 'text_en', "")
    if lang == 'bn':
        return getattr(obj, 'text_bn', "")
    return getattr(obj, 'text_bnl', "")


def get_data_dict(lang='en'):
    intent_objs = Intent.objects.all()

    intents = []
    for obj in intent_objs:
        intents.append(obj.name)

    response_objs = Response.objects.all().select_related(
        'intent', 'sub_intent'
    )
    responses = []
    for resp_obj in response_objs:
        cur_dict = {
            "intent": resp_obj.intent.name if resp_obj.intent else "",
            "sub_intent": resp_obj.sub_intent.name if resp_obj.sub_intent else "",
            "response": resp_obj.text_bn,
            "examples": []
        }
        # print(resp_obj.text_en)
        samples = Question.objects.filter(response=resp_obj.id)
        for sample in samples:
            text = get_text(sample, lang)
            if len(text):
                cur_dict["examples"].append(text)
        responses.append(cur_dict)

    return responses, intents


def create_nlu_files(self, lang='en'):
    nlu_data_path = PATH_EN
    if lang == 'bn':
        nlu_data_path = PATH_BN
    if lang == 'bnl':
        nlu_data_path = PATH_BNL

    responses, intents = get_data_dict(lang)
    print(responses)
    create_nlu_yml(response_list=responses, path=nlu_data_path)
    create_rule_yml(intent_list=intents, path=nlu_data_path)
    create_domain_yml(responses=responses, intents=intents, path=nlu_data_path)


class Command(BaseCommand):
    help = 'Add Relief Report district'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('lang', nargs='+', type=str)

        # Named (optional) arguments
        parser.add_argument(
            '--lang',
            action='store_true',
            help='Get Language option',
        )

    def handle(self, *args, **options):
        lang = 'en'
        if options['lang']:
            lang = options['lang'][0]
        print("Lang: ", lang)
        create_nlu_files(self, lang)
        msg = 'Successfully Created nlu file....'
        # task_logger.info(msg)
        self.stdout.write(self.style.SUCCESS(msg))
