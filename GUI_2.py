from tkinter import*
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
import os
import shutil
import read_files
import rewrite_files
import analysis_functions
import export_csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
analysis_failures_image1 = PhotoImage(file = "C:/Users/krist/OneDrive/Desktop/Report/GUI/GUI_additional/analysis_failures/image_1.png")
analysis_failures_button1 = PhotoImage(file = "C:/Users/krist/OneDrive/Desktop/Report/GUI/GUI_additional/analysis_failures/button_1.png")
analysis_failures_button2 = PhotoImage(file = "C:/Users/krist/OneDrive/Desktop/Report/GUI/GUI_additional/analysis_failures/button_2.png")
analysis_failures_button3 = PhotoImage(file = "C:/Users/krist/OneDrive/Desktop/Report/GUI/GUI_additional/analysis_failures/button_3.png")
analysis_other_image1 = PhotoImage(file = "C:/Users/krist/OneDrive/Desktop/Report/GUI/GUI_additional/analysis_others/image_1.png")
analysis_other_button1 = PhotoImage(file = "C:/Users/krist/OneDrive/Desktop/Report/GUI/GUI_additional/analysis_others/button_1.png")
analysis_other_button2 = PhotoImage(file = "C:/Users/krist/OneDrive/Desktop/Report/GUI/GUI_additional/analysis_others/button_2.png")
analysis_other_button3 = PhotoImage(file = "C:/Users/krist/OneDrive/Desktop/Report/GUI/GUI_additional/analysis_others/button_3.png")

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
            if isinstance(frames['current'], startGUI):
                for file_path in files:
                    folder_path = 'C:/Users/krist/OneDrive/Desktop/Report/uploads'
                    read_files.read_files_in_folder(folder_path)
            if isinstance(frames['current'], reimportGUI):
                for file_path in files:
                    folder_path = 'C:/Users/krist/OneDrive/Desktop/Report/uploads'

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
        self.selected_value = None

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
        self.current_option = "Basics"
        self.content_frame = Frame(self.canvas, bg="#D9D9D9")
        self.content_frame.place(x=601.0, y=117.0, width=399.0, height=240.0)
        self.widgets_list = []
        self.change_canvas(self.current_option)

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

        
        self.canvas.place(x=0, y=0)
    
    def change_canvas(self, option):
        for widget in self.widgets_list:
            widget.destroy()

        self.widgets_list = []
        canvas = Canvas(self.content_frame, bg="#D9D9D9", width=399.0, height=240.0)
        canvas.pack(fill="both", expand=True)
        
        if option == "Basics":
            canvas.create_text(
            150.0,
            8.0,
            anchor="nw",
            text="ANALYSIS TOOLS",
            fill="#C43746",
            font=("InriaSans Regular", 16 * -1)
            )

            canvas.create_text(
                40.0,
                44.0,
                anchor="nw",
                text="Please choose if you want to check Failures or other\n things you want to analyse.",
                fill="#000000",
                font=("InriaSans Regular", 15 * -1)
            )

            button_2 = Button(
                image=analysisbutton_image_2,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.change_canvas("Other"),
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
                command=lambda: self.change_canvas("Failures"),
                relief="flat"
            )
            button_3.place(
                x=636.0,
                y=259.0,
                width=165.0,
                height=50.0
            )
            self.widgets_list.extend([button_2, button_3, canvas])
        #failures
        if option == "Failures":

            canvas.create_text(
                149.0,
                13.0,
                anchor="nw",
                text="FAILURES",
                fill="#C43746",
                font=("InriaSans Regular", 16 * -1)
            )

            canvas.create_text(
                32.0,
                44.0,
                anchor="nw",
                text="Choose if you want to see the graphs or outputs",
                fill="#000000",
                font=("InriaSans Regular", 15 * -1)
            )

            button_2 = Button(
                image=analysis_failures_button2,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.change_canvas("AnalysisFailOutput"),
                relief="flat"
            )
            button_2.place(
                x=823.0,
                y=259.0,
                width=165.0,
                height=50.0
            )

            button_3 = Button(
                image=analysis_failures_button3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.change_canvas("AnalysisFailGraph"),
                relief="flat"
            )
            button_3.place(
                x=636.0,
                y=259.0,
                width=165.0,
                height=50.0
            )
            self.widgets_list.extend([button_2, button_3, canvas])
        #other
        elif option == "Other":
            canvas.create_rectangle(
                601.0,
                117.0,
                1000.0,
                358.0,
                fill="#D9D9D9",
                outline="")

            canvas.create_text(
                149.0,
                13.0,
                anchor="nw",
                text="OTHER",
                fill="#C43746",
                font=("InriaSans Regular", 16 * -1)
            )

            canvas.create_text(
                32.0,
                44.0,
                anchor="nw",
                text="Choose if you want to see the graphs or export",
                fill="#000000",
                font=("InriaSans Regular", 15 * -1)
            )

            button_2 = Button(
                image=analysis_other_button2,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.change_canvas("AnalysisOtherExport"),
                relief="flat"
            )
            button_2.place(
                x=823.0,
                y=259.0,
                width=165.0,
                height=50.0
            )

            button_3 = Button(
                image=analysis_other_button3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.change_canvas("AnalysisOtherGraph"),
                relief="flat"
            )
            button_3.place(
                x=636.0,
                y=259.0,
                width=165.0,
                height=50.0
            )
            self.widgets_list.extend([button_2, button_3, canvas])
            
        if option == "AnalysisFailGraph":
            canvas.create_rectangle(
                601.0,
                117.0,
                1000.0,
                358.0,
                fill="#D9D9D9",
                outline="")
            canvas.create_text(
                149.0,
                13.0,
                anchor="nw",
                text="FAILURES - GRAPHS",
                fill="#C43746",
                font=("InriaSans Regular", 16 * -1)
            )
            
            options_map = {
                "Graphs of overlimits/flights" : "ovr_flight",
                "Graphs of overlimits/dates" : "ovr_date",
                "Graphs of occurrences of errors/flights" : "errorfn_occr",
                "Graphs of errors/dates" : "error_dates",
            }
            
            selected_option = StringVar()
            selected_option.set(list(options_map.keys())[0])  # Set the default option
            drop_down_menu = OptionMenu(canvas, selected_option, *options_map.keys())
            drop_down_menu.place(x=100, y=100)  # Adjust the position as needed

            def on_option_change(*args):
                selected_display_text = selected_option.get()
                self.selected_value = options_map.get(selected_display_text)
                print(f"Selected option: {selected_display_text}, Value: {self.selected_value}")
                # Now you can use 'selected_value' in your function

            selected_option.trace_add("write", on_option_change)

            # Add a "Go" button
            go_button = Button(
                text="Go",
                command=lambda: self.failure_graphs(self.selected_value),
                relief="flat"
            )
            go_button.place(x=900, y=217)
            
            self.widgets_list.extend([go_button, drop_down_menu, canvas])
            
        if option == "AnalysisOtherGraph":
            canvas.create_rectangle(
                601.0,
                117.0,
                1000.0,
                358.0,
                fill="#D9D9D9",
                outline="")
            canvas.create_text(
                149.0,
                13.0,
                anchor="nw",
                text="OTHER - GRAPHS",
                fill="#C43746",
                font=("InriaSans Regular", 16 * -1))

            options_map = {
                "Graph of flightime/date" : "fd_date",
                "Graph of time/date" : "time_date",
                "Graph of engine Cycles/flight" : "engCyc_fn",
                "Graph of engine Cycles/date" : "engCyc_date",
            }
            
            selected_option = StringVar()
            selected_option.set(list(options_map.keys())[0])  # Set the default option
            drop_down_menu = OptionMenu(canvas, selected_option, *options_map.keys())
            drop_down_menu.place(x=100, y=100)  # Adjust the position as needed

            def on_option_change(*args):
                selected_display_text = selected_option.get()
                self.selected_value = options_map.get(selected_display_text)
                print(f"Selected option: {selected_display_text}, Value: {self.selected_value}")
                # Now you can use 'selected_value' in your function

            selected_option.trace_add("write", on_option_change)

            # Add a "Go" button
            go_button = Button(
                text="Go",
                command=lambda: self.other_graphs(self.selected_value),
                relief="flat"
            )
            go_button.place(x=900, y=217)
            self.widgets_list.extend([go_button,canvas])
            
        if option == "AnalysisOtherExport":
            canvas.create_rectangle(
                601.0,
                117.0,
                1000.0,
                358.0,
                fill="#D9D9D9",
                outline="")
            canvas.create_text(
                149.0,
                13.0,
                anchor="nw",
                text="OTHER - EXPORT",
                fill="#C43746",
                font=("InriaSans Regular", 16 * -1))
            self.widgets_list.extend([canvas])

            options_map = {
                "export data for flights" : "fn",
                "export data for specific flight" : "fn_spec",
                "export data of all flights with error" : "error",
                "export data for dates" : "dates",
                "export data for a specific date" : "date_spec",
            }
            
            selected_option = StringVar()
            selected_option.set(list(options_map.keys())[0])  # Set the default option
            drop_down_menu = OptionMenu(canvas, selected_option, *options_map.keys())
            drop_down_menu.place(x=100, y=100)  # Adjust the position as needed

            def on_option_change(*args):
                selected_display_text = selected_option.get()
                self.selected_value = options_map.get(selected_display_text)
                print(f"Selected option: {selected_display_text}, Value: {self.selected_value}")
                # Now you can use 'selected_value' in your function

            selected_option.trace_add("write", on_option_change)

            # Add a "Go" button
            go_button = Button(
                text="Go",
                command=lambda: self.other_export(self.selected_value),
                relief="flat"
            )
            go_button.place(x=900, y=217)
        if option == "AnalysisFailOutput":
            canvas.create_rectangle(
                601.0,
                117.0,
                1000.0,
                358.0,
                fill="#D9D9D9",
                outline="")
            canvas.create_text(
                149.0,
                13.0,
                anchor="nw",
                text="OTHER - OUTPUTS",
                fill="#C43746",
                font=("InriaSans Regular", 16 * -1))
            self.widgets_list.extend([canvas])

            options_map = {
                "Data error/date" : "error_date",
                "Data error/dates" : "error_dates",
                "Error code data" : "error_code_data",
                "Error code flight" : "error_code_flight",
            }
            
            selected_option = StringVar()
            selected_option.set(list(options_map.keys())[0])  # Set the default option
            drop_down_menu = OptionMenu(canvas, selected_option, *options_map.keys())
            drop_down_menu.place(x=100, y=100)  # Adjust the position as needed

            def on_option_change(*args):
                selected_display_text = selected_option.get()
                self.selected_value = options_map.get(selected_display_text)
                print(f"Selected option: {selected_display_text}, Value: {self.selected_value}")
                # Now you can use 'selected_value' in your function

            selected_option.trace_add("write", on_option_change)

            # Add a "Go" button
            go_button = Button(
                text="Go",
                command=lambda: self.failure_outputs(self.selected_value),
                relief="flat"
            )
            go_button.place(x=900, y=217)

            canvas.place(x=0, y=0)
    
    def failure_graphs(self, option):
        if option == "ovr_flight":
            entry_label = Label(self.canvas, text="Flight Number from:")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            entry_label = Label(self.canvas, text="Flight Number to:")
            entry_label.place(x=650, y=300)
            data_entry_to = Entry(self.canvas)
            data_entry_to.place(x=800, y=300)
            
            go_button = Button(
                text="Go",
                command=lambda: analysis_functions.overlimits_flight(data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
            
        if option == "ovr_date":
            entry_label = Label(self.canvas, text="Date from (Y-M-D):")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            entry_label = Label(self.canvas, text="Date to (Y-M-D):")
            entry_label.place(x=650, y=300)
            data_entry_to = Entry(self.canvas)
            data_entry_to.place(x=800, y=300)
            
            go_button = Button(
                text="Go",
                command=lambda: analysis_functions.overlimits_date(data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
        if option == "errorfn_occr":
            entry_label = Label(self.canvas, text="From Flight Number:")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            entry_label = Label(self.canvas, text="To Flight Number:")
            entry_label.place(x=650, y=300)
            data_entry_to = Entry(self.canvas)
            data_entry_to.place(x=800, y=300)
            
            go_button = Button(
                text="Go",
                command=lambda: analysis_functions.error_fn(data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
        if option == "error_dates":
            entry_label = Label(self.canvas, text="Dates from (Y-M-D):")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            entry_label = Label(self.canvas, text="Dates to (Y-M-D):")
            entry_label.place(x=650, y=300)
            data_entry_to = Entry(self.canvas)
            data_entry_to.place(x=800, y=300)
            
            go_button = Button(
                text="Go",
                command=lambda: analysis_functions.error_dates(data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)

    def failure_outputs(self, option):
        if option == "error_date":
            entry_label = Label(self.canvas, text="Error on date (Y-M-D):")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            go_button = Button(
                text="Go",
                command=lambda: analysis_functions.error_date_output(data_entry_from.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
        if option == "error_dates":
            entry_label = Label(self.canvas, text="From date (Y-M-D):")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            entry_label = Label(self.canvas, text="To date (Y-M-D):")
            entry_label.place(x=650, y=300)
            data_entry_to = Entry(self.canvas)
            data_entry_to.place(x=800, y=300)
            
            go_button = Button(
                text="Go",
                command=lambda: analysis_functions.error_dates_output(data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
        if option == "error_code_data":
#HERE
            entry_label = Label(self.canvas, text="From Flight Number:")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            entry_label = Label(self.canvas, text="To Flight Number:")
            entry_label.place(x=650, y=300)
            data_entry_to = Entry(self.canvas)
            data_entry_to.place(x=800, y=300)
            
            go_button = Button(
                text="Go",
                command=lambda: self.show_output(data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
        if option == "error_code_flight":
            entry_label = Label(self.canvas, text="From Flight Number:")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            entry_label = Label(self.canvas, text="To Flight Number:")
            entry_label.place(x=650, y=300)
            data_entry_to = Entry(self.canvas)
            data_entry_to.place(x=800, y=300)
            
            go_button = Button(
                text="Go",
                command=lambda: analysis_functions.error_fn(data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)

    def other_graphs(self, option):
        if option == "fd_date":
            entry_label = Label(self.canvas, text="Date (Y-M-D):")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            go_button = Button(
                text="Go",
                command=lambda: analysis_functions.date_flightTime(data_entry_from.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
        if option == "time_date":
            entry_label = Label(self.canvas, text="From date:")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            entry_label = Label(self.canvas, text="To date:")
            entry_label.place(x=650, y=300)
            data_entry_to = Entry(self.canvas)
            data_entry_to.place(x=800, y=300)
            
            go_button = Button(
                text="Go",
                command=lambda: analysis_functions.time_per_day(data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
        if option == "engCyc_fn":
            print("got to function")
        if option == "engCyc_date":
            print("got to function")

    def other_export(self, option):
        if option == "fn":
            print("got to function")
        if option == "fn_spec":
            print("got to function")
        if option == "error":
            print("got to function")
        if option == "dates":
            print("got to function")
        if option == "date_spec":
            print("got to function")
    
    def show_output(self, date_from, date_to):
        result_text = analysis_functions.error_dates_output(date_from, date_to)

        self.canvas.create_text(
            50,
            130,
            anchor="nw",
            text=result_text,
            fill="#FFFFFF",
            font=("InriaSans Regular", 30 * -1)
        )
    def destroy(self):
        self.frame.destroy()

class reimportGUI:
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
            683.0,
            518.0,
            image=reimportimage_image_1
        )

        button_1 = Button(
            image=reimportbutton_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: rewrite_files.rewriting_files(),
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
