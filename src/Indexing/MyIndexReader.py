# import necessry libraries
import Classes.Path as Path
import csv
import sys
import json

# Efficiency and memory cost should be paid with extra attention.
class MyIndexReader:

    def __init__(self, type):
        
        # We are increasing the column length that csv reader can read
        maxInt = sys.maxsize
        while True:        
            try:
                csv.field_size_limit(maxInt)
                break
            except OverflowError:
                maxInt = int(maxInt/10)
                
        # This variable will hold the type of the input corpus file
        self.type = type
        
        # Create a dictionary object to load Index dictionary file
        self.dictionary =  {}
        
        # Load the Index dictionary file during the init
        self.loadDictionaryFile(type)
        
    # Loads the dictionary file
    def loadDictionaryFile(self, fileType):
        # Read the csv file and populate the dictionary object
        with open(Path.ResultHM1 + "-dictionary" + "." + fileType, encoding="utf8") as dictionary_file:
            reader = csv.reader(dictionary_file)
            self.dictionary = { rows[0] : [ rows[1], rows[2] ] for rows in reader}
                   
            
    # Return the integer DocumentID of input string DocumentNo.
    def getDocId(self, docNo):
        if self.file_type == "trecweb":
            return docNo[6:].replace('-','')
        else:
            return docNo[3:].replace('.','')
        

    # Return the string DocumentNo of the input integer DocumentID.
    def getDocNo(self, docId):        
        
        # First convert the int docId to String for further processing
        docNo = str(docId)
        
        # When the file type is trectext
        if self.type == 'trectext':
            if int(docNo[:4]) >= 1998:
                docNo = "NYT" + docNo
            else:
                docNo = "XIE" + docNo
            docNo = docNo[:11] + "." + docNo[11:]
        
        # When the file type is trecweb
        if self.type == "trecweb":
            docNo = "lists-" + docNo
            docNo = docNo[:9] + "-" + docNo[9:]
        
        return docNo

    # Return DF.
    def DocFreq(self, token):
        return int(self.dictionary[token][1])
        
    # Return the frequency of the token in whole collection/corpus.
    def CollectionFreq(self, token):
        return int(self.dictionary[token][0])

    # Return posting list in form of [{documentID:frequency}].
    def getPostingList(self, token):
        
        # Read the postings file
        with open(Path.ResultHM1 + "-postings" + "." + self.type, 
                  encoding="utf8") as postings_file:
            reader = csv.reader(postings_file)
            
            # Loop through the file until we find the term
            for rows in reader:
                
                # CHeck if we have a match on the term/token
                if rows[0] == token:
                    
                    # Replace single quotes with double so we can load json
                    res = rows[1].replace("\'", "\"")
                    res = json.loads(res)
                    return res
