from tkinter import Button, Label, Entry, StringVar, OptionMenu, PhotoImage
import tkinter as tk
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
ASSETS_PATH = os.path.join(ROOT_DIR, "assets")
ASSETS_PATH = ASSETS_PATH.replace("\\", "/")

class OtherSection:
    def __init__(self, parent_frame, analysis_functions, export_functions):
        self.parent_frame = parent_frame
        self.af = analysis_functions
        self.ex = export_functions
        self.frame = tk.Frame(parent_frame, bg="#D9D9D9")

        self.analysis_other_image1 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_others/image_1.png"))
        self.analysis_other_button1 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_others/button_1.png"))
        self.analysis_other_button2 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_others/button_2.png"))
        self.analysis_other_button3 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_others/button_3.png"))

    def build(self):
        Label(self.canvas, text="OTHER SEARCH SECTION", font=("Arial", 18)).place(x=650, y=100)

        options_map = {
            "Overlimits per Flight": "ovr_flight",
            "Overlimits per Date": "ovr_date",
            "Errors per Flight": "error_fn",
            "Errors per Date": "error_dates",
        }

        selected_option = StringVar(value=list(options_map.keys())[0])
        OptionMenu(self.canvas, selected_option, *options_map.keys()).place(x=700, y=150)

        Button(
            text="Go",
            command=lambda: self.run(selected_option.get(), options_map),
        ).place(x=900, y=150)

    def run(self, selected_display_text, options_map):
        option = options_map[selected_display_text]
        if option == "ovr_flight":
            self.af.overlimits_flight(self.canvas, 100, 120)
        elif option == "ovr_date":
            self.af.overlimits_date(self.canvas, "2025-01-01", "2025-01-10")
