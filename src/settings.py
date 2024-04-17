import tkinter as tk
import tkinter.messagebox as msgbox
from matplotlib.colors import is_color_like
from os import getenv
from os import path
from os import makedirs

def open_settings(window,bg_color,fg_color,window_x,window_y,accessable,transparent):
    global access
    global trans
    global fg_org
    global bg_org
    
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
        
    def save_settings(bg_color,fg_color,window_x,window_y,accessable):
        global access
        global fg_org
        global bg_org
        if not is_color_like(bgcolor.get()):
            msgbox.showinfo(title='Wrong input', message="Backround-color: please enter a valid color or hex-code.")
        elif not is_color_like(fgcolor.get()):
            msgbox.showinfo(title='Wrong input', message="Font-color: please enter a valid color or hex-code.")
        else:
            bg_color.set(bgcolor.get())
            fg_color.set(fgcolor.get())
            window_x.set(windowx.get())
            window_y.set(windowy.get())
            accessable.set(access.get())
            transparent.set(trans.get())
            
            if (not fg_org == fg_color.get()) or (not bg_org == bg_color.get()):
                msgbox.showinfo(title='Colors changed', message="You changed the colors. For sliders and Sizegrip to be adjusted you need to close and reopen the tracker.")
            
            configpath = getenv('LocalAppData') + 'Low\Acid Nerve\DeathsDoor\DD_rando_tracker\Config.cfg'
            
            makedirs(path.dirname(configpath), exist_ok=True)
            f = open(configpath, "w")
            f.write(f"bg_color = {bg_color.get()}\nfg_color = {fg_color.get()}\nwidth = {window_x.get()}\nheight = {window_y.get()}\naccessable = {accessable.get()}\ntransparent = {transparent.get()}")
            f.close()
            
            window.geometry(f"{window_x.get()}x{window_y.get()}")
            
            newWindow.destroy()
        
    newWindow = tk.Toplevel(window)
    newWindow.configure(bg=bg_color.get())
    newWindow.title("Settings")
    newWindow.geometry("200x255")
    newWindow.wm_attributes("-topmost", 1)
    
    fg_org = fg_color.get()
    bg_org = bg_color.get()

    tk.Label(newWindow, text ="Background-color:", bg=bg_color.get(), fg=fg_color.get()).pack()
    bgcolor = tk.Entry(newWindow, bg=bg_color.get(), fg=fg_color.get(), textvariable = tk.StringVar(newWindow, value=bg_color.get()))
    bgcolor.pack()
    tk.Label(newWindow, text ="Foreground-color:", bg=bg_color.get(), fg=fg_color.get()).pack()
    fgcolor = tk.Entry(newWindow, bg=bg_color.get(), fg=fg_color.get(), textvariable = tk.StringVar(newWindow, value=fg_color.get()))
    fgcolor.pack()
    tk.Label(newWindow, text ="window-width:", bg=bg_color.get(), fg=fg_color.get()).pack()
    windowx = tk.Entry(newWindow, bg=bg_color.get(), fg=fg_color.get(), textvariable = tk.StringVar(newWindow, value=window_x.get()))
    windowx.pack()
    tk.Label(newWindow, text ="window-height:", bg=bg_color.get(), fg=fg_color.get()).pack()
    windowy = tk.Entry(newWindow, bg=bg_color.get(), fg=fg_color.get(), textvariable = tk.StringVar(newWindow, value=window_y.get()))
    windowy.pack()
        
    trans = tk.IntVar(value=transparent.get())
    checkbutton = tk.Checkbutton(newWindow, bg=bg_color.get(), fg=fg_color.get(), selectcolor=bg_color.get(), text="transparent background", variable=trans, onvalue=1, offvalue=0).pack()
    
    access = tk.IntVar(value=accessable.get())
    checkbutton = tk.Checkbutton(newWindow, bg=bg_color.get(), fg=fg_color.get(), selectcolor=bg_color.get(), text="only accessable locations", variable=access, onvalue=1, offvalue=0).pack()
    
    buttonframe = tk.Frame(newWindow, bg=bg_color.get())
    buttonframe.pack(pady=(10, 0))
    
    settings_get_button = tk.Button(buttonframe, command=get_settings, text="Get sizes", bg=bg_color.get(), fg=fg_color.get())
    settings_get_button.pack(side="left", padx=(5,5))
    
    settings_default_button = tk.Button(buttonframe, command=default_settings, text="Default", bg=bg_color.get(), fg=fg_color.get())
    settings_default_button.pack(side="left", padx=(5,5))
    
    settings_save_button = tk.Button(buttonframe, command=lambda:save_settings(bg_color,fg_color,window_x,window_y,accessable), text="Save", bg=bg_color.get(), fg=fg_color.get())
    settings_save_button.pack(side="left", padx=(5,5))