import os
def read_sentences():
    print("Reading the sentences from the sentences.txt file...")

    if not os.path.exists("sentences.txt"):
        print("🔴 Sentences file does not exist, creating it now...")
        open("sentences.txt", "w").close()

    with open("sentences.txt", "r") as file:
        sentences = file.readlines()
    if len(sentences) == 0:
        print("🔴 Sentences file is empty, please add some sentences to it!")
        return None
    print("🟢 Successfully read the sentences from the sentences.txt file!")
    return sentences

__all__ = ["read_sentences"]
