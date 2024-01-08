import db_communication
import os
import csv
from datetime import datetime
import re
import shutil


def read_files_in_folder(folder_path):
    
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    connection = db_communication.connect_to_database()
    mycursor = connection[0]
    conn = connection[1]

    try:
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, newline='', encoding='cp1250') as file:
                data = clean_csv(file_path)
                write_to_db(data, mycursor)
                conn.commit()  # Commit changes to the database after processing each file
                move_read_files(file_name)
    finally:
        conn.close()  # Ensure the connection is closed even if an exception occurs


def clean_csv(file):
    data = []
    
    with open(file, newline='', encoding='cp1250') as file:
        reader = csv.reader(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data = [field for row in reader for field in row if any(field)]
    
    return data

def write_to_db(data, mycursor):
    val = []
    field=0
    x=0
    fn_checkVal = 0
    fn = 0
    
    #fill in the table basics
    while field < len(data):
        if data[field] == 'Aircraft type':
            val.append(data[field+1])
        if data[field] == 'Aircraft S/N':
            z=data[field+1].strip()
            val.append(z)
        if data[field] == 'Flight Number ':
            
            z=data[field+1].strip()
            fn_checkVal= fn_check(z, mycursor)
            val.append(z)
            fn = z
            
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
    
    if fn_checkVal == 0:
        placeholders = ", ".join(["%s"] * len(val))
        sql = f"INSERT INTO basics (type, srlNmb, FN, mode, GPSdt, VEMDfd, GPSfd, fd, n1cycles, n2cycles, NRol, TRQol, Engol) VALUES ({placeholders})"
        mycursor.execute(sql, val)
        print(mycursor.rowcount, "was inserted.")
    else:
        print('the flight number already exists')
    
    #fill the Failure table
    
    field = 0
    fail = []
    while field < len(data):
        print(data[field])
        if data[field] == 'Failures':
            fail.append(data[field+3])
            fcd= data[field+3]
            fail.append(data[field+5])
            fail.append(data[field+7])
            failure=1
        field+=1
    
    if code_check(fcd, mycursor) == 0:
        sql = f"INSERT INTO failure values ( %s, %s, %s )"
        mycursor.execute(sql, fail)
    else:
        print("the failure with this code already exists")
    
    #fill the FailData table
    
    field = 0
    faildata = []
    if failure != 0:
        while field < len(data):
            if data[field] == 'Code':
                faildata.append(data[field+1].strip())
                faildata.append(fn)
                
            if data[field]== 'Occurrences':
                faildata.append(data[field+2].strip())
                
            if data[field]== 'N1 (NG):':
                n1r = numeric(data[field+3], 'float')
                n1l = numeric(data[field+2], 'float')
                faildata.append(n1r)
                faildata.append(n1l)
                
            if data[field]== 'NR:':
                nrr = numeric(data[field+3], 'int')
                nrl = numeric(data[field+2], 'int')
                faildata.append(nrr)
                faildata.append(nrl)
                
            if data[field]== 'N2 (NF):':
                n2r = numeric(data[field+3], 'int')
                n2l = numeric(data[field+2], 'int')
                faildata.append(n2r)
                faildata.append(n2l)
                
            if data[field]== 'T4a:':
                t4a = numeric(data[field+3], 'float')
                faildata.append(t4a)
                
            if data[field]== 'T4b:':
                t4b = numeric(data[field+3], 'float')
                faildata.append(t4b)
                
            if data[field]== 'OAT:':
                oatr = numeric(data[field+3], 'float')
                oatl = numeric(data[field+2], 'float')
                faildata.append(oatr)
                faildata.append(oatl)
                
            if data[field]== 'TOT (T4):':
                tot1= numeric(data[field+1], 'int')
                tot2= numeric(data[field+2], 'int')
                tot3= numeric(data[field+3], 'int')
                tot4= numeric(data[field+4], 'int')
                faildata.append(tot1)
                faildata.append(tot2)
                faildata.append(tot3)
                faildata.append(tot4)
                
            if data[field]== 'TRQ (TQ):':
                trq1= numeric(data[field+1], 'float')
                trq2= numeric(data[field+2], 'float')
                trq3= numeric(data[field+3], 'float')
                trq4= numeric(data[field+4], 'float')
                faildata.append(trq1)
                faildata.append(trq2)
                faildata.append(trq3)
                faildata.append(trq4)
                
            if data[field]== 'P0:':
                po1= numeric(data[field+1], 'float')
                po2= numeric(data[field+2], 'float')
                po3= numeric(data[field+3], 'float')
                po4= numeric(data[field+4], 'float')
                faildata.append(po1)
                faildata.append(po2)
                faildata.append(po3)
                faildata.append(po4)
                
            if data[field]== 'GENC:':
                genc1= numeric(data[field+1], 'int')
                genc2= numeric(data[field+2], 'int')
                genc3= numeric(data[field+3], 'int')
                genc4= numeric(data[field+4], 'int')
                faildata.append(genc1)
                faildata.append(genc2)
                faildata.append(genc3)
                faildata.append(genc4)
                
            if data[field]== 'BUSV:':
                bv1= numeric(data[field+1], 'float')
                bv2= numeric(data[field+2], 'float')
                bv3= numeric(data[field+3], 'float')
                bv4= numeric(data[field+4], 'float')
                faildata.append(bv1)
                faildata.append(bv2)
                faildata.append(bv3)
                faildata.append(bv4)
                
            if data[field]== 'STARTC:':
                startc = numeric(data[field+3], 'int')
                faildata.append(startc)
            
            field+=1
        if failcheck(fn, fcd, mycursor) == 0:
            sql = f"INSERT INTO faildata VALUES ( %s, %s, %s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql, faildata)
        else:
            print("the faildata already exists, the file was already processed once")


def fn_check(fn, mycursor):
    sql_fn= "SELECT COUNT(*) FROM basics WHERE FN = %s"
    mycursor.execute(sql_fn, (fn,))
    check = mycursor.fetchone()[0]
    
    return check

def code_check(fcd, mycursor):
    sql_cd = "SELECT COUNT(*) FROM failure where code = %s"
    mycursor.execute(sql_cd, (fcd,))
    check = mycursor.fetchone()[0]
    
    return check

def failcheck(fn, code, mycursor):
    sql_fcheck = "SELECT COUNT(*) FROM faildata WHERE failCode = %s AND FN = %s"
    mycursor.execute(sql_fcheck, (code, fn))
    check = mycursor.fetchone()[0]
    
    return check

def numeric(text, type):
    
    if type == 'int':
        number = re.findall(r'\b\d+\b', text)
        if number:
            return int(number[0])
    elif type == 'float':
        number = re.findall(r'\d+\.\d+|\d+', text)
        if number:
            return float(number[0])
    return None

def move_read_files(file_name):
    source_folder = r"C:\Users\krist\OneDrive\Desktop\Report\uploads"
    destination_folder = r"C:\Users\krist\OneDrive\Desktop\Report\processed"
    
        # Ensure that both source and destination folders exist
    if not os.path.exists(source_folder) or not os.path.exists(destination_folder):
        print("Source or destination folder does not exist.")
        return

    else:
        file_path = os.path.join(source_folder, file_name)

        # Check if the file has the specified extension (.csv in this case)
        if file_path.lower().endswith('.csv'):
            # Create full paths for the source and destination
            save_path = os.path.join(destination_folder, file_name)

            print(f"Moving file from: {file_path}")
            print(f"Saving file to: {save_path}")

            try:
                # Move the file
                shutil.move(file_path, save_path)
                print("File moved successfully!")
            except Exception as e:
                print(f"Error moving file: {e}")
        else:
            print(f"Skipped non-.csv file: {file_path}")
