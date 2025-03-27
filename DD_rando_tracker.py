import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox
from os import getenv
from os import path
from PIL import Image, ImageTk
import sys
from matplotlib.colors import is_color_like
from os import makedirs
from PIL import Image, ImageDraw, ImageTk
from win32gui import (SetWindowLong, GetWindowLong, SetLayeredWindowAttributes)
from win32con import (WS_EX_LAYERED, WS_EX_TRANSPARENT, WS_EX_LTRREADING, GWL_EXSTYLE,  LWA_COLORKEY, LWA_ALPHA)
from win32api import RGB
import ctypes

bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
sys.path.insert(1, path.join(bundle_dir, 'src/'))
    
from functions import *
from read_file import *
from ResizingCanvas import *
from settings import *
from window import *

version = "1.3.1"
err = False

def Check_for_updates(version):
    import requests
    response = requests.get("https://api.github.com/repos/SpR3AD1/DD_rando_tracker/releases/latest")
    version = version.split(".")
    upToDate = True
    latest = response.json()["name"].split(".")
    for i in range(len(version)):
        if version[i] > latest[i]:
            break
        if version[i] < latest[i]:
            upToDate = False
    return upToDate


def callback(url):
    import webbrowser
    webbrowser.open_new_tab(url)
   
def CallForUpdates(toplevel):    
    toplevel = tk.Toplevel(toplevel)
    
    user32 = ctypes.windll.user32

    toplevel.title("Newer version available")
    toplevel.geometry(f"500x80+{int((user32.GetSystemMetrics(0)/2)-250)}+{int((user32.GetSystemMetrics(1)/2)-180)}")
    toplevel.wm_attributes("-topmost", 1)

    tk.Label(toplevel, text = "There is a newer version available.\nPlease check:").pack()
    link = tk.Button(toplevel,text="https://github.com/SpR3AD1/DD_rando_tracker/releases/latest", command=lambda:callback("https://github.com/SpR3AD1/DD_rando_tracker/releases/latest")).pack()

