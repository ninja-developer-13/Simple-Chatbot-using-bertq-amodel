import speech_recognition as sr
from gtts import gTTS
import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import torch
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer
from transformers import pipeline

class TalkBot:
    LANGUAGE_EN = 'en'
    question = None
    def speechToText(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Devotee, Please tell us your problem: ")
            audio_text = r.listen(source)
            print("Loading ...") 
            try:
                self.question = r.recognize_google(audio_text)
                #self.textToSpeech()
                self.getAnswer()
                # using google speech recognition
                #print("Text: "+r.recognize_google(audio_text))
            except:
                 print("Sorry, I did not get that")
    def textToSpeech(self):
        myobj = gTTS(text=self.question, lang=self.LANGUAGE_EN, slow=False) 
        myobj.save("temp_audio.mp3") 
        os.system("mpg321 temp_audio.mp3") 
    def getAnswer(self):
        try:
            data = pd.read_csv("sai_baba_question_answer.csv")
            #data.head(500)
            #print(data)
            random_num = np.random.randint(0,len(data))
            question = data["question"][random_num]
            text = data["text"][random_num]
        
            question_answerer = pipeline("question-answering", model='distilbert-base-cased-distilled-squad')

            context = data["answer"][random_num]
            result = question_answerer(question=self.question,     context=context)
            
            answer = result['answer']
            print(answer)
        except Exception as e:
            print(e.message)

talkBot = TalkBot()
talkBot.speechToText()
#talkBot.textToSpeech()