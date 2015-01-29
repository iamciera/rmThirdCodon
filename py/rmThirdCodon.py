#!/usr/bin/env python
#rmThirdCodon.py 
#Ciera Martinez

#This script inputs a fasta file alignment from transx aligner.  
#These are for CDS sequences only!
#It removes the third codon from all the sequences

#The verifying part needs a bit of work, but you should get 1/3 of the 
#nucleotides missing from the file that was input.
#- How do I print to console or file?  Right now the verifying part prints to 
#only the out put file
# - The result is 14 nucleotides off!
# - Write a true false test to test it. 

import re
import sys	

#This sets up output file
orig_stdout = sys.stdout
data = open("./fasta/rmThirdCodonOutput.fasta", 'w')
sys.stdout = data

fastaFile = open(sys.argv[1]) #file that contains fasta file

fastaRead = fastaFile.read() #Makes a one item string

#this removes the third codon and reasults in one item string
thirdGone = re.sub(r"([ATCG])([ATCG])[ATCG]", r"\1\2", fastaRead)
print thirdGone

#Verify
beforeMatchResult = re.findall(r"[ATCG][ATCG][ATCG]*",fastaRead)
beforeResult = ''.join(beforeMatchResult)
lengthBefore = len(beforeResult)
print 'before %d' %(lengthBefore)

afterMatchResult = re.findall(r"[ATCG][ATCG][ATCG]*",thirdGone)
afterResult = ''.join(afterMatchResult)
lengthAfter = len(afterResult)
print 'after %d' %(lengthAfter)

fastaFile.close()
data.close()
