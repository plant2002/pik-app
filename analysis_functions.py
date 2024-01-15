import pandas as pd 
import db_communication
import datetime as dt
import matplotlib.pyplot as plt

#flying time per day and per flight number
def date_flightTime(date):
    connection = db_communication.connect_to_database()
    sql = "SELECT FN, fd FROM basics WHERE DATE(GPSdt) = %s"
    
    df = pd.read_sql(sql, connection[1], params=(date,))
    
    df['fd_minutes'] = df['fd'].dt.total_seconds() / 60
    
    #bar chart
    plt.bar(df['FN'], df['fd_minutes'], color='blue')
    plt.title('Flight Time per flight on {}'.format(date.strftime("%Y-%m-%d")))
    plt.xlabel('Flight Number')
    plt.ylabel('Flight Time (minutes)')

    # Round FN values and set them as x-axis ticks
    plt.xticks(df['FN'].round(), df['FN'].round())

    # Add fd_minutes values on top of each bar
    for index, value in enumerate(df['fd_minutes']):
        plt.text(df['FN'].iloc[index], value + 0.1, str(round(value, 2)), ha='center', va='bottom')

    plt.show()
    db_communication.close_connection(connection)

#flight time per day all flights in one day together
def time_per_day(date_from, date_to):
    connection = db_communication.connect_to_database()
    sql = "SELECT FN, fd, GPSdt FROM basics WHERE DATE(GPSdt) BETWEEN %s AND %s"
    
    df = pd.read_sql(sql, connection[1], params=(date_from, date_to))
    
    df['GPSdt'] = pd.to_datetime(df['GPSdt'])  # Convert GPSdt to datetime
    df['fd_minutes'] = df['fd'].dt.total_seconds() / 60
    
    grouped_df = df.groupby(df['GPSdt'].dt.date)['fd_minutes'].sum().reset_index()

    plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
    bars = plt.bar(grouped_df['GPSdt'].astype(str), grouped_df['fd_minutes'])
    
    # Annotate each bar with its value
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 2), ha='center', va='bottom')

    plt.xlabel('')
    plt.ylabel('Minutes per day')
    plt.title('Total Minutes per Day')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()
    
    db_communication.close_connection(connection)

#def engineCyc_fn(fn_from, fn_to):
def engineCyc_fn(fn_from, fn_to):
    
    connection = db_communication.connect_to_database()

    # Assuming fn_from and fn_to are defined earlier in your code
    sql = "SELECT FN, n1cycles, n2cycles FROM basics WHERE FN BETWEEN %s AND %s"
    df = pd.read_sql(sql, connection[1], params=(fn_from, fn_to))

    # Plot the bar chart using Pandas
    ax = df.plot(kind='bar', x='FN', y=['n1cycles', 'n2cycles'], width=0.8, position=0.5, figsize=(8, 6))

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

    # Show the plot
    plt.show()

    # Close the database connection
    connection[1].close()

#maximum engineCyc values per day (n1 & n2)
def engineCyc_date(date_from, date_to):
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
    plt.plot(df_max['date'], df_max['n1cycles'], marker='o', linestyle='-')
    for i, txt in enumerate(df_max['n1cycles']):
        plt.annotate(txt, (df_max['date'].iloc[i], df_max['n1cycles'].iloc[i]), textcoords="offset points", xytext=(10,5), ha='center')
    plt.plot(df_max['date'], df_max['n2cycles'], marker='o', linestyle='-', label='n2cycles')
    for i, txt in enumerate(df_max['n2cycles']):
        plt.annotate(txt, (df_max['date'].iloc[i], df_max['n2cycles'].iloc[i]), textcoords="offset points", xytext=(10, -10), ha='center')

    # Formatting the plot
    plt.xlabel('Date')
    plt.ylabel('Maximum Cycles')
    plt.title('Maximum Cycles over dates')

    # Set x-axis ticks & grid only for existing dates
    plt.xticks(existing_dates, rotation=45, ha='right')
    plt.grid(True, linestyle='--', which='major', color='grey', alpha=0.5, axis='x')

    plt.show()
    
    db_communication.close_connection(connection[1])

#the overlimits per flight --> flightnmb_from to flightnmb_to
def overlimits_flight(fn_from, fn_to):
    connection = db_communication.connect_to_database()

    sql = "SELECT FN, NRol, TRQol, Engol FROM basics WHERE FN BETWEEN %s AND %s"
    df = pd.read_sql(sql, connection[1], params=(fn_from, fn_to))
    
    if df.empty or df[['NRol', 'TRQol', 'Engol']].isnull().all().all():
        # Display a new window message if there is no data or only NULL values
        print("There is no data.")
    else:
        # Calculate the sum of 'NRol', 'TRQol', and 'Engol' for each flight
        df['Overlimits'] = df[['NRol', 'TRQol', 'Engol']].sum(axis=1)

        # Plotting the data with only existing flight numbers on the x-axis
        plt.figure(figsize=(10, 6))
        plt.bar(df['FN'], df['Overlimits'])
        plt.xticks(df['FN'])  # Set x-axis ticks to only existing flight numbers
        plt.xlabel('Flight Number (FN)')
        plt.ylabel('Sum of Overlimits')
        plt.title('Overlimits during Flight')
        plt.show()
    
    db_communication.close_connection(connection[1])

#the overlimits per flight --> date_from to date_to
def overlimits_date (date_from, date_to):
    connection = db_communication.connect_to_database()

    sql = "SELECT FN, NRol, TRQol, Engol FROM basics WHERE DATE(GPSdt) BETWEEN %s AND %s"
    df = pd.read_sql(sql, connection[1], params=(date_from, date_to))
    
    if df.empty or df[['NRol', 'TRQol', 'Engol']].isnull().all().all():
        # Display a new window message if there is no data or only NULL values
        print("There is no data.")
    else:
        # Calculate the sum of 'NRol', 'TRQol', and 'Engol' for each flight
        df['Overlimits'] = df[['NRol', 'TRQol', 'Engol']].sum(axis=1)

        title= date_from + " to " + date_to
        # Plotting the data with only existing flight numbers on the x-axis
        plt.figure(figsize=(10, 6))
        plt.bar(df['FN'], df['Overlimits'])
        plt.xticks(df['FN'])  # Set x-axis ticks to only existing flight numbers
        plt.xlabel(title)
        plt.ylabel('Sum of Overlimits')
        plt.title('Overlimits during Flight')
        plt.show()
    
    db_communication.close_connection(connection[1])

#def error_fn(fn):

#def error_date(date):

#failures

#which fail codes appeared in the flights between fn_from and fn_to
#def failCode(fn_from, fn_to):
    # connection = db_communication.connect_to_database()
    #sql = "SELECT FN, fd, GPSdt FROM basics WHERE DATE(GPSdt) BETWEEN %s AND %s"
    
    
    #df = pd.read_sql(sql, connection[1], params=(date_from, date_to))


