'''
@author: AmeLaporte
'''


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
	#Output the random FASTA sequences.
    with open(filename1,'w') as output1:
        output1.writelines('>{}\n{}\n'.format(k,v) for k,v in dicrdm.items())
        output1.close()
        
    #Output the troncated database.
    for key in dicrdm:
        if key in dicall:
            del dicall[key]
            
    with open(filename2,'w') as output2:
        output2.writelines('>{}\n{}\n'.format(k,v) for k,v in dicall.items())
        output2.close()



def main():
    #Open the database of your choice
    data=sys.argv[1]
    fasta_sequences = SeqIO.parse(open(data),'fasta')
    
    #Set all the variables
    dict_all={}
    acs_lst=[]
    random_dct={}
    lst=[]
    
    # Create a dictionary containing the accession number as key and the corresponding sequence as value.
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        dict_all[name]=sequence
        acs_lst.append(name)

    #Select randomly 10% of accession numbers.
    perc=len(acs_lst)*10/100
    for i in range(0,perc):
        random_dct[random.choice(acs_lst)]=''

	#Create a dictionary of the random accession number with their sequence as value.
    for i in dict_all:
        for j in random_dct:
            if j == i:
                random_dct[j]=dict_all[j]

    #To change the name automatically in the bash script.
    name=sys.argv[2]
    #Output two text files.
    outputFiles('random-'+name+'.fasta',random_dct,'removed_random-'+name+'.fasta',dict_all)

    
if __name__ == '__main__':
    main()
