import pandas as pd 
import db_communication
import datetime
import matplotlib.pyplot as plt

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

date1 = input("in Y-m-d format")
date = datetime.datetime.strptime(date1, "%Y-%m-%d")
