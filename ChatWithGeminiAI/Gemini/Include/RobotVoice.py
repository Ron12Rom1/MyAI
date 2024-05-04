import pyttsx3

def text_to_speech(text, voice_id=None, rate=None):
    engine = pyttsx3.init()

    # Changing voice
    if voice_id:
        voices = engine.getProperty('voices')
        if voice_id < len(voices):
            engine.setProperty('voice', voices[voice_id].id)
        else:
            print("Invalid voice ID. Using default voice.")

    # Changing speed
    if rate:
        engine.setProperty('rate', rate)  # Speed rate adjustment

    engine.say(text)
    engine.runAndWait()


text = "שלום"
voice_id = 1  # Change this number to select different voices
rate = 200  # Adjust this number for different speed rates
text_to_speech(text, voice_id, rate)
