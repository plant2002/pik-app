import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core import db_communication

#error codes and number during one day
def error_date_output(date):
    connection = db_communication.connect_to_database()
    sql1 = "SELECT FN, GPSdt FROM basics WHERE DATE(GPSdt) = %s"
    df1 = pd.read_sql(sql1, connection[1], params=(date, ))
    db_communication.close_connection(connection[1])

    connection = db_communication.connect_to_database()
    sql2 = f"SELECT failCode, FN FROM faildata WHERE FN IN ({', '.join(map(str, df1['FN']))})"
    df2 = pd.read_sql(sql2, connection[1])
    db_communication.close_connection(connection[1])
    num_rows = df2.shape[0]
    
    merged_df = pd.merge(df1, df2, on='FN', how='inner')
    error_counts = merged_df['failCode'].value_counts().reset_index()
    error_counts.columns = ['failCode', 'count']
    unique_failcodes = merged_df['failCode'].unique()
    
    connection = db_communication.connect_to_database()
    sql3 = f"SELECT code, name, descr FROM failure WHERE code IN ({', '.join(map(str, unique_failcodes))})"
    df3 = pd.read_sql(sql3, connection[1])
    db_communication.close_connection(connection[1])
    return df3
    
#error codes and number of them over multiple days
def error_dates_output(date_from, date_to):
    connection = db_communication.connect_to_database()
    sql1 = "SELECT FN, GPSdt FROM basics WHERE DATE(GPSdt) BETWEEN %s AND %s"
    df1 = pd.read_sql(sql1, connection[1], params=(date_from, date_to ))
    db_communication.close_connection(connection[1])

    connection = db_communication.connect_to_database()
    sql2 = f"SELECT failCode, FN FROM faildata WHERE FN IN ({', '.join(map(str, df1['FN']))})"
    df2 = pd.read_sql(sql2, connection[1])
    db_communication.close_connection(connection[1])
    num_rows = df2.shape[0]
    
    merged_df = pd.merge(df1, df2, on='FN', how='inner')
    error_counts = merged_df['failCode'].value_counts().reset_index()
    error_counts.columns = ['failCode', 'count']
    unique_failcodes = merged_df['failCode'].unique()

    connection = db_communication.connect_to_database()
    sql3 = f"SELECT code, name, descr FROM failure WHERE code IN ({', '.join(map(str, unique_failcodes))})"
    df3 = pd.read_sql(sql3, connection[1])

    db_communication.close_connection(connection[1])
    
    result_string = f"Between {date_from} and {date_to}, there were {num_rows} errors and {unique_failcodes.shape[0]} unique errors\n"
    

    return result_string, df3
