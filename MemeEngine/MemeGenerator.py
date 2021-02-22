"""Construct the random or customized meme.

The 'make_meme' function resizes the image and adds quote and author name texts
to the image.
"""

from PIL import Image, ImageDraw, ImageFont
import random
import os


class MemeGenerator():
    """Class to generate a meme."""

    def __init__(self, output_dir):
        """Create a new meme.

        :param output_dir: path for saving the meme
        """
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a new meme.

        :param img_path: path of the image
        :param text: quote for the meme
        :param author: author of the quote
        :param width: width of the meme image - default set to 500
        :return: path of the meme
        """
        img = Image.open(img_path)

        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)

        x = 50
        y = 150

        x_ = 80
        y_ = 180

        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', 20)
        font_ = ImageFont.truetype('./fonts/SANTO___.ttf', 35)

        draw.text((x-1, y-1), text, font=font, fill='white')
        draw.text((x+1, y-1), text, font=font, fill='white')
        draw.text((x-1, y+1), text, font=font, fill='white')
        draw.text((x+1, y+1), text, font=font, fill='white')

        draw.text((x_-1, y_-1), author, font=font_, fill='white')
        draw.text((x_+1, y_-1), author, font=font_, fill='white')
        draw.text((x_-1, y_+1), author, font=font_, fill='white')
        draw.text((x_+1, y_+1), author, font=font_, fill='white')

        draw.text((x, y), text, font=font, fill='black')
        draw.text((x_, y_), author, font=font_, fill='black')

        tmp = f'{random.randint(0, 10000000)}.jpg'
        output = self.output_dir+'/'+str(tmp)
        img.save(output)
        return output
