import random                           
import time
import pyttsx3
import speech_recognition as sr

def SpeakText(command):

    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    engine.say(command)
    engine.runAndWait()

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # The listen() method is then used to record microphone input
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # responce object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # RequestError or UnknownValueError exception is caught, update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5

    # creating recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    word = random.choice(WORDS)

    instructions = (
        "I'm thinking of one of these words:\n"
        "{words}\n"
        "You have {n} tries to guess which one.\n"
    ).format(words=', '.join(WORDS), n=NUM_GUESSES)

    SpeakText("Hi! this is a guess the word game and i am your bot, jett.")
    print(instructions)
    SpeakText(instructions)
    time.sleep(2)                 # waiting 2 seconds bfore starting the game

    for i in range(NUM_GUESSES):
        for j in range(PROMPT_LIMIT):
            print('Guess {}. Speak!'.format(i+1))
            SpeakText("Guess {}. Speak!".format(i+1))
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. What did you say?\n")
            SpeakText("I didn't catch that. What did you say?")

        # if there was an error, stop the game
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            SpeakText("ERROR: {}".format(guess["error"]))
            break

        # showing the transcription
        print("You said: {}".format(guess["transcription"]))
        SpeakText("You said: {}".format(guess["transcription"]))

        # determine if guess is correct and if any attempts remain
        guess_is_correct = guess["transcription"].lower() == word.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        if guess_is_correct:
            print("Correct! You win!".format(word))
            SpeakText("Correct! You win!")
            break
        elif user_has_more_attempts:
            print("Incorrect. Try again.\n")
            SpeakText("Incorrect. Try again.")
        else:
            print("Sorry, you lose!\nI was thinking of '{}'.".format(word))
            SpeakText("Sorry, you lose!\nI was thinking of '{}'.".format(word))
            break