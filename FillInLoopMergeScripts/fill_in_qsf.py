import os
import Interface

#These macros are constants based on the format of a .qsf file
#The Keyword begins every block's fields
KEYWORD = "Static\":"
#The Blank location is where the urls need to be filled in
BLANKLOCATION = "\"\""
#The end question is the point at which all the fields for the block have come before
ENDBLOCK = "}}"


def thereAreMoreBlocksToBeFilled(keywordStartIndex):
	return keywordStartIndex != -1
	
def thereIsAnotherBlankInBlock(replacementStartIndex, closingBracketIndex):
	return (replacementStartIndex < closingBracketIndex) and (replacementStartIndex != -1)

def getNextURLFromCSV(csvGenerator):
	csvURL = next(csvGenerator)[2];
	csvURL = csvURL.replace("/", "\/");
	return csvURL;

def fillInBlankURL(currentIndex, replacementStartIndex, result, csvGenerator):
	ImageFileURL = getNextURLFromCSV(csvGenerator);
	result = "{}{}{}".format(result, fullFileText[int(currentIndex): int(replacementStartIndex)], ImageFileURL)
	currentIndex = replacementStartIndex
	replacementStartIndex = fullFileText.find(BLANKLOCATION, currentIndex+2)+1
	return (currentIndex, result, replacementStartIndex)

def fillInBlock(keywordStartIndex, currentIndex, result, csvGenerator):
	closingBracketIndex = fullFileText.find(ENDBLOCK, keywordStartIndex)
	replacementStartIndex = fullFileText.find(BLANKLOCATION, keywordStartIndex)+1
	while thereIsAnotherBlankInBlock(replacementStartIndex, closingBracketIndex):
		currentIndex, result, replacementStartIndex = fillInBlankURL(currentIndex, replacementStartIndex, result, csvGenerator)
	return (result, currentIndex)

if __name__ == "__main__":
	result = "";
	currentIndex = 0;
	
	#The provided files are set as macros in Interface and can be changed as needed
	fullFileText = Interface.readOriginalQSF();
	csvGenerator = Interface.readCSV();
	#This ignores the header line in the spreadsheet
	next(csvGenerator);

	keywordStartIndex = fullFileText.find(KEYWORD)
	while thereAreMoreBlocksToBeFilled(keywordStartIndex):
		result, currentIndex = fillInBlock(keywordStartIndex, currentIndex, result, csvGenerator)
		keywordStartIndex = fullFileText.find(KEYWORD, currentIndex)

	#Once all blanks have been filled, copy the rest of the file onto the end of the string
	result += fullFileText[int(currentIndex):]
	#Overwrite the original .qsf with the new, filled in text
	Interface.writeFinalQSF(result)