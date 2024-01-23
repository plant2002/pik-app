import pandas as pd
from tkinter import filedialog
import db_communication
import datetime

def export_to_csv_fn_from_to(fn_from, fn_to):

    connection = db_communication.connect_to_database()
    sql1 = "SELECT * FROM basics WHERE FN BETWEEN %s AND %s"
    df1 = pd.read_sql(sql1, connection[1], params=(fn_from, fn_to))
    db_communication.close_connection(connection[1])

    connection = db_communication.connect_to_database()
    sql2 = "SELECT * FROM faildata WHERE FN BETWEEN %s AND %s"
    df2 = pd.read_sql(sql2, connection[1], params=(fn_from, fn_to))
    db_communication.close_connection(connection[1])
    
    result_df = pd.merge(df1, df2, on='FN', how='left')
    
    # Ask user for the destination folder
    folder_selected = filedialog.askdirectory()

    if folder_selected:
        # Create CSV file
        csv_file_path = f"{folder_selected}/flights{fn_from}to{fn_to}.csv"
        result_df.to_csv(csv_file_path, index=False)

        print(f"Data exported to: {csv_file_path}")

def export_to_csv_fn(fn_spec):
    
    connection = db_communication.connect_to_database()
    sql1 = "SELECT * FROM basics WHERE FN = %s"
    df1 = pd.read_sql(sql1, connection[1], params=(fn_spec, ))
    db_communication.close_connection(connection[1])

    connection = db_communication.connect_to_database()
    sql2 = "SELECT * FROM faildata WHERE FN = %s"
    df2 = pd.read_sql(sql2, connection[1], params=(fn_spec, ))
    db_communication.close_connection(connection[1])
    
    if not df2.empty and 'failCode' in df2.columns:
        code = int(df2["failCode"].iloc[0])
        
        connection = db_communication.connect_to_database()
        sql3 = "SELECT * FROM failure WHERE code = %s"
        df3 = pd.read_sql(sql3, connection[1], params=(code, ))
        db_communication.close_connection(connection[1])

        result_df1 = pd.merge(df1, df2, on='FN', how='left')
        result_df = pd.merge(result_df1, df3, left_on='failCode', right_on='code', how='left')
    else:
        result_df = pd.merge(df1, df2, on='FN', how='left')
    
    # Ask user for the destination folder
    folder_selected = filedialog.askdirectory()

    if folder_selected:
        # Create CSV file
        csv_file_path = f"{folder_selected}/flight{fn_spec}.csv"
        result_df.to_csv(csv_file_path, index=False)

        print(f"Data exported to: {csv_file_path}")

def error_number(error):
    connection = db_communication.connect_to_database()
    sql1 = "SELECT * FROM failure WHERE code = %s"
    df1 = pd.read_sql(sql1, connection[1], params=(error, ))
    db_communication.close_connection(connection[1])
    
    connection = db_communication.connect_to_database()
    sql2= "SELECT * FROM faildata WHERE failCode = %s"
    df2 = pd.read_sql(sql2, connection[1], params = (error, ))
    db_communication.close_connection(connection[1])
    
    fn=df2["FN"]
    
    connection = db_communication.connect_to_database()
    sql3 = f"SELECT FN, GPSdt, fd FROM basics WHERE FN IN ({', '.join(map(str, fn))})"
    df3 = pd.read_sql(sql3, connection[1])
    db_communication.close_connection(connection[1])
    
    
    folder_selected = filedialog.askdirectory()
    merged_df = pd.merge(df2, df3, on='FN', how='inner')
    

    if folder_selected:
        # Create CSV file
        csv_file_path = f"{folder_selected}/error{error}allAffectedFlights.csv"
        merged_df.to_csv(csv_file_path, index=False)
        print(f"Data exported to: {csv_file_path}")
        
        #maybe one day make a formatted csv file

