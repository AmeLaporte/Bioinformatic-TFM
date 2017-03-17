
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

    fungi_genera_file=sys.argv[1]

    silva_genera=[]

    silva_lst=[]
    
    fungi_txt=open(fungi_genera_file,'r')
    fungi=fungi_txt.read().splitlines(0)
    for i in range(0,len(fungi)):
        silva_genera.append(reftree.getNode(fungi[i]))
    for i in range(0,len(silva_genera)):
        if silva_genera[i]!=None:
            silva_lst.append(silva_genera[i])
    
    silva_gen=[taxa.name for taxa in silva_lst]
    

    randomTaxa=random.choice(silva_gen)

    species=reftree.getImmediateChildren(randomTaxa)
    
    lstSpecies=[taxa.name for taxa in species]
    

    while len(lstSpecies)%2!=0:
        randomTaxa=random.choice(silva_gen)    
        species=reftree.getImmediateChildren(randomTaxa)
        lstSpecies=[taxa.name for taxa in species]
        
    print randomTaxa, '\n', lstSpecies, '\n'
    
    randomChildren=[]
    
    nb=len(lstSpecies)/2
    for i in range(0,nb):
        randomChildren.append(random.choice(lstSpecies))

    print randomChildren

    
    

if __name__ == '__main__':
    main()
