from utils import config_init
from helpers.Sentences import read_sentences
from utils.generate_images import generate_images

def main():

    # initialize configuration files
    config = config_init()

    # read the sentences for the images from the sentences.txt file
    sentences = read_sentences()

    # generate the images using the sentences
    if config["generate_images"] == "True":
        if sentences is not None:
            generate_images(sentences, config)

    
    
    


main()


