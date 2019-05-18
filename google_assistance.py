import wolframalpha
import wikipedia
from pygame import *
from tkinter import *
from gtts import gTTS

def wolf():
    question = input("enter your question : ")
    app_id = "AXT46A-T3GXG98W9R"

    client = wolframalpha.Client(app_id) 

    res = client.query(question)
    answer = next(res.results).text
    print(answer)

def wiki():
    while True:
        question = input("question: ")
        wikipedia.set_lang("es") #es spanish, en = english, zh= chinese
        print(wikipedia.summary(question, sentences = 3))

def mix():
    while True:
        print("\n\t\tWELCOME TO THE GOOGLE ASSISTANT")
        lang = int(input("\n Select language \n1.english\n2.spanish\n3.chinese\n  "))
        question = input("\nHello! how can I help you?\n")

    


        try:
            #wolframalpha
            app_id = "AXT46A-T3GXG98W9R"

            client = wolframalpha.Client(app_id) 

            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            
        except:
            #wikipedia 
            if lang ==1:
                wikipedia.set_lang("en")
            elif lang == 2:
                wikipedia.set_lang("es")
            else:
                wikipedia.set_lang("zh")
            
            print(wikipedia.summary(question))
            
mix()
