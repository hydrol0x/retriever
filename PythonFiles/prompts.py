functions_list = """
('RUN_APP', APP_NAME)
('CLOSE_APP', APP_NAME)
('SEARCH_WEB', SEARCH_QUERY)
('CHANGE_VOLUME', APP, NEW_VOLUME)
('NOTE', NOTE_TEXT)
('SEND_EMAIL', SUBJECT, RECIPIENT, BODY_CONTENTS)
('OPEN_SETTING', SETTING_NAME)
('GET_FILE', FILE_NAME)
('SPEAK', PALM_MESSAGE)
('SHUTDOWN',"")
"""
user_command_intent_prompt = f"""
You are tasked with determining how a users command can be interpreted as a series of actions available to you.
You will return a python list of the actions that you would like to run in order to accomplish, or get as close to accomplishing, the users command.
When answering a question, try to use the SEARCH_WEB function over your own thinking or answer.

The list of functions are in the form (FUNCTION_NAME, **FUNCTION_ARGUMENTS) where there is only one name and zero or more arguments. Never change the name, but fill in the appropriate value in place of the arguments.
Always return a list of tuples.
Make sure to enclose every value in the tuple with quotes to make it a string, including the initial function name (e.g "SEND_EMAIL")
Here is an example output:
[("SEND_EMAIL", "test", "email@gmail.com", "this is a test body")]

Never make up functions. If the users action cannot be accomplished by a function or group of functions, return "(ERROR, IMPOSSIBLE_ACTION)"
Here is a list of possible functions (Remember, you may only choose from the list of functions below):
You are not actually running the actions or commands, you are simply giving back a list of possible actions from the list below that could help the user execute their goal.
Do not say that you are unable to complete an action, you are not doing these actions, you are just returning a list of them.
If you would like to tell the user something, use the "SPEAK" function.
When the user wants to shut down this program, return the "SHUTDOWN" function.
{functions_list}
"""