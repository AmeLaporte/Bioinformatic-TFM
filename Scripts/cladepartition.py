from LCAClassifier.taxa import CRESTree
from LCAClassifier.classify import ClassificationTree
from LCAClassifier.config import config
import sys
from Bio import Phylo
import random




def main():
    
    #Creation of the phylogenetic tree from the database
    database="silvamod"
    mapFile = ("%s/%s.map" %
               (config.DATABASES[database], database))
    treFile = ("%s/%s.tre" %
               (config.DATABASES[database], database))
    
    
    reftree = ClassificationTree(treFile, mapFile)

    fungi_uniq = sys.argv[1]

    silvafamily=[]

    silva_lst=[]
    
    fungi_txt=open(fungi_uniq,'r')
    fungi=fungi_txt.read().splitlines(0)
    for i in range(0,len(fungi)):
        silvafamily.append(reftree.getNode(fungi[i]))
    for i in range(0,len(silvafamily)):
        if silvafamily[i]!=None:
            silva_lst.append(silvafamily[i])
    
    silva_fam=[taxa.name for taxa in silva_lst]
  
    for i in range(0,len(silva_fam)):
        randomTaxa=random.choice(silva_fam)

    genera=reftree.getImmediateChildren(randomTaxa)
    
    lstGenera=[taxa.name for taxa in genera]
    

    while len(lstGenera)%2!=0:
        for i in range(0,len(silva_fam)):
            randomTaxa=random.choice(silva_fam)    
        genera=reftree.getImmediateChildren(randomTaxa)
        lstGenera=[taxa.name for taxa in genera]
        
    print randomTaxa, '\n', lstGenera, '\n'
 
    

if __name__ == '__main__':
    main()
