from tkinter import*
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
import os
import shutil
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import DragDrop

absolute_path = os.path.dirname(__file__)
absolute_path = absolute_path.replace("\\", "/")

startimage_image_1 = PhotoImage(file=os.path.join(absolute_path, "start/image_1.png"))
startimage_image_2 = PhotoImage(file=os.path.join(absolute_path,"start/image_2.png"))
startimage_image_3 = PhotoImage(file=os.path.join(absolute_path,"start/image_3.png"))
startbutton_image_1 = PhotoImage(file=os.path.join(absolute_path,"start/button_1.png"))
startbutton_image_2 = PhotoImage(file=os.path.join(absolute_path,"start/button_2.png"))
startbutton_image_3 = PhotoImage(file=os.path.join(absolute_path,"start/button_3.png"))

class startGUI:
    def __init__(self, master, show_frame):
        self.master = master
        self.show_frame = show_frame

        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)

        self.canvas = DragDrop.DragDrop(
            self.frame,
            bg="#FFFFFF",
            height=682,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        
        self.canvas.pack(fill="both", expand=True)
        image_1 = self.canvas.create_image(
            512.0,
            341.0,
            image=startimage_image_1
        )

        button_1 = Button(
            image=startbutton_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: show_frame('analysis'),
            relief="flat"
        )
        button_1.place(
            x=657.5,
            y=135.0,
            width=285.5,
            height=48.5
        )

        button_2 = Button(
            image=startbutton_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: show_frame("reimport"),
            relief="flat"
        )
        button_2.place(
            x=657.5,
            y=214.5,
            width=285.5,
            height=48.5
        )

        button_3 = Button(
            image=startbutton_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=657.5,
            y=299.0,
            width=285.5,
            height=48.5
        )

        image_2 = self.canvas.create_image(
            730.0,
            526.5,
            image=startimage_image_2
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1024.0,
            98.5,
            fill="#0033B8",
            outline="")

        self.canvas.create_text(
            27.5,
            30.0,
            anchor="nw",
            text="PIK-APP for 350B2",
            fill="#FFFFFF",
            font=("InriaSans Regular", 30 * -1)
        )

        self.canvas.create_rectangle(
            31.5,
            135.0,
            339.5,
            638.5,
            fill="#AAAAAA",
            outline="")

        image_3 = self.canvas.create_image(
            79.5,
            161.0,
            image=startimage_image_3
        )

        self.canvas.create_text(
            110.5,
            149.5,
            anchor="nw",
            text="drag here to import\n",
            fill="#000000",
            font=("InriaSans Regular", 15 * -1)
        )
        
        self.canvas.dnd_bind('<<Drop>>', self.canvas.on_drop)
        
        self.canvas.place(x=0, y=0)
    def destroy(self):
        self.frame.destroy()