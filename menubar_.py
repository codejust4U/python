# Menubar in tkinter

# importing the libraries
from tkinter import *
from tkinter import ttk

from tkinter import *

root = Tk()
root.title('VLC media player')
root.iconbitmap(r'D:\copy_of_htdocs\practice\Python\300days\Day 259 Tkinter Day - 8\vlc_gif.gif')

#lbl1 = Label(root, text='VLC media player')
#lbl1.pack()

menubar = Menu(root)
# Adding a cascade with a submenu -- media
media_menu = Menu(menubar, tearoff=0)
media_menu.add_command(label='Open file')
media_menu.add_command(label='Open multiple files')
media_menu.add_command(label='Open folder')
media_menu.add_command(label='Open disc')
media_menu.add_command(label='Open folder')
media_menu.add_command(label='Open network stream')
media_menu.add_command(label='Open capture device')
media_menu.add_command(label='Open location from clipboard')
media_menu.add_command(label='Open recent media')
media_menu.add_command(label='Save playlist to file')
media_menu.add_command(label='Convert/save')
media_menu.add_command(label='Stream')
media_menu.add_command(label='Quit at the end of playlist')
media_menu.add_command(label='Quit',command=root.destroy)
media_menu.add_separator()
menubar.add_cascade(label='Media', menu=media_menu)


# Adding a cascade with a submenu -- playback
playback_menu = Menu(menubar,tearoff=0)
playback_menu.add_cascade(label='Title')
playback_menu.add_cascade(label='Chapter')
playback_menu.add_cascade(label='Program')
playback_menu.add_cascade(label='Custom bookmarks')
playback_menu.add_cascade(label='Renderer')
playback_menu.add_cascade(label='Speed')
playback_menu.add_cascade(label='Jump forward')
playback_menu.add_cascade(label='Jump backward')
playback_menu.add_cascade(label='Jump to specific time')
playback_menu.add_cascade(label='Previous chapter')
playback_menu.add_cascade(label='Next chapter')
playback_menu.add_cascade(label='Pause')
playback_menu.add_cascade(label='Stop')
playback_menu.add_cascade(label='Previous')
playback_menu.add_cascade(label='Next')
playback_menu.add_cascade(label='Record')
playback_menu.add_separator()
menubar.add_cascade(label='Playback', menu=playback_menu)



root.config(menu=menubar)

root.mainloop()
