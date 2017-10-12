
import glob, os
import sys
import json


#{doi}

#key: keyword, value: number
dict_keywords = {}


dataPath = "/ACM"


#remove space
def cleanText(text):
	#print(text)
	#remove first space
	while (len(text)>1 and text[0]==' ' ):
	 	text = text[1:]

	#remove last space
	while (len(text)>1 and text[len(text)-1]==' '):
		text = text[:-1]
	#print("new :"+text)
	return text

#extract key, value of bib text and add 'type', 'index'
def extractBibText(text):
	dict_pub = {}
	
	dict_pub['type'] = text[:text.find('{')]
	
	text = text[text.find('{')+1:text.rfind('}')]
	dict_pub['index'] = text[:text.find(',')]
	text = text[text.find(',')+1:]
	#print(text)
	elements = text.split('},')
	
	#print(dict_pub)
	for ele in elements:
		#print("ele: "+ele)
		key = cleanText(ele[:ele.find('=')])
		value = cleanText(ele[ele.find('{')+1:])
		#print(key+" - "+value)
		if (len(key)>1 and len(value)>1):
			dict_pub[key]=value

	return dict_pub

def checkDoiExist(value, publist):
	for pub in publist:
		if (pub['doi'] == value):
			return True

	return False


def extractFromBibFile(nameFile):
	infile = open(nameFile, encoding='UTF8')
	document = infile.read().replace('\n','')
	#print(document)

	publications = document.split('@')
	publist = []	

	for pubText in publications[1:]:
		pubElement = extractBibText(pubText)
		print('doi' in pubElement)
		if ('doi' in pubElement):
			if (checkDoiExist(pubElement['doi'], publist)==False):
				publist.append(pubElement)
	
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
