from tkinterdnd2 import TkinterDnD
from .start_page import StartGUI
from .analysis.main_page import AnalysisGUI
from .reimport_page import ReimportGUI

def launch_app():
    root = TkinterDnD.Tk()
    root.geometry("1024x682")
    root.configure(bg="#FFFFFF")

    frames = {}

    def show_frame(page_name):
        # Destroy current frame
        if frames.get('current'):
            frames['current'].destroy()

        # Pick the correct page class
        page_class = {
            'start': StartGUI,
            'analysis': AnalysisGUI,
            'reimport': ReimportGUI
        }[page_name]

        # Create and show the new page
        frames['current'] = page_class(root, show_frame)

    # Start with the start page
    show_frame('start')
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()
