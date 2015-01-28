#Phylogenetics 
Date: January 26, 2015
Since Devin O’Connors and Jill’s paper came out about the phylogentics of PIN, it became apparent to me that I should try my tree by removing the third codon of each sequence. The monocots were never placed correctly in my trees. 

I think the easiest way to do this is to auctually write a perl script that deletes the third codon, then proceed with analysis.  I already have the alignment. 

##Script to remove third codon

###Specifications for the program
1. reads in fasta file
2. ignores lines that start with "<"
3. ignores "-" 
4. removes every third letter

###Strategy
- Captures sequence has any length of ACTGs.  
- This might just might be a regex problem.  Capture any length of a string of ACTGs.

###To-do
[ ] read in fasta file
[ ] start playing
[ ] 


IPLANT

iamciera
Harvest9117!

Phylemon
ciera.martinez@gmail.com
noass4u