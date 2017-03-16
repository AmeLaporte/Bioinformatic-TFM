import sys
import random

def getIndex(txt,mot1,mot2,int1,int2):
    """This function is written by LAPORTE Amelie.

    Args:
       txt:correspond to the genbank entry stored in memory with the readFlatFile function.
       mot1, mot2: the words used as index to separate the information.
       int1,int2: the number of characters to delete in the separated information. 
        
    Returns:
       The function return the same thing than if we've had used the index method but simplified to have a clearer code.
    """
    txt=txt[txt.index(mot1)+int1:txt.index(mot2,txt.index(mot1))+int2]
    return txt

def parserFasta(filename,acs,dic):
    """This function is written by LAPORTE Amelie.
    Args:
       filename:The FASTA file of the population you want to compare to the reference.
       acs:The list containing the accession numbers. 
       dic: empty dictionary
    Returns:
       The function return a dictionary with the accession numbers as keys.
    """
    #open the FASTA file
    sourceText=open(filename,"r")
    #create a list which contain one line per index
    source=sourceText.read().splitlines(1)
    #loop to only keep the headers
    for i in range(0,len(source),2):
        if '>' in source[i]:
            #to store accession number in list
            acs.append(getIndex(source[i],">","\t",0,0))
    for i in range(0,len(acs)):
        dic[acs[i]]=''
    sourceText.close()
    return acs,dic

def randomAcsNumber(acs,dic,rdm,nb):
    """This function is written by LAPORTE Amelie.
    Args:
       acs:The list containing the accession numbers. 
       dic: empty dictionary
       rdm:The output list containing the random accession numbers.
       nb: The percentage of accession numbers you want to select
        
    Returns:
       The function return a list of random amount of (choosen by the user) accession numbers and a corresponding dictionary with these numbers as keys.
    """
    perc=len(acs)*nb/100
    for i in range(0,perc):
        rdm.append(random.choice(acs))
    for i in range(0,len(rdm)):
        dic[rdm[i]]=''
    return dic,rdm

def dictionariesFasta(filename,lstrdm,lstall,dicrdm,dicall):
    """This function is written by LAPORTE Amelie.
    Args:
       filename:The FASTA file of the database.
       lstrdm: the list of random accession numbers
       lstall: the list of all the accession numbers
       dicrdm: the dictionary with the random numbers as key
       dicall: the dictionary with all the accession numbers as key
    Returns:
       The function return 2 dictionaries: one with the random accession number + their sequence and one for all the accession number +their sequence.
    """
    sourceText=open(filename,"r")
    source=sourceText.read().splitlines(1)
    #loop to only keep the sequences corresponding to the random accession numbers
    for i in range(0,len(source)):
        for j in range(0,len(lstrdm)):
            if lstrdm[j] in source[i]:
                dicrdm[lstrdm[j]]=getIndex(source[i+1],'','\n',0,0)
    #loop to only keep the sequences corresponding to all the accession numbers
    for i in range(0,len(source)):
        for j in range(0,len(lstall)):
            if lstall[j] in source[i]:
                dicall[lstall[j]]=getIndex(source[i],'\t','\n',0,0)+'\n'+getIndex(source[i+1],'','\n',0,0)
    sourceText.close()
    return dicrdm,dicall

def outputFiles(filename1,dicrdm,filename2,dicall):
    """This function is written by LAPORTE Amelie.
    Args:
       filename1:The output name for the random FASTA sequence.
       dicrdm: the dictionary containing the random numbers as key.
       filename2:The output name for the FASTA sequence with the removed random sequences.
       dicall: the dictionary with all the accession numbers as key.
    Returns:
       The function return 2 dictionaries: one with the random accession number + their sequence and one for all the accession number +their sequence.
    """
    with open(filename1,'w') as output1:
        output1.writelines('{}\t{}\n'.format(k,v) for k,v in dicrdm.items())
        output1.close()
    for key in dicrdm:
        if key in dicall:
            del dicall[key]
    with open(filename2,'w') as output2:
        output2.writelines('{}\t{}\n'.format(k,v) for k,v in dicall.items())
        output2.close()

        
def main():
    # to put the FASTA file as argument on terminal
    fastafile = sys.argv[1]

    dicFasta={}
    accessionListFasta=[]
    randomAcsList=[]
    randomDict={}
    
    #Parse the FASTA file to only get the accession number
    parserFasta(fastafile, accessionListFasta,dicFasta)
    
    #Get x% of accession number and store them in a list
    randomAcsNumber(accessionListFasta,randomDict,randomAcsList,10)

    #return a dictionary for the random accession number selected + one dictionary for all the Fasta sequence
    dictionariesFasta(fastafile,randomAcsList,accessionListFasta,randomDict,dicFasta)

    #Output two text files
    outputFiles('random.fasta',randomDict,'removed_random.fasta',dicFasta)

    
if __name__ == '__main__':
    main()
