from tkinter import*
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
import os
import shutil
import read_files
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DragDrop(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.on_drop)

    def on_drop(self, event):
        files = self.tk.splitlist(event.data)
        if files:
            print("Dropped files:", files)

            # Display the dropped files on the screen
            y_position = 200
            for file_path in files:
                display_text = os.path.basename(file_path)
                self.create_text(200, y_position, text=display_text, fill="black", anchor="center", font=("Arial", 12))
                y_position += 20

                # Save only .csv files to a folder
                if file_path.lower().endswith('.csv'):
                    save_folder = r"C:\Users\milas\Desktop\Report\uploads"
                    os.makedirs(save_folder, exist_ok=True)
                    save_path = os.path.join(save_folder, os.path.basename(file_path))

                    print(f"Copying file from: {file_path}")
                    print(f"Saving file to: {save_path}")

                    try:
                        shutil.copy(file_path, save_path)
                        print("File copied successfully!")
                    except Exception as e:
                        print(f"Error copying file: {e}")
                else:
                    print(f"Skipped non-.csv file: {file_path}")
            if isinstance(frames['current'], startGUI):
                for file_path in files:
                    folder_path = 'C:/Users/milas/Desktop/Report/uploads'
                    read_files.read_files_in_folder(folder_path)
            if isinstance(frames['current'], reimportGUI):
                for file_path in files:
                    folder_path = 'C:/Users/milas/Desktop/Report/uploads'