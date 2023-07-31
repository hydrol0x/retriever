import os
from pathlib import Path
import pickle
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# App cache
app_cache = {}
# A dictionary of all installed program names and their paths.
programs = {}

def unpack_pickle_file(filename):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except pickle.UnpicklingError as e:
        print(f"Error while unpickling '{filename}': {e}")
        return None


def update_programs_list(programs_file):
    # Index PATH.
    for path in os.environ["PATH"].split(os.pathsep):
        if os.access(os.path.join(path, '.exe'), os.X_OK):
            programs[os.path.basename(path)] = path

    # Index Start Menu.
    start_menu_dir = "C:\\Users\\" + os.getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"
    for root, dirs, files in os.walk(start_menu_dir):
        for file in files:
            if file.endswith('.lnk'):
                programs[os.path.splitext(file)[0]] = os.path.join(root, file)
    
    # Index Program Files directories.
    program_files_dirs = [os.environ["ProgramFiles"], os.environ["ProgramFiles(x86)"]]
    for dir in program_files_dirs:
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith('.exe'):
                    programs[os.path.splitext(file)[0]] = os.path.join(root, file)

    # Save the programs dictionary to a file.
    with open(programs_file, 'wb') as file:
        pickle.dump(programs, file)


def open_program(program_name):
    programs_file = './USER_PROGRAMS.pickle'
    if not Path(programs_file).exists():
        update_programs_list(programs_file)
    programs = unpack_pickle_file(programs_file)
    print(programs)

    # Find the best match for the program name.
    best_match, score = process.extractOne(program_name, list(programs.keys()))

    # If the score is not high enough, the program does not exist.
    if score < 95:
        print(f"{program_name} does not exist on this computer.")
        return

    # Check the cache first.
    if best_match in app_cache:
        os.startfile(app_cache[best_match])
        return

    # If the program is not in the cache, check the programs dictionary.
    if best_match in programs:
        app_cache[best_match] = programs[best_match]
        os.startfile(app_cache[best_match])

# Update the list of installed programs.
# Try to open a program.
