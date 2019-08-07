# factfile-generator
Generates pdf fact files through Tableau Server

## Requirements
* Python 3
* Additional python modules: unicodecsv, shutil
* Tableau `tabcmd` client installed
* A valid username and password for Tableau Server\
username and password  must be placed in the same directory in a file called `credentials.py`
* A valid Tableau workbook already published in the server 
* A valid list of universities in a csv file
* A valid ID paramter for dynamic contents

## Usage
Amend generator.bat with the correct parameters, then from Windows command prompt
```
generator
```

## Example
**generator.bat**
```
SET TABCMD_PATH=C:\Program Files\Tableau\Tableau Server\2019.1\extras\Command Line Utility
SET OUTPUT_DIR=C:\Box\QSIU Shared\Rankings\World\WUR 2020\Fact Files\PrintOuts\Extended
SET UNI_LIST=.\lists\WUR2020_example.csv
SET TABLEAU_WORKBOOK=ff_wur_2020ExtendedVersion/Cover
SET ID_PARM=ID (Parameter)
```

**credentials.py**
```
username = 'my_username'
password = 'my_password'
```

**WUR2020_example.csv**
```
core_id,institution
365,UCL (University College London)
356,Imperial College London
69,University of Bristol
170,Durham University
```
