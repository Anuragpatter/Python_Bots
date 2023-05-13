import speech_recognition as sr
from gtts import gTTS                            
from playsound import playsound
r = sr.Recognizer()
language = 'en'
with sr.Microphone() as source:
    obj2 = gTTS(text='Welcome! I am Rebecca, a chat bot. Please tell me whats your name',lang=language,slow=False)
    obj2.save("welcome.mp3")
    print('User name:')
    playsound("welcome.mp3")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    get = r.recognize_google(audio)
    print(get)
except:
    print("error")
get = r.recognize_google(audio)
obj = gTTS(text="Hi"+get,lang=language,slow=False)

obj.save("hi_user.mp3")

playsound("hi_user.mp3")