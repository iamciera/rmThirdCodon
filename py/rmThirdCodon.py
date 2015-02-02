#!/usr/bin/env python
#rmThirdCodon.py 
#Ciera Martinez

#This script removes the third codon and replaces with a "-"
#Made to work with already aligned sequences. 
#Output is fasta file.
#Only use with CDS sequences.

import re
import sys	

#This sets up output file
orig_stdout = sys.stdout
#set where you want the output file to go
data = open("./fasta/rmThirdCodonOutput.fasta", 'w')
sys.stdout = data

#open and read in fasta file
fastaFile = open(sys.argv[1]) 
fastaRead = fastaFile.read() 

#Split by ">"
fastaList = fastaRead.split(">")

#Removes the third codon, sequence by sequence.
thirdGoneList = []
for sequence in fastaList:
	a = re.sub(r"([ATCG])([ATCG])[ATCG]", r"\1\2-", sequence);
	thirdGoneList.append(a)

#join together the list
thirdGoneString = ''.join(thirdGoneList)
print thirdGoneString

#resets standard output back to terminal
sys.stdout = sys.__stdout__

#Verification Test
#Tests that exactly one third of the total nucleotides where removed

#How many nucleotides before the third codon was removed?
nucBefore = re.findall(r"[ATCG][ATCG][ATCG]*",fastaRead)
beforeResult = ''.join(nucBefore)
lengthBefore = len(beforeResult)
print '\nNucleotides before %d' %(lengthBefore)

#How many nucleotides after the thrid codon was removed?
nucAfter = re.findall(r"[ATCG][ATCG][ATCG]*",thirdGoneString)
afterResult = ''.join(nucAfter)
lengthAfter = len(afterResult)
print 'Nucleotides after %d' %(lengthAfter)

#Did it work?  
if (lengthBefore/3)*2 != lengthAfter:
	print '\nWARNING: Something is off! You should have %d nucleotides, but you have %d\n' %((lengthBefore/3)*2, lengthAfter);

if (lengthBefore/3)*2 == lengthAfter:
	print '\nLooks Good!\n'
		
fastaFile.close()
data.close()

