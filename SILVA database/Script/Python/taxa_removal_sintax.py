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


def main ():
    #Open the Sintax database of your choice
    database_sintax=sys.argv[1]
    unite_db_sintax=open(database_sintax,'r')

        
    #get all the accession number of the SINTAX Unite DB
    fasta_seq_sintax=SeqIO.parse(unite_db_sintax,'fasta')
    lst_head_sintax=[]
    lst_acs_sintax=[]
    dict_acs_taxon_sintax={}
    dict_acs_seq_sintax={}

    for fasta in fasta_seq_sintax:
    #Get all the headers in a list for futur parsing
        name, sequence= fasta.id, str(fasta.seq)
        try:
            acs_sintax=getIndex(name,'','|',0,0)
        except ValueError:
            acs_sintax=getIndex(name,'',';',0,0)
        lst_head_sintax.append(name)
        
    #Create a dictionary of all the accession numbers with their corresponding sequence
        dict_acs_seq_sintax[acs_sintax]={'name':name,'sequence':sequence}
        lst_acs_sintax.append(acs_sintax)
        


    

    #Create a dictionary of the accession as key and the taxonomic path as value
    for acs in lst_head_sintax:
        try:
            number=getIndex(acs,'','|',0,0)
        except ValueError:
            number=getIndex(acs,'',';',0,0)
        try:
            domain=getIndex(acs,'d:',",",2,0)
        except ValueError:
            try:
                if getIndex(acs,'d:','',2,0):
                    domain=getIndex(acs,'d:','',2,0)
            except ValueError:
                domain='None' 
        try:
            kingdom=getIndex(acs,'k:',",",2,0)
        except ValueError:
            try:
                if getIndex(acs,'k:','',2,0):
                    kingdom=getIndex(acs,'k:','',2,0)
            except ValueError:
                kingdom='None'            
        try:
            phylum=getIndex(acs,'p:',',',2,0)
        except ValueError:
            try:
                if getIndex(acs,'p:',';',2,0):
                    phylum=getIndex(acs,'p:',';',2,0)
            except ValueError:
                phylum='None'
            
        try:
            classe=getIndex(acs,'c:',',',2,0)
        except ValueError:
            try:
                if getIndex(acs,'c:',';',2,0):
                    classe=getIndex(acs,'c:',';',2,0)
            except ValueError:
                classe='None'
            
        try:
            order=getIndex(acs,'o:',',',2,0)
        except ValueError:
            try:
                if getIndex(acs,'o:',';',2,0):
                    order=getIndex(acs,'o:',';',2,0)
            except ValueError:
                order='None'

        try:
            family=getIndex(acs,'f:',',',2,0)
        except ValueError:
            try:
                if getIndex(acs,'f:',';',2,0):
                    family=getIndex(acs,'f:',';',2,0)
            except ValueError:
                family='None'

        try:
            genus=getIndex(acs,'g:',',',2,0)
        except ValueError:
            try:
                if getIndex(acs,'g:',';',2,0):
                    genus=getIndex(acs,'g:',';',2,0)
            except ValueError:
                genus='None'

        try:
            specie=getIndex(acs,'s:',';',2,0)
        except ValueError:
            specie='None'


        dict_acs_taxon_sintax[number]={'kingdom':kingdom,'domain':domain,'phylum':phylum,'class':classe,'order':order,'family':family,'genus':genus,'specie':specie}

    #To select a taxon to delete from the database.
    taxon_file=sys.argv[2]

    taxon_name=open(taxon_file,'r')

    taxon_list=[]
    for line in taxon_name:
        taxon_list.append(line.replace('\n',''))
    
    level=str(sys.argv[3])
	#Outputs: 1) the taxonomic level sequences selected, 2) the troncated database without the taxonomic level selected.
    for taxon in taxon_list:
        with open(taxon.replace(' ','_')+'.fasta','w') as output1:
            for acs in lst_acs_sintax:
                if taxon in dict_acs_taxon_sintax[acs][level]:
                    print >> output1, '>'+dict_acs_seq_sintax[acs]['name'],'\n',dict_acs_seq_sintax[acs]['sequence']

            
            
        output1.close()
    unite_db_sintax.close()

    
if __name__ == '__main__':
    main()
