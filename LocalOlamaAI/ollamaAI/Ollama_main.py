from olama import get_OllamaAnswer
from Recorder import record_audio
from RobotVoice import text_to_speech
from VoiceReconizer import transcribe_audio
import keyboard, wave

print("\nPress RIGHT_SHIFT to start talking with ollamaBot")
while True:
        if keyboard.is_pressed('RIGHT_SHIFT'):
            record_audio()
            transcribedText = transcribe_audio()
            print("You:\n " + transcribedText + "\n")
            break
        if keyboard.is_pressed(" "):
              print("You:\n ")
              transcribedText = input()
              break




print ("Llama:")
get_OllamaAnswer(transcribedText)
#print (ollamaAnswer)
#text_to_speech(ollamaAnswer)