import speech_recognition as sr       # Working
from gtts import gTTS
from playsound import playsound
import webbrowser as wb

r = sr.Recognizer()
language = 'en'
obj1 = gTTS(text='Hello! I am your personal search bot. Please tell me what do you want to Search',lang=language,slow=False)
obj1.save("search1.mp3")
print('What do you want to search: ')    
playsound("search1.mp3")

with sr.Microphone() as source:
    print("calibrating background noise")
    r.adjust_for_ambient_noise(source)
    print("Now speak...")
    audio = r.listen(source)
    
try:
    get = r.recognize_google(audio)
    print(get)
    url = 'https://www.google.com/search?q='
    wb.get().open_new(url+get)
except:
    print('error')
get = r.recognize_google(audio)
obj2 = gTTS(text="Result is being displayed for the searched keyword"+get,lang=language,slow=False)

obj2.save("Vvoice.mp3")

playsound("Vvoice.mp3")