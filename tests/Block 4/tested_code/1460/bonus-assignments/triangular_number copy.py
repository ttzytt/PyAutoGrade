from tkinter import *
from PIL import ImageTk, Image
import os
from random import choice, random

scale = 3

class Main:
    def __init__ (self,root, title, geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)


if __name__ == '__main__':
    titles = [
        'this is a virus >:)',
        'you will never escape',
        'hehehehehehehehea',
        'amognus sussy imposter',
        'grrrrrrrrrrrrrrr',
        'hop on valorant pls',
        'wsg gamers',
        ]
    for i in range(100):
        root = Tk()
        if random() < 0.05:
            obj = Main(root, choice(titles), '1280x720')
            image = Image.open("amongus_legendary.jpg")
        else:
            obj = Main(root, choice(titles), '258x387')
            image = Image.open("amongus.jpg")
        resize_image = image.resize((258 * scale, 387 * scale))
        img = ImageTk.PhotoImage(image)
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        root.mainloop()
        
