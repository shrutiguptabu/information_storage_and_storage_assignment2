A short instruction on how to read your scripts and how to run your scripts, including environment configuration. (This should be a txt file.)

Environment configuration:
 - Windows 10 Home
 - Processor : Intel(R) Core(TM) i7-8750H CPU @ 2.20GHZ 2.21 GHZ
 - Installed Memore(RAM) : 16.0 GB
 - System Type : 64 - bits Operating System

Instructions:
1. Open Anaconda. Open Spyder 3.3.6 (Python 3.7) and upload the folder.
2. Run the HW2Main.py file. This will run the entire code:
    a. First an index will be created for the trecweb file. The index is broken into a Dictionary file and a Postings file.
    b. Next we will read the index. In this step we load the entire Dictionary file into memory.
    c. To search a term, dictionary object is searched in memory and its corresponding entry is searched sequentially in postings file.
    d. Once the term is found, postings data is returned.
3. The step 2 will repeat for result.trectext file as well.


Results:
The results of the processed data is stored in the data folder 
data/result-posting.trecweb and data/result-dictionary.trecweb for input file docset.trecweb 
data/result-posting.trectext and data/result-dictionary.trectext for input file docset.trectext