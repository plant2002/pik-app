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

a=input("fn_from")
b=input ("fn_to")
export_to_csv_fn_from_to(a, b)