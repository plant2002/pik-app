<h1>Pik-App</h1>

Analysis: 
- analysis of parameters according to:
- [ ] Flight number (kinda useless so maybe not)
- [x]	Flight duration (per day & per flight)
- [x]	Engine cycles (2 graphs)
- [x]	Overlimits
-	Anallysis of failures:
- [x]	Name (also show code when choosing so I killed two birds with one stone)
- [x]	Occurrences
- [x]	get the name, descr, code of errors happening on date or date_from/date_to
- [ ]	calculate averages and find the ones that are above/below average and show them on a graph <h3>this should probably be left for after presentation though it's super important so idk</h3>
-	Graphs:
- [x]	Duration of flights / date
- [x]	Duration of flight/ flight number
- [x]	Engine cycles / flight number or date
- [x]	Overlimits / flight
- [x]	Number of errors/flight number or date
-	export CSVs:
- [x]	data fn_from/fn_to
- [x]	data for specific fn
- [x]	data for fns for specific date
- [x]	data for fns date_from/date_to
- [x]	export all data about fns with specific error

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
