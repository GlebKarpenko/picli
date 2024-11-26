import os
import configparser

"""
Determine the appropriate USER path for the config file based on the OS.
"""
def get_config_path():
    # Windows
    if os.name == 'nt':
        return os.path.join(os.environ['APPDATA'], "picli_config.ini")
    # Linux/Mac
    return os.path.expanduser("~/.picli_config.ini")

# Config path is set based on users OS
CONFIG_PATH = get_config_path()
DEFAULT_INPUT_FOLDER = "../input_folder"
INPUT_ROOT_DIR = os.path.dirname(DEFAULT_INPUT_FOLDER)
DEFAULT_OUTPUT_FOLDER = os.path.join(INPUT_ROOT_DIR, "output_folder")

"""
Save configuration to USER config path.
"""
def save_config(config):
    with open(CONFIG_PATH, "w") as configfile:
        config.write(configfile)

"""
Loads configuration from the config file.
Returns a ConfigParser object.
"""
def load_config():
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_PATH):
        config.read(CONFIG_PATH)
    else:
        config["FOLDERS"] = {"input_folder": DEFAULT_INPUT_FOLDER, "output_folder": DEFAULT_OUTPUT_FOLDER}
        save_config(config)
    return config

"""
Get the default folder for folder_type=input or output.
"""
def get_default_folder(folder_type):
    config = load_config()
    return config["FOLDERS"].get(folder_type, "").strip()

"""
Set the default folder_path for folder_type of input or output folder.
"""
def set_default_folder(folder_type, folder_path):
    config = load_config()
    config["FOLDERS"][folder_type] = folder_path
    save_config(config)

def get_folder_path(user_input, folder_type):
    return user_input if user_input else get_default_folder(folder_type)

def main(args):
    """Entry point for the config subcommand."""
    try:
        load_config()
    except:
        print("ERROR: Could not access configuration file.")
        return

    if args.input_folder:
        user_input_path = args.input_folder
        set_default_folder("input_folder", user_input_path)
        print(f"Successfully set input_folder to path: {user_input_path}")

    if args.output_folder:
        user_output_path = args.output_folder
        set_default_folder("output_folder", user_output_path)
        print(f"Successfully set output_folder to path: {user_output_path}")       

    input_folder = get_default_folder("input_folder")
    output_folder = get_default_folder("output_folder")

    print()
    print("Store images you want to edit in input_folder. Edited result will be stored in output_folder")
    print("Current input_folder path with images to edit (use --input_folder to edit): ", input_folder)
    print("Current output_folder path with edited images(use --output_folder to edit): ", output_folder)

if __name__ == "__main__":
    print("This script is meant to be imported.")