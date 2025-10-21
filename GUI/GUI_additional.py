from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class analysis_failure:
    canvas.create_rectangle(
        601.0,
        117.0,
        1000.0,
        358.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        750.0,
        130.0,
        anchor="nw",
        text="FAILURES",
        fill="#C43746",
        font=("InriaSans Regular", 16 * -1)
    )

    canvas.create_text(
        633.0,
        161.0,
        anchor="nw",
        text="Choose if you want to see the graphs or outputs",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
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

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
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
    
class analysis_other:
    canvas.create_rectangle(
        601.0,
        117.0,
        1000.0,
        358.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        750.0,
        130.0,
        anchor="nw",
        text="OTHER",
        fill="#C43746",
        font=("InriaSans Regular", 16 * -1)
    )

    canvas.create_text(
        633.0,
        161.0,
        anchor="nw",
        text="Choose if you want to see the graphs or export",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
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

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
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

class analysis_space_menu:
    canvas.create_rectangle(
        601.0,
        117.0,
        1000.0,
        358.0,
        fill="#D9D9D9",
        outline="")