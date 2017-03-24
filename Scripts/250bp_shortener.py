'''
@author: Amelie Laporte

Created date: 03-23-2017
Modified date: 03-23-2017 

Description: 
Cut randomly the sequences > 250bp of a Fasta file and output a fasta file with sequences of 250bp max.
'''

import sys
import random

def getIndex(txt,mot1,mot2,int1,int2):
    """Args:
        txt:correspond to the genbank entry stored in memory with the readFlatFile function.
        mot1, mot2: the words used as index to separate the information.
        int1,int2: the number of characters to delete in the separated information. 
        
       Returns:
        The function return the same thing than if we've had used the index method but simplified to have a clearer code.
  
    """
    txt=txt[txt.index(mot1)+int1:txt.index(mot2,txt.index(mot1))+int2]
    return txt

def main():
    fasta_input=sys.argv[1]
    
    fasta_to_truncate=open(fasta_input,'r')
    read_fasta=fasta_to_truncate.read().splitlines(1)

    accession_nb=[]
    
    for i in range(0,len(read_fasta),2):
        if '>' in read_fasta[i]:
            accession_nb.append(getIndex(read_fasta[i],">","\n",0,0))

    fasta_dict={}
    for i in accession_nb:
        fasta_dict[i]=''

    for i in range(0,len(read_fasta),2):
        for j in range(0,len(accession_nb)):
            if accession_nb[j] in read_fasta[i]:
                fasta_dict[accession_nb[j]]=getIndex(read_fasta[i+1],'','\n',0,0)
    for i in accession_nb:
        seq_length=len(fasta_dict[i])
        if seq_length >250:
            random_start=random.randint(0,(seq_length)-250)
            sequence=fasta_dict[i]
            sequence_cut=sequence[random_start:random_start+250]
            fasta_dict[i]=sequence_cut
        else:
            del fasta_dict[i]

    output_filename=sys.argv[2]

    with open(output_filename,"w") as output:
            output.writelines('{}\n{}\n'.format(k,v) for k,v in fasta_dict.items())
    output.close()


if __name__ == '__main__':
    main()
