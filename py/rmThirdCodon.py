#!/usr/bin/env python
#rmThirdCodon.py 
#Ciera Martinez

###Specifications for the program
#1. reads in fasta file
#2. ignores lines that start with "<"
#3. ignores "-" 
#4. removes every third letter

import re
import sys	

#This sets up output file
orig_stdout = sys.stdout
#data = open("./data/pyOutputs/rmThirdCodonOutput", 'w')
#sys.stdout = data

fastaFile = open(sys.argv[1]) #file that contains fasta file

print fastaFile.readline(100)

fastaRead = fastaFile.read() #Makes a one item string

print(fastaRead)

#Simple sub to remove third codon, need to make
#sampleReadClean = re.sub('[^A-Za-z0-9\s]+', '', sampleRead) #removes symbols

fastaFile.close()
#data.close()
