import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core import db_communication

#error occurrences in flight from fn_from to fn_to
def error_fn(frame, fn_from, fn_to):
    connection = db_communication.connect_to_database()

    all_flight_numbers = pd.DataFrame({'FN': range(int(fn_from), int(fn_to)+1)})

    # Fetch data from the database for the specified flight_number range
    sql = "SELECT FN, occr FROM faildata WHERE FN BETWEEN %s AND %s"
    df = pd.read_sql(sql, connection[1], params=(fn_from, fn_to))

    # Merge the data with all_flight_numbers to fill missing flight_numbers with 0 occurrences
    if df.empty:
        merged_df = all_flight_numbers.assign(occr=0)
    else:
        # Merge the data with all_flight_numbers to fill missing flight_numbers with 0 occurrences
        merged_df = all_flight_numbers.merge(df, on='FN', how='left').fillna(0)

    # Plotting the graph with formatting adjustments
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(merged_df['FN'], merged_df['occr'])
    ax.set_xlabel('Flight Number (FN)')
    ax.set_ylabel('Number of Occurrences (occr)')
    ax.set_title('Occurrences of Errors per Flight Number')

    # Format y-axis to display only integer values
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    # Set x-axis ticks for all flight numbers
    ax.set_xticks(merged_df['FN'])
    ax.tick_params(axis='x', rotation=45)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()
    db_communication.close_connection(connection[1])

#error occurrences from date_from to date_to per day --> update later for monthly/yearly number !
def error_dates(frame, date_from, date_to):
    connection = db_communication.connect_to_database()
    sql1 = "SELECT FN, GPSdt FROM basics WHERE DATE(GPSdt) BETWEEN %s AND %s"
    df1 = pd.read_sql(sql1, connection[1], params=(date_from, date_to))
    db_communication.close_connection(connection[1])

    # All FN that show up on dates from date_from to date_to
    min_value = int(df1['FN'].min())
    max_value = int(df1['FN'].max())

    # Get occr from faildata from min_value of fn to max_value of fn
    connection = db_communication.connect_to_database()
    sql2 = "SELECT FN, occr FROM faildata WHERE FN BETWEEN %s AND %s"
    df2 = pd.read_sql(sql2, connection[1], params=(min_value, max_value))
    db_communication.close_connection(connection[1])

    # Merge dataframes on 'FN'
    merged_df = pd.merge(df1, df2, how='left', on='FN')
    merged_df['occr'] = merged_df['occr'].fillna(0).astype(int)
    merged_df['date'] = merged_df['GPSdt'].dt.date
    
    date_range = pd.date_range(start=date_from, end=date_to, freq='D').date
    date_range_df = pd.DataFrame({'date': date_range})
    result_df = pd.merge(date_range_df, merged_df.groupby('date')['occr'].sum().reset_index(), how='left', on='date')
    result_df['occr'] = result_df['occr'].fillna(0).astype(int)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(result_df['date'], result_df['occr'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of error occurrences')
    ax.set_title('Occurrences of errors by Date')
    ax.set_xticks(result_df['date'])
    ax.set_xticklabels(result_df['date'], rotation=90)
    ax.set_yticks(range(int(result_df['occr'].max()) + 1))

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()
