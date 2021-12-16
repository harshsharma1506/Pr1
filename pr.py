import openai
import speech_recognition as sr 
from gtts import gTTS
import os
import speech_recognition as sr
import subprocess as sp



    
h=gTTS(text="how can i help",lang='en',slow=False)
h.save("aud.mp3")
os.system("aud.mp3")



r= sr.Recognizer()
with sr.Microphone() as source:
    a_u=r.listen(source)
    t_o=r.recognize_google(a_u)
    try :
        m= print("you said :{}".format(t_o))
    except:
        print("couldn't hear please try again")

a=m

class coco:
    def __init__(self,text):
        self.text=text

    def experiment(self,text):
        openai.api_key=' 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 '
        global response
        
        def response(self):
            response=openai.Completion.create(engine='curie',prompt=self.text,temperature=0.1,max_tokens=90,
                                        top_p = 0,
                                        frequency_penalty = 0,
                                        presence_penalty = 0
            )
            e=response.choices[0].text
            print(response.choices[0].text)


    def speech(self,b):
         c=gTTS(text=self.text,lang='en',slow=False)
         c.save("audio.mp3")
         os.system("audio.mp3")


class coco2(coco):
    def __init__(self,text):
        super().__init__(text)

    def answer(self):
        output=sp.getoutput(self.experiment(e))
        return self.speech(output)

    def main(self):
        print(self.speech(self.experiment(a)))
        return self.answer()

schrodinger_cat1=coco2(a)
schrodinger_cat1.main()

        
