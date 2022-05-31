# NAMA  : SAUL SAYERS
# NIM   : 13520094
# TASK 7 SELEKSI ASISTEN IRK

# FILE INI MERUPAKAN FILE UNTUK MAIN PAGE DARI GUI

import networkx as nx
import pylab
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import matplotlib
import matplotlib.pyplot as plt
import pylab
from tkinter import *
from tkinter.ttk import *
from graph import *
import os
from tkinter.filedialog import askopenfile 

def btn_clicked():
    pass

def mencoba():
    print("TES")

class MainPage(Frame):
    
    '''
    Initializes main component
    '''
    def __init__(self, parent, controller, frames):
        Frame.__init__(self, parent)
        self.controller = controller
        self.frames = frames
        self.graf = Graph()
        self.container = Frame(self)
        self.container.pack(fill="both", expand=True)
        self.start = StringVar()
        self.end = StringVar()
        self.start.set("none") # default value
        self.end.set("none") # default value

        self.canvas = Canvas(
            self.container,
            bg = "#ffffff",
            height = 540,
            width = 960)
        self.canvas.place(x = 0, y = 0)
        self.canvas.pack(fill = "both", expand = True)

        self.background_img = PhotoImage(file = "asset/background.png")
        self.canvas.create_image(
            472.5, 282.0,
            image=self.background_img)

        self.img1 = PhotoImage(file = "asset/img1.png")
        b1 = Button(
            image = self.img1,
            command = lambda: [self.open_file()])

        b1.place(
            x = 741, y = 21,
            width = 91,
            height = 32)

        self.solusi = self.canvas.create_text(
            663.0, 460.5,
            text = "x1",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.step = self.canvas.create_text(
            435.0, 415.5,
            text = "x2",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.canvas.create_text(
            810.0, 415.5,
            text = "end: ",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.canvas.create_text(
            660.0, 415.5,
            text = "start: ",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.filename = self.canvas.create_text(
            560, 32.0,
            text = "filename",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.cost = self.canvas.create_text(
            580.0, 415.5,
            text = "x3",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.iteration = self.canvas.create_text(
            519.0, 516.5,
            text = "x4",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.time = self.canvas.create_text(
            840.0, 516.5,
            text = "x5",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        start_register_entry  = Entry(
            self.canvas,
            textvariable = self.start)

        start_register_entry.place(
            x = 700, y = 400,
            width = 60.0,
            height = 35)

        end_register_entry  = Entry(
            self.canvas,
            textvariable = self.end)

        end_register_entry.place(
            x = 850, y = 400,
            width = 60.0,
            height = 35)
        
        self.img0 = PhotoImage(file = "asset/img0.png")
        b0 = Button(
            image = self.img0,
            command =  lambda:
            [   self.solve(self.start.get(),self.end.get()),
                start_register_entry.delete(0,END),
                end_register_entry.delete(0,END)
            ],)

        b0.place(
            x = 840, y = 21,
            width = 87,
            height = 32)

    def open_file(self):
        plt.clf()
        file_path = askopenfile(mode='r', filetypes=[('Text Files', '*txt')])
        self.graf.readFileParameter(file_path.name)
        self.canvas.itemconfig(self.filename, text=os.path.basename(file_path.name))
        G = nx.DiGraph()
        temp = []
        for key in self.graf.Edges:
            for value in self.graf.Edges[key]:
                temp.append((key,value[0],value[1]))
        G.add_weighted_edges_from(temp)
        nx.draw(G,with_labels=True)
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        
        fig = plt.figure(plt.get_fignums()[0])
        fig.set_size_inches(6.5, 3)

        frm = Frame(self.container)
        frm.place(x=320, y = 55)
        canvas = FigureCanvasTkAgg(fig, master=frm)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        plt.close()

    def solve(self,start,end):
        if (start not in self.graf.Nodes) or (end not in self.graf.Nodes):
            self.canvas.itemconfig(self.step, text="none")
            self.canvas.itemconfig(self.solusi, text="start/end tidak ada")
            self.canvas.itemconfig(self.cost, text="none")
            self.canvas.itemconfig(self.iteration, text="none")
            self.canvas.itemconfig(self.time, text="none")
            return
        self.graf.Djiktra(start,end)
        if len(self.graf.Solution) == 0 :
            self.canvas.itemconfig(self.step, text="none")
            self.canvas.itemconfig(self.solusi, text="Tidak ditemukan rute")
            self.canvas.itemconfig(self.cost, text="none")
            return
        solusi = ""
        for i in range (len(self.graf.Solution)) :
            solusi += str(self.graf.Solution[i]) + "->"
        solusi= solusi[:-2]
        if len(self.graf.Solution) == 1:
            self.canvas.itemconfig(self.step, text="1")
            self.canvas.itemconfig(self.solusi, text=start)
            self.canvas.itemconfig(self.cost, text=self.graf.shortesttable[start][0])
        self.canvas.itemconfig(self.solusi, text=solusi)
        self.canvas.itemconfig(self.time, text= str(self.graf.ExecTime) + " s")
        self.canvas.itemconfig(self.iteration, text=self.graf.Iterations)
