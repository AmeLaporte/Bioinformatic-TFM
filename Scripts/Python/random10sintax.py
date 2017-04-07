import sys
import random
from Bio import SeqIO

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


def main ():
    database_sintax=sys.argv[1]
    unite_db_sintax=open(database_sintax,'r')

    database_lca=sys.argv[2]
    unite_db_lca=open(database_lca,'r')

    #get all the accession number of the CREST Unite DB
    fasta_seq_lca=SeqIO.parse(unite_db_lca,'fasta')
    lst_acs_lca=[]
    for fasta in fasta_seq_lca:
        name,sequence= fasta.id, str(fasta.seq)
        lst_acs_lca.append(name)
        
    #get all the accession number of the SINTAX Unite DB
    fasta_seq_sintax=SeqIO.parse(unite_db_sintax,'fasta')
    lst_head_sintax=[]
    lst_acs_sintax=[]
    dict_acs_taxon_sintax={}
    dict_acs_seq_sintax={}

    for fasta in fasta_seq_sintax:
    #Get all the headers in a list for futur parsing
        name, sequence= fasta.id, str(fasta.seq)
        acs_sintax=getIndex(name,'','|',0,0)
        lst_head_sintax.append(name)
        
    #Create a dictionary of all the accession numbers with their corresponding sequence
        dict_acs_seq_sintax[acs_sintax]={'name':name,'sequence':sequence}
        lst_acs_sintax.append(acs_sintax)

    dict_acs_sintax={}
    lst_short_sintax=[]

    #Create a list of the accession number of the SINTAX Unite DB that are in common with the ones in the CREST Unite DB
    for acs in lst_acs_lca:
        if acs in dict_acs_seq_sintax:
            lst_short_sintax.append(acs)

            #Create the dictionary of those sequences 
            dict_acs_sintax[acs]=dict_acs_seq_sintax[acs]

        
    unite_db_sintax.close()
    unite_db_lca.close()

    taxon_name=sys.argv[3]

    random_dct={}

    perc=len(lst_short_sintax)*10/100
    for i in range(0,perc):
        random_dct[random.choice(lst_short_sintax)]=''

    for i in random_dct:
        for j in dict_acs_sintax:
            if j == i:
                random_dct[j]=dict_acs_sintax[j]

    with open(taxon_name+'_random10.fasta','w') as output3:
        for acs in random_dct:
            print >> output3, '>'+random_dct[acs]['name'],'\n',random_dct[acs]['sequence']
    output3.close()

    for acs in random_dct:
        if acs in dict_acs_sintax:
            del dict_acs_sintax[acs]
    with open(taxon_name+'_random10_db.fasta','w') as output4:
        for acs in dict_acs_sintax:
            print >> output4, '>'+dict_acs_sintax[acs]['name'],'\n',dict_acs_sintax[acs]['sequence']
    output4.close()


if __name__ == '__main__':
    main()
