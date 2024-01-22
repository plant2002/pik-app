import pandas as pd
from tkinter import filedialog
import db_communication

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
    
    if 'failCode' in df2.columns:
        code = int(df2["failCode"].iloc[0])
        
        connection = db_communication.connect_to_database()
        sql3 = "SELECT * FROM failure WHERE code = %s"
        df3 = pd.read_sql(sql3, connection[1], params=(code, ))
        db_communication.close_connection(connection[1])

        result_df1 = pd.merge(df1, df2, on='FN', how='left')
        result_df = pd.merge(result_df1, df3, left_on='failCode', right_on='code', how='left')
    else:
        result_df = pd.merge(df1, df2, df3, on='FN', how='left')
    
    # Ask user for the destination folder
    folder_selected = filedialog.askdirectory()

    if folder_selected:
        # Create CSV file
        csv_file_path = f"{folder_selected}/flight{fn_spec}to.csv"
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
        csv_file_path = f"{folder_selected}/error{error}allAffectedFLights.csv"
        df1.to_csv(f"{folder_selected}/failure{error}details.csv", index=False)
        merged_df.to_csv(csv_file_path, index=False)

        print(f"Data exported to: {csv_file_path}")

