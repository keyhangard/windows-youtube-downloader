import os
import shutil
import youtube_dl
import tkinter as tk

from tkinter.filedialog import askdirectory
from tkinter import messagebox

window = tk.Tk()
window.title("kehiy youtube downloader")
window.iconbitmap ("E:\Amir\py\icon\icon.ico")
window.minsize(450 , 200)
window.maxsize(450 , 200)

def widget():
    link_lable = tk.Label(window , text = "video link:")
    link_lable.grid(row=0 , column=0 , padx=40 , pady=20)
    link_lable.config(font=("none" , 15),fg="red")

    link_input = tk.Entry(window , width=40 , textvariable=video_link)
    link_input.grid(row=0 , column=1)

    place_lable = tk.Label(window , text = " file location:")
    place_lable.grid(row=2 , column=0)
    place_lable.config(font=("none" , 15),fg="green")

    place_input = tk.Entry(window , width=30 , textvariable=download_dir)
    place_input.grid(row=2 , column=1 , sticky="w")

    place_btn = tk.Button(window , text="open" , width=7 , bg="black" , fg="white" , command=brows)
    place_btn.grid(row=2 , column=1 , sticky="e" )

    download_btn = tk.Button(window , text="download" , bg="green" , fg="black" , command=down)
    download_btn.grid(row=5 , column=1 , pady=10)
    download_btn.config(width=8 , height=2)

def brows():
    directory = askdirectory(initialdir="YOUR DIRECTORY PATH" , title="save")
    download_dir.set(directory)

def down():
    link = video_link.get()
    save_dir = download_dir.get()
    ydl_opts = {
            'outtmpl':save_dir + '/%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    
    messagebox.showinfo(title="Success" , message="your video downloaded successfuly!")

    
download_dir = tk.StringVar()
video_link = tk.StringVar()



widget()
window.mainloop()
