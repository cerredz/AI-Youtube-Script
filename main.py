from utils import config_init
from helpers.Sentences import read_sentences
from utils.generate_images import generate_images
from utils.GoogleDrive import save_images_drive

def main():

    # initialize configuration files
    config = config_init()

    # read the sentences for the images from the sentences.txt file
    sentences = read_sentences()

    # generate the images using the sentences
    if config["generate_images"] == "True":
        if sentences is not None:
            generate_images(sentences, config)

    # save the images to google drive

    if config["save_images"] == "True":
        save_images_drive(config)


    
    
    


main()


