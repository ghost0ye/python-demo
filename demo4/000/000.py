# coding: utf-8

from PIL import Image, ImageFont, ImageDraw

image = Image.open('bug.jpg')
w, h = image.size
font = ImageFont.truetype('arial.ttf', 60)
draw = ImageDraw.Draw(image)
draw.text((5*w/6, h/9), '99+', fill=(0, 128, 128), font=font)
image.save('result.png', 'png')