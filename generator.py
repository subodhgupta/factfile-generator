#!/usr/bin/env python
# File name: generator.py
# Author: Tony
# Date created: 
# Date last modified: 
# Python Version: 3.8

# usage:
# add tabcmd path to %PATH% variable
# generator.py "C:\output\folder" "csvFileCoreIDInstitutionName.csv" "TableauViewFolder/Cover" "ID Parameter"

# example:
# python generator.py "C:\Tony\Box Sync\QSIU Shared\Rankings\Arab Region\2018\FactFiles" "arab_list.csv" "RegionalFactFiles2018-ArabRegion/Cover"


import unicodecsv as csv
import subprocess
import credentials
import os
import sys
import shutil
import datetime

def login():
	subprocess.call ("tabcmd login -s http://analytics.qs.com/ -u " + credentials.username + " -p " + credentials.password + " --no-certcheck")

def export(tableauView, coreID, factfilename):
	subprocess.call ('tabcmd export "%s?%s=%s" --fullpdf -f "%s" --pagelayout portrait --pagesize a4 --width 2480 --height 3508 --no-certcheck' %(tableauView, parm.replace(" ", "%20"), coreID, factfilename))

def safestring(s):
	return "".join([c for c in s if c.isalpha() or c.isdigit() or c==' ']).rstrip()

	
boxdir = sys.argv[1] +"\\"
ranking_list = sys.argv[2]
tableauView = sys.argv[3]
parm = sys.argv[4] #ID parameter

#log
readable = safestring(datetime.datetime.now().isoformat())
logfile = open('log_'+readable,'w', encoding="utf-8")
logfile.write('timestamp: '+datetime.datetime.now().isoformat()+"\n")
logfile.write('boxdir: '+boxdir+"\n")
logfile.write('ranking_list: '+ranking_list+"\n")
logfile.write('tableauView: '+tableauView+"\n")
logfile.write('ID parameter: '+parm+"\n")

with open (ranking_list, 'rb') as csvfile:
	login()
	csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	next(csvreader)	#header
	
	for row in csvreader:
		coreID = row[0]
		institution = row[1]
		
		institution = safestring(institution)
		factfilename = coreID+"-"+institution+".pdf"
		
		export(tableauView, coreID, factfilename)
		fexists = os.path.isfile(factfilename)
		
		attempt = 0
		
		while fexists == False and attempt < 5:
			login()
			export(tableauView, coreID, factfilename)
			fexists = os.path.isfile(factfilename)
			attempt = attempt + 1
			
		if fexists == False:
			logfile.write(coreID+","+factfilename + ',PRINT ERROR\n')
		else:
			logfile.write(coreID+","+factfilename + ',PRINT OK\n')
			
		try:
			shutil.move(factfilename, boxdir + factfilename)
			logfile.write(coreID+","+factfilename + ',MOVE OK\n')
		except:
			logfile.write(coreID+","+factfilename + ',MOVE ERROR\n')

logfile.close()
