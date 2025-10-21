<h1>Pik-App</h1>

TO DO:
- [ ]	Make sure it's bulletproof (after presentation, such as that date_from is earlier than date_to, fn_from smaller than fn_to etc)
- [ ]	get the code cleaned up
- [x]	connect GUI to functions
- [x]	show graphs in GUI Analysis
- [x]	change GUI Analysis
- [x]	create a Jupyter notebook with analysis + export in it
- [x]	PowerPoint presentation
- [x]	added client, company, helicopter tables to database
- [ ]	client login/register
- [ ]	company login/register
- [ ]	add new helicopter GUI + queries

Analysis: 
- analysis of parameters according to:
- [x]	Flight duration (per day & per flight)
- [x]	Engine cycles (2 graphs)
- [x]	Overlimits
-	Analysis of failures:
- [x]	Name (also show code when choosing so I killed two birds with one stone)
- [x]	Occurrences
- [x]	get the name, descr, code of errors happening on date or date_from/date_to
- [ ]	calculate averages and find the ones that are above/below average and show them on a graph (function error_code_data, not working)<h3>this should probably be left for after presentation though it's super important so idk</h3>
- [ ] calculate standard deviations (1σ, 2σ,....)
- [ ] calculate the deviation of a parameter from standard deviation*N (N is chosen by user)
- [ ] reading the additional data from files (there is more in some)
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
-	Basic functions:
- [x] cleaning up CSV 
- [x] database 
- [x] connecting DB to python 
- [x] main page of GUI 
- [x] GUI is okay now 
- [x] GUI connect to other frames works okay, all in one file though (GUI2.py) since the links weren't working as they should in multiple files.
- [ ] Clean up GUI_2
- [x] uploading csv files to a folder 'uploads' 
- [x] importing into DB (all works and gets inserted. Failures only when a new code is detected)
- [x] moving csv after it was processed
- [x] reimporting works and rewrites the rows in the database

https://www.figma.com/file/sVt59DgmlymZQrweML1bTM/Pik-app?type=design&node-id=36-27&mode=design&t=1rqOvimrYzFkVntX-0 tkdesigner notes:

- a) run it on 3.10 since it doesn't work with newer Pillow version (py gui.py -version) 
- b) change utils.py --> add PIL.Image.ANTIALIAS = PIL.Image.LANCZOS 
- c) watch the naming and amount of frames you use on Figma


