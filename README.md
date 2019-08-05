# factfile-generator
Generates pdf fact files through Tableau Server

## Requirements
* Python 3
* Additional python modules: unicodecsv, shutil
* Tableau `tabcmd` client installed
* A valid username and password for Tableau Server
  username and password  must be placed in the same directory in a file called `credentials.py`
* A valid Tableau workbook already published in the server 
* A valid list of universities in a csv file
* A valid ID paramter for dynamic contents

## Usage
* amend generator.bat with the correct parameters
```
generator.bat
```

## Example
```
generator.bat
```

**credentials.py**
```
username = 'my_username'
password = 'my_password'
```

