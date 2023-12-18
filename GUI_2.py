from tkinter import*
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
import os
import shutil
import read_files

root = TkinterDnD.Tk()
root.geometry("1024x682")
root.configure(bg = "#FFFFFF")


startimage_image_1 = PhotoImage(file="C:/Users/krist/OneDrive/Desktop/Report/GUI/start/start_images/image_1.png")
startimage_image_2 = PhotoImage(file="C:/Users/krist/OneDrive/Desktop/Report/GUI/start/start_images/image_2.png")
startimage_image_3 = PhotoImage(file="C:/Users/krist/OneDrive/Desktop/Report/GUI/start/start_images/image_3.png")
startbutton_image_1 = PhotoImage(file="C:/Users/krist/OneDrive/Desktop/Report/GUI/start/start_images/button_1.png")
startbutton_image_2 = PhotoImage(file="C:/Users/krist/OneDrive/Desktop/Report/GUI/start/start_images/button_2.png")
startbutton_image_3 = PhotoImage(file="C:/Users/krist/OneDrive/Desktop/Report/GUI/start/start_images/button_3.png")

analysisimage_image_1 = PhotoImage(file= "C:/Users/krist/OneDrive/Desktop/Report/GUI/analysis/analysis_images/image_1.png")
analysisbutton_image_1 = PhotoImage(file= "C:/Users/krist/OneDrive/Desktop/Report/GUI/analysis/analysis_images/button_1.png")
analysisbutton_image_2 = PhotoImage(file= "C:/Users/krist/OneDrive/Desktop/Report/GUI/analysis/analysis_images/button_2.png")
analysisbutton_image_3 = PhotoImage(file= "C:/Users/krist/OneDrive/Desktop/Report/GUI/analysis/analysis_images/button_3.png")

reimportimage_image_1 = PhotoImage(file = "C:/Users/krist/OneDrive/Desktop/Report/GUI/reimport/reimport_images/image_1.png")
reimportimage_image_2 = PhotoImage(file = "C:/Users/krist/OneDrive/Desktop/Report/GUI/reimport/reimport_images/image_2.png")
reimportimage_image_3 = PhotoImage(file = "C:/Users/krist/OneDrive/Desktop/Report/GUI/reimport/reimport_images/image_3.png")
reimportbutton_image_1 = PhotoImage(file = "C:/Users/krist/OneDrive/Desktop/Report/GUI/reimport/reimport_images/button_1.png")
reimportbutton_image_2 = PhotoImage(file = "C:/Users/krist/OneDrive/Desktop/Report/GUI/reimport/reimport_images/button_2.png")
reimportbutton_image_3 = PhotoImage(file = "C:/Users/krist/OneDrive/Desktop/Report/GUI/reimport/reimport_images/button_3.png")

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
                    save_folder = r"C:\Users\krist\OneDrive\Desktop\Report\uploads"
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
            
            for file_path in files:
                folder_path = 'C:/Users/krist/OneDrive/Desktop/Report/uploads'
                read_files.read_files_in_folder(folder_path)

class startGUI:
    def __init__(self, master, show_frame):
        self.master = master
        self.show_frame = show_frame

        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)

        self.canvas = DragDrop(
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

class analysisGUI:
    def __init__(self, master, show_frame):
        self.master = master
        self.show_frame = show_frame

        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)

        self.canvas = Canvas(
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
            804.0,
            539.0,
            image=analysisimage_image_1
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

        button_1 = Button(
            image=analysisbutton_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: show_frame('start'),
            relief="flat"
        )
        button_1.place(
            x=754.0,
            y=25.0,
            width=253.0,
            height=48.0
        )

        self.canvas.create_rectangle(
            27.0,
            117.0,
            577.0,
            667.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            601.0,
            117.0,
            1000.0,
            358.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_text(
            644.0,
            125.0,
            anchor="nw",
            text="ANALYSIS TOOLS",
            fill="#C43746",
            font=("InriaSans Regular", 16 * -1)
        )

        self.canvas.create_text(
            633.0,
            161.0,
            anchor="nw",
            text="Please choose if you want to check Failures or other\n things you want to analyse.",
            fill="#000000",
            font=("InriaSans Regular", 15 * -1)
        )

        button_2 = Button(
            image=analysisbutton_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=823.0,
            y=259.0,
            width=165.0,
            height=50.0
        )

        button_3 = Button(
            image=analysisbutton_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=636.0,
            y=259.0,
            width=165.0,
            height=50.0
        )
        
        self.canvas.place(x=0, y=0)
    def destroy(self):
        self.frame.destroy()

class reimportGUI:
    def __init__(self, master, show_frame):
        self.master = master
        self.show_frame = show_frame

        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)

        self.canvas = Canvas(
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
            683.0,
            518.0,
            image=reimportimage_image_1
        )

        button_1 = Button(
            image=reimportbutton_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=502.0,
            y=222.0,
            width=368.0,
            height=64.0
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

        button_2 = Button(
            image=reimportbutton_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: show_frame('start'),
            relief="flat"
        )
        button_2.place(
            x=754.0,
            y=25.0,
            width=253.0,
            height=48.0
        )

        self.canvas.create_rectangle(
            51.0,
            134.0,
            359.0,
            637.5,
            fill="#AAAAAA",
            outline="")

        image_2 = self.canvas.create_image(
            99.0,
            160.0,
            image=reimportimage_image_2
        )

        self.canvas.create_text(
            130.0,
            148.5,
            anchor="nw",
            text="drag here to import\n",
            fill="#000000",
            font=("InriaSans Regular", 15 * -1)
        )

        self.canvas.create_rectangle(
            423.0,
            134.0,
            946.0,
            199.0,
            fill="#C43645",
            outline="")

        self.canvas.create_text(
            452.0,
            149.0,
            anchor="nw",
            text="WARNING! If you change a file you will have to reimport it here again! \nReimporting deletes the previous file and changes the data in database!",
            fill="#FFFFFF",
            font=("Inter", 14 * -1)
        )
        
        self.canvas.place(x=0, y=0)
        
    def destroy(self):
        self.frame.destroy()

frames = {
    'start': startGUI,
    'analysis': analysisGUI,
    'reimport': reimportGUI,
    'current': None
}

def show_frame(page_name):
    if frames['current']:
        frames['current'].destroy()

    # Update the current frame
    frames['current'] = frames[page_name](root, lambda page=page_name: show_frame(page))

frames['current'] = frames['start'](root, lambda page='start': show_frame(page))

root.protocol("WM_DELETE_WINDOW", root.destroy)
root.mainloop()