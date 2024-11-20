from helpers.GoogleDrive import authenticate_google_drive

# save the images generated from the script
def save_images_drive(config):
    print("Saving the images to google drive...")

    output_folder = config["output_directory"]
    service = authenticate_google_drive()
    # get the images paths of the ouput folder
    pass

__all__ = ["save_images_drive"]
