"""Provide images and quotes.

The 'generate_meme' function either produces a random meme or customized meme
considering the user input (image path, quote and author).
"""

import os
import random
import argparse

from MemeEngine.MemeGenerator import MemeGenerator
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine import QuoteModel


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/pics/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        #img = path[0]
        img = path

    if body is None:
        quote_files = ['./_data/Quotes/QuotesTXT.txt',
                       './_data/Quotes/QuotesDOCX.docx',
                       './_data/Quotes/QuotesPDF.pdf',
                       './_data/Quotes/QuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeGenerator('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Show me a meme')
    parser.add_argument('--path', type=str, default=None,
                        help='path to an image')
    parser.add_argument('--body', type=str, default=None,
                        help='quote body to add to the image')
    parser.add_argument('--author', type=str, default=None,
                        help='quote author to add to the image')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
