# Import neccesory libraries 
import Classes.Path as Path
from collections import defaultdict
import csv

# Efficiency and memory cost should be paid with extra attention.
class MyIndexWriter:

    def __init__(self, type):
        
        # This variable will hold the type of the input corpus file
        self.file_type = type
        
        # Create the Dictionary object for Index Dictionary
        # Terms will be keys and its corresponding data as values
        self.dictionaries =  defaultdict(dict)
        
        # Create the Dictionary object for Index Postings
        # Terms will be keys and its corresponding data as values
        self.postings =  defaultdict(list)
        
        return

    # This method build index for each document.
	# NT: in your implementation of the index, you should transform your string docno into non-negative integer docids,
    # and in MyIndexReader, you should be able to request the integer docid for each docno.
    def index(self, docNo, content):
        
        # Initialize local variables scoped to each unique document
        
        # Unique terms in a document
        unique_terms = set()
        
        # Dictionary to hold term frequency in a document
        doc_freq = {}
        
        # Let us convert the DocNo to DocId and store it for
        # use during entire document processing
        doc_id = self.getDocId(docNo)
        
        # Split the document content into a list
        terms = content.split()
        
        # Loop through each term in the document
        for term in terms:
                  
            # First check if the term is existing in index or not
            existing_term = self.dictionaries.get(term)
            
            # Existing term in the Index Dictionary
            if existing_term:
                # Let us check if the term is new for document as well
                if term in unique_terms:
                    # The term has been seen in the document before
                    # increment both corpus and document frequency
                    self.dictionaries[term]['corpus_freq'] = existing_term['corpus_freq'] + 1
                    doc_freq[term] += 1
                # Existing term for both corpus and document
                else:
                    # Term has been seen in corpus but no in this document
                    # increment corpus frequency, number of documents
                    # also add this term in list of unique terms for the doc
                    self.dictionaries[term]['corpus_freq'] = existing_term['corpus_freq'] + 1
                    self.dictionaries[term]['num_docs'] = existing_term['num_docs'] + 1
                    unique_terms.add(term)
                    doc_freq[term] = 1
            # New term in the entire corpus
            else:
                # Since the term is new for both corpus and document,
                # initialize all frequecies to 1
                self.dictionaries[term] = {'corpus_freq': 1, 'num_docs': 1}
                unique_terms.add(term)
                doc_freq[term] = 1
                
        
        # We have processed the entire document, Flatten the postings
        for term, term_count in doc_freq.items():
            # If the term is already existing, increment frequency
            if term in self.postings.keys():
                self.postings[term][doc_id] = term_count
            # Term is new, initialize the dictionary object
            else:
                self.postings[term] = {doc_id : term_count}

    # Close the index writer, and you should output all the buffered content (if any).
    def close(self):

        # Write the dictonaries list onto file, using csv writer and 16MB buffer
        with open(Path.ResultHM1 + "-dictionary." + self.file_type, "w", 
                  encoding="utf8", newline='', buffering=16777216 ) as dictionary_file:
            dictionary_writer = csv.writer(dictionary_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            # Loop through the dictionary object and write o/p file
            for term, values in self.dictionaries.items():
                dictionary_writer.writerow([term, values['corpus_freq'], values['num_docs']])   
        
        # Write the object list onto file, using csv writer and 16MB buffer
        with open(Path.ResultHM1 + "-postings." + self.file_type, "w", 
                  encoding="utf8", newline='', buffering=16777216 ) as posting_file:
            posting_writer = csv.writer(posting_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            # Loop through the dictionary object and write o/p file
            for term, values in self.postings.items():
                    posting_writer.writerow([term, values])        
        
        return
    
    # Return the integer DocumentID of input string DocumentNo.
    def getDocId(self, docNo):
        if self.file_type == "trecweb":
            return docNo[6:].replace('-','')
        else:
            return docNo[3:].replace('.','')