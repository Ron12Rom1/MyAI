import google.generativeai as genai
import os, pyautogui

api_key = "AIzaSyCeRW0rL4DSa8hjqxc4wK1XssuxMclRhQk"
def getAIResponse(UserIn):
    print ("Thinking...")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(UserIn)
    return (response._result.candidates[0].content.parts[0].text)


def getAIResponseWithImage(UserIn):
    genai.configure(api_key=api_key)
    # Prepare file to upload to GenAI File API
    print ("Looking at youre screen...")

    
    pyautogui.screenshot("screenshot.png")
    file_path = "screenshot.png"
    display_name = "Screenshot"
    file_response = genai.upload_file(path=file_path,
                                display_name=display_name)

    # Verify the file is uploaded to the API
    get_file = genai.get_file(name=file_response.name)

    # Make Gemini 1.5 API LLM call
    prompt = UserIn
    model_name = "models/gemini-1.5-pro-latest"
    model = genai.GenerativeModel(model_name=model_name)
    response = model.generate_content([prompt + """explain in simple terms like youre talking to a friend dont
                                       try to pronouns any wired word and dont use '*' or any other symbols, don't go into too much diteils unless asked to""", file_response])
    return (response._result.candidates[0].content.parts[0].text)

