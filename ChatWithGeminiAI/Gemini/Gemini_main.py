from Include.Recorder import record_audio
from Include.RobotVoice import text_to_speech
from Include.VoiceReconizer import transcribe_audio
from Include.GoogleAIRespons import getAIResponse, getAIResponseWithImage
import keyboard, pyautogui, os

transcribedText = []
while not("goodbye" in transcribedText or "see you later" in transcribedText):
    # Record audio
    print("\nPress RIGHT_SHIFT to start recording")
    while True:
        if keyboard.is_pressed('RIGHT_SHIFT'):
            record_audio()
            break


    # Transcribe audio
    transcribedText = transcribe_audio()
    os.remove("input.wav")
    print ("\nQ: \n" + transcribedText)
    
    # Get AI response
    if "screen" in transcribedText: 
        AIResponse = getAIResponseWithImage(transcribedText)
        os.remove("screenshot.png")
    elif "```" in transcribedText:
        AIResponse = getAIResponse(transcribedText + ", explain to me in words or provide links to online resources")
    else: 
        AIResponse = getAIResponse(transcribedText + ", don't use '*' or other spacial characters")
        

    # Text to speech
    voice_id = 1  # Change this number to select different voices
    rate = 200 # Adjust this number for different speed rates
    print ("\nA: \n" + AIResponse)
    text_to_speech(AIResponse, voice_id, rate)
    print ("\n")
