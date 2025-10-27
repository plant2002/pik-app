from core import db_communication
from datetime import datetime
from core import read_files
import os

def rewriting_files():
    
    file_path = 'C:/Users/krist/OneDrive/Desktop/Report/uploads'
    files = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]

    for file_name in files:
        folder_path = 'C:/Users/krist/OneDrive/Desktop/Report/uploads'
        try:
            # Open the database connection
            connection = db_communication.connect_to_database()
            mycursor = connection[0]
            conn = connection[1]

            file_path = os.path.join(folder_path, file_name)
            with open(file_path, newline='', encoding='cp1250') as file:
                data = read_files.clean_csv(file_path)
                rewrite(data, mycursor)
                conn.commit()  # Commit changes to the database after processing each file
            file.close()
            read_files.move_read_files(file_name)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Close the database connection in the finally block
            if connection:
                conn.close()
    
    
def rewrite(data, mycursor):
    val = []
    field=0
    x=0
    fn_checkVal=0
    fn = 0
    failure=0
    
    
    #fill in the basics array
    while field < len(data):
        if data[field] == 'Aircraft type':
            val.append(data[field+1])
        if data[field] == 'Aircraft S/N':
            z=data[field+1].strip()
            val.append(z)
        if data[field] == 'Flight Number ':
            
            z=data[field+1].strip()
            fn_checkVal= read_files.fn_check(z, mycursor)
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
        if data[field] == 'Failures':
            failure=1
        field+=1
    
    #delete previous rows
    sql = "delete from faildata where FN = %s"
    mycursor.execute(sql, (fn,))
    print('faildata with FN ', fn, "was deleted")
    
    sql = "delete from basics where FN = %s"
    mycursor.execute(sql, (fn,))
    print ('basics with FN ', fn, "was deleted")
    
    placeholders = ", ".join(["%s"] * len(val))
    sql = f"INSERT INTO basics (type, srlNmb, FN, mode, GPSdt, VEMDfd, GPSfd, fd, n1cycles, n2cycles, NRol, TRQol, Engol) VALUES ({placeholders})"
    mycursor.execute(sql, val)
    print(mycursor.rowcount, "was inserted.")
    
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
                n1r = read_files.numeric(data[field+3], 'float')
                n1l = read_files.numeric(data[field+2], 'float')
                faildata.append(n1r)
                faildata.append(n1l)
                
            if data[field]== 'NR:':
                nrr = read_files.numeric(data[field+3], 'int')
                nrl = read_files.numeric(data[field+2], 'int')
                faildata.append(nrr)
                faildata.append(nrl)
                
            if data[field]== 'N2 (NF):':
                n2r = read_files.numeric(data[field+3], 'int')
                n2l = read_files.numeric(data[field+2], 'int')
                faildata.append(n2r)
                faildata.append(n2l)
                
            if data[field]== 'T4a:':
                t4a = read_files.numeric(data[field+3], 'float')
                faildata.append(t4a)
                
            if data[field]== 'T4b:':
                t4b = read_files.numeric(data[field+3], 'float')
                faildata.append(t4b)
                
            if data[field]== 'OAT:':
                oatr = read_files.numeric(data[field+3], 'float')
                oatl = read_files.numeric(data[field+2], 'float')
                faildata.append(oatr)
                faildata.append(oatl)
                
            if data[field]== 'TOT (T4):':
                tot1= read_files.numeric(data[field+1], 'int')
                tot2= read_files.numeric(data[field+2], 'int')
                tot3= read_files.numeric(data[field+3], 'int')
                tot4= read_files.numeric(data[field+4], 'int')
                faildata.append(tot1)
                faildata.append(tot2)
                faildata.append(tot3)
                faildata.append(tot4)
                
            if data[field]== 'TRQ (TQ):':
                trq1= read_files.numeric(data[field+1], 'float')
                trq2= read_files.numeric(data[field+2], 'float')
                trq3= read_files.numeric(data[field+3], 'float')
                trq4= read_files.numeric(data[field+4], 'float')
                faildata.append(trq1)
                faildata.append(trq2)
                faildata.append(trq3)
                faildata.append(trq4)
                
            if data[field]== 'P0:':
                po1= read_files.numeric(data[field+1], 'float')
                po2= read_files.numeric(data[field+2], 'float')
                po3= read_files.numeric(data[field+3], 'float')
                po4= read_files.numeric(data[field+4], 'float')
                faildata.append(po1)
                faildata.append(po2)
                faildata.append(po3)
                faildata.append(po4)
                
            if data[field]== 'GENC:':
                genc1= read_files.numeric(data[field+1], 'int')
                genc2= read_files.numeric(data[field+2], 'int')
                genc3= read_files.numeric(data[field+3], 'int')
                genc4= read_files.numeric(data[field+4], 'int')
                faildata.append(genc1)
                faildata.append(genc2)
                faildata.append(genc3)
                faildata.append(genc4)
                
            if data[field]== 'BUSV:':
                bv1= read_files.numeric(data[field+1], 'float')
                bv2= read_files.numeric(data[field+2], 'float')
                bv3= read_files.numeric(data[field+3], 'float')
                bv4= read_files.numeric(data[field+4], 'float')
                faildata.append(bv1)
                faildata.append(bv2)
                faildata.append(bv3)
                faildata.append(bv4)
                
            if data[field]== 'STARTC:':
                startc = read_files.numeric(data[field+3], 'int')
                faildata.append(startc)
            
            field+=1
        sql = f"INSERT INTO faildata VALUES ( %s, %s, %s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, faildata)
        print(mycursor.rowcount, "was inserted.")
