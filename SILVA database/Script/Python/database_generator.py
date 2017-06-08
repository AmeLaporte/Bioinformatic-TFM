import sys
from Bio import SeqIO

""" 
This script takes the whole database as first argument, the extracted sequences from the removal_of_taxa script as second argument, the name of the taxon removed as third argument and returns a truncated database (the extracted sequences are deleted).
"""

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
    #Open the Silva database formatted for SINTAX.
    database_sintax=sys.argv[1]
    unite_db_sintax=open(database_sintax,'r')

    #Open the extracted sequences to delete.
    sequences_file=sys.argv[2]
    sequence_todel=open(sequences_file,'r')

    fasta_seq_sintax=SeqIO.parse(unite_db_sintax,'fasta')
    lst_head_sintax=[]
    lst_acs_sintax=[]
    dict_acs_taxon_sintax={}
    dict_acs_seq_sintax={}
    lst_seq=[]

    for fasta in fasta_seq_sintax:
    #Get all the accession numbers of the database in a list.
        name, sequence= fasta.id, str(fasta.seq)
        try:
            acs_sintax=getIndex(name,'','|',0,0)
        except ValueError:
            acs_sintax=getIndex(name,'',';',0,0)
        lst_head_sintax.append(name)
        
    #Create a dictionary of all the accession numbers with their corresponding sequence.
        dict_acs_seq_sintax[acs_sintax]={'name':name,'sequence':sequence}
        lst_acs_sintax.append(acs_sintax)
        

    sequences=SeqIO.parse(sequence_todel,'fasta')
    
    #Get the accession numbers from the extracted sequences.
    for seq in sequences:
        nom=seq.id
        try:
            noms=getIndex(nom,'','|',0,0)
        except ValueError:
            noms=getIndex(nom,'',';',0,0)
        lst_seq.append(noms)

    #Delete the sequences from the database.
    for acs in lst_seq:
        if acs in dict_acs_seq_sintax:
            del dict_acs_seq_sintax[acs]

    #Output the new database.
    filename=sys.argv[3]
    with open(filename+'_db.fasta','w') as output:
        for key in dict_acs_seq_sintax:
            print >> output, '>'+dict_acs_seq_sintax[key]['name'],'\n',dict_acs_seq_sintax[key]['sequence']

    output.close()

if __name__ == '__main__':
    main()
        
