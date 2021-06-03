# জয়-বাংলা-আলাপন 

## Installation and Dependencies

To install RASA in your local machine :
```commandline
pip3 install rasa[full]
```
To start a new project,to go a directory where you want to install RASA and then enter the following command:

```commandline
rasa init
```
( When asked for which directory you want to use . Use simply ```.``` to denote the current directory )

To Train a model:
```commandline
rasa train 
```

To Run the ChatBOT in command shell:
```commandline
rasa shell
```

To Run the ChatBOT under a certain port:
```commandline
rasa run --enable-api -p 5001 --cors "*"
```
This command will run the bot in Port Number 5001.

## Exploroing this repository : Structure

This faq-chatbot-combined Repo has 3 BOT models under the folder **chatbot-main** . They are :
- bangla
- english
- banglish

To run any of these BOT models with pretrained files:
- Copy a trained tarball file in **models** directory created under the BOT folder
- Open the project directory in command prompt 
- Hit `rasa shell` in command prompt 

