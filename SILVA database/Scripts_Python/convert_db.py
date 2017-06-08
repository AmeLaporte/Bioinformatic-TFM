import sys
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

def main():

#Open the Sintax database of your choice
    database_sintax=sys.argv[1]
    unite_db_sintax=open(database_sintax,'r')

    #Open the CREST database you want to compare with
    database_lca=sys.argv[2]
    unite_db_lca=open(database_lca,'r')

    #get all the accession number of the CREST Unite DB
    fasta_seq_lca=SeqIO.parse(unite_db_lca,'fasta')
    lst_acs_lca=[]
    for fasta in fasta_seq_lca:
        name,sequence= fasta.id, str(fasta.seq)
        lst_acs_lca.append(name)
    print len(lst_acs_lca)
        
    #get all the accession number of the SINTAX Unite DB
    fasta_seq_sintax=SeqIO.parse(unite_db_sintax,'fasta')
    lst_head_sintax=[]
    lst_acs_sintax=[]
    dict_acs_taxon_sintax={}
    dict_acs_seq_sintax={}

    for fasta in fasta_seq_sintax:
    #Get all the headers in a list for futur parsing
        name, sequence= fasta.id, str(fasta.seq)
        #print name
        try:
            acs_sintax=getIndex(name,'','|',0,0)
        except ValueError:
           acs_sintax=getIndex(name,'','.',0,0)
        lst_head_sintax.append(name)
        
    #Create a dictionary of all the accession numbers with their corresponding sequence
        dict_acs_seq_sintax[acs_sintax]={'name':name,'sequence':sequence}
        lst_acs_sintax.append(acs_sintax)
    print len(lst_acs_sintax) 
    dict_acs_sintax={}
    lst_short_sintax=[]

    #Create a list of the accession number of the SINTAX Unite DB that are in common with the ones in the CREST Unite DB
    for acs in lst_acs_lca:
        if acs in dict_acs_seq_sintax:
            lst_short_sintax.append(acs)
            #Create the dictionary of those sequences 
            dict_acs_sintax[acs]=dict_acs_seq_sintax[acs]
    print len(lst_short_sintax)

    unite_db_sintax.close()
    unite_db_lca.close()

    print len(dict_acs_sintax)
    print len(dict_acs_seq_sintax)
    with open('new_db.fasta','w') as output4:
        for acs in dict_acs_sintax:
            print >> output4, '>'+dict_acs_sintax[acs]['name'],'\n',dict_acs_sintax[acs]['sequence']
    output4.close()

if __name__ == '__main__':
    main()
