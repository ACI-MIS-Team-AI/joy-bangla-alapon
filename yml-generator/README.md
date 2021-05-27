# yml generator


To train our chat-bot with new datapoint, we need to create 3 YAML file. They are:

- nlu.yml 
- rules.yml
- domain.yml

The ```generate_yml_files.py``` creates these 3 files as per a list of dictionary intents.

## data input structure

The structure for the list of intent_dictionary is :

```python
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
```

For the synnonyms in **nlu.yml** file we will need to add this list of synonyms in the following format:

```python
synonym_list = [
    {
        "synonym": "Hand",
        "examples": ["syn01", "syn02", "syn03"]
    }
]
```
## generating the yml files

To run the ```generate_yml_files.py``` from command line:

```commandline
python3 generate_yml_files.py 
```

### Probable Todo:

- Need to create the list of dictionaries from a csv file