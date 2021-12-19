
import os

import openai
import speech_recognition as sr
from gtts import gTTS

h=gTTS(text="how can i help",lang='en',slow=False)
h.save("aud.mp3")
os.system("aud.mp3")







class coco:
    def __init__(self,text):
        self.text=text

    def experiment(self):
        openai.api_key=' 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 '
        
        
        
        response=openai.Completion.create(engine='curie',prompt=self.text,temperature=0.1,max_tokens=90,
        top_p = 0.9,
        frequency_penalty = 0,
        presence_penalty = 0
        )
            
        def output(self):
            print(response.choices[0].text)
    
    def speech_r(self):
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print("speak")
            a_u=r.listen(source)
            t_o=r.recognize_google(a_u)
        try :
            print("you said :{}".format(t_o))
        except:
            print("couldn't hear please try again")
    
    a=speech_r(self=0)

    w=experiment.__init__(output(self=0))

       


    def speech(self,b):
         c=gTTS(text=self.text,lang='en',slow=False)
         c.save("audio.mp3")
         os.system("audio.mp3")


class coco2(coco):
    def __init__(self,text):
        super().__init__(text)

  

    def main(self):
        print(self.speech(self.experiment().self.output(self.speech_r(self.a))))
        print(self.speech(self.experiment(self.speech_r(self.w))))
       

schrodinger_cat1=coco2()
schrodinger_cat1.main()

        
