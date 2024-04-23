from tkinter import *
from random import choice


class Main:
    def __init__ (self,root, title):
        self.root = root
        self.root.title(title)
        self.root.geometry("1800x25")


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
        obj = Main(root, choice(titles))






        root.mainloop()
        
