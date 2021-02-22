"""Generate a meme with predefined pictures and quotes or create your own meme.

See 'README.md' for a detailed description of this project.

This script can be invoked from the command line:
    $ python app.py

The generator can be accessed at http://127.0.0.1:5000/
"""

import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeEngine.MemeGenerator import MemeGenerator
from QuoteEngine.Ingestor import Ingestor

app = Flask(__name__)

meme = MemeGenerator('./static')

for file in os.listdir('./static'):
    os.unlink(os.path.join('./static', file))


def setup():
    """Load all resources."""
    quote_files = ['./_data/Quotes/QuotesTXT.txt',
                   './_data/Quotes/QuotesDOCX.docx',
                   './_data/Quotes/QuotesPDF.pdf',
                   './_data/Quotes/QuotesCSV.csv']

    quotes = list()
    for file in quote_files:
        try:
            quotes.extend(Ingestor.parse(file))
        except TypeError:
            print(f'{file} extension unknown')
            continue

    images_path = "./_data/photos/pics/"

    imgs = list()
    for image in os.listdir(images_path):
        if image.endswith('.jpg'):
            imgs.append(os.path.join(images_path, image))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    img_url = request.form.get('image_url')
    img_data = requests.get(img_url, stream=True).content
    with open('temp.jpg', 'wb') as f:
        f.write(img_data)

    body = request.form.get('body', '')
    author = request.form.get('author', 'unknown')
    path = meme.make_meme('temp.jpg', body, author)
    os.remove('temp.jpg')
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
