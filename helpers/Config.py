
import json
# Creates a configuration file if the file does not exist
def create_config():
    try:
        print("Creating the config file...")
        
        with open("config.json", "w") as file:
            json.dump({}, file)
        pass
    except Exception as e:
        print(f"Error creating the config file: {e}")
        return None


# Validates the configuration file, making sure it is in the correct format
def validate_config():
    pass

# Prompts the user to enter the necessary information to create a configuration file
def prompt_config():
    pass

# Reads the configuration file
def read_config():
    pass


__all__ = ["create_config", "validate_config", "prompt_config", "read_config"]

