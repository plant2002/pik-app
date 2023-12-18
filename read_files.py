import db_communication
import os
import csv
from datetime import datetime


connection=db_communication.connect_to_database()
mycursor = connection[0]
conn = connection[1]
data = []

def read_files_in_folder(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            print(f"Contents of {file_name}\n")
    clean_csv(folder_path, files)

def clean_csv(folder_path, files):
    
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, newline='', encoding='cp1250') as file:
            reader = csv.reader(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                for field in row:
                    if any(field):
                        #print(field)
                        data.append(field)
    write_to_db(data)

def write_to_db(data):
    val = []
    field=0
    x=0
    while field < len(data):
        if data[field] == 'Aircraft type':
            val.append(data[field+1])
        if data[field] == 'Aircraft S/N':
            z=data[field+1].strip()
            val.append(z)
        if data[field] == 'Flight Number ':
            z=data[field+1].strip()
            val.append(z)
        if data[field] == 'Mode ':
            z=data[field+1].strip()
            val.append(z)
        if data[field] == 'GPS Date Time':
            datex = datetime.strptime(data[field+3], "%m/%d/%Y %I:%M:%S %p ")
            formatted_datetime = datex.strftime("%Y-%m-%d %H:%M:%S")
            val.append(formatted_datetime)
        if data[field] == 'VEMD Flight Duration':
            z=data[field+2].strip()
            val.append(z)
        if data[field] == 'GPS Flight Duration':
            z=data[field+2].strip()
            val.append(z)
        if data[field] == 'Flight Duration':
            z=data[field+1].strip()
            val.append(z)
        if data[field] == 'N1 (NG) Cycles':
            z=data[field+3].strip()
            val.append(z)
        if data[field] == 'N2 (NF) Cycles':
            z=data[field+3].strip()
            val.append(z)
        if data[field] == 'NR overlimits':
            if data[field+3].isnumeric():
                val.append(data[field+6])
            else: 
                val.append(None)
                x+=1
        if data[field] == 'TRQ (TQ) overlimits':
            if data[field+3].isnumeric():
                val.append(data[field+6])
            else: 
                val.append(None)
                x+=1
        if data[field] == 'Engine overlimits':
            if data[field+3].isnumeric():
                val.append(data[field+6])
            else: 
                val.append(None)
                x+=1
        field+=1
    
    placeholders = ", ".join(["%s"] * len(val))
    sql = f"INSERT INTO basics (type, srlNmb, FN, mode, GPSdt, VEMDfd, GPSfd, fd, n1cycles, n2cycles, NRol, TRQol, Engol) VALUES ({placeholders})"
    mycursor.execute(sql, val)
    conn.commit()
    print(mycursor.rowcount, "was inserted.")
    #print(f"SQL Query: {sql}")
    #print(f"Values: {val}")
    #print(f"Number of values: {len(val)}")
