import time
from selenium import webdriver
import speech_recognition as sr
import pyttsx3

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except Exception as e:
        print("Sorry, I couldn't understand. Please try again.")
        return ""

def send_prompt_to_chatGPT(prompt):
    driver = webdriver.Chrome()  # Path to your ChromeDriver
    driver.get("https://chatgpt.com/c/97297fbb-b76a-4010-86cd-006e06202337")  # URL of your ChatGPT prompt bar
    prompt_input = driver.find_element_by_css_selector('textarea[data-message-author-role="user"]')
    prompt_input.send_keys(prompt)
    time.sleep(2)  # Adjust delay as needed for ChatGPT to generate response
    response_element = driver.find_element_by_css_selector('div[data-message-author-role="assistant"]')
    response = response_element.text.strip()
    driver.quit()
    return response

def convert_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        user_input = get_voice_input()
        if user_input:
            chatGPT_response = send_prompt_to_chatGPT(user_input)
            print("ChatGPT Response:", chatGPT_response)
            convert_to_speech(chatGPT_response)
