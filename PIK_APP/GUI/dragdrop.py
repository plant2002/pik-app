import os
import shutil
import tkinter as tk
from tkinterdnd2 import DND_FILES

class DragDrop(tk.Canvas):
    def __init__(self, master=None, on_files_dropped=None, **kwargs):
        """
        Reusable drag-and-drop widget.
        :param on_files_dropped: callback function(files: list[str]) -> None
        """
        super().__init__(master, **kwargs)
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self._on_drop)
        self.on_files_dropped = on_files_dropped  # Store callback

    def _on_drop(self, event):
        files = self.tk.splitlist(event.data)
        if not files:
            return

        y_position = 200
        for file_path in files:
            display_text = os.path.basename(file_path)
            self.create_text(
                200, y_position, text=display_text,
                fill="black", anchor="center", font=("Arial", 12)
            )
            y_position += 20

            # Save only CSVs
            if file_path.lower().endswith('.csv'):
                save_folder = r"C:\Users\milas\Desktop\Report\uploads"
                os.makedirs(save_folder, exist_ok=True)
                save_path = os.path.join(save_folder, os.path.basename(file_path))
                try:
                    shutil.copy(file_path, save_path)
                    print(f"✅ Copied file: {save_path}")
                except Exception as e:
                    print(f"⚠️ Error copying {file_path}: {e}")
            else:
                print(f"Skipped non-CSV file: {file_path}")

        #  Notify the parent GUI
        if self.on_files_dropped:
            self.on_files_dropped(files)
