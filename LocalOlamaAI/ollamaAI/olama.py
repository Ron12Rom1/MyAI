from RobotVoice import text_to_speech
import ollama


def get_OllamaAnswer(uerIn):
    textToRead = ''
    ollama.pull("stablelm-zephyr")

    stream = ollama.chat(
        model = "stablelm-zephyr",
        messages=[{
            "role": "user",
            "content": uerIn
        }],
        #stream=True
    )

    ## This is to print all in once (you also need to comment the stream in line 15)
    #print (" " + stream['message']['content'])
    print (' ', end = '')
    for message in stream:
        print (message['message']['content'])
    #     #textToRead += (message['message']['content'])
    #     #text_to_speech(message['message']['content'])

get_OllamaAnswer("say 5 words")