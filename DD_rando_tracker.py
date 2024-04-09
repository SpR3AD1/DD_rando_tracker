import tkinter as tk
import tkinter.messagebox as msgbox
from os import getenv
from os import path
from os import makedirs
from PIL import Image, ImageTk
import sys
from matplotlib.colors import is_color_like
from tkinter import ttk

show = True
exitFlag = False
err = False
bg_color = "#101010"
fg_color = "#ffffff"
window_x = 288
window_y = 657
accessable = 1

def button_found_click():
    global show
    show = True
    
def button_missing_click():
    global show
    show = False

def insert_text(x):
    if not list(listbox.get(0,tk.END)) == x:
        if listbox.size()>0:
            listbox.delete(0,tk.END)
        listbox.insert(0,*x)
    
def read_file():
    Locations = []
    Items_found = []
    Time_found = []
    Locations_missing = []
    souls_found = 0
    seeds_found = 0
    vitality_found = 0
    magic_found = 0
    souls_count = 0
    seeds_count = 0
    vitality_count = 0
    magic_count = 0
    pink_key_found = 0
    green_key_found = 0
    yellow_key_found = 0
    pink_key_count = 0
    green_key_count = 0
    yellow_key_count = 0
    filepath = getenv('LocalAppData') + 'Low\Acid Nerve\DeathsDoor\SAVEDATA\\' + filepath_var.get() + '-ItemChanger.json'

    if path.isfile(filepath):
        f = open(filepath, 'r')
        content = f.read()
        if len(content)>0:
            # found items
            for x in content.split('"LocationName"'):
                y = x.split('"')
                if not y[1] == 'Placements' and len(y)>5:
                    Locations.append(y[1])
                    # Items_found.append(y[5])
                    match y[5]:
                        case '100 Souls':
                            souls_found += 1
                        case 'Life Seed':
                            seeds_found += 1
                        case 'Vitality Shard':
                            vitality_found += 1
                        case 'Magic Shard':
                            magic_found += 1
                        case 'Pink Key':
                            pink_key_found += 1
                        case 'Green Key':
                            green_key_found += 1
                        case 'Yellow Key':
                            yellow_key_found += 1
                        case _:
                            Items_found.append(y[5])
                    if len(y)>12:
                        z = y[12].split(':')
                        Time_found.append(float(z[1][:-3]))
            # missing items
            x = content.split('"TrackerLog"')
            loc = True
            insert = False
            go = False
            for y in x[0].split('"'):
                if go and y not in [',',':','},']:
                    if loc:
                        if not y in Locations:
                            Locations.append(y)
                            Locations_missing.append(y)
                            insert = True
                        loc = False
                    else:
                        if insert:
                            insert = False
                        loc = True
                        match y:
                            case '100 Souls':
                                 souls_count += 1
                            case 'Life Seed':
                                 seeds_count += 1
                            case 'Vitality Shard':
                                 vitality_count += 1
                            case 'Magic Shard':
                                 magic_count += 1
                            case 'Pink Key':
                                pink_key_count += 1
                            case 'Green Key':
                                green_key_count += 1
                            case 'Yellow Key':
                                yellow_key_count += 1
                else:
                    if ':{' in y:
                        go = True
        f.close()
        Items_found = [x for _, x in sorted(zip(Time_found, Items_found), reverse=True)]
        
    filepath = getenv('LocalAppData') + 'Low\Acid Nerve\DeathsDoor\SAVEDATA\\Randomizer Helper Log.txt'
    Locations_accessable = []
    if path.isfile(filepath):
        f = open(filepath, 'r')
        for line in f.readlines():
            if not ':' in line and line.strip():
                if not line in Locations_accessable:
                    Locations_accessable.append(line)
        
    return Items_found, Time_found, Locations, Locations_missing, Locations_accessable, souls_found, seeds_found, vitality_found, magic_found, souls_count, seeds_count, vitality_count, magic_count, pink_key_found, yellow_key_found, green_key_found, pink_key_count, yellow_key_count, green_key_count
    
def filter_list(x):
    lookfor = entry.get()
    if len(lookfor)>0:
        x = [y for y in x if lookfor.lower() in y.lower()]
    return(x)

def on_closing():
    global exitFlag
    exitFlag = True
    window.destroy()

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(tk.Canvas):
    def __init__(self,**kwargs):
        tk.Canvas.__init__(self,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

def mainloop():
    global exitFlag
    global bg_color
    global fg_color
    global err
    if err:
        err = False
        msgbox.showinfo(title='Error', message="Error when using colors. Reverting to default.")
    if not exitFlag:
        Items_found, Time_found, Locations, Locations_missing, Locations_accessable, souls_found, seeds_found, vitality_found, magic_found, souls_count, seeds_count, vitality_count, magic_count, pink_key_found, yellow_key_found, green_key_found, pink_key_count, yellow_key_count, green_key_count = read_file()
        if "Giant Soul of The Urn Witch" in Items_found:
            canvas.itemconfig(grandma,image=grandma_found)
        else:
            canvas.itemconfig(grandma,image=grandma_missing)
        if "Giant Soul of The Frog King" in Items_found:
            canvas.itemconfig(frog,image=frog_found)
        else:
            canvas.itemconfig(frog,image=frog_missing)
        if "Giant Soul of Betty" in Items_found:
            canvas.itemconfig(betty,image=betty_found)
        else:
            canvas.itemconfig(betty,image=betty_missing)
        '''
        if "Discarded Umbrella" in Items_found:
            canvas.itemconfig(umbrella,image=umbrella_found)
        else:
            canvas.itemconfig(umbrella,image=umbrella_missing)
        if "Rogue Daggers" in Items_found:
            canvas.itemconfig(daggers,image=daggers_found)
        else:
            canvas.itemconfig(daggers,image=daggers_missing)
        if "Thunder Hammer" in Items_found:
            canvas.itemconfig(hammer,image=hammer_found)
        else:
            canvas.itemconfig(hammer,image=hammer_missing)
        if "Reaper's Greatsword" in Items_found:
            canvas.itemconfig(greatsword,image=greatsword_found)
        else:
            canvas.itemconfig(greatsword,image=greatsword_missing)
        '''
        if "Arrow Level 2" in Items_found:
            canvas.itemconfig(arrow,image=arrow_found2)
        elif "Arrow" in Items_found or True:
            canvas.itemconfig(arrow,image=arrow_found)
        else:
            canvas.itemconfig(arrow,image=arrow_missing)
            canvas.itemconfig(arrow,image=arrow_found)
        if "Fire Level 2" in Items_found:
            canvas.itemconfig(fire,image=fire_found2)
        elif "Fire" in Items_found:
            canvas.itemconfig(fire,image=fire_found)
        else:
            canvas.itemconfig(fire,image=fire_missing)
        if "Bomb Level 2" in Items_found:
            canvas.itemconfig(bomb,image=bomb_found2)
        elif "Bomb" in Items_found:
            canvas.itemconfig(bomb,image=bomb_found)
        else:
            canvas.itemconfig(bomb,image=bomb_missing)
        if "Hookshot Level 2" in Items_found:
            canvas.itemconfig(hookshot,image=hookshot_found2)
        elif "Hookshot" in Items_found:
            canvas.itemconfig(hookshot,image=hookshot_found)
        else:
            canvas.itemconfig(hookshot,image=hookshot_missing)
        canvas.itemconfig(pink_key_text,text=f'{pink_key_found} / {pink_key_count}', fill=fg_color)
        canvas.itemconfig(yellow_key_text,text=f'{yellow_key_found} / {yellow_key_count}', fill=fg_color)
        canvas.itemconfig(green_key_text,text=f'{green_key_found} / {green_key_count}', fill=fg_color)
        canvas.itemconfig(souls_text,text=f'{souls_found} / {souls_count}', fill=fg_color)
        canvas.itemconfig(seeds_text,text=f'{seeds_found} / {seeds_count}', fill=fg_color)
        canvas.itemconfig(vitality_text,text=f'{vitality_found} / {vitality_count}', fill=fg_color)
        canvas.itemconfig(magic_text,text=f'{magic_found} / {magic_count}', fill=fg_color)
        
        if accessable:
            accessable_text.config(text=f'accessable locations: {len(Locations_accessable)} / {len(Locations_missing)} / {len(Locations)}')
        else:
            accessable_text.config(text=f'unchecked locations: {len(Locations_missing)} / {len(Locations)}')

        filterlist = ["Giant Soul of The Urn Witch", "Giant Soul of The Frog King", "Giant Soul of Betty", "Discarded Umbrella", "Rogue Daggers", "Thunder Hammer", "Reaper's Greatsword", "Reaper's Greatsword", "Arrow Level 2", "Fire", "Fire Level 2", "Bomb", "Bomb Level 2", "Hookshot", "Hookshot Level 2"]
        Items_found = [x for x in Items_found if x not in filterlist]
        
        if show:
            insert_text(filter_list(Items_found))
        else:
            if accessable:
                insert_text(filter_list(Locations_accessable))
            else:
                insert_text(filter_list(Locations_missing))

        window.after(200, mainloop)

        try:
            window.configure(bg=bg_color)
            canvas.configure(bg=bg_color)
            settings_button.configure(bg=bg_color)
            entry.configure(bg=bg_color, fg=fg_color)
            listbox.configure(bg=bg_color, fg=fg_color)
            button_found.configure(bg=bg_color, fg=fg_color)
            button_missing.configure(bg=bg_color, fg=fg_color)
            filecount.configure(bg=bg_color, fg=fg_color, activebackground=bg_color, activeforeground=fg_color)
        except:
            err = True
            bg_color = "#101010"
            fg_color = "#ffffff"
            global window_x
            global window_y
            
            configpath = getenv('LocalAppData') + 'Low\Acid Nerve\DeathsDoor\DD_rando_tracker\Config.cfg'
            
            makedirs(path.dirname(configpath), exist_ok=True)
            f = open(configpath, "w")
            f.write(f"bg_color = {bg_color}\nfg_color = {fg_color}\nwidth = {window_x}\nheight = {window_y}\naccessable = {accessable}")
            f.close()
            
            window.configure(bg=bg_color)
            canvas.configure(bg=bg_color)
            settings_button.configure(bg=bg_color)
            entry.configure(bg=bg_color, fg=fg_color)
            listbox.configure(bg=bg_color, fg=fg_color)
            button_found.configure(bg=bg_color, fg=fg_color)
            button_missing.configure(bg=bg_color, fg=fg_color)
            filecount.configure(bg=bg_color, fg=fg_color, activebackground=bg_color, activeforeground=fg_color)
            
        
def open_settings():
    global bg_color
    global fg_color
    global window_x
    global window_y
    global access
    global accessable
    
    def get_settings():
        windowx.delete(0,tk.END)
        windowx.insert(0,window.winfo_width())
        windowy.delete(0,tk.END)
        windowy.insert(0,window.winfo_height())
        
    def default_settings():
        bgcolor.delete(0,tk.END)
        bgcolor.insert(0,"#101010")
        fgcolor.delete(0,tk.END)
        fgcolor.insert(0,"#ffffff")
        windowx.delete(0,tk.END)
        windowx.insert(0,"288")
        windowy.delete(0,tk.END)
        windowy.insert(0,"657")
        
    def save_settings():
        global bg_color
        global fg_color
        global window_x
        global window_y
        global access
        global accessable
        if not is_color_like(bgcolor.get()):
            msgbox.showinfo(title='Wrong input', message="Backround-color: please enter a valid color or hex-code.")
        elif not is_color_like(fgcolor.get()):
            msgbox.showinfo(title='Wrong input', message="Font-color: please enter a valid color or hex-code.")
        else:
            bg_color = bgcolor.get()
            fg_color = fgcolor.get()
            window_x = windowx.get()
            window_y = windowy.get()
            accessable = access.get()
            
            configpath = getenv('LocalAppData') + 'Low\Acid Nerve\DeathsDoor\DD_rando_tracker\Config.cfg'
            
            makedirs(path.dirname(configpath), exist_ok=True)
            f = open(configpath, "w")
            f.write(f"bg_color = {bg_color}\nfg_color = {fg_color}\nwidth = {window_x}\nheight = {window_y}\naccessable = {accessable}")
            f.close()
            
            window.geometry(f"{window_x}x{window_y}")
            
            newWindow.destroy()
        
    newWindow = tk.Toplevel(window)
    newWindow.configure(bg=bg_color)
    newWindow.title("Settings")
    newWindow.geometry("200x255")

    tk.Label(newWindow, text ="Background-color:", bg=bg_color, fg=fg_color).pack()
    bgcolor = tk.Entry(newWindow, bg=bg_color, fg=fg_color, textvariable = tk.StringVar(newWindow, value=bg_color))
    bgcolor.pack()
    tk.Label(newWindow, text ="Foreground-color:", bg=bg_color, fg=fg_color).pack()
    fgcolor = tk.Entry(newWindow, bg=bg_color, fg=fg_color, textvariable = tk.StringVar(newWindow, value=fg_color))
    fgcolor.pack()
    tk.Label(newWindow, text ="window-width:", bg=bg_color, fg=fg_color).pack()
    windowx = tk.Entry(newWindow, bg=bg_color, fg=fg_color, textvariable = tk.StringVar(newWindow, value=window_x))
    windowx.pack()
    tk.Label(newWindow, text ="window-height:", bg=bg_color, fg=fg_color).pack()
    windowy = tk.Entry(newWindow, bg=bg_color, fg=fg_color, textvariable = tk.StringVar(newWindow, value=window_y))
    windowy.pack()
    
    access = tk.IntVar(value=accessable)
    checkbutton = tk.Checkbutton(newWindow, bg=bg_color, fg=fg_color, selectcolor=bg_color, text="only accessable locations", variable=access, onvalue=1, offvalue=0).pack()
    
    buttonframe = tk.Frame(newWindow, bg=bg_color)
    buttonframe.pack(pady=(10, 0))
    
    settings_get_button = tk.Button(buttonframe, command=get_settings, text="Get sizes")
    settings_get_button.pack(side="left", padx=(5,5))
    
    settings_default_button = tk.Button(buttonframe, command=default_settings, text="Default")
    settings_default_button.pack(side="left", padx=(5,5))
    
    settings_save_button = tk.Button(buttonframe, command=save_settings, text="Save")
    settings_save_button.pack(side="left", padx=(5,5))
    
    
configpath = getenv('LocalAppData') + 'Low\Acid Nerve\DeathsDoor\DD_rando_tracker\Config.cfg'
if path.isfile(configpath):
    f = open(configpath, 'r')
    content = f.read()
    content = content.split('\n')
    if len(content)>0:
        bg_color = content[0].split(" = ")[1]
    if len(content)>1:
        fg_color = content[1].split(" = ")[1]
    if len(content)>2:
        window_x = int(content[2].split(" = ")[1])
    if len(content)>3:
        window_y = int(content[3].split(" = ")[1])
    if len(content)>4:
        accessable = int(content[4].split(" = ")[1])
    f.close()

window = tk.Tk()
window.configure(bg=bg_color)
window.geometry(f"{window_x}x{window_y}")
window.title("Death's Door Randomizer Tracker")

window.protocol("WM_DELETE_WINDOW", on_closing)

canvas = ResizingCanvas(width=window_x, height=235, bg=bg_color, highlightthickness=0)
canvas.pack(fill="x")

bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))

photo = tk.PhotoImage(file = path.join(bundle_dir, "images/icon.png"))
window.iconphoto(True, photo)

img= Image.open(path.join(bundle_dir, "images/settings.png"))
settings_image = ImageTk.PhotoImage(img) 
settings_button = tk.Button(window,height=16,width=16,bd=0, bg=bg_color, activebackground=bg_color, command=open_settings, relief="flat", image=settings_image)
button1_window = canvas.create_window(window_x, 0, anchor="ne", window=settings_button)

img= Image.open(path.join(bundle_dir, "images/Grandma_missing.png"))
grandma_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
grandma = canvas.create_image(window_x/4,5,image=grandma_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Grandma.png"))
grandma_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/FrogKing_missing.png"))
frog_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
frog = canvas.create_image(window_x/2,5,image=frog_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/FrogKing.png"))
frog_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/Betty_missing.png"))
betty_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
betty = canvas.create_image(3*window_x/4,5,image=betty_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Betty.png"))
betty_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))


img= Image.open(path.join(bundle_dir, "images/Arrow_missing.png"))
arrow_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
arrow = canvas.create_image(window_x/(288/37.6),65,image=arrow_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Arrow.png"))
arrow_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
img= Image.open(path.join(bundle_dir, "images/Arrow2.png"))
arrow_found2 = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/Fire_missing.png"))
fire_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
fire = canvas.create_image(window_x/(288/110.2),65,image=fire_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Fire.png"))
fire_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
img= Image.open(path.join(bundle_dir, "images/Fire2.png"))
fire_found2 = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/Bomb_missing.png"))
bomb_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
bomb = canvas.create_image(window_x/(288/182.8),65,image=bomb_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Bomb.png"))
bomb_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
img= Image.open(path.join(bundle_dir, "images/Bomb2.png"))
bomb_found2 = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/Hookshot_missing.png"))
hookshot_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
hookshot = canvas.create_image(window_x/(288/250.4),65,image=hookshot_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Hookshot.png"))
hookshot_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
img= Image.open(path.join(bundle_dir, "images/Hookshot2.png"))
hookshot_found2 = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/PinkKey.png"))
pink_key_img = ImageTk.PhotoImage(img.resize((30,30), Image.LANCZOS))
pink_key = canvas.create_image(window_x/(288/10),125,image=pink_key_img, anchor="nw")

pink_key_text = canvas.create_text(window_x/(288/43), 128, text='X / Y', anchor="nw", fill=fg_color, font=('Helvetica 16 bold'))

img= Image.open(path.join(bundle_dir, "images/YellowKey.png"))
yellow_key_img = ImageTk.PhotoImage(img.resize((30,30), Image.LANCZOS))
yellow_key = canvas.create_image(window_x/(288/105),125,image=yellow_key_img, anchor="nw")

yellow_key_text = canvas.create_text(window_x/(288/138), 128, text='X / Y', anchor="nw", fill=fg_color, font=('Helvetica 16 bold'))

img= Image.open(path.join(bundle_dir, "images/GreenKey.png"))
green_key_img = ImageTk.PhotoImage(img.resize((30,30), Image.LANCZOS))
green_key = canvas.create_image(window_x/(288/205),125,image=green_key_img, anchor="nw")

green_key_text = canvas.create_text(window_x/(288/238), 128, text='X / Y', anchor="nw", fill=fg_color, font=('Helvetica 16 bold'))

'''
img= Image.open(path.join(bundle_dir, "images/Umbrella_missing.png"))
umbrella_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
umbrella = canvas.create_image(window_x/(288/37.6),120,image=umbrella_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Umbrella.png"))
umbrella_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/Daggers_missing.png"))
daggers_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
daggers = canvas.create_image(window_x/(288/110.2),120,image=daggers_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Daggers.png"))
daggers_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/ThunderHammer_missing.png"))
hammer_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
hammer = canvas.create_image(window_x/(288/182.8),120,image=hammer_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/ThunderHammer.png"))
hammer_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/Greatsword_missing.png"))
greatsword_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
greatsword = canvas.create_image(window_x/(288/250.4),120,image=greatsword_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Greatsword.png"))
greatsword_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
'''

img= Image.open(path.join(bundle_dir, "images/Seed.png"))
seed_img = ImageTk.PhotoImage(img.resize((30,30), Image.LANCZOS))
seed = canvas.create_image(window_x/(288/5),165,image=seed_img, anchor="nw")

seeds_text = canvas.create_text(window_x/(288/45), 168, text='X / Y', anchor="nw", fill=fg_color, font=('Helvetica 16 bold'))

img= Image.open(path.join(bundle_dir, "images/Soul.png"))
soul_img = ImageTk.PhotoImage(img.resize((30,30), Image.LANCZOS))
soul = canvas.create_image(window_x/(288/283),165,image=soul_img, anchor="ne")

souls_text = canvas.create_text(window_x/(288/243), 168, text='X / Y', anchor="ne", fill=fg_color, font=('Helvetica 16 bold'))


img= Image.open(path.join(bundle_dir, "images/VitalityShard.png"))
vitality_img = ImageTk.PhotoImage(img.resize((30,30), Image.LANCZOS))
vitality = canvas.create_image(window_x/(288/5),200,image=vitality_img, anchor="nw")

vitality_text = canvas.create_text(window_x/(288/45), 203, text='X / Y', anchor="nw", fill=fg_color, font=('Helvetica 16 bold'))

img= Image.open(path.join(bundle_dir, "images/MagicShard.png"))
magic_img = ImageTk.PhotoImage(img.resize((30,30), Image.LANCZOS))
magic = canvas.create_image(window_x/(288/283),200,image=magic_img, anchor="ne")

magic_text = canvas.create_text(window_x/(288/243), 203, text='X / Y', anchor="ne", fill=fg_color, font=('Helvetica 16 bold'))

accessable_text = tk.Label(window, bg=bg_color, fg=fg_color,  font=('Helvetica 12 bold'), text='X / Y / Z')
accessable_text.pack()

entry = tk.Entry(bg=bg_color, fg=fg_color)
entry.pack(fill=tk.X)

scrollbar = tk.Scrollbar(window, orient="vertical") 
scrollbar.pack(side="right", fill="y") 
listbox = tk.Listbox(yscrollcommand=scrollbar.set, bg=bg_color, fg=fg_color, font=(14))
listbox.pack(fill=tk.BOTH, expand=1)
scrollbar.config(command = listbox.yview) 

button_found = tk.Button(window, text="Items found", command=button_found_click, bg=bg_color, fg=fg_color)
button_found.pack(side="left")

button_missing = tk.Button(window, text="Missing locations", command=button_missing_click, bg=bg_color, fg=fg_color)
button_missing.pack(side="right")

filepath_var = tk.StringVar(window)
filepath_var.set("Save_slot1") # default value

filecount = tk.OptionMenu(window, filepath_var, "Save_slot1", "Save_slot2", "Save_slot3")
filecount.config(bg=bg_color, fg=fg_color, highlightthickness=0, activebackground=bg_color, activeforeground=fg_color)
filecount.pack()

mainloop()

window.mainloop()

