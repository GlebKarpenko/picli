import os
import yaml

RESOURCE_DIR_PATH = "resources"
RESOURCE_FILE_PATH = "messages.yaml"
DEFAULT_MESSAGE = "<!Message not found!>"

messages = {}

def get_resource_path():
    return os.path.join(RESOURCE_DIR_PATH, RESOURCE_FILE_PATH)

def load_message_category(category):
    resource_path = get_resource_path()
    if os.path.exists(resource_path):
        try:    
            with open (resource_path, "r") as f:
                all_messages = yaml.safe_load(f)
            messages[category] = all_messages.get(category, {})
        except yaml.YAMLError as e:
            raise RuntimeError(f"Failed to parse YAML file: {resource_path}. Error: {e}")
    else:
        messages[category] = {}
        
def get(category, key, subcategory=None, **kwargs):
    if category not in messages:
        load_message_category(category)
    if subcategory:
        sub_messages = messages[category].get(subcategory, {})
        return sub_messages.get(key, DEFAULT_MESSAGE).format(**kwargs)
    return messages[category].get(key, DEFAULT_MESSAGE).format(**kwargs)

def get_tools_message(key, subcategory=None, **kwargs):
    return get(category="editing_tools", key=key, subcategory=subcategory, **kwargs)

def get_tools_error(key, **kwargs):
    return get(category="editing_tools", key=key, subcategory="errors", **kwargs)

def get_general_message(key, subcategory=None, **kwargs):
    return get(category="general", key=key, subcategory=subcategory, **kwargs)

def get_general_error(key, **kwargs):
    return get(category="general", key=key, subcategory="errors", **kwargs)
