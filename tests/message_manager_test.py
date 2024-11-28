import pytest

import picli.message_manager as tested_module

def test_get_resource_path():
    tested_module.MESSAGES_FILE_PATH = "messages.yaml"
    result = tested_module.get_resource_path(tested_module.MESSAGES_FILE_PATH)
    expected = "resources\messages.yaml"

    assert result == expected, f"Expected: {expected} but got: {result}"

def test_config_connection():
    messages = tested_module.load_messages()
    number_of_messages = len(messages)
    
    assert number_of_messages > 0, f"Expected: number of messages to be > 0 but got {number_of_messages}"

def test_get_message():
    result = tested_module.get_message(
        category="editing_tools", 
        key="no_config_access", 
        subcategory="errors"
    )
    
    expected = "ERROR: Could not access configuration file."

    assert result == expected, f"Expected: {expected} but got: {result}"

def test_get_command_prop():
    result = tested_module.get_command_prop(
        command_name="config",
    )

    expected = "Config editor input and output folder."

    assert result == expected, f"Expected: {expected} but got: {result}"

def test_get_command_arg_prop():
    result = tested_module.get_command_arg_prop(
        command_name="compress",
        arg_name="--width",
        prop="help"
    )

    expected = "Width for result image. Height is determined respectivly to aspect ratio."

    assert result == expected, f"Expected: {expected} but got: {result}"
