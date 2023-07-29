import random

def generate_haiku():
    # List of possible words for each line of the haiku
    line1 = ["Autumn", "Cherry blossoms", "Crisp leaves"]
    line2 = ["Whispering wind", "Gentle raindrops", "Morning dew"]
    line3 = ["Quiet reflection", "Eternal beauty", "Peaceful harmony"]

    # Getting a random word from each line
    word1 = random.choice(line1)
    word2 = random.choice(line2)
    word3 = random.choice(line3)

    # Returning the haiku as a single string
    return f"{word1}\n{word2}\n{word3}"

# Generating a haiku
haiku = generate_haiku()

# Printing the haiku
print(haiku)