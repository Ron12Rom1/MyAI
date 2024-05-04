from RobotVoice import text_to_speech
import ollama

def get_OllamaAnswer(uerIn):
    ollama.pull("llama3")

    stream = ollama.chat(
        model = "llama3",
        messages=[{
            "role": "user",
            "content": uerIn
        }],
        stream=True
    )

    print (' ', end = '')
    for message in stream:
        print (message['message']['content'], end = '')
        text_to_speech(message['message']['content'])