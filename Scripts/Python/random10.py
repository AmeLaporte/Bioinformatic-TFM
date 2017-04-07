from Bio import SeqIO
import sys
import random

def outputFiles(filename1,dicrdm,filename2,dicall):
    """
    Args:
       filename1:The output name for the random FASTA sequence.
       dicrdm: the dictionary containing the random numbers as key.
       filename2:The output name for the FASTA sequence with the removed random sequences.
       dicall: the dictionary with all the accession numbers as key.
    Returns:
       The function return 2 dictionaries: one with the random accession number + their sequence and one for all the accession number +their sequence.
    """
    with open(filename1,'w') as output1:
        output1.writelines('>{}\n{}\n'.format(k,v) for k,v in dicrdm.items())
        output1.close()
        
    for key in dicrdm:
        if key in dicall:
            del dicall[key]
            
    with open(filename2,'w') as output2:
        output2.writelines('>{}\n{}\n'.format(k,v) for k,v in dicall.items())
        output2.close()



def main():
    data=sys.argv[1]
    fasta_sequences = SeqIO.parse(open(data),'fasta')
    
    dict_all={}
    acs_lst=[]
    random_dct={}
    lst=[]
    
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        dict_all[name]=sequence
        acs_lst.append(name)

    perc=len(acs_lst)*10/100
    for i in range(0,perc):
        random_dct[random.choice(acs_lst)]=''

    for i in dict_all:
        for j in random_dct:
            if j == i:
                random_dct[j]=dict_all[j]

    name=sys.argv[2]
    #Output two text files
    outputFiles('random-'+name+'.fasta',random_dct,'removed_random-'+name+'.fasta',dict_all)

    
if __name__ == '__main__':
    main()
