#coffee app v2

#import
from cProfile import run
from telnetlib import LOGOUT
import tkinter as tk
from tkinter import LabelFrame, StringVar, Y, simpledialog
from tkinter.tix import IMAGETEXT
import tkinter.ttk as ttk
from tkinter import Frame, Image, PhotoImage, font as tkfont
import time
from turtle import bgcolor, width, window_height, window_width
from PIL import ImageTk,Image  

from setuptools import Command


#class def

class MainFrame(tk.Tk):
    #frame object holding all the pages
    #controller of the pages
    def __init__(self, *args, **kwargs) :
        tk.Tk.__init__(self, *args, **kwargs)

        
        #window size
        window_width = 385
        window_height = 660

        OffsetLeft = int((self.winfo_screenwidth() - window_width) / 2)
        OffsetTop = int((self.winfo_screenheight() - window_height) / 2)

        self.geometry('{}x{}+{}+{}'.format(window_width, window_height, OffsetLeft, OffsetTop))

        self.titlefont = tkfont.Font(family = "Bely Display", size = 50)

        self.buttonfont = tkfont.Font(family = "Menlo", size = 15)
        
        #putting all the frames into one container
        container = tk.Frame(self)
        container.grid(row = 0, column = 0, sticky = "nesw")
        container.pack_propagate()

        self.id = tk.StringVar()


        self.listing = {} #holding 2 arguments 

        for p in (WelcomePage, fw, moc, lat, cap, done):
            page_name = p.__name__
            frame = p(parent = container, controller = self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.listing[page_name] = frame
        
        self.up_frame('WelcomePage')
    


    def up_frame(self, page_name) : 
        page = self.listing[page_name]
        page.tkraise()


class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        self.configure(background="#815940")


        
        logo = tk.Button(self, fg = 'black', highlightbackground='#4A3223', text = "Ros Coffee", 
        font = controller.titlefont, command= lambda: controller.up_frame("fw"))
        logo.pack(padx= 60, pady= 300)


class fw(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id


    
        
        self.configure(background="#815940")


        self.cup = tk.PhotoImage(file="images/fw2.png")
        labelcup = tk.Label(self, image = self.cup, background="#815940")
        labelcup.pack()
        labelcup.place(x=62, y=100)

        

        

        fw = tk.Button(self, text = "Flat White", font = controller.buttonfont, command= lambda: controller.up_frame("fw"))
        fw.pack()

        fw.place(x = 145, y = 550)

        done = tk.Button(self, text = "Make!!!", font = controller.buttonfont, command= lambda: controller.up_frame("done"))
        done.pack()

        done.place(x = 155, y = 500)

        moc = tk.Button(self, text = "Mocha", font = controller.buttonfont, command= lambda: controller.up_frame("moc"))
        moc.pack()

        moc.place(x = 166, y = 620)

        lat = tk.Button(self, text = "Latte", font = controller.buttonfont, command= lambda: controller.up_frame("lat"))
        lat.pack()

        lat.place(x = 100, y = 585)

        cap = tk.Button(self, text = "Cappucino", font = controller.buttonfont, command= lambda: controller.up_frame("cap"))
        cap.pack()

        cap.place(x = 220, y = 585)


class moc(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        
        self.configure(background="#815940")

        self.cup = tk.PhotoImage(file="images/moc2.png")
        labelcup = tk.Label(self, image = self.cup, background="#815940")
        labelcup.pack()
        labelcup.place(x=62, y=100)


        fw = tk.Button(self, text = "Flat White", font = controller.buttonfont, command= lambda: controller.up_frame("fw"))
        fw.pack()

        fw.place(x = 145, y = 550)

        done = tk.Button(self, text = "Make!!!", font = controller.buttonfont, command= lambda: controller.up_frame("done"))
        done.pack()

        done.place(x = 155, y = 500)

        moc = tk.Button(self, text = "Mocha", font = controller.buttonfont, command= lambda: controller.up_frame("moc"))
        moc.pack()

        moc.place(x = 166, y = 620)

        lat = tk.Button(self, text = "Latte", font = controller.buttonfont, command= lambda: controller.up_frame("lat"))
        lat.pack()

        lat.place(x = 100, y = 585)

        cap = tk.Button(self, text = "Cappucino", font = controller.buttonfont, command= lambda: controller.up_frame("cap"))
        cap.pack()

        cap.place(x = 220, y = 585)


class lat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        
        self.configure(background="#815940")
        
        self.cup = tk.PhotoImage(file="images/lat2.png")
        labelcup = tk.Label(self, image = self.cup, background="#815940")
        labelcup.pack()
        labelcup.place(x=62, y=100)



        fw = tk.Button(self, text = "Flat White", font = controller.buttonfont, command= lambda: controller.up_frame("fw"))
        fw.pack()

        fw.place(x = 145, y = 550)

        done = tk.Button(self, text = "Make!!!", font = controller.buttonfont, command= lambda: controller.up_frame("done"))
        done.pack()

        done.place(x = 155, y = 500)

        moc = tk.Button(self, text = "Mocha", font = controller.buttonfont, command= lambda: controller.up_frame("moc"))
        moc.pack()

        moc.place(x = 166, y = 620)

        lat = tk.Button(self, text = "Latte", font = controller.buttonfont, command= lambda: controller.up_frame("lat"))
        lat.pack()

        lat.place(x = 100, y = 585)

        cap = tk.Button(self, text = "Cappucino", font = controller.buttonfont, command= lambda: controller.up_frame("cap"))
        cap.pack()

        cap.place(x = 220, y = 585)

class cap(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id


        
        self.configure(background="#815940")

        self.cup = tk.PhotoImage(file="images/cap2.png")
        labelcup = tk.Label(self, image = self.cup, background="#815940")
        labelcup.pack()
        labelcup.place(x=62, y=100)

    

        fw = tk.Button(self, text = "Flat White", font = controller.buttonfont, command= lambda: controller.up_frame("fw"))
        fw.pack()

        fw.place(x = 145, y = 550)


        done = tk.Button(self, text = "Make!!!", font = controller.buttonfont, command= lambda: controller.up_frame("done"))
        done.pack()

        done.place(x = 155, y = 500)

        moc = tk.Button(self, text = "Mocha", font = controller.buttonfont, command= lambda: controller.up_frame("moc"))
        moc.pack()

        moc.place(x = 166, y = 620)

        lat = tk.Button(self, text = "Latte", font = controller.buttonfont, command= lambda: controller.up_frame("lat"))
        lat.pack()

        lat.place(x = 100, y = 585)

        cap = tk.Button(self, text = "Cappucino", font = controller.buttonfont, command= lambda: controller.up_frame("cap"))
        cap.pack()

        cap.place(x = 220, y = 585)

class done(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id


    
        
        self.configure(background="#815940")


        self.cup = tk.PhotoImage(file="images/cup done.png")
        labelcup = tk.Label(self, image = self.cup, background="#815940")
        labelcup.pack()
        labelcup.place(x=62, y=100)

        restart = tk.Button(self, text = "restart?", font = controller.buttonfont, command= lambda: controller.up_frame("WelcomePage"))
        restart.pack()

        restart.place(x = 100, y = 585)

        gb = tk.Button(self, text = "go back?", font = controller.buttonfont, command= lambda: controller.up_frame("fw"))
        gb.pack()

        gb.place(x = 220, y = 585)



if __name__ == '__main__':
    app = MainFrame()
    app.mainloop()



    














        
        

    


    


