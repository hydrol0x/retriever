"""
File where we will prompt LLM to get user intent and return the fns
"""
import asyncio
from palm import handle_chat

# Give PaLM the users command -> PaLM decides on a list of actions to run 

# ! this might just be too hard for LLM!
async def get_program_name(name: str, program_list: list) -> str:
    prompt=f"""
Here are a list of programs on the user's computer. 
{program_list}


Return the program name from the list above that most closely matches {name}
"""

    print(prompt)
    resp = await handle_chat(prompt)
    resp = resp["response"]
    return resp

from prompts import user_command_intent_prompt
async def get_user_actions(user_command:str) -> list:
    prompt=f"""
    {user_command_intent_prompt}
User: {user_command}
PaLM:
    """
    print(prompt)
    resp = await handle_chat(prompt)
    resp = resp["response"]
    return resp


if __name__ == "__main__":
    user_command = "Open firefox"
    resp = asyncio.run(get_user_actions(user_command))
    print(resp)