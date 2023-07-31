from whisper import transcribe_mic_input
from LLM import get_user_actions
import asyncio
import ast 
from functions.run_app import open_program
from elevenlabs import play, generate, set_api_key
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


while True:
    command = transcribe_mic_input()
    try:
        resp = asyncio.run(get_user_actions(command))
        resp = resp.replace("))", ")")
        if resp[-1] != "]":
            resp+="]"
        print(resp)
        resp = ast.literal_eval(resp)
        print(resp)
        for tup in resp:
            print(f"tup[0] {tup[0]}")
            print(f"tup[1] {tup[1]}")
            if tup[0] == "RUN_APP":
                open_program(tup[1])
            elif tup[0] == "SPEAK":
                say(tup[1])
            elif tup[0] == "ERROR":
                say("Sorry, I couldn't get that.")
                print("ERROR")
            else:
                say("Sorry, I can't do that yet.")
                print('Unsupported')
    except:
        say("Sorry, I couldn't get that")