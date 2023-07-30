from whisper import transcribe_mic_input
from LLM import get_user_actions
import asyncio

command = transcribe_mic_input()
resp = asyncio.run(get_user_actions(command))
print(resp)