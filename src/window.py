import sys
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageTk
from os import path


def sizegrip_style(background, foreground):
    """Create style configuration for ttk sizegrip
    Args:
        background (str): The color used for the background.
        foreground (str): The color used for the grips
    Returns:
        dict: The settings used to update the sizegrip style.
    """
    image = create_sizegrip_image(foreground)
    settings = dict()
    settings.update({
        'Sizegrip.sizegrip': {
            'element create': ('image', image)},
        'TSizegrip': {
            'configure': {'background': background},
            'layout': [('Sizegrip.sizegrip', {'side': 'bottom', 'sticky': 'se'})]}})
    return settings


def create_sizegrip_image(color):
    """Create assets for size grip
    Args:
        color (str): The hexadecimal color to use for drawing the widget.
    """
    im = Image.new('RGBA', (14, 14))
    draw = ImageDraw.Draw(im)

    # draw the grips
    draw.rectangle((9, 3, 10, 4), fill=color)  # top row
    
    draw.rectangle((6, 6, 7, 7), fill=color)  # middle row
    draw.rectangle((9, 6, 10, 7), fill=color)

    draw.rectangle((3, 9, 4, 10), fill=color)  # bottom row
    draw.rectangle((6, 9, 7, 10), fill=color)
    draw.rectangle((9, 9, 10, 10), fill=color)

    # could also save the image here... im.save(filepath)
    return ImageTk.PhotoImage(im)

def draw_scrollbars(bundle_dir,color):
    """Create assets for size grip
    Args:
        color (str): The hexadecimal color to use for drawing the widget.
    """
    
    transcolor = color.lstrip('#')
    transcolor = tuple(int(transcolor[i:i+2], 16) for i in (0, 2, 4))+(100,)
    
    im = Image.new('RGBA', (30, 20))
    draw = ImageDraw.Draw(im)
    draw.rectangle((3, 7, 27, 12), fill=color)
    draw.ellipse((0, 7, 6, 12), fill=color)
    draw.ellipse((14, 7, 29, 12), fill=color)
    im.save(path.join(bundle_dir, 'themes/breeze-dark/scrollbar-slider-horiz-active.png'))
    im.save(path.join(bundle_dir, 'themes/breeze-dark/scrollbar-slider-horiz.png'))
    
    '''
    im = Image.new('RGBA', (56, 20))
    draw = ImageDraw.Draw(im)
    draw.rectangle((3, 7, 53, 12), fill=transcolor)
    draw.ellipse((0, 7, 6, 12), fill=transcolor)
    draw.ellipse((14, 7, 55, 12), fill=transcolor)
    im.save(path.join(bundle_dir, 'themes/breeze-dark/scrollbar-trough-horiz-active.png'))
    '''

    im = Image.new('RGBA', (20, 30))
    draw = ImageDraw.Draw(im)
    draw.rectangle((7, 3, 12, 27), fill=color)
    draw.ellipse((7, 0, 12, 6), fill=color)
    draw.ellipse((7, 14, 12, 29), fill=color)
    im.save(path.join(bundle_dir, 'themes/breeze-dark/scrollbar-slider-vert-active.png'))
    im.save(path.join(bundle_dir, 'themes/breeze-dark/scrollbar-slider-vert.png'))
    
    '''
    im = Image.new('RGBA', (20, 56))
    draw = ImageDraw.Draw(im)
    draw.rectangle((7, 3, 12, 53), fill=transcolor)
    draw.ellipse((7, 0, 12, 6), fill=transcolor)
    draw.ellipse((7, 14, 12, 55), fill=transcolor)
    im.save(path.join(bundle_dir, 'themes/breeze-dark/scrollbar-trough-vert-active.png'))
    '''

class NewRoot(tk.Tk):    
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 0.0)

class MyMain(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.overrideredirect(1)
        self.attributes('-topmost', 1)


    def OnMotion(self, event):
        x1 = self.winfo_pointerx()
        y1 = self.winfo_pointery()
        x0 = self.winfo_rootx()
        y0 = self.winfo_rooty()
        self.geometry("%sx%s" % ((x1-x0),(y1-y0)))
        return

    def on_close(self, event):
        self.master.destroy()