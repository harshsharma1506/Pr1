import openai
from gtts import gTTS
import os
import subprocess as sp

h=gTTS(text="how can i help",lang='en',slow=False)
h.save("aud.mp3")
os.system("aud.mp3")

a=input("how can i help you")
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
        output=sp.getoutput(self.experiment)
        return self.speech(output)

    def main(self):
        print(self.speech(self.experiment(a)))
        return self.answer()

schrodinger_cat1=coco2(a)
schrodinger_cat1.main()

        
