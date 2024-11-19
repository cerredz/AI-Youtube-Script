
from helpers.generate_images import generate_image

# Given a list of sentences, generate the images for the video
def generate_images(sentences, config):
    try:
        print("Generating the images for your video...")
        images_paths= []
        # Generate the images for each sentence
        
        for i in range(len(sentences)):
            image_path = generate_image(sentences[i], config, i)
            images_paths.append(image_path)

        return images_paths

    except Exception as e:
        print(f"Error generating the images for your video: {e}")
        return 


__all__ = ["generate_images"]