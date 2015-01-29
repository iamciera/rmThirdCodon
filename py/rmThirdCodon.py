#!/usr/bin/env python
#rmThirdCodon.py 
#Ciera Martinez

#This script inputs a fasta file alignment from transx aligner.  
#These are for CDS sequences only!
#It removes the third codon from all the sequences

#The verifying part needs a bit of work, but you should get 1/3 of the 
#nucleotides missing from the file that was input.
# - The result is 14 nucleotides off!
# - Write a true false test to test it. 

import re
import sys	

#This sets up output file
orig_stdout = sys.stdout
data = open("./fasta/rmThirdCodonOutput.fasta", 'w')
sys.stdout = data

fastaFile = open(sys.argv[1]) #file that contains fasta file

fastaRead = fastaFile.read() 

#this removes the third codon
thirdGone = re.sub(r"([ATCG])([ATCG])[ATCG]", r"\1\2", fastaRead)
print thirdGone

#resets standard output back to terminal
sys.stdout = sys.__stdout__

#Verification Test

#How many nucleotides before the third codon was removed?
nucBefore = re.findall(r"[ATCG][ATCG][ATCG]*",fastaRead)
beforeResult = ''.join(nucBefore)
lengthBefore = len(beforeResult)
print '\nbefore %d' %(lengthBefore)

#How many nucleotides after the third codon was removed?
nucAfter = re.findall(r"[ATCG][ATCG][ATCG]*",thirdGone)
afterResult = ''.join(nucAfter)
lengthAfter = len(afterResult)
print 'after %d' %(lengthAfter)

#Did it work?  The message displayed.
if (lengthBefore/3)*2 != lengthAfter:
	print '\nWARNING: Something is off! You should have %d nucleotides, but you have %d\n' %((lengthBefore/3)*2, lengthAfter);

if (lengthBefore/3)*2 == lengthAfter:
	print '\nLooks Good!\n'
		
fastaFile.close()
data.close()

