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
            text = "",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.step = self.canvas.create_text(
            435.0, 415.5,
            text = "",
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
            text = "",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.iteration = self.canvas.create_text(
            519.0, 516.5,
            text = "",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.time = self.canvas.create_text(
            850.0, 512.5,
            text = "",
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

        b3 = Button(
            text = "Table",
            command =  lambda:
            [   self.djiktrapopup()
            ])

        b3.place(
            x = 650, y = 21,
            width = 87,
            height = 32)

    def open_file(self):
        plt.clf()
        file_path = askopenfile(mode='r', filetypes=[('Text Files', '*txt')])
        self.graf.readFileParameter(file_path.name)
        self.canvas.itemconfig(self.filename, text=os.path.basename(file_path.name))
        self.G = nx.DiGraph()
        for key in self.graf.Edges:
            for value in self.graf.Edges[key]:
                self.G.add_edge(key,value[0],color="black", weight=value[1])
        pos = nx.spring_layout(self.G,seed = 500)
        nx.draw(self.G,pos,with_labels=True,connectionstyle=f'arc3, rad = {0.1}')
        labels = nx.get_edge_attributes(self.G,'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels, label_pos=0.5, font_size=7)
        
        fig = plt.figure(plt.get_fignums()[0])
        fig.set_size_inches(6.5, 3)

        frm = Frame(self.container)
        frm.place(x=320, y = 55)
        canvas = FigureCanvasTkAgg(fig, master=frm)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        plt.close()

    def waithere(self,time):
        var = IntVar()
        self.after(time, var.set, 1)
        self.wait_variable(var)

    def djiktrapopup(self):
        top= Toplevel(self.controller)
        width = 350
        height = len(self.graf.visited)*40+30
        top.geometry(str(width) + "x" + str(height))
        top.title("Djiktra Table")
        self.labelpesan = Label(top, text= "", font=("Roboto", 10))
        self.labelpesan.pack()
        if len(self.graf.visited) == 0 :
            self.labelpesan.config(text = "TABEL PER STEP TIDAK TERSEDIA")
            return
        for i in range (len(self.graf.visited)+1):
            teks = "iterasi ke: " + str(i) + "\n\n"
            if i == 0 :
                teks += "current Node : " + "None"
                teks += "\n\nTabel djiktra: \n\n"
            else:
                teks += "current Node : " + self.graf.visited[i-1]
                teks += "\n\nTabel djiktra: \n\n"
            for key in self.graf.shortesttablestep[i]:
                teks += key + " : " + str(self.graf.shortesttablestep[i][key]) + "\n"
            self.labelpesan.config(text = teks)
            self.waithere(5000)

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

        # BAGIAN MENUNJUKKAN STEP DARI AWAL SAMPE AKHIR
        if len(self.graf.Solution) == 1:
            self.canvas.itemconfig(self.step, text="1")
            self.canvas.itemconfig(self.solusi, text=start)
            self.canvas.itemconfig(self.cost, text=self.graf.shortesttable[start][0])
        else:
            solusistepi = []
            for i in range (len(self.graf.Solution)):
                solusistepi.append([self.graf.Solution[i-1], self.graf.Solution[i]])
                self.canvas.itemconfig(self.step, text=str(i+1))
                self.canvas.itemconfig(self.cost, text=self.graf.shortesttable[self.graf.Solution[i]][0])
                solusi += str(self.graf.Solution[i]) 
                if i != len(self.graf.Solution)-1:
                    solusi += " -> "
                self.canvas.itemconfig(self.solusi, text=solusi)
                plt.clf()
                if i > 0 : 
                    for key in self.graf.Edges:
                        for value in self.graf.Edges[key]:
                            if ([key,value[0]] in solusistepi) :
                                self.G.add_edge(key,value[0],color='r',weight=value[1])
                            else:
                                self.G.add_edge(key,value[0],color="black", weight=value[1])
                else :
                    for key in self.graf.Edges:
                        for value in self.graf.Edges[key]:
                            self.G.add_edge(key,value[0],color='black',weight=value[1])
                edges = self.G.edges()
                colors = [self.G[u][v]['color'] for u,v in edges]

                pos = nx.spring_layout(self.G,seed = 500)
                nx.draw(self.G,pos,with_labels=True,connectionstyle=f'arc3, rad = {0.1}', edge_color=colors)
                
                labels = nx.get_edge_attributes(self.G,'weight')
                nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels, label_pos=0.3, font_size=7)
                # nx.draw_networkx_edge_labels(self.G,pos,edge_labels=weights)

                fig = plt.figure(plt.get_fignums()[0])
                fig.set_size_inches(6.5, 3)

                frm = Frame(self.container)
                frm.place(x=320, y = 55)
                canvas = FigureCanvasTkAgg(fig, master=frm)
                canvas.draw()
                canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
                plt.close()

                self.waithere(1500)
        self.canvas.itemconfig(self.time, text= "{:.3f}".format(self.graf.ExecTime) + " ms")
        self.canvas.itemconfig(self.iteration, text=self.graf.Iterations)

