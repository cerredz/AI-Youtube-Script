from helpers.GoogleDrive import authenticate_google_drive, get_images_folder
import os
# save the images generated from the script
def save_images_drive(config):
    print("Saving the images to google drive...")

    output_folder = config["output_directory"]

    # authenticate to google drive
    service = authenticate_google_drive()
    # get the images paths of the ouput folder
    images_paths = [f"{output_folder}/{image}" for image in os.listdir(output_folder)]

    # get the root "images" folder from the google drive
    images_folder_id = get_images_folder(service)

    # create the subfolder for the current images paths
    subfolder_id = create_subfolder(service, images_folder_id, output_folder.split("/")[-1])

    




    pass

__all__ = ["save_images_drive"]
