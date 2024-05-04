import speech_recognition as sr

def transcribe_audio():
    recognizer = sr.Recognizer()

    with sr.AudioFile("input.wav") as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


#print (transcribe_audio())