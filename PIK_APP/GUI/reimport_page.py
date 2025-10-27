import os
from tkinter import Frame, Button, PhotoImage
from .dragdrop import DragDrop
from core import rewrite_files

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ASSETS_PATH = os.path.join(ROOT_DIR, "assets")
ASSETS_PATH = ASSETS_PATH.replace("\\", "/")

class ReimportGUI:
    def __init__(self, master, show_frame):
        self.master = master
        self.show_frame = show_frame
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)

        # Load image assets
        self.image_bg = PhotoImage(file=os.path.join(ASSETS_PATH, "reimport/image_1.png"))
        self.button_1_img = PhotoImage(file=os.path.join(ASSETS_PATH, "reimport/button_1.png"))
        self.button_2_img = PhotoImage(file=os.path.join(ASSETS_PATH, "reimport/button_2.png"))

        self.canvas = DragDrop(
            self.frame,
            bg="#FFFFFF",
            height=682,
            width=1024,
            on_files_dropped=self.handle_files_dropped
        )
        self.canvas.pack(fill="both", expand=True)

        Button(
            image=self.button_1_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: rewrite_files.rewriting_files(),
            relief="flat"
        ).place(x=502.0, y=222.0, width=368.0, height=64.0)

        Button(
            image=self.button_2_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: show_frame('start'),
            relief="flat"
        ).place(x=754.0, y=25.0, width=253.0, height=48.0)

    def handle_files_dropped(self, files):
        print("Reimport dropped:", files)
        folder_path = r"C:\Users\milas\Desktop\Report\uploads"
        # add handling if needed

    def destroy(self):
        self.frame.destroy()
