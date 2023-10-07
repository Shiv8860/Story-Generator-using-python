import random
import nltk

def generate_story():
    intro = random.choice(phrases)
    character = random.choice(nouns)
    action = random.choice(verbs)
    item = random.choice(objects)

    story = f"{intro} {character} {action} the {item}."
    return story

phrases = [
    "Once upon a time,",
    "In a land far away,",
    "On a sunny morning,",
    "In a bustling city,",
    "Deep in the forest,",
    "Under a starry sky,",
]

nouns = ["dragon", "princess", "knight", "wizard", "pirate", "unicorn"]
verbs = ["found", "rescued", "defeated", "discovered", "captured", "befriended"]
objects = ["treasure", "magic potion", "secret map", "mysterious amulet", "enchanted sword"]


if __name__ == "__main__":
    nltk.download("punkt")  # Download NLTK data

    while True:
        input("Press Enter to generate a story...")
        story = generate_story()
        print("\nHere's your story:\n")
        print(story + "\n")

