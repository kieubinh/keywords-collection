
import os

dataPath = "F:\data\Aminer"
files = ['citation-network2.txt', 'outputacm.txt', 'DBLPOnlyCitationOct19.txt']
#files = ['citation-network2.txt']
output = 'keywords-statistics.txt'
keywordCount = dict()
FLAG_START = "Keywords:"
#convert to default break comma: ","
BREAK_COMMAS = [';', 'and',"."]

def normalizeText(str):

    #remove space in header
    while (len(str)>1 and str[0]==" "):
        str = str[1:]
    #remove space in last
    while (len(str)> 1 and str[len(str)-1]==" "):
        str = str[:-1]

    str = str.replace(",","")
    str = str.replace(";", "")
    str = str.replace(".", "")

    return str

def extractFromFiles():

    for file in files:
        infile = open(os.path.join(dataPath, file), encoding='UTF8')
        for line in infile:
            if line.find(FLAG_START)!=-1:
                keywords = line[line.find(FLAG_START)+len(FLAG_START):]
                keywords = keywords[:keywords.find(".")]
                if (keywords.find("The ACM Portal")!=-1):
                    keywords = keywords[:keywords.find("The ACM Portal")]
                #print(keywords + "\n")
                for comma in BREAK_COMMAS:
                    keywords = keywords.replace(comma,",")

                keywordList = keywords.split(",")
                for keyword in keywordList:
                    keyword = normalizeText(keyword)
                #print(keyword+"\n")
                if (len(keyword)>1):
                    if (keyword in keywordCount):
                        keywordCount[keyword]+=1
                    else:
                        keywordCount[keyword]=1
        infile.close()

def writeToFile():
    #sortedKeywordCount = sorted(keywordCount.items(), key=operator.itemgetter(1))
    #print(keywordCount)
    outfile = open(output, 'w', encoding='UTF8')
    for (key, value) in sorted(keywordCount.items(), reverse=True):
        outfile.writelines(key +":"+str(value)+"\n")
    outfile.close()

#MAIN
extractFromFiles()
writeToFile()






