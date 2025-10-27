import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core import db_communication

#failures
#for drop-down menu of which codes you can check over (which ones are in database at the moment)
def errors_code_selection():
    connection = db_communication.connect_to_database()
    sql1 = "SELECT code, name FROM failure"
    df1 = pd.read_sql(sql1, connection[1])
    db_communication.close_connection(connection[1])
    
    option_mapping = df1.set_index('name')['code'].to_dict()
    return option_mapping
#all flights with specific error (chosen with errors_code_selection drop-down menu) and their specs
#still have to figure out how to connect this with my graphs
def error_code_flight(code):
    #all rows with error code same as input, FN to connect to table basics
    connection = db_communication.connect_to_database()
    sql1 = "SELECT FN, failCode FROM faildata WHERE failCode = %s"
    df1 = pd.read_sql(sql1, connection[1], params=(code, ))
    db_communication.close_connection(connection[1])
    
    #number of rows with this code error
    number_of_flights=df1.shape[0]
    
    #information about flights from table basics that showed up in previous connection 
    connection = db_communication.connect_to_database()
    sql2 = f"SELECT FN, GPSdt, fd FROM basics WHERE FN IN ({', '.join(map(str, df1['FN']))})"
    df2 = pd.read_sql(sql2, connection[1])
    db_communication.close_connection(connection[1])
    
    #information about the flight from table failData via code and FN
    connection = db_communication.connect_to_database()
    sql3 = f"SELECT * FROM faildata WHERE FN IN ({', '.join(map(str, df1['FN']))}) AND failCode = %s"
    df3 = pd.read_sql(sql3, connection[1], params=(code, ))
    db_communication.close_connection(connection[1])
    
    #merged_df = pd.merge(df2, df3, on='FN', how='inner')
    return df2
    
#two graphs about flights per day + all flying time of flights that got an error code per date
#not connected, not in use. Will do after presentation
def error_code_flights(df2):
    df2['GPSdt'] = pd.to_datetime(df2['GPSdt'])

    # Create a new column for the date
    df2['Date'] = df2['GPSdt'].dt.date

    # Plotting the number of flights per day
    plt.figure(figsize=(10, 6))
    df2['Date'].value_counts().sort_index().plot(kind='bar', color='skyblue', align='center')
    plt.title('Number of Flights per Day')
    plt.xlabel('Date')
    plt.ylabel('Number of Flights')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.yticks(range(0, df2['Date'].value_counts().max() + 1, 1))  # Show only integer y-axis values
    plt.show()

    # Plotting the length of flights
    plt.figure(figsize=(10, 6))
    df2['fd'] = pd.to_timedelta(df2['fd'])  # Convert to timedelta
    df2['Flight Length'] = df2['fd'].dt.total_seconds() / 60  # Convert to minutes
    df2.groupby('Date')['Flight Length'].sum().plot(kind='bar', color='salmon', align='center')
    plt.title('Total Flight Length per Day')
    plt.xlabel('Date')
    plt.ylabel('Total Flight Length (minutes)')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.show()
def error_code_faildata(df3):
    column_means = df3.mean()

    # Calculate the deviation of each value from the mean in percentage
    deviations_percentage = ((df3 - column_means) / column_means) * 100

    # Plotting
    plt.figure(figsize=(12, 8))

    # Plot horizontal bars for each flight number
    for i, fn in enumerate(df3['FN'].unique()):
        fn_data = df3.loc[df3['FN'] == fn].iloc[0]
        width_value = column_means.iloc[i]

        # Set colors based on deviations from mean
        colors = ['green' if val > 0 else 'red' for val in deviations_percentage.iloc[i]]

        # Plot horizontal bars with different colors for each deviation
        plt.barh(i, width_value, color='lightgrey')  # Main bar representing width
        plt.barh(i, fn_data, color=colors, left=[width_value] * len(fn_data))

        # Plot a red horizontal line for the mean value
        plt.axvline(x=width_value, color='red', linestyle='--', linewidth=2)

    # Set y-axis labels to flight numbers
    plt.yticks(range(len(df3['FN'].unique())), df3['FN'].unique())

    # Set x-axis limits based on mean and mean difference percentage
    max_deviation = 10 / 100 * column_means.abs().max()
    plt.xlim(column_means.min() - max_deviation, column_means.max() + max_deviation)

    plt.title('Width Deviation from Mean for Each Flight Number')
    plt.xlabel('Width Deviation from Mean')
    plt.ylabel('Flight Number')
    plt.show()
