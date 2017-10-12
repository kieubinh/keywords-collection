
import glob, os
import sys
import json


#{doi}

#key: keyword, value: number
dict_keywords = {}

dataPath = "/ACM"


#remove space
def cleanText(text):
	#remove first space
	while (len(text)>1 and text[0]==' ' ):
	 	text = text[1:]

	#remove last space
	while (len(text)>1 and text[-1]==' '):
		text = text[:-1]
	return text

#extract key, value of bib text and add 'type', 'index'
def extractBibText(text):
	dict_pub = {}
	dict_pub['type'] = text[:text.find('{')]
	text = text[text.find('{')+1:text.rfind('}')]
	#print(text)
	elements = text.split(',')
	dict_pub['index'] = elements[0]
	for ele in elements:
		key = cleanText(ele[:ele.find('=')])
		value = cleanText(ele[ele.find('{')+1: ele.rfind('}')])
		if (len(key)>1 and len(value)>1):
			dict_pub[key]=value

	return dict_pub


def extractFromBibFile(nameFile):
	infile = open(nameFile, encoding='UTF8')
	document = infile.read().replace('\n','')
	#print(document)

	publications = document.split('@')
	publist = []

	for pubText in publications:
		publist.append(extractBibText(pubText))
	
	jsonPub = json.dumps(publist)
	print(jsonPub)


def readFolder():

	for file in os.listdir(os.getcwd()+dataPath):
		#print(file)
		if file.endswith(".bib"):
			#print(os.path.join(dataPath, file))			
			extractFromBibFile(os.path.join(os.getcwd()+dataPath, file))


def main():
    readFolder()


if __name__ == "__main__":
    main()
