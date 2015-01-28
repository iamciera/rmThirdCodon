#!/usr/bin/env python
#rmThirdCodon.py 
#Ciera Martinez

###Specifications for the program
#1. reads in fasta file
#2. ignores lines that start with "<"
#3. ignores "-" this shouldn't be nessisary if you specify 
#4. removes every third letter

import re
import sys	

#This sets up output file
orig_stdout = sys.stdout
#data = open("./data/pyOutputs/rmThirdCodonOutput", 'w')
#sys.stdout = data

fastaFile = open(sys.argv[1]) #file that contains fasta file

fastaRead = fastaFile.read() #Makes a one item string

match = re.findall(r"[ATCG][ATCG][ATCG]*",fastaRead)
print match

#Simple sub to remove third codon, need to make
#sampleReadClean = re.sub('', '', sampleRead) #removes symbols

fastaFile.close()
#data.close()
