
#Make Sure that the default audio/media player is Windows Media Player ( the old one ) 

#I wrote this little script that plays(myText) in Text To Speech whenever a random time interval has passed
#Reasoning: at our school we have an unwritten rule; "If you forget to lock your PC before exiting the classroom, studens and teachers can, and will mess with your PC".

from gtts import gTTS
import os
import subprocess
from time import sleep
from random import randint

myText = "æ-æ-æ-æ-æ-æ-ææ ææ æ--æ You Forgot Windows L" #Be-E-e-e-eE-Ee-e-ee-E-eI-'
language = "no"
output = gTTS(text=myText, lang=language, slow=False)

while True:
    N = randint(0,44)
    print(N)
    output.save("e.mp3")
    os.system("start e.mp3")
    sleep(5)
    subprocess.call(["taskkill", "/F", "/IM", "wmplayer.exe"])
    sleep(N)
