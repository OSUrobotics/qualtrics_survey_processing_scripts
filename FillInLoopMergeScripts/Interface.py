import os
import csv

#These are macros for the file paths to the .qsf and the .csv
#Change them as needed
QSFFILENAME = os.path.expanduser("/home/reu4/qualtrics_survey_processing_scripts/FillInLoopMergeScripts/Shape_complexity_refined.qsf")
CSVFILENAME = os.path.expanduser("/home/reu4/qualtrics_survey_processing_scripts/FillInLoopMergeScripts/QualtricsMapping.csv")


#returns the entire text of the .qsf as a string
def readOriginalQSF():
	inputFile = open(QSFFILENAME, "r");
	fullFileText = inputFile.read();
	inputFile.close();
	return fullFileText;

#overrights the .qsf file with the new, filled in, text
def writeFinalQSF(result):
	inputFile = open(QSFFILENAME, "w");
	inputFile.write(result);
	inputFile.close();

#Generator to read the URLs row by row
def readCSV():
	with open(CSVFILENAME) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			yield row


