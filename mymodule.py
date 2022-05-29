from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os
from tkinter import filedialog
from tkinter import *

def Openfolder():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print (root.filename)
        
def inst1():
    for pic in os.listdir('images'):
        if pic.endswith('.jpg' or '.png' or '.img' or '.jpeg'):
            img = Image.open(pic)
            fn, flext = os.path.splitext(pic)

            new = img.convert('L')
            new1 = new.filter(ImageFilter.DETAIL)
            new2 = new1.resize((1080, 1080))
            width, height = new2.size

            draw = ImageDraw.Draw(new2)
            text = "hecker!"
            title = "BLACK"
            font = ImageFont.truetype("font.ttf", 80)
            textwidth, textheight = draw.textsize(text, font)

            margin = 10
            x = width - textwidth - margin
            y = height - textheight - margin

            draw.text((x, y), text, title, font=font)

            new2.save('pic/{}{}'.format(fn, flext))
