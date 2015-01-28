#!/usr/bin/env python
#rmThirdCodon.py 
#Ciera Martinez

###Specifications for the program
# [x] 1. reads in fasta file
# [x] 2. ignores lines that start with "<"
# [x] 3. ignores "-" this shouldn't be nessisary if you specify 
# [x] 4. removes every third letter
# [ ] 5. Now I have to write a test that checks the number of nucleotides removed per sequence.

import re
import sys	

#This sets up output file
orig_stdout = sys.stdout
#data = open("./data/pyOutputs/rmThirdCodonOutput", 'w')
#sys.stdout = data

fastaFile = open(sys.argv[1]) #file that contains fasta file

fastaRead = fastaFile.read() #Makes a one item string

#This matches all sequences
match = re.findall(r"[ATCG][ATCG][ATCG]*",fastaRead)
print match

#This matches all codons
# matchTry = re.findall(r"[ATCG][ATCG][ATCG]",fastaRead)
# print matchTry

#this re
thirdGone = re.sub(r"([ATCG])([ATCG])[ATCG]", r"\1\2", fastaRead)
print thirdGone

#what if instead I capture just the three letters.  Ty

#Simple sub to remove third codon, need to make
#sampleReadClean = re.sub('', '', sampleRead) #removes symbols

fastaFile.close()
#data.close()



