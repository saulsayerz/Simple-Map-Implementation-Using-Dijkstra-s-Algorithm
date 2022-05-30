# NAMA  : SAUL SAYERS
# NIM   : 13520094
# TASK 7 SELEKSI ASISTEN IRK

# FILE INI MERUPAKAN FILE UNTUK MAIN PAGE DARI GUI

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 

class MainPage(Frame):
    
    '''
    Initializes main component
    '''
    def __init__(self, parent, controller, frames):
        Frame.__init__(self, parent)
        self.controller = controller
        self.frames = frames
        container = Frame(self)
        container.pack(fill="both", expand=True)

        self.canvas = Canvas(
            container,
            bg = "#ffffff",
            height = 540,
            width = 960,
            bd = 0)
        self.canvas.place(x = 0, y = 0)
        self.canvas.pack()

        background_img = PhotoImage(file = f"asset/background.png")
        self.canvas.create_image(
            472.5, 282.0,
            image=background_img)

        img0 = PhotoImage(file = f"asset/img0.png")
        b0 = Button(
            image = img0,
            command = self.btn_clicked())

        b0.place(
            x = 840, y = 21,
            width = 87,
            height = 32)

        img1 = PhotoImage(file = f"asset/img1.png")
        b1 = Button(
            image = img1,
            command = self.btn_clicked())

        b1.place(
            x = 505, y = 18,
            width = 317,
            height = 32)

        self.canvas.create_text(
            463.0, 469.5,
            text = "xxx",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.canvas.create_text(
            435.0, 426.5,
            text = "xxx",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.canvas.create_text(
            580.0, 426.5,
            text = "xxx",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.canvas.create_text(
            519.0, 525.5,
            text = "xxx",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.canvas.create_text(
            840.0, 525.5,
            text = "xxx",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

    def open_file(self):
        file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')])
        if file_path is not None:
            pass

    def btn_clicked(self):
        pass