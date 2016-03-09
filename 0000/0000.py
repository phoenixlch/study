#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont

number = str(5)
color = (255.0, 0)
windows_font = 'arial.ttf'


def draw_text(text, fill_color, windows_font):
    im = Image.open('aaa.jpg')
    x, y = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(windows_font, 35)
    draw.text((x - 20, 7), text, fill_color, font)

    im.save('bbb.jpg')
draw_text(number, color, windows_font)
