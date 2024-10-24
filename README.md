# TalkBot: An Interactive Voice-Based Question Answering System
TalkBot is a Python-based application that enables users to interact with a voice-activated question-and-answer system. 
It utilizes speech recognition to convert spoken queries into text and then employs a pre-trained BERT model to provide answers based on a dataset of questions and answers.

## Features

#### Speech Recognition: 
It converts spoken questions into text using Google Speech Recognition.
#### Question Answering: 
It utilizes a BERT model to understand context and provide relevant answers.
#### Text-to-Speech: **(Its in progress)**
It converts the response back into audio, allowing for a seamless interactive experience.

**Requirements**

Python 3.x
Libraries: speech_recognition, gtts, pandas, numpy, matplotlib, seaborn, torch, transformers
Additional software: mpg321 for audio playback (Linux users)

## Installation

#### Clone the repository:
git clone [<repository-url>](https://github.com/ninja-developer-13/Simple-Chatbot-using-bertq-amodel/)
cd Simple-Chatbot-using-bertq-amodel

Install the required libraries:
pip install -r requirements.txt

## Usage
Prepare a CSV file named sai_baba_question_answer.csv containing columns for "question", "text", and "answer".
**Run the TalkBot:**
python index.py

Follow the prompts to ask your questions.

#### How It Works

1.The user is prompted to speak their question.
2.The application captures the audio and converts it to text.
3.A random question-answer pair is selected from the CSV file, and the BERT model processes the user's question against the selected context.
4.The answer is then printed and can optionally be converted to speech.

**Contributions**
**Contributions are welcome! Please fork the repository and submit a pull request with your changes.**

**License**
This project is licensed under the MIT License.

## Sample Response from TalkBot:

(base) PrabakaranP@ bertq-amodel-main % python index.py
Devotee, Please tell us your problem: 

Loading ...
Sai baba: dear one

(base) PrabakaranP@ bertq-amodel-main % python index.py
Devotee, Please tell us your problem: 
Loading ...
Sai baba: love and determination

(base) PrabakaranP@ bertq-amodel-main % python index.py
Devotee, Please tell us your problem: 
Loading ...
Sai baba: My dear one, in the midst of property disputes

(base) PrabakaranP@ bertq-amodel-main % python index.py
Devotee, Please tell us your problem: 
Loading ...
Sai baba: My child

(base) PrabakaranP@ bertq-amodel-main % python index.py
Devotee, Please tell us your problem: 
Loading ...
Sai baba: My dear devotee, your health is a precious gift from the Divine

