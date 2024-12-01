import os
import yaml
from picli import __file__ as package_root

RESOURCE_DIR_PATH = os.path.join(os.path.dirname(package_root), "./resources")
COMMANDS_FILE_PATH = "commands.yaml"
MESSAGES_FILE_PATH = "messages.yaml"
DEFAULT_MESSAGE = "<!Message not found!>"

_messages = None
_commands = None

def get_resource_path(file_path):
    """Construct full path to a resource file"""
    return os.path.join(RESOURCE_DIR_PATH, file_path)

def load_yaml(filename):
    """Load a YAML file and return its content"""
    resource_path = get_resource_path(filename)
    if not os.path.exists(resource_path):
        return {}
    try:
        with open(resource_path, 'r') as f:
            config = yaml.safe_load(f) or {}
        return config
    except yaml.YAMLError as e:
        raise RuntimeError(f"Failed to parse YAML file: {resource_path}. Error: {e}")

# ---- Messages Handling ---- #

def load_messages():
    """Load all messages"""
    global _messages
    if _messages is None:
        _messages = load_yaml(MESSAGES_FILE_PATH)
    return _messages

def get_message(category, key, subcategory=None, **kwargs):
    """Retrieve a message from all loaded messages"""
    messages = load_messages()
    category_messages = messages.get(category, {})

    if subcategory:
        sub_messages = category_messages.get(subcategory, {})
        message = sub_messages.get(key, DEFAULT_MESSAGE)
        return message.format(**kwargs)
    
    message = category_messages.get(key, DEFAULT_MESSAGE)
    return message.format(**kwargs)

def get_tools_message(key, subcategory=None, **kwargs):
    return get_message(category="editing_tools", key=key, subcategory=subcategory, **kwargs)

def get_tools_error(key, **kwargs):
    return get_message(category="editing_tools", key=key, subcategory="errors", **kwargs)

def get_general_message(key, subcategory=None, **kwargs):
    return get_message(category="general", key=key, subcategory=subcategory, **kwargs)

def get_general_error(key, **kwargs):
    return get_message(category="general", key=key, subcategory="errors", **kwargs)

# ---- Commands Handling ---- #

def load_commands():
    """Load all commands"""
    global _commands
    if _commands is None:
        _commands = load_yaml(COMMANDS_FILE_PATH)
    return _commands

def get_command(name):
    """Retrieve a command by name """
    commands = load_commands()
    return commands.get(name, {})

def get_command_prop(command_name, prop="help", **kwargs):
    """Get property of a command"""
    command = get_command(command_name)
    value = command.get(prop, DEFAULT_MESSAGE)
    return value.format(**kwargs)

def get_command_arg_prop(command_name, arg_name, prop="help", **kwargs):
    """Get command argument property"""
    command = get_command(command_name)
    args = command.get("args", {})
    arg = args.get(arg_name, {})
    value = arg.get(prop, DEFAULT_MESSAGE)
    return value.format(**kwargs)
