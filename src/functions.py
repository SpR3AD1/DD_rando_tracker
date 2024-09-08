from win32gui import (SetWindowLong, GetWindowLong, SetLayeredWindowAttributes)
from win32con import (WS_EX_LAYERED, WS_EX_TRANSPARENT, WS_EX_LTRREADING, GWL_EXSTYLE,  LWA_COLORKEY, LWA_ALPHA)
from win32api import RGB
import tkinter.messagebox as msgbox

def button_found_click(show):
    show.set(True)
    
def button_missing_click(show):
    show.set(False)
    
from tkinter import END as END

def insert_text(x,listbox):
    if not list(listbox.get(0,END)) == x:
        if listbox.size()>0:
            listbox.delete(0,END)
        listbox.insert(0,*x)
        
def filter_list(x,lookfor):
    if len(lookfor)>0:
        x = [y for y in x if lookfor.lower() in y.lower()]
    return(x)
    
def list_clicked(event,listbox,clicked_str,checked):
    if not checked.get():
        if listbox.curselection():
            clicked_list = clicked_str.get().split('\n')
            if listbox.get(listbox.curselection()).split(' [')[0] not in clicked_list:
                if '[' in listbox.get(listbox.curselection()):
                    clicked_list.append(listbox.get(listbox.curselection()).split(' [')[0])
            else:
                clicked_list.remove(listbox.get(listbox.curselection()).split(' [')[0])
            clicked_str.set('\n'.join(clicked_list))
        

def on_closing(window,exitFlag,configpath,bg_color,fg_color,window_x,window_y,accessable,transparent,window_border,show_go,position_x,position_y,show_unchecked,update_check):
    exitFlag.set(True)
    f = open(configpath, "w")
    f.write(f"bg_color = {bg_color.get()}\nfg_color = {fg_color.get()}\nwidth = {window_x.get()}\nheight = {window_y.get()}\naccessable = {accessable.get()}\ntransparent = {transparent.get()}\nwindow_border = {window_border.get()}\nshow_go = {show_go.get()}\nposition_x = {position_x}\nposition_y = {position_y}\nshow_found_locations = {show_unchecked.get()}\ncheck_for_updates = {update_check.get()}")
    f.close()
    window.destroy()
    
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    
def set_clickthrough(hwnd, bg_color, on, trans):
    if on==1:
        color = '#000000'
        styles = WS_EX_LAYERED | WS_EX_TRANSPARENT
    else:
        color = '#FFFFFF'
        styles = WS_EX_LTRREADING | WS_EX_LAYERED
    if trans==1:
        try:
            hwnd.attributes('-transparentcolor', color) 
            SetWindowLong(hwnd.winfo_id(), GWL_EXSTYLE, styles)
            color = hex_to_rgb(bg_color)
            SetLayeredWindowAttributes(hwnd.winfo_id(), RGB(color[0],color[1],color[2]), 255, LWA_COLORKEY)

        except Exception as e:
            print(e)
    else:
        try:
            hwnd.attributes('-transparentcolor', color)
            SetWindowLong(hwnd.winfo_id(), GWL_EXSTYLE, styles)
            SetLayeredWindowAttributes(hwnd.winfo_id(), 0, 255, LWA_ALPHA)
        except Exception as e:
            print(e)
            
def toggle_minimize(event,window,bg_color,clickthrough,transparent,root,start):
    if not start.get():
        if clickthrough.get()==1:
            clickthrough.set(0)
        else:
            if (window.state() == "normal"):
                window.state("withdrawn")
            elif (window.state() == "withdrawn"):
                window.state("normal")
    else:
        start.set(False)
    root.lower()
    root.iconify()
    
def msg_clickthrough(start):
    if not start.get():
        msgbox.showinfo(title='Clickthrough enabled', message="Clickthrough enabled. To disable again, click the icon in the taskbar.")
        
def on_drag_start(event,window,x,y):
    x.set(value=event.x)
    y.set(value=event.y)

def on_drag_motion(event,window,x,y):
    x = window.winfo_x() - x.get() + event.x
    y = window.winfo_y() - y.get() + event.y
    window.geometry(f"{window.winfo_width()}x{window.winfo_height()}+{x}+{y}")
    
def do_popup(event,m): 
    try: 
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release()

def strtobool(val):
    """Convert a string representation of truth to true (1) or false (0).
    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return 1
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return 0
    else:
        raise ValueError("invalid truth value %r" % (val,))