def export_fn_date_to_from(date_to, date_from):
    connection = db_communication.connect_to_database()
    sql1 = "SELECT * FROM basics WHERE DATE(GPSdt) BETWEEN %s AND %s"
    df1 = pd.read_sql(sql1, connection[1], params=(date_to, date_from))
    db_communication.close_connection(connection[1])
    
    fn=df1["FN"]

    df1['VEMDfd'] = pd.to_timedelta(df1['VEMDfd']).astype(str)
    df1['GPSfd'] = pd.to_timedelta(df1['GPSfd']).astype(str)
    df1['fd'] = pd.to_timedelta(df1['fd']).astype(str)
    
    
    df1['VEMDfd'] = df1['VEMDfd'].apply(lambda x: ':'.join(str(x).split()[-1].split(':')))
    df1['GPSfd'] = df1['GPSfd'].apply(lambda x: ':'.join(str(x).split()[-1].split(':')))
    df1['fd'] = df1['fd'].apply(lambda x: ':'.join(str(x).split()[-1].split(':')))

    
    connection = db_communication.connect_to_database()
    sql2 = f"SELECT * FROM faildata WHERE FN IN ({', '.join(map(str, fn))})"
    df2 = pd.read_sql(sql2, connection[1])
    db_communication.close_connection(connection[1])
    
    code = df2["failCode"]
    
    connection = db_communication.connect_to_database()
    sql3 = f"SELECT * FROM failure WHERE code IN ({', '.join(map(str, code))})"
    df3 = pd.read_sql(sql3, connection[1])
    db_communication.close_connection(connection[1])
    
    result_df1 = pd.merge(df1, df2, on='FN', how='left')
    result_df = pd.merge(result_df1, df3, left_on='failCode', right_on='code', how='left')
    
    folder_selected = filedialog.askdirectory()

    if folder_selected:
        # Create CSV file
        csv_file_path = f"{folder_selected}/date{date_from}to{date_to}.csv"
        result_df.to_csv(csv_file_path, index= False)

        print(f"Data exported to: {csv_file_path}")

def export_fn_date_spec(date_specific):
    connection = db_communication.connect_to_database()
    sql1 = "SELECT * FROM basics WHERE DATE(GPSdt) = %s"
    df1 = pd.read_sql(sql1, connection[1], params=(date_specific, ))
    db_communication.close_connection(connection[1])
    
    fn=df1["FN"]

    df1['VEMDfd'] = pd.to_timedelta(df1['VEMDfd']).astype(str)
    df1['GPSfd'] = pd.to_timedelta(df1['GPSfd']).astype(str)
    df1['fd'] = pd.to_timedelta(df1['fd']).astype(str)
    
    
    df1['VEMDfd'] = df1['VEMDfd'].apply(lambda x: ':'.join(str(x).split()[-1].split(':')))
    df1['GPSfd'] = df1['GPSfd'].apply(lambda x: ':'.join(str(x).split()[-1].split(':')))
    df1['fd'] = df1['fd'].apply(lambda x: ':'.join(str(x).split()[-1].split(':')))

    
    connection = db_communication.connect_to_database()
    sql2 = f"SELECT * FROM faildata WHERE FN IN ({', '.join(map(str, fn))})"
    df2 = pd.read_sql(sql2, connection[1])
    db_communication.close_connection(connection[1])
    
    code = df2["failCode"]
    
    connection = db_communication.connect_to_database()
    sql3 = f"SELECT * FROM failure WHERE code IN ({', '.join(map(str, code))})"
    df3 = pd.read_sql(sql3, connection[1])
    db_communication.close_connection(connection[1])
    
    result_df1 = pd.merge(df1, df2, on='FN', how='left')
    result_df = pd.merge(result_df1, df3, left_on='failCode', right_on='code', how='left')
    
    folder_selected = filedialog.askdirectory()

    if folder_selected:
        # Create CSV file
        csv_file_path = f"{folder_selected}/date{date_specific}data.csv"
        result_df.to_csv(csv_file_path, index= False)

        print(f"Data exported to: {csv_file_path}")

