'''
Created on Mar 7, 2017

@author: andersl, ameliel
'''
from LCAClassifier.classify import ClassificationTree
from LCAClassifier.config import config

import sys


def getIndex(txt,mot1,mot2,int1,int2):
    """
    Args:
       txt:correspond to the genbank entry stored in memory with the readFlatFile function.
       mot1, mot2: the words used as index to separate the information.
       int1,int2: the number of characters to delete in the separated information. 
        
    Returns:
       The function return the same thing than if we've had used the index method but simplified to have a clearer code.
  
    """
    txt=txt[txt.index(mot1)+int1:txt.index(mot2,txt.index(mot1))+int2]
    return txt

def parserFasta(filename,acs,pth):
    """
    Args:
       filename:The FASTA file of the population you want to compare to the reference.
       acs:The list containing the accession numbers. 
       pth:The list containing the taxonomic pathways.
        
    Returns:
       The function appends to a list for the accession numbers and one for the pathways.
    """
    #open the FASTA file
    far = open(filename,"r")
    for line in far:
        if line[0]==">":
            if ":" in line:
                ac = line[line.find(":")+1:line.find(" ")]
            else:
                ac = line[1:line.find(" ")]
            pt = line[line.find(" ")+1:-1]
            acs.append(ac)
            pth.append(pt.split(";"))
    far.close()

def counter(sftLst,refLst,errLst):
    """
    Args:
       sftLst:correspond to the taxonomic pathway list of the Reference tree.
       refLst:correspond to the taxonomic pathway list of the FASTA file.
       errLst: correspond to the list where the result are displayed for each accession number. 
        
    Returns:
       The function a list with scores for each taxonomic level studied.
    """
    for i in range (0, 9):
        if sftLst[i]==refLst[i] and sftLst[i]!="None" and refLst!="None":
            errLst.append("TP")
        
        elif sftLst[i]!=refLst[i] and sftLst[i]!="None" and refLst[i]!="None":
            errLst.append("FP")
            
        elif sftLst[i]!=refLst[i] and refLst[i]=="None":
            errLst.append("FP")
            
        elif sftLst[i]=="None" and refLst[i]=="None":
            errLst.append("TN")
            
        elif sftLst[i]!=refLst[i] and sftLst[i]=="None":
            errLst.append("FN")
        
    return errLst

def correctLength(lst):
    """
    Args:
       lst: correspond to the list we want to correct the length in order to compare it in the counter function.
        
    Returns:
       A list of length=9.
    """
    while len(lst)<9:
        lst.append("None")
    for i in range(0,len(lst)):
        if lst[i]=="No hits":
            lst[i]="None"
    return lst

def scorePerLevel(lst,dct):
    """
    Args:
        lst: correspond to the list of score in each taxonomic level of each accession number.
        dct: Is a list of 9 dictionaries (for each level) containing the 4 score possible
    Returns:
       returns the list of dictionaries containing the scores at each taxonomic level
  
    """
    for i in range(0,len(lst)):
            if lst[i]=='TP':
                dct[i]['True Positive']+=1
            if lst[i]=='FP':
                dct[i]['False Positive']+=1
            if lst[i]=='TN':
                dct[i]['True Negative']+=1
            if lst[i]=='FN':
                dct[i]['False Negative']+=1      
    return dct
        
def main():
    
    #Creation of the phylogenetic tree from the database
    database="silvamod128"
    mapFile = ("%s/%s.map" %
               (config.DATABASES[database], database))
    treFile = ("%s/%s.tre" %
               (config.DATABASES[database], database))
    
    
    reftree = ClassificationTree(treFile, mapFile)
    
    # to put the FASTA file as argument on terminal
    fastafile = sys.argv[1]

    #create the accession number and taxonomic pathways lists of the FASTA file
    accessionListFasta=[]
    seqPath=[]
    
    #Parse the FASTA file
    parserFasta(fastafile, accessionListFasta, seqPath)
    
    #Set the result lists
    errorList=[]
    matrix=[]
    taxaName=["Meta","Domain","Superkingdom","Kingdom","Phylum","Class","Order","Family","Genus"]
    #set total
    score_total= []
    for depth in taxaName:
        score_total.append({'True Positive':0,'True Negative':0,'False Positive':0,'False Negative':0})

    for i in range(0,len(accessionListFasta)):
        if reftree.getNode(accessionListFasta[i]):
            dbPath=reftree.getPath(reftree.getNode(accessionListFasta[i]))
            refPath=[taxa.name for taxa in dbPath]
        
    
        #Count the TP,FP,TN,FN in the result
            counter(correctLength(seqPath[i]),correctLength(refPath),errorList)
            matrix.append(errorList)

        #Calcule the amount of each score in each taxonomic level
            scorePerLevel(errorList, score_total)

        #Reinitialize the list
            errorList=[]
        
        else:
            pass
        
        #Remove the hash to verify the score for each domain of each accession number
        resultList=zip(taxaName,matrix[i])
        print accessionListFasta[i], '\t', resultList
        print seqPath[i],'\n', refPath,'\n\n'
        
        
        
    #total score output
    for i in range(0,len(score_total)):
        print taxaName[i],'\n\t','%s' % (score_total[i])
    
    outName=sys.argv[2]

    with open(outName,"w") as output:
        for i in range(0,len(score_total)):
            print >> output, taxaName[i]
            output.writelines('{}\t{}\n'.format(k,v) for k,v in score_total[i].items())
            print >>output, '\n'
    output.close()
    

if __name__ == '__main__':
    main()
