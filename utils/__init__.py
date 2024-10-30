import os
import json
from helpers.Config import create_config, validate_config, prompt_config, read_config


# Initialize the config file
def config_init():
    try:
        print("Initializing the config file...")
        files = os.listdir()
        config = None

        if "config.json" not in files:
            # config file does not exist, create it
            create_config()
        else:
            # config file exists, validate it
            if not validate_config():
                # config file is not in the correct format, prompt the user to enter the necessary information
                prompt_config()

        # after above steps, read the config file and then return it
        config = read_config()
    except Exception as e:
        print(f"Error initializing the config file: {e}")
        return None
    return config

    