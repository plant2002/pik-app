from tkinter import Button, Label, Entry, StringVar, OptionMenu, PhotoImage
import os
import tkinter as tk

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
ASSETS_PATH = os.path.join(ROOT_DIR, "assets")
ASSETS_PATH = ASSETS_PATH.replace("\\", "/")

class FailuresSection:
    def __init__(self, parent_frame, analysis_functions):
        self.parent_frame = parent_frame
        self.af = analysis_functions
        self.frame = tk.Frame(parent_frame, bg="#D9D9D9")  # section container

        self.analysis_failures_image1 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_failures/image_1.png"))
        self.analysis_failures_button1 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_failures/button_1.png"))
        self.analysis_failures_button2 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_failures/button_2.png"))
        self.analysis_failures_button3 = PhotoImage(file = os.path.join(ASSETS_PATH,"analysis/analysis_failures/button_3.png"))

    def build(self):
        self.frame.pack(fill="both", expand=True)
        Label(self.frame, text="FAILURES SECTION", font=("Arial", 18)).pack(pady=10)

        options_map = {
            "Overlimits per Flight": "ovr_flight",
            "Overlimits per Date": "ovr_date",
            "Errors per Flight": "error_fn",
            "Errors per Date": "error_dates",
        }

        selected_option = StringVar(value=list(options_map.keys())[0])
        OptionMenu(self.frame, selected_option, *options_map.keys()).pack(pady=5)

        Button(
            self.frame,
            text="Go",
            command=lambda: self.run(selected_option.get(), options_map)
        ).pack(pady=5)

    def run(self, selected_display_text, options_map):
        option = options_map[selected_display_text]
        # Example call: pass the parent_frame to analysis functions
        if option == "ovr_flight":
            self.af.overlimits_flight(self.parent_frame, 100, 120)
        elif option == "ovr_date":
            self.af.overlimits_date(self.parent_frame, "2025-01-01", "2025-01-10")

    def destroy(self):
        self.frame.destroy()
