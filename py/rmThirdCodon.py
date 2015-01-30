#!/usr/bin/env python
#rmThirdCodon.py 
#Ciera Martinez

#This script inputs a fasta file alignment from transx aligner.  
#These are for CDS sequences only!
#It removes the third codon from all the sequences

#The verifying part needs a bit of work, but you should get 1/3 of the 
#nucleotides missing from the file that was input.
# - The result is 14 nucleotides off!


#We should really start the counting fresh for each sequence, 
#that way we make sure that we are geting the third codon for each sequence 
#and one sequence doesn't mess up the rest. IN order to that, seperate each 
#sequence into it's own item in a list. 
#also, instead of getting rid of the nucleotide, maybe we just add a "-" that 
#the alignment is not messed up. 

#To-do

# [ ] Split each sequence into an item in a list
# [ ] How many nucleotides in each sequence. 
# [ ] Can they be divided by three?

import re
import sys	

#This sets up output file
orig_stdout = sys.stdout
# data = open("./fasta/rmThirdCodonOutput.fasta", 'w')
# sys.stdout = data

fastaFile = open(sys.argv[1]) #file that contains fasta file

fastaRead = fastaFile.read() 


#Split by > 
fastaList = fastaRead.split(">")

thirdGoneList = {}
#this removes the third codon
for sequence in fastaList:
	thirdGoneList[sequence] = re.sub(r"([ATCG])([ATCG])[ATCG]", r"\1\2-", sequence);

thirdGoneString = ''.join(thirdGoneList)
print thirdGoneString

# #resets standard output back to terminal
# sys.stdout = sys.__stdout__


# #Verification Test
# #How many nucleotides before the third codon was removed?
# nucBefore = re.findall(r"[ATCG][ATCG][ATCG]*",fastaRead)
# beforeResult = ''.join(nucBefore)
# lengthBefore = len(beforeResult)
# print '\nbefore %d' %(lengthBefore)

# lengths = [(len(i)/float(3)) for i in nucBefore]
# print lengths

# #How many nucleotides after the thrid codon was removed?
# nucAfter = re.findall(r"[ATCG][ATCG][ATCG]*",thirdGone)
# afterResult = ''.join(nucAfter)
# lengthAfter = len(afterResult)
# print 'after %d' %(lengthAfter)

# #Did it work?  The message displayed.
# if (lengthBefore/3)*2 != lengthAfter:
# 	print '\nWARNING: Something is off! You should have %d nucleotides, but you have %d\n' %((lengthBefore/3)*2, lengthAfter);

# if (lengthBefore/3)*2 == lengthAfter:
# 	print '\nLooks Good!\n'
		
# fastaFile.close()
# data.close()

