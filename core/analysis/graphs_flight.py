import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core import db_communication

#flying time per day and per flight number
def date_flightTime(frame, date):
    connection = db_communication.connect_to_database()
    sql = "SELECT FN, fd FROM basics WHERE DATE(GPSdt) = %s"
    
    df = pd.read_sql(sql, connection[1], params=(date,))
    
    df['fd_minutes'] = df['fd'].dt.total_seconds() / 60
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(df['FN'], df['fd_minutes'], color='blue')
    ax.set_title(f'Flight Time per flight on {date}')
    ax.set_xlabel('Flight Number')
    ax.set_ylabel('Flight Time (minutes)')

    # Round FN values and set them as x-axis ticks
    ax.set_xticks(df['FN'].round())
    ax.set_xticklabels(df['FN'].round())

    # Add fd_minutes values on top of each bar
    for index, value in enumerate(df['fd_minutes']):
        ax.text(df['FN'].iloc[index], value + 0.1, str(round(value, 2)), ha='center', va='bottom')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()
    db_communication.close_connection(connection[1])

#flight time per day all flights in one day together
def time_per_day(frame, date_from, date_to):

    connection = db_communication.connect_to_database()
    sql = "SELECT FN, fd, GPSdt FROM basics WHERE DATE(GPSdt) BETWEEN %s AND %s"
    
    df = pd.read_sql(sql, connection[1], params=(date_from, date_to))
    
    df['GPSdt'] = pd.to_datetime(df['GPSdt'])  # Convert GPSdt to datetime
    df['fd_minutes'] = df['fd'].dt.total_seconds() / 60
    
    grouped_df = df.groupby(df['GPSdt'].dt.date)['fd_minutes'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(12, 6))  # Adjust the figure size as needed
    bars = ax.bar(grouped_df['GPSdt'].astype(str), grouped_df['fd_minutes'])

    # Annotate each bar with its value
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 2), ha='center', va='bottom')

    ax.set_xlabel('')
    ax.set_ylabel('Minutes per day')
    ax.set_title('Total Minutes per Day')
    ax.tick_params(axis='x', rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()
    db_communication.close_connection(connection[1])

#def engineCyc_fn(fn_from, fn_to):
def engineCyc_fn(frame, fn_from, fn_to):
    
    connection = db_communication.connect_to_database()

    # Assuming fn_from and fn_to are defined earlier in your code
    sql = "SELECT FN, n1cycles, n2cycles FROM basics WHERE FN BETWEEN %s AND %s"
    df = pd.read_sql(sql, connection[1], params=(fn_from, fn_to))

    # Plot the bar chart using Pandas
    fig, ax = plt.subplots(figsize=(8, 6))
    df.plot(kind='bar', x='FN', y=['n1cycles', 'n2cycles'], width=0.8, position=0.5, ax=ax)

    # Set labels and title
    ax.set_xlabel('Flight Numbers')
    ax.set_ylabel('Cycles')
    ax.set_title('Engine cycles on specific flights')

    plt.xticks(rotation=360, ha='right')

    # Display actual numbers on top of the bars with float formatting
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points')

    # Set y-axis ticks as floats
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.2f}'))

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()

    # Close the database connection
    db_communication.close_connection(connection[1])

#maximum engineCyc values per day (n1 & n2)
def engineCyc_date(frame, date_from, date_to):
    connection = db_communication.connect_to_database()

    sql = "SELECT FN, n1cycles, n2cycles, GPSdt FROM basics WHERE DATE(GPSdt) BETWEEN %s AND %s"
    df = pd.read_sql(sql, connection[1], params=(date_from, date_to))
    
    df['GPSdt'] = pd.to_datetime(df['GPSdt'])  # Convert GPSdt to datetime
    df['date'] = df['GPSdt'].dt.date
    existing_dates = df['date'].unique()

    # Group by date and find the maximum 'n1cycles' for each date
    df_max = df.groupby('date').agg({'n1cycles': 'max', 'n2cycles': 'max'}).reset_index()
    df_max = df_max[df_max['date'].isin(existing_dates)]

    # Plotting the line chart
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_max['date'], df_max['n1cycles'], marker='o', linestyle='-', label='n1cycles')
    for i, txt in enumerate(df_max['n1cycles']):
        ax.annotate(txt, (df_max['date'].iloc[i], df_max['n1cycles'].iloc[i]), textcoords="offset points", xytext=(10, 5), ha='center')
    ax.plot(df_max['date'], df_max['n2cycles'], marker='o', linestyle='-', label='n2cycles')
    for i, txt in enumerate(df_max['n2cycles']):
        ax.annotate(txt, (df_max['date'].iloc[i], df_max['n2cycles'].iloc[i]), textcoords="offset points", xytext=(10, -10), ha='center')

    # Formatting the plot
    ax.set_xlabel('Date')
    ax.set_ylabel('Maximum Cycles')
    ax.set_title('Maximum Cycles over Dates')

    # Set x-axis ticks & grid only for existing dates
    ax.set_xticks(existing_dates)
    ax.tick_params(axis='x', rotation=45, ha='right')
    ax.grid(True, linestyle='--', which='major', color='grey', alpha=0.5, axis='x')

    ax.legend()  # Show legend

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()
    db_communication.close_connection(connection[1])