# A flask web application for generating stories

from flask import Flask, render_template
import random

app = Flask(__name__)

# Lists of story elements

beginnings = ["Once upon a time", "In a land far away", "In the not-so-distant future"]
characters = ["a brave knight", "an adventure explorer", "a curious scientist"]
settings = ["a mysterious forest", "a bustling city", "an ancient castle"]
conflicts = ["batlling a fearsome dragon", "discovering a hidden treasure", "solving a perplexing mystery"]
endings = ["and they all lived happily ever after", "and the world was forever changed", "and they found their way back home."]

# Generate a random story

def generate_story():
    beginning = random.choice(beginnings)
    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    ending = random.choice(endings)

    story = f"{beginning}, {character} set out on a journey to {setting}. They faced the challenge of {conflict}. {ending}"

    return story

# Define a route to generate and display a story

@app.route('/')
def index():
    story = generate_story()
    return render_template('index.html', story=story)

if __name__ == '__main__':
    app.run(debug=True)