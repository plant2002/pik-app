#Pik-App

current stuff I am working on:

-graphs, analysis of the data in DB

Analysis: 
-	Analize parametrov glede na količino oz. od/do tip poizvedb nad:
- [ ] Flight number
- [x]	Flight duration (per day & per flight)
- [x]	Engine cycles (2 graphs)
- [x]	Overlimits
-	Analize dela z napakami (failures)
- [x]	Name (also show code when choosing so I killed two birds with one stone)
- [x]	Occurrences
- [x]	get the name, descr, code of errors happening on date or date_from/date_to
- [ ]	calculate averages and find the ones that are above/below average and show them on a graph
o	Context (kaj je šlo narobe, se deli dalje na NG, NF, T4a, T4b,…., tukaj dodatne posamezne analize kaj je šlo narobe, dodatne forme za poizvedbe)
-	Grafi:
- [x]	Duration of flights / date
- [x]	Duration of flight/ flight number
- [x]	Engine cycles / flight number or date
- [x]	Overlimits / flight
- [x]	Number of errors/flight number or date
-	Izpisi/export CSV datotek o:
- [ ]	Napake glede na flight number oz. od/do flight number
- [ ]	Izpis podatkov za flight number
- [ ]	Izpis letov in podatkov glede na datum

<h3>MAKE SURE IT'S BULLETPROOF (SUCH AS MAKING SURE THAT THEY CAN'T INSERT BIGGER NUMBER IN FN_FROM AND SMALLER NUMBER IN FN_TO BECAUSE IT MAKES THE WHOLE THING INCORRECT!!!!)</h3>

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
