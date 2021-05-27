input_format = [
    {
        "intent": "intent01",
        "response": "response01",
        "examples": ["que01", "que02", "que03"]
    },
    {
        "intent": "intent02",
        "response": "response02",
        "examples": ["que01", "que02", "que03"]
    }
]

synonyms = [
    {
        "synonym": "Hand",
        "examples": ["syn01", "syn02", "syn03"]
    }
]

# version: "2.0"
#
# intents:
#   - greet
#   - query
#
# responses:
#   utter_greet:
#   - text: "Hey! How are you?"
#
#   utter_query:
#   - text: "I am fine"
def create_domain_yml(intent_list):
    with open("domain.yml", 'w+') as domain_file:
        domain_file.write("version: \"2.0\"\n")
        # intents:
        domain_file.write("intents:\n")
        for train_sample in intent_list:
            domain_file.write("  - " + train_sample["intent"] + "\n")
        # responses:
        domain_file.write("\nresponses:\n")
        for train_sample in intent_list:
            domain_file.write("  utter_" + train_sample["intent"] + ":\n")
            domain_file.write("  - text: " + train_sample["response"] + "\n\n")
        domain_file.write("session_config:\n")
        domain_file.write("  session_expiration_time: 60\n")
        domain_file.write("  carry_over_slots_to_new_session: true")


# nlu:
# - intent: greet
#   examples: |
#     - Hi
#     - Hello
#     - Hey
#
# - intent: query
#   examples: |
#     - How are you
#     - How was Your Day
#     - How you doing
# - synonym: Slippery
#   examples: |
#     - picchil
#     - pisla

def create_nlu_yml(intent_list,synonym_list):
    with open("nlu.yml", 'w+') as nlu_file:
        nlu_file.write("version: \"2.0\"\n\n")
        # nlu:
        # intents:
        nlu_file.write("nlu:\n")
        for train_sample in intent_list:
            nlu_file.write("- intent: " + train_sample["intent"] + "\n")
            nlu_file.write("  examples: |\n")
            for each_example in train_sample["examples"]:
                nlu_file.write("    - " + each_example + "\n")
            nlu_file.write("\n")
        # synnonyms:
    with open("nlu.yml", 'a+') as nlu_file:
        for train_sample in synonym_list:
            nlu_file.write("- synonym: " + train_sample["synonym"] + "\n")
            nlu_file.write("  examples: |\n")
            for each_example in train_sample["examples"]:
                nlu_file.write("    - " + each_example + "\n")
            nlu_file.write("\n")


# - rule: respond to FAQs
#   steps:
#   - intent: chitchat
#   - action: utter_chitchat
def create_rules_yml(intent_list):
    with open("rules.yml", 'w+') as rules_file:
        rules_file.write("version: \"2.0\"\n\n")
        rules_file.write("rules: \"2.0\"\n\n")
        for train_sample in intent_list:
            rules_file.write("- rule: respond to FAQs\n"
                             "  steps:\n")
            rules_file.write("  - intent: " + train_sample["intent"] + "\n" +
                             "  - action: utter_" + train_sample["intent"] + "\n\n")


create_domain_yml(input_format)
create_rules_yml(input_format)
create_nlu_yml(input_format,synonyms)
