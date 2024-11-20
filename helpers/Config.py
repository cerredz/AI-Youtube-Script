import json
import os
from dotenv import load_dotenv
load_dotenv()
# Creates a configuration file if the file does not exist
def create_config():
    try:
        print("Creating the config file...")
        
        with open("config.json", "w") as file:
            json.dump({
                "output_directory":"images/(____)",
                "hf_token": "",
                "generate_images": True,
                "save_images": False,
                "model_options": {
                    "model": "black-forest-labs/FLUX.1-dev",
                    "num_inference_steps": 28,
                    "guidance_scale":3.5,
                    "image": {
                        "width": 768,
                        "height":1024
                    },
                },
                "youtube_api": {
                    "api_key": "",
                    "channel_id": "",
                    "video_title": "",
                    "video_description": "",
                }
            }, file)
        print("🟢 Successfully created the config file!")

        
    except Exception as e:
        print(f"Error creating the config file: {e}")
        return None


# Validates the configuration file, making sure it is in the correct format
def validate_config():
    try:
        print("Validating the config file...")
        config = read_config()
        
        if "output_directory" not in config or config["output_directory"] == "":
            print("🔴 The output directory is not set in the config file!")
            prompt_config("output_directory")

        if "generate_images" not in config or (config["generate_images"] != "True" and config["generate_images"] != "False"):
            print("🔴 The generate images option is not set in the config file!")
            prompt_config("generate_images")

        if ("hf_token" not in config or config["hf_token"] == "") and os.getenv("HF_TOKEN") is None:
            print("🔴 The Hugging Face token is not set in the config file!")
            prompt_config("hf_token")

        if ("youtube_api" not in config or config["youtube_api"] == "") and os.getenv("YOUTUBE_API_KEY") is None:
            print("🔴 The YouTube API key is not set in the config file!")
            prompt_config("youtube_api.api_key")
        
        model_options = config.get("model_options", {})
        if "model" not in model_options or model_options["model"] == "":
            print("🔴 The model is not set in the model options!")
            prompt_config("model_options.model")
        if "num_inference_steps" not in model_options or model_options["num_inference_steps"] == "":
            print("🔴 The number of inference steps is not set in the model options!")
            prompt_config("model_options.num_inference_steps")
        if "guidance_scale" not in model_options or model_options["guidance_scale"] == "":
            print("🔴 The guidance scale is not set in the model options!")
            prompt_config("model_options.guidance_scale")
        if "image" not in model_options:
            print("🔴 The image properties are not set in the model options!")
            prompt_config("model_options.image.width")
            prompt_config("model_options.image.height")
    
        image = model_options["image"]
        if "width" not in image or image["width"] == "":
            print("🔴 The image width is not set in the model options!")
            prompt_config("model_options.image.width")
        if "height" not in image or image["height"] == "":
            print("🔴 The image height is not set in the model options!")
            prompt_config("model_options.image.height")
        
        youtube_api = config.get("youtube_api", {})
        if ("channel_id" not in youtube_api or youtube_api["channel_id"] == "") and os.getenv("YOUTUBE_API_KEY") is None:
            print("🔴 The YouTube channel ID is not set in the config file!")
            prompt_config("youtube_api.channel_id")
        if "video_title" not in youtube_api or youtube_api["video_title"] == "":
            print("🔴 The YouTube video title is not set in the config file!")
            prompt_config("youtube_api.video_title")
        if "video_description" not in youtube_api or youtube_api["video_description"] == "":
            print("🔴 The YouTube video description is not set in the config file!")
            prompt_config("youtube_api.video_description")

        if "save_images" not in config or (config["save_images"] != "True" and config["save_images"] != "False"):
            print("🔴 The save images option is not set in the config file!")
            prompt_config("save_images")



        # check if all the required keys are present
        if all(key in config for key in ["output_directory", "hf_token", "model_options", "youtube_api"]):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error reading the config file: {e}")
        return None

# Prompts the user to enter the necessary information to create a configuration file
def prompt_config(key):
    user_input = input(f"Please enter the value for the '{key}': ")
    config = read_config()
    
    # Split the key into parts
    key_parts = key.split(".")
    
    # Navigate through nested dictionaries
    current = config
    for i, part in enumerate(key_parts[:-1]):  # All parts except the last one
        if part not in current:
            current[part] = {}
        current = current[part]
    
    # Set the final value
    current[key_parts[-1]] = user_input
    
    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)
    print(f"🔄 Updated '{key}' in the config file with the value: {user_input}")

# Reads the configuration file
def read_config():
    config = None
    try:
        with open("config.json", "r") as file:
            config = json.load(file)
        if not config:  # If config is empty dict or None
            config = {}
    except json.JSONDecodeError:  # If file is empty or invalid JSON
        config = {}

    config["hf_token"] = os.getenv("HF_TOKEN") if os.getenv("HF_TOKEN") else config["hf_token"]
    return config

__all__ = ["create_config", "validate_config", "prompt_config", "read_config"]

