from whisper import transcribe_mic_input
from LLM import get_user_actions
import asyncio
import ast 
from functions.run_app import open_program
from elevenlabs import play, generate, set_api_key
from browser import run_web_search
from send_email import open_mail_app_with_start_menu
from notepad import open_notepad_and_type
from settings import open_settings
import os

from dotenv import load_dotenv
load_dotenv()

set_api_key(os.getenv("ELEVENLABS_API_KEY"))

def say(message:str) -> None:
    audio = generate(
    text=message,
    voice="Bella",
    model="eleven_monolingual_v1"
    )

    play(audio, use_ffmpeg=False)


say("Hello! I am Retriever, your digital guide dog. What would you like to do?")
run=True 
while run:
    command = transcribe_mic_input()
    try:
        resp = asyncio.run(get_user_actions(command))
        resp = resp.replace("))", ")")
        if resp[-1] != "]":
            resp+="]"
        if resp[0] != "[":
            resp = "[" + resp
        print(resp)
        resp = ast.literal_eval(resp)
        print(resp)
        for tup in resp:
            print(f"tup[0] {tup[0]}")
            print(f"tup[1] {tup[1]}")
            if tup[0] == "RUN_APP":
                say(f"I'm opening {tup[1]}")
                open_program(tup[1])
            elif tup[0] == "SPEAK":
                say(tup[1])
            elif tup[0] == "SEARCH_WEB":
                say("Searching the web")
                result = run_web_search(tup[1])
                say(result)
            elif tup[0] == "SEND_EMAIL":
                say("Sending an email")
                open_mail_app_with_start_menu(subject=tup[1], recipient=tup[2], body=tup[3])
            elif tup[0] == "NOTE":
                say("I've written that down")
                open_notepad_and_type(tup[1]) 
            elif tup[0] == "OPEN_SETTING":
                say(f"Opening the setting {tup[1]}")
                open_settings(tup[1])
            elif tup[0] == "SHUTDOWN":
                say("Goodbye.")
                run=False
            elif tup[0] == "ERROR":
                say("Sorry, I couldn't get that.")
                print("ERROR")
            else:
                say("Sorry, I can't do that yet.")
                print('Unsupported')
    except:
        say("Sorry, something went wrong.")