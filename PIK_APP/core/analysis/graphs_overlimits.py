import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core import db_communication

#the overlimits per flight --> flightnmb_from to flightnmb_to
def overlimits_flight(frame, fn_from, fn_to):
    connection = db_communication.connect_to_database()

    sql = "SELECT FN, NRol, TRQol, Engol FROM basics WHERE FN BETWEEN %s AND %s"
    df = pd.read_sql(sql, connection[1], params=(fn_from, fn_to))
    
    if df.empty or df[['NRol', 'TRQol', 'Engol']].isnull().all().all():
        # Display a new window message if there is no data or only NULL values
        print("There is no data.")
    else:
        # Calculate the sum of 'NRol', 'TRQol', and 'Engol' for each flight
        df['Overlimits'] = df[['NRol', 'TRQol', 'Engol']].sum(axis=1)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(df['FN'], df['Overlimits'])
        ax.set_xticks(df['FN'])  # Set x-axis ticks to only existing flight numbers
        ax.set_xlabel('Flight Number (FN)')
        ax.set_ylabel('Sum of Overlimits')
        ax.set_title('Overlimits during Flight')

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas.draw()
    
    db_communication.close_connection(connection[1])

#the overlimits per flight --> date_from to date_to
def overlimits_date (frame, date_from, date_to):
    connection = db_communication.connect_to_database()

    sql = "SELECT FN, NRol, TRQol, Engol FROM basics WHERE DATE(GPSdt) BETWEEN %s AND %s"
    df = pd.read_sql(sql, connection[1], params=(date_from, date_to))
    
    if df.empty or df[['NRol', 'TRQol', 'Engol']].isnull().all().all():
        # Display a new window message if there is no data or only NULL values
        print("There is no data.")
    else:
        # Calculate the sum of 'NRol', 'TRQol', and 'Engol' for each flight
        df['Overlimits'] = df[['NRol', 'TRQol', 'Engol']].sum(axis=1)

        title = f"{date_from} to {date_to}"
        # Plotting the data with only existing flight numbers on the x-axis
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(df['FN'], df['Overlimits'])
        ax.set_xticks(df['FN'])  # Set x-axis ticks to only existing flight numbers
        ax.set_xlabel(title)
        ax.set_ylabel('Sum of Overlimits')
        ax.set_title('Overlimits during Flight')

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas.draw()
    
    db_communication.close_connection(connection[1])