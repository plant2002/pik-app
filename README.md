#Pik-App

current stuff I am working on:

-graphs, analysis of the data in DB

Analysis: 
-	Analize parametrov glede na količino oz. od/do tip poizvedb nad:
o	Flight number
o	Flight duration
o	Engine cycles
o	Overlimits
-	Analize dela z napakami (failures)
o	Code
o	Name
o	Occurrences
o	Start time
o	Duration
o	Context (kaj je šlo narobe, se deli dalje na NG, NF, T4a, T4b,…., tukaj dodatne posamezne analize kaj je šlo narobe, dodatne forme za poizvedbe)
-	Grafi:
o	Duration of flights / date
o	Duration of flight/ flight number
o	Engine cycles / flight number or date
o	Overlimits / flight
o	Number of errors/flight number or date
-	Izpisi/export CSV datotek o:
o	Napake glede na flight number oz. od/do flight number
o	Izpis podatkov za flight number
o	Izpis letov in podatkov glede na datum


currently done:

- cleaning up CSV 
- database 
- connecting DB to python 
- main page of GUI 
- GUI is okay now 
- GUI connect to other frames works okay, all in one file though (GUI2.py) since the links weren't working as they should in multiple files. 
- uploading csv files to a folder 'uploads' 
- importing into DB (all works and gets inserted. Failures only when a new code is detected)
- moving csv after it was processed
- reimporting works and rewrites the rows in the database

https://www.figma.com/file/sVt59DgmlymZQrweML1bTM/Pik-app?type=design&node-id=36-27&mode=design&t=1rqOvimrYzFkVntX-0 tkdesigner notes:

a) run it on 3.10 since it doesn't work with newer Pillow version (py gui.py -version) 
b) change utils.py --> add PIL.Image.ANTIALIAS = PIL.Image.LANCZOS 
c) watch the naming and amount of frames you use on Figma


#Previous versions are under Report depository on my GitHub...kinda have a hard time editing it
