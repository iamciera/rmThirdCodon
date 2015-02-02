#Phylogenetics 
Date: January 26, 2015
Since Devin O’Connors and Jill’s paper came out about the phylogentics of PIN and the only disagreeament between our results is the placement of the grasses. I wanted to to see if my grass placement ambiguity was corrected simply by removing the third codon of each sequence. 

I think the easiest way to do this is to auctually write a perl script that deletes the third codon, then proceed with the same analysis pipeline I developed before. 

##Script to remove third codon

###Specifications for the program
1. reads in fasta file
2. ignores lines that start with "<"
3. ignores "-" 
4. removes every third letter

