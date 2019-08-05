:: factfile-generator
:: generator.bat

:: PARAMETERS
:: no double quotes
SET TABCMD_PATH=C:\Program Files\Tableau\Tableau Server\2019.1\extras\Command Line Utility
SET OUTPUT_DIR=C:\Users\tony.fregoli\Box\QSIU Shared\Rankings\World\WUR 2020\Fact Files\PrintOuts\Extended
SET UNI_LIST=.\lists\WUR2020_FF_IDlist_first1000_with_priority_after_extFF_mistake.csv
SET TABLEAU_WORKBOOK=ff_wur_2020ExtendedVersion/Cover
SET ID_PARM=ID (Parameter)

:: generator
SET PATH=%TABCMD_PATH%;%PATH%
python generator.py "%OUTPUT_DIR%" %UNI_LIST% "%TABLEAU_WORKBOOK%" "%ID_PARM%"


