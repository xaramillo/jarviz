import openai
import speech_recognition as sr
import pyttsx3
import keyboard
from dotenv import load_dotenv
import os

# OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# TTS Init
engine = pyttsx3.init()

# Additional function to convert text to speech
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

# Capture speech until a space keyboard is pressed and then starts to launch the openAI request
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening... press space key to stop.")
        audio_data = []
        try:
            while True:
                if keyboard.is_pressed(" "):  # Stops at being pressed " "
                    print("Recording stopped.")
                    break
                audio = recognizer.listen(source, timeout=1, phrase_time_limit=5)
                audio_data.append(audio)
        except sr.WaitTimeoutError:
            print("Waiting audio input convertion...")
        except sr.UnknownValueError:
            print("Sorry, what was you trying to say? Please repeat me.")
            return None

        # Process captured audio
        try:
            print("Processing audio...")
            full_audio = sr.AudioData(
                b"".join(a.get_raw_data() for a in audio_data),
                source.SAMPLE_RATE,
                source.SAMPLE_WIDTH,
            )
            text = recognizer.recognize_google(full_audio, language="en-US")
            print(f"Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Oops, try again.")
            return None

# Querying the text to Open AI turbo model
def ask_openai(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        answer = response["choices"][0]["message"]["content"]
        return answer
    except Exception as e:
        print(f"Error connecting to OpenAI: {e}")
        return "I'm sorry, there is something wrong with OpenAI connection."

# Programa principal
def main():
    print("Press SPACE key to init/stop hearing. Press 'q' to exit the program.")
    while True:
        # Exit routine
        if keyboard.is_pressed("q"):
            print("Bye!")
            break

        # Capture voice and convert to text
        question = speech_to_text()
        if question:
            # Send question to OpenAI an get the answer
            answer = ask_openai(question)
            print(f"OpenAI: {answer}")
            # Read the answer
            text_to_speech(answer)


if __name__ == "__main__":
    main()