def mainloop():
    global bg_color
    global fg_color
    global err
    if err:
        err = False
        msgbox.showinfo(title='Error', message="Error when using colors. Reverting to default.")
    if not exitFlag.get():    
        Items_found, Time_found, Locations, Locations_missing, Locations_accessable, souls_found, seeds_found, vitality_found, magic_found, souls_count, seeds_count, vitality_count, magic_count, pink_key_found, yellow_key_found, green_key_found, pink_key_count, yellow_key_count, green_key_count, IncludeBelltowerKey = read_file(filepath_var)
        
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
        
        canvas.itemconfig(pink_key_text,text=f'{pink_key_found} / {pink_key_count}', fill=fg_color.get())
        canvas.itemconfig(yellow_key_text,text=f'{yellow_key_found} / {yellow_key_count}', fill=fg_color.get())
        canvas.itemconfig(green_key_text,text=f'{green_key_found} / {green_key_count}', fill=fg_color.get())
        canvas.itemconfig(souls_text,text=f'{souls_found} / {souls_count}', fill=fg_color.get())
        canvas.itemconfig(seeds_text,text=f'{seeds_found} / {seeds_count}', fill=fg_color.get())
        canvas.itemconfig(vitality_text,text=f'{vitality_found} / {vitality_count}', fill=fg_color.get())
        canvas.itemconfig(magic_text,text=f'{magic_found} / {magic_count}', fill=fg_color.get())
        

        filterlist = []#["100 Souls", "Life Seed", "Pink Key", "Yellow Key", "Green Key", "Giant Soul of The Urn Witch", "Giant Soul of The Frog King", "Giant Soul of Betty", "Arrow Level 2", "Fire", "Fire Level 2", "Bomb", "Bomb Level 2", "Hookshot", "Hookshot Level 2"]
        Items_found = [x for x in Items_found if x not in filterlist]
        accessable_count = 0
        listtext = []
        click_list = clicked_list.get().split('\n')
        filtered_locations = []
        gomode_active = False
        for x in Locations_accessable.keys():
            if filter_list(Locations_accessable[x],entry.get()):
                filtered_locations.append(x)
        for x in filtered_locations:
            accessable_count += len(Locations_accessable[x])
            listtext.append(f'{x} [{str(len(Locations_accessable[x]))}]')
            if "Rusty Belltower Key" in Locations_accessable[x]: gomode_active = True
            if x in click_list:
                for y in filter_list(Locations_accessable[x],entry.get()):
                    listtext.append(f'     {y}')
        
        if show_go.get() and IncludeBelltowerKey:        
            canvas.itemconfig(gomode,state='normal')
            if gomode_active:
                canvas.itemconfig(gomode,image=gomode_found)
            else:
                canvas.itemconfig(gomode,image=gomode_missing)
        else:
            canvas.itemconfig(gomode,state='hidden')
        
        if show.get():
            insert_text(filter_list(Items_found,entry.get()),listbox)
        else:
            if accessable.get()==1:
                insert_text(listtext,listbox)
            else:
                insert_text(filter_list(Locations_missing,entry.get()),listbox)
                
        if accessable.get():
            accessable_text.config(bg=bg_color.get(), fg=fg_color.get(),text=f'accessable locations: {accessable_count} / {len(Locations_missing)} / {len(Locations)}')
        else:
            accessable_text.config(bg=bg_color.get(), fg=fg_color.get(),text=f'unchecked locations: {len(Locations_missing)} / {len(Locations)}')

        window.after(200, mainloop)

        try:
            window.update()
            window.update_idletasks()
            window.style.configure("Horizontal.TScrollbar", gripcount=0, background=bg_color.get())
            window.style.configure("Vertical.TScrollbar", gripcount=0, background=bg_color.get())
            window.configure(bg=bg_color.get())
            canvas.configure(bg=bg_color.get())
            entry.configure(bg=bg_color.get(), fg=fg_color.get())
            listbox.configure(bg=bg_color.get(), fg=fg_color.get(), selectbackground=bg_color.get())
            button_found.configure(bg=bg_color.get(), fg=fg_color.get())
            button_missing.configure(bg=bg_color.get(), fg=fg_color.get())
            filecount.configure(bg=bg_color.get(), fg=fg_color.get(), activebackground=bg_color.get(), activeforeground=fg_color.get())
            filler1.configure(bg=bg_color.get(), fg=fg_color.get())
        except:
            err = True
            bg_color.set("#101010")
            fg_color.set("#ffffff")
            
            configpath = getenv('LocalAppData') + 'Low\\Acid Nerve\\DeathsDoor\\DD_rando_tracker\\Config.cfg'
            
            makedirs(path.dirname(configpath), exist_ok=True)
            f = open(configpath, "w")
            f.write(f"bg_color = {bg_color.get()}\nfg_color = {fg_color.get()}\nwidth = {window_x.get()}\nheight = {window_y.get()}\naccessable = {accessable.get()}\ntransparent = {transparent.get()}\nwindow_border = {window_border.get()}\nshow_go = {show_go.get()}")
            f.close()
            
            window.configure(bg=bg_color.get())
            canvas.configure(bg=bg_color.get())
            entry.configure(bg=bg_color.get(), fg=fg_color.get())
            listbox.configure(bg=bg_color.get(), fg=fg_color.get(), selectbackground=bg_color.get())
            button_found.configure(bg=bg_color.get(), fg=fg_color.get())
            button_missing.configure(bg=bg_color.get(), fg=fg_color.get())
            filecount.configure(bg=bg_color.get(), fg=fg_color.get(), activebackground=bg_color.get(), activeforeground=fg_color.get())
        
        if window_border.get():
            set_clickthrough(window,bg_color.get(),clickthrough.get(),transparent.get())
    

# start of programm
bg_color_v = "#101010"
fg_color_v = "#ffffff"
window_x_v = 288
window_y_v = 657
accessable_v = 1
transparent_v = 0
window_border_v = False
show_go_v = 1
position_x = 0
position_y = 0
show_unchecked = True
checkForUpdates = True

configpath = getenv('LocalAppData') + 'Low\\Acid Nerve\\DeathsDoor\\DD_rando_tracker\\Config.cfg'
if path.isfile(configpath):
    f = open(configpath, 'r')
    content = f.read()
    content = content.split('\n')
    if not content[0] == "":
        bg_color_v = content[0].split(" = ")[1]
    if len(content)>1:
        fg_color_v = content[1].split(" = ")[1]
    if len(content)>2:
        window_x_v = int(content[2].split(" = ")[1])
    if len(content)>3:
        window_y_v = int(content[3].split(" = ")[1])
    if len(content)>4:
        accessable_v = int(content[4].split(" = ")[1])
    if len(content)>5:
        transparent_v = int(content[5].split(" = ")[1])
    if len(content)>6:
        window_border_v = strtobool(content[6].split(" = ")[1])
    if len(content)>7:
        show_go_v = strtobool(content[7].split(" = ")[1])
    if len(content)>8:
        position_x = int(content[8].split(" = ")[1])
    if len(content)>9:
        position_y = int(content[9].split(" = ")[1])
    if len(content)>10:
        show_unchecked = strtobool(content[10].split(" = ")[1])
    if len(content)>11:
        checkForUpdates = strtobool(content[11].split(" = ")[1])
    f.close()
    
