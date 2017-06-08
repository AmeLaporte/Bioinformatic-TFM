import sys
import csv

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
    sintax_file=sys.argv[1]
    sintax=open(sintax_file,'r')
    cutoff=float(sys.argv[2])

    all_path_sintax=[]
    
    for line in sintax:
        sintax_text=line.split('\t')
        sintax_exp=sintax_text[0]
        sintax_obs=sintax_text[1]

        lst_sintax_obs=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]


        #OBSERVED LIST
        try:
            domain_obs=getIndex(sintax_obs,'d:',',',2,0)
        except ValueError:
            try:
                domain_obs=getIndex(sintax_obs,'d:',';',2,0)
            except ValueError:            
                domain_obs='None'
        lst_sintax_obs[0]=domain_obs
        
        try:
            phylum_obs=getIndex(sintax_obs,'p:',',',2,0)
        except ValueError:
            try:
                phylum_obs=getIndex(sintax_obs,'p:',';',2,0)
            except ValueError:            
                phylum_obs='None'
        lst_sintax_obs[2]=phylum_obs
        
        try:
            class_obs=getIndex(sintax_obs,'c:',',',2,0)
        except ValueError:
            try:
                class_obs=getIndex(sintax_obs,'c:',';',2,0)
            except ValueError:            
                class_obs='None'
        lst_sintax_obs[4]=class_obs
       
        try:
            order_obs=getIndex(sintax_obs,'o:',',',2,0)
        except ValueError:
            try:
                order_obs=getIndex(sintax_obs,'o:',';',2,0)
            except ValueError:            
                order_obs='None'
        lst_sintax_obs[6]=order_obs

        try:
            family_obs=getIndex(sintax_obs,'f:',',',2,0)
        except ValueError:
            try:
                family_obs=getIndex(sintax_obs,'f:',';',2,0)
            except ValueError:            
                family_obs='None'
        lst_sintax_obs[8]=family_obs

        try:
            genus_obs=getIndex(sintax_obs,'g:',',',2,0)
        except ValueError:
            try:
                genus_obs=getIndex(sintax_obs,'g:',';',2,0)
            except ValueError:            
                genus_obs='None'
        lst_sintax_obs[10]=genus_obs
        
        try:
            specie_obs=getIndex(sintax_obs,'s:',',',2,0)
        except ValueError:
            try:
                specie_obs=getIndex(sintax_obs,'s:',';',2,0)
            except ValueError:            
                specie_obs='None'
        lst_sintax_obs[12]=specie_obs

        if lst_sintax_obs[0]!='None':
            lst_sintax_obs[1]=float(getIndex(lst_sintax_obs[0],'(',')',1,0))
        if lst_sintax_obs[2]!='None':
            lst_sintax_obs[3]=float(getIndex(lst_sintax_obs[2],'(',')',1,0))
        if lst_sintax_obs[4]!='None':
            lst_sintax_obs[5]=float(getIndex(lst_sintax_obs[4],'(',')',1,0))
        if lst_sintax_obs[6]!='None':
            lst_sintax_obs[7]=float(getIndex(lst_sintax_obs[6],'(',')',1,0))
        if lst_sintax_obs[8]!='None':
            lst_sintax_obs[9]=float(getIndex(lst_sintax_obs[8],'(',')',1,0))
        if lst_sintax_obs[10]!='None':
            lst_sintax_obs[11]=float(getIndex(lst_sintax_obs[10],'(',')',1,0))
        if lst_sintax_obs[12]!='None':
            lst_sintax_obs[13]=float(getIndex(lst_sintax_obs[12],'(',')',1,0))

        if lst_sintax_obs[0]!='None':
            lst_sintax_obs[0]=getIndex(lst_sintax_obs[0],'','(',0,0)
        if lst_sintax_obs[2]!='None':
            lst_sintax_obs[2]=getIndex(lst_sintax_obs[2],'','(',0,0)
        if lst_sintax_obs[4]!='None':
            lst_sintax_obs[4]=getIndex(lst_sintax_obs[4],'','(',0,0)
        if lst_sintax_obs[6]!='None':
            lst_sintax_obs[6]=getIndex(lst_sintax_obs[6],'','(',0,0)
        if lst_sintax_obs[8]!='None':
            lst_sintax_obs[8]=getIndex(lst_sintax_obs[8],'','(',0,0)
        if lst_sintax_obs[10]!='None':
            lst_sintax_obs[10]=getIndex(lst_sintax_obs[10],'','(',0,0)
        if lst_sintax_obs[12]!='None':
            lst_sintax_obs[12]=getIndex(lst_sintax_obs[12],'','(',0,0)
        
        all_path_sintax.append(lst_sintax_obs)
    for i in range(0,len(all_path_sintax)):
        for j in range(0,len(all_path_sintax[i])):
            if all_path_sintax[i][1]<cutoff:
                all_path_sintax[i][1]='None'
                all_path_sintax[i][0]='None'

            if all_path_sintax[i][3]<cutoff:
                all_path_sintax[i][3]='None'
                all_path_sintax[i][2]='None'
            if all_path_sintax[i][5]<cutoff:
                all_path_sintax[i][5]='None'
                all_path_sintax[i][4]='None'

            if all_path_sintax[i][7]<cutoff:
                all_path_sintax[i][7]='None'
                all_path_sintax[i][6]='None'

            if all_path_sintax[i][9]<cutoff:
                all_path_sintax[i][9]='None'
                all_path_sintax[i][8]='None'

            if all_path_sintax[i][11]<cutoff:
                all_path_sintax[i][11]='None'
                all_path_sintax[i][10]='None'

            if all_path_sintax[i][13]<cutoff:
                all_path_sintax[i][13]='None'
                all_path_sintax[i][12]='None'

        print all_path_sintax[i]

    with open('first_csv.csv','w') as output:
        for i in range(0,len(all_path_sintax)):
            print >> output, all_path_sintax[i][0],'\t',all_path_sintax[i][2],'\t',all_path_sintax[i][4],'\t',all_path_sintax[i][6],'\t',all_path_sintax[i][8],'\t',all_path_sintax[i][10],'\t',all_path_sintax[i][12]


if __name__ == '__main__':
    main()


