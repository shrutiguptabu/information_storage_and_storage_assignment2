import Classes.Path as Path


class PreprocessedCorpusReader:

    def __init__(self, type):
        try:
            # Read the trecweb/trextext file
            self.fileReader = open(Path.ResultHM1+"."+type, encoding="utf8")
            
        # Throw an exception if unable to open file
        except IOError:
            print('Unable to open the file')
        
        # Initialize a variable count which will keep track of number of documents
        self.count = 0
        return

    # Read a line for docNo from the corpus, read another line 
    # for the content, and return them in [docNo, content].
    def nextDocument(self):
        # load the line in 'line' variable and strip any spaces on the right
        line = self.fileReader.readline().rstrip()
        # initailize a empty list that will return (index number and content)
        result = []
        #check if next line is None
        if not line:
            # close the fileReader as there are no more lines to read
            self.fileReader.close()
            return None
        
        while True:
            # increase the count
            self.count = self.count + 1
            # append the line in the result list
            result.append(line)
            # read another line from document
            line = self.fileReader.readline()
            # append the line in the result list
            result.append(line)
            
            # return the result
            return result
        