if window_border_v:
    root = NewRoot()
    root.lower()
    root.iconify()
    root.title("Death's Door Randomizer Tracker")

    window = MyMain(root)
    window.overrideredirect(1)
else:
    window = tk.Tk()
    root = window
    

user32 = ctypes.windll.user32
if (position_x > (user32.GetSystemMetrics(78) - window_x_v)) or (position_y > (user32.GetSystemMetrics(79) - window_y_v)):
    position_x = 0
    position_y = 0
    
bg_color = tk.StringVar(value=bg_color_v)
fg_color = tk.StringVar(value=fg_color_v)
window_x = tk.IntVar(value=window_x_v)
window_y = tk.IntVar(value=window_y_v)
accessable = tk.IntVar(value=accessable_v)
transparent = tk.IntVar(value=transparent_v)
show_go = tk.IntVar(value=show_go_v)
window_border = tk.BooleanVar(value=window_border_v)
show = tk.BooleanVar(value=show_unchecked)
exitFlag = tk.BooleanVar(value=False)
x = tk.IntVar(value=position_x)
y = tk.IntVar(value=position_y)
clickthrough = tk.IntVar(value=0)
start = tk.BooleanVar(value=True)
clicked_list = tk.StringVar()
check_for_updates = tk.BooleanVar(value=checkForUpdates)

window.attributes("-alpha", 1)
window.wm_attributes("-topmost", 1)
window.configure(bg=bg_color.get())

draw_scrollbars(bundle_dir, fg_color.get())

window.tk.call('source', path.join(bundle_dir, 'themes/breeze-dark.tcl'))

window.style = ttk.Style()
s = 'breeze-dark'
window.style.theme_use(s)

if window_border.get():
    window.grip = ttk.Sizegrip(window)
    sg_settings = sizegrip_style(background=bg_color.get(), foreground=fg_color.get())
    window.style.theme_settings(s, sg_settings)
    window.grip.place(relx=1.0, rely=1.0, anchor="se")
    window.grip.bind("<B1-Motion>", window.OnMotion)
    set_clickthrough(window,bg_color.get(),clickthrough.get(),transparent.get())
    root.bind("<Map>", lambda event, window=window, bg_color=bg_color, clickthrough=clickthrough, transparent=transparent,root=root,start=start: toggle_minimize(None,window,bg_color,clickthrough,transparent,root,start))

window.style.configure("Horizontal.TScrollbar", gripcount=0, background=bg_color.get())
window.style.configure("Vertical.TScrollbar", gripcount=0, background=bg_color.get())

photo = tk.PhotoImage(file = path.join(bundle_dir, "images/icon.png"))
window.iconphoto(True, photo)
window.geometry(f"{window_x.get()}x{window_y.get()}+{x.get()}+{y.get()}")
window.title("Death's Door Randomizer Tracker")

window.protocol("WM_DELETE_WINDOW", lambda:on_closing(window,exitFlag,configpath,bg_color,fg_color,window_x,window_y,accessable,transparent,window_border,show_go,window.winfo_rootx(),window.winfo_rooty(),show,check_for_updates))

if not window_border.get():
    disabled = 'disabled'
else:
    disabled = 'normal'

m = tk.Menu(root, tearoff = 0) 
m.add_checkbutton(label="Enable clickthrough", state=disabled, onvalue=1, offvalue=0, variable=clickthrough, command=lambda:msg_clickthrough(start))
m.add_command(label="Options",command=lambda:open_settings(version,window,bg_color,fg_color,window_x,window_y,accessable,transparent,window_border,show_go,window.winfo_rootx(),window.winfo_rooty(),show,check_for_updates))
m.add_separator() 
m.add_command(label ="Close",command=lambda:on_closing(root,exitFlag,configpath,bg_color,fg_color,window_x,window_y,accessable,transparent,window_border,show_go,window.winfo_rootx(),window.winfo_rooty(),show,check_for_updates))
  
window.bind("<Button-3>", lambda event, m=m:do_popup(event,m)) 

if check_for_updates.get():
    if not Check_for_updates(version):
        CallForUpdates(window)


canvas = ResizingCanvas(master=window,width=window_x.get(), height=235, bg=bg_color.get(), highlightthickness=0)
canvas.pack(fill="x")

canvas.bind("<Button-1>", lambda event, window=window,x=x,y=y: on_drag_start(event,window,x,y))
canvas.bind("<B1-Motion>", lambda event, window=window,x=x,y=y: on_drag_motion(event,window,x,y))


