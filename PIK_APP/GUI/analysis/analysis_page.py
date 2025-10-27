from tkinter import Frame, Canvas, Button, Label, Entry, OptionMenu, StringVar, RIDGE, PhotoImage
import tkinter as tk
import os
from core import analysis
from core import export_csv

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ASSETS_PATH = os.path.join(ROOT_DIR, "assets")
ASSETS_PATH = ASSETS_PATH.replace("\\", "/")

class AnalysisGUI:
    def __init__(self, master, show_frame):
        self.master = master
        self.show_frame = show_frame
        self.selected_value = None

        self.analysisimage_image_1 = PhotoImage(file= os.path.join(ASSETS_PATH,"analysis/image_1.png"))
        self.analysisbutton_image_1 = PhotoImage(file= os.path.join(ASSETS_PATH,"analysis/button_1.png"))
        self.analysisbutton_image_2 = PhotoImage(file= os.path.join(ASSETS_PATH,"analysis/button_2.png"))
        self.analysisbutton_image_3 = PhotoImage(file= os.path.join(ASSETS_PATH,"analysis/button_3.png"))

        self.analysis_failures_image1 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_failures/image_1.png"))
        self.analysis_failures_button1 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_failures/button_1.png"))
        self.analysis_failures_button2 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_failures/button_2.png"))
        self.analysis_failures_button3 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_failures/button_3.png"))

        self.analysis_other_image1 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_others/image_1.png"))
        self.analysis_other_button1 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_others/button_1.png"))
        self.analysis_other_button2 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_others/button_2.png"))
        self.analysis_other_button3 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_others/button_3.png"))


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
        self.output_frame = Frame(self.canvas, bg="#D9D9D9")
        self.output_frame.place(x=27.0, y=117.0, width=550.0, height=550.0,)
        self.widgets_list = []
        self.change_canvas(self.current_option)
        self.result_label = None

        image_1 = self.canvas.create_image(
            804.0,
            539.0,
            image = self.analysisimage_image_1
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
            image = self.analysisbutton_image_1,
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
                image = self.analysisbutton_image_2,
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
                image = self.analysisbutton_image_3,
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
                image = self.analysis_failures_button2,
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
                image = self.analysis_failures_button3,
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
                image = self.analysis_other_button2,
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
                image = self.analysis_other_button3,
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
        for widget in self.widgets_list:
            widget.destroy()
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
                command=lambda: analysis.overlimits_flight(self.output_frame, data_entry_from.get(), data_entry_to.get()),
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
                command=lambda: analysis.overlimits_date(self.output_frame, data_entry_from.get(), data_entry_to.get()),
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
                command=lambda: analysis.error_fn(self.output_frame, data_entry_from.get(), data_entry_to.get()),
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
                command=lambda: analysis.error_dates(self.output_frame, data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)

#have to correct this here!!!!!!
    def failure_outputs(self, option):
        if option == "error_date":
            entry_label = Label(self.canvas, text="Error on date (Y-M-D):")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            go_button = Button(
                text="Go",
                command=lambda: self.display_error_date_output(data_entry_from.get()),
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
                command=lambda: self.display_error_dates_output(data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
        if option == "error_code_data":
            option_map = analysis.errors_code_selection()
            selected_option = StringVar()
            selected_option.set(list(option_map.keys())[0])  # Set the default option
            drop_down_menu = OptionMenu(self.canvas, selected_option, *option_map.keys())
            drop_down_menu.place(x=750, y=270)  # Adjust the position as needed

            def on_option_change(*args):
                selected_display_text = selected_option.get()
                self.selected_value = option_map.get(selected_display_text)
                print(f"Selected option: {selected_display_text}, Value: {self.selected_value}")
                # Now you can use 'selected_value' in your function

            selected_option.trace_add("write", on_option_change)

            # Add a "Go" button
            go_button = Button(
                text="Go",
                command=lambda: analysis.error_code_data(self.selected_value),
                relief="flat"
            )
            go_button.place(x=950, y=300)
        if option == "error_code_flight":
            option_map = analysis.errors_code_selection()
            selected_option = StringVar()
            selected_option.set(list(option_map.keys())[0])  # Set the default option
            drop_down_menu = OptionMenu(self.canvas, selected_option, *option_map.keys())
            drop_down_menu.place(x=750, y=270)  # Adjust the position as needed

            def on_option_change(*args):
                selected_display_text = selected_option.get()
                self.selected_value = option_map.get(selected_display_text)
                print(f"Selected option: {selected_display_text}, Value: {self.selected_value}")
                # Now you can use 'selected_value' in your function

            selected_option.trace_add("write", on_option_change)

            # Add a "Go" button
            go_button = Button(
                text="Go",
                command=lambda: self.display_error_flight_output(self.selected_value),
                relief="flat"
            )
            go_button.place(x=950, y=300)

    def display_error_flight_output(self, code):
        if self.result_label:
            self.result_label.destroy()

        # Call the analysis function to get the result
        df3 = analysis.error_code_flight(code)

        # Define column widths
        column_widths = [10, 30, 20]  # You can adjust these values as needed

        # Display column names for the DataFrame
        for col, (col_name, width) in enumerate(zip(df3.columns, column_widths)):
            label = Label(self.output_frame, text=col_name, relief=tk.RIDGE, width=width)
            label.grid(row=1, column=col, padx=5, pady=5, sticky="nsew")
            self.widgets_list.append(label)

        # Display data from the DataFrame
        for row, row_data in df3.iterrows():
            for col, (value, width) in enumerate(zip(row_data, column_widths)):
                label = Label(self.output_frame, text=str(value), width=width)
                label.grid(row=row + 2, column=col, padx=5, pady=5, sticky="nsew")
                self.widgets_list.append(label)

    def display_error_date_output(self, data):
        if self.result_label:
            self.result_label.destroy()

        # Destroy other widgets if needed
        for widget in self.widgets_list:
            widget.destroy()

        # Call the analysis function to get the result
        df3 = analysis.error_date_output(data)
        # Define column widths
        column_widths = [10, 20, 35]  # You can adjust these values as needed

        # Display column names for the DataFrame
        for col, (col_name, width) in enumerate(zip(df3.columns, column_widths)):
            label = Label(self.output_frame, text=col_name, relief=tk.RIDGE, width=width)
            label.grid(row=1, column=col, padx=5, pady=5, sticky="nsew")
            self.widgets_list.append(label)

        # Display data from the DataFrame
        for row, row_data in df3.iterrows():
            for col, (value, width) in enumerate(zip(row_data, column_widths)):
                label = Label(self.output_frame, text=str(value), width=width)
                label.grid(row=row + 2, column=col, padx=5, pady=5, sticky="nsew")
                self.widgets_list.append(label)

#everything works but the cleaning up is a bit iffy and a bit unpredictable. sometimes it works sometimes not
    def display_error_dates_output(self, data_from, data_to):
        if self.result_label:
            self.result_label.destroy()

        # Call the analysis function to get the result
        result_string, df3 = analysis.error_dates_output(data_from, data_to)

        # Display the result string
        label_result = Label(self.output_frame, text=result_string, relief=tk.RIDGE, width=60)
        label_result.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")
        self.widgets_list.append(label_result)

        # Define column widths
        column_widths = [10, 20, 35]  # You can adjust these values as needed

        # Display column names for the DataFrame
        for col, (col_name, width) in enumerate(zip(df3.columns, column_widths)):
            label = Label(self.output_frame, text=col_name, relief=tk.RIDGE, width=width)
            label.grid(row=1, column=col, padx=5, pady=5, sticky="nsew")
            self.widgets_list.append(label)

        # Display data from the DataFrame
        for row, row_data in df3.iterrows():
            for col, (value, width) in enumerate(zip(row_data, column_widths)):
                label = Label(self.output_frame, text=str(value), width=width)
                label.grid(row=row + 2, column=col, padx=5, pady=5, sticky="nsew")
                self.widgets_list.append(label)

    def other_graphs(self, option):
        if option == "fd_date":
            entry_label = Label(self.canvas, text="Date (Y-M-D):")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            go_button = Button(
                text="Go",
                command=lambda: analysis.date_flightTime(self.output_frame, data_entry_from.get()),
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
                command=lambda: analysis.time_per_day(self.output_frame, data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
        if option == "engCyc_fn":
            entry_label = Label(self.canvas, text="From Flight:")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            entry_label = Label(self.canvas, text="To flight:")
            entry_label.place(x=650, y=300)
            data_entry_to = Entry(self.canvas)
            data_entry_to.place(x=800, y=300)
            
            go_button = Button(
                text="Go",
                command=lambda: analysis.engineCyc_fn(self.output_frame, data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
        if option == "engCyc_date":
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
                command=lambda: analysis.engineCyc_date(self.output_frame, data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)

    def other_export(self, option):
        if option == "fn":
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
                command=lambda: export_csv.export_to_csv_fn_from_to(data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
        if option == "fn_spec":
            entry_label = Label(self.canvas, text="flight number:")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            go_button = Button(
                text="Go",
                command=lambda: export_csv.export_to_csv_fn(data_entry_from.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
#here also check which errors we have in database and make a drop down menu!
        if option == "error":
            option_map = analysis.errors_code_selection()
            selected_option = StringVar()
            selected_option.set(list(option_map.keys())[0])  # Set the default option
            drop_down_menu = OptionMenu(self.canvas, selected_option, *option_map.keys())
            drop_down_menu.place(x=750, y=270)  # Adjust the position as needed

            def on_option_change(*args):
                selected_display_text = selected_option.get()
                self.selected_value = option_map.get(selected_display_text)
                print(f"Selected option: {selected_display_text}, Value: {self.selected_value}")
                # Now you can use 'selected_value' in your function

            selected_option.trace_add("write", on_option_change)

            # Add a "Go" button
            go_button = Button(
                text="Go",
                command=lambda: export_csv.error_number(self.selected_value),
                relief="flat"
            )
            
#here a problem if another one got chosen before... clean canvas!
            go_button.place(x=950, y=300)
        if option == "dates":
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
                command=lambda: export_csv.export_fn_date_to_from(data_entry_from.get(), data_entry_to.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
        if option == "date_spec":
            entry_label = Label(self.canvas, text="date:")
            entry_label.place(x=650, y=270)
            data_entry_from = Entry(self.canvas)
            data_entry_from.place(x=800, y=270)
            
            go_button = Button(
                text="Go",
                command=lambda: export_csv.export_fn_date_spec(data_entry_from.get()),
                relief="flat"
            )
            go_button.place(x=950, y=300)
    
    def show_output(self, date_from, date_to):
        result_text = analysis.error_dates_output(date_from, date_to)

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

