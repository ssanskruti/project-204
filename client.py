import socket
from tkinter import *
from threading import Thread
from PIL import ImageTk, Image
import random

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None

playerName = None
nameEntry = None
nameWindow = None

def save_name():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName=nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()
    SERVER.send(playerName.encode())

def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    global screen_width
    global screen_height

    nameWindow=Tk()
    nameWindow.title("Tambola family fun")
    nameWindow.geometry("800x600")

    screen_width=nameWindow.winfo_screenwidth()
    screen_height=nameWindow.winfo_screenheight()

    bg=ImageTk.PhotoImage(file="./assets/background.jpg")
    canvas1=Canvas(nameWindow,width=500,height=500)
    canvas1.pack(fill="both",expand=True)
    canvas1.create_image(0,0,image=bg,anchor="nw")
    canvas1.create_text(screen_width/4,screen_height/6,text="Enter Name",font=("Chalkboard SE",50),fill="blue")

    nameEntry=Entry(nameWindow,width=15,justify="center",font=("Chalkboard SE",30),bg="white")
    nameEntry.place(x=200,y=300)

    button=Button(nameWindow,text="SAVE",font=("Chalkboard SE",30),width=10,command=save_name,height=2,bg="#80deea",bd=3)
    button.place(x=screen_width/6,y=400)


    nameWindow.resizable(True,True)
    nameWindow.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 6000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    askPlayerName()

setup()