img= Image.open(path.join(bundle_dir, "images/Grandma_missing.png"))
grandma_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
grandma = canvas.create_image(window_x.get()/4,5,image=grandma_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Grandma.png"))
grandma_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/FrogKing_missing.png"))
frog_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
frog = canvas.create_image(window_x.get()/2,5,image=frog_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/FrogKing.png"))
frog_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/Betty_missing.png"))
betty_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
betty = canvas.create_image(3*window_x.get()/4,5,image=betty_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Betty.png"))
betty_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))


img= Image.open(path.join(bundle_dir, "images/Arrow_missing.png"))
arrow_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
arrow = canvas.create_image(window_x.get()/(288/37.6),65,image=arrow_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Arrow.png"))
arrow_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
img= Image.open(path.join(bundle_dir, "images/Arrow2.png"))
arrow_found2 = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/Fire_missing.png"))
fire_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
fire = canvas.create_image(window_x.get()/(288/110.2),65,image=fire_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Fire.png"))
fire_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
img= Image.open(path.join(bundle_dir, "images/Fire2.png"))
fire_found2 = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/Bomb_missing.png"))
bomb_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
bomb = canvas.create_image(window_x.get()/(288/182.8),65,image=bomb_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Bomb.png"))
bomb_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
img= Image.open(path.join(bundle_dir, "images/Bomb2.png"))
bomb_found2 = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/Hookshot_missing.png"))
hookshot_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
hookshot = canvas.create_image(window_x.get()/(288/250.4),65,image=hookshot_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Hookshot.png"))
hookshot_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
img= Image.open(path.join(bundle_dir, "images/Hookshot2.png"))
hookshot_found2 = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/PinkKey.png"))
pink_key_img = ImageTk.PhotoImage(img.resize((30,30), Image.LANCZOS))
pink_key = canvas.create_image(window_x.get()/(288/10),125,image=pink_key_img, anchor="nw")

pink_key_text = canvas.create_text(window_x.get()/(288/43), 128, text='X / Y', anchor="nw", fill=fg_color.get(), font=('Helvetica 16 bold'))

img= Image.open(path.join(bundle_dir, "images/YellowKey.png"))
yellow_key_img = ImageTk.PhotoImage(img.resize((30,30), Image.LANCZOS))
yellow_key = canvas.create_image(window_x.get()/(288/105),125,image=yellow_key_img, anchor="nw")

yellow_key_text = canvas.create_text(window_x.get()/(288/138), 128, text='X / Y', anchor="nw", fill=fg_color.get(), font=('Helvetica 16 bold'))

img= Image.open(path.join(bundle_dir, "images/GreenKey.png"))
green_key_img = ImageTk.PhotoImage(img.resize((30,30), Image.LANCZOS))
green_key = canvas.create_image(window_x.get()/(288/205),125,image=green_key_img, anchor="nw")

green_key_text = canvas.create_text(window_x.get()/(288/238), 128, text='X / Y', anchor="nw", fill=fg_color.get(), font=('Helvetica 16 bold'))

'''
img= Image.open(path.join(bundle_dir, "images/Umbrella_missing.png"))
umbrella_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
umbrella = canvas.create_image(window_x.get()/(288/37.6),120,image=umbrella_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Umbrella.png"))
umbrella_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/Daggers_missing.png"))
daggers_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
daggers = canvas.create_image(window_x.get()/(288/110.2),120,image=daggers_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Daggers.png"))
daggers_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/ThunderHammer_missing.png"))
hammer_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
hammer = canvas.create_image(window_x.get()/(288/182.8),120,image=hammer_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/ThunderHammer.png"))
hammer_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/Greatsword_missing.png"))
greatsword_missing = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
greatsword = canvas.create_image(window_x.get()/(288/250.4),120,image=greatsword_missing, anchor="n")
img= Image.open(path.join(bundle_dir, "images/Greatsword.png"))
greatsword_found = ImageTk.PhotoImage(img.resize((50,50), Image.LANCZOS))
'''

img= Image.open(path.join(bundle_dir, "images/Seed.png"))
seed_img = ImageTk.PhotoImage(img.resize((30,30), Image.LANCZOS))
seed = canvas.create_image(window_x.get()/(288/5),165,image=seed_img, anchor="nw")

seeds_text = canvas.create_text(window_x.get()/(288/45), 168, text='X / Y', anchor="nw", fill=fg_color.get(), font=('Helvetica 16 bold'))

img= Image.open(path.join(bundle_dir, "images/Soul.png"))
soul_img = ImageTk.PhotoImage(img.resize((30,30), Image.LANCZOS))
soul = canvas.create_image(window_x.get()/(288/283),165,image=soul_img, anchor="ne")

souls_text = canvas.create_text(window_x.get()/(288/243), 168, text='X / Y', anchor="ne", fill=fg_color.get(), font=('Helvetica 16 bold'))

img= Image.open(path.join(bundle_dir, "images/Gomode_missing.png"))
gomode_missing = ImageTk.PhotoImage(img.resize((70,70), Image.LANCZOS))
gomode = canvas.create_image(window_x.get()/(288/144),200,image=gomode_missing, anchor="c")
img= Image.open(path.join(bundle_dir, "images/Gomode.png"))
gomode_found = ImageTk.PhotoImage(img.resize((70,70), Image.LANCZOS))

img= Image.open(path.join(bundle_dir, "images/VitalityShard.png"))
vitality_img = ImageTk.PhotoImage(img.resize((30,30), Image.LANCZOS))
vitality = canvas.create_image(window_x.get()/(288/5),200,image=vitality_img, anchor="nw")

vitality_text = canvas.create_text(window_x.get()/(288/45), 203, text='X / Y', anchor="nw", fill=fg_color.get(), font=('Helvetica 16 bold'))

img= Image.open(path.join(bundle_dir, "images/MagicShard.png"))
magic_img = ImageTk.PhotoImage(img.resize((30,30), Image.LANCZOS))
magic = canvas.create_image(window_x.get()/(288/283),200,image=magic_img, anchor="ne")

magic_text = canvas.create_text(window_x.get()/(288/243), 203, text='X / Y', anchor="ne", fill=fg_color.get(), font=('Helvetica 16 bold'))

accessable_text = tk.Label(window, bg=bg_color.get(), fg=fg_color.get(),  font=('Helvetica 12 bold'), text='X / Y / Z')
accessable_text.pack()

entry = tk.Entry(window,bg=bg_color.get(), fg=fg_color.get())
entry.pack(fill=tk.X)

scolled_listbox = tk.Frame(window)
scolled_listbox.pack(fill=tk.BOTH,expand=1, padx=(5, 5), pady=(5, 5))

scrollbar_v = ttk.Scrollbar(scolled_listbox, orient="vertical")
scrollbar_v.pack(side = 'right', fill=tk.Y)

scrollbar_h = ttk.Scrollbar(scolled_listbox, orient='horizontal')
scrollbar_h.pack(side = 'bottom', fill=tk.X)

listbox = tk.Listbox(scolled_listbox, bg=bg_color.get(), fg=fg_color.get(), border=0, font=(14))
listbox.pack(fill=tk.BOTH,expand=1)
listbox.bind("<<ListboxSelect>>", lambda event=None,self=listbox,clicked_list=clicked_list,checked=show:list_clicked(event,self,clicked_list,checked))

listbox.configure(yscrollcommand=scrollbar_v.set,xscrollcommand=scrollbar_h.set)
listbox.configure(selectbackground=bg_color.get(),highlightthickness=0,activestyle='none')
scrollbar_v.config(command = listbox.yview) 
scrollbar_h.config(command = listbox.xview) 

scrollbar_v.pack(side = 'right', fill=tk.Y)
scrollbar_h.pack(side = 'bottom', fill=tk.X)

pixel = tk.PhotoImage(width=1, height=1)
filler1 = tk.Label(window, width=window_x.get()-275, image=pixel, bg=bg_color.get(), fg=bg_color.get())
filler1.pack(side="right")

button_missing = tk.Button(window, text="Unchecked", command=lambda:button_missing_click(show), bg=bg_color.get(), fg=fg_color.get())
button_missing.pack(side="right")

button_found = tk.Button(window, text="Items found", command=lambda:button_found_click(show), bg=bg_color.get(), fg=fg_color.get())
button_found.pack(side="right")

filepath_var = tk.StringVar(window)
filepath_var.set("Save_slot1") # default value

filecount = tk.Menubutton(window, borderwidth=0, indicatoron=True, textvariable=filepath_var, direction="above",anchor="e", bg=bg_color.get(), fg=fg_color.get())
filecount_menu = tk.Menu(filecount, tearoff=False)
filecount.configure(menu=filecount_menu)
filecount_menu.add_radiobutton(label="Save_slot1", variable=filepath_var, value="Save_slot1")
filecount_menu.add_radiobutton(label="Save_slot2", variable=filepath_var, value="Save_slot2")
filecount_menu.add_radiobutton(label="Save_slot3", variable=filepath_var, value="Save_slot3")

filecount.pack(side="left")




mainloop()

window.mainloop()

