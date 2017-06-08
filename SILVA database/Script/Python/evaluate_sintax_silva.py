'''
Created on Apr 10, 2017

@author: AmeLaporte
'''

import sys

def Counter(lst_sintax_exp,lst_sintax_obs,error_lst,cutoff):
    """
    Args:
     lst_sintax_exp: the expected path from the database
     lst_sintax_obs: the result of sintax to be compared
     error_lst: the empty list where the score will be added
     cutoff: if the sintax score is under the cutoff, then the classification is counted as a False negative

    Returns: a list of score, one index correspond to one taxonomic level

    """
    for i in range(0,len(lst_sintax_obs),2):
        if lst_sintax_obs[i]==lst_sintax_exp[i] and lst_sintax_obs[i]!="None" and lst_sintax_exp!="None" and lst_sintax_obs[i+1]>=cutoff:
            error_lst.append("TP")
        
        elif lst_sintax_obs[i]!=lst_sintax_exp[i] and lst_sintax_obs[i]!="None" and lst_sintax_exp[i]!="None" and lst_sintax_obs[i+1]>=cutoff:
            error_lst.append("FP")
            
        elif lst_sintax_obs[i]!=lst_sintax_exp[i] and lst_sintax_exp[i]=="None" and lst_sintax_obs[i+1]>=cutoff:
            error_lst.append("FP")
            
        elif lst_sintax_obs[i]=="None" and lst_sintax_exp[i]=="None":
            error_lst.append("TN")
            
        elif lst_sintax_obs[i]!=lst_sintax_exp[i] and lst_sintax_obs[i]=="None" and lst_sintax_obs[i+1]>=cutoff:
            error_lst.append("FN ")

        elif lst_sintax_obs[i+1]<cutoff:
            error_lst.append("FN")
    print error_lst
    return error_lst


def scorePerLevel(error_lst,score_total):
    """This function is written by LAPORTE Amelie.

    Args:
        error_lst: correspond to the list of score in each taxonomic level of each accession number.
        score_total: Is a list of 8 dictionaries (for each level) containing the 4 score possible
    Returns:
       returns the list of dictionaries containing the scores at each taxonomic level
  
    """
    for i in range(0,len(error_lst)):
            if error_lst[i]=='TP':
                score_total[i]['True Positive']+=1
            if error_lst[i]=='FP':
                score_total[i]['False Positive']+=1
            if error_lst[i]=='TN':
                score_total[i]['True Negative']+=1
            if error_lst[i]=='FN':
                score_total[i]['False Negative']+=1      
    return score_total

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

#Input Sintax file
    x=0
    cutoff=float(sys.argv[2])

    
    Sintax_file=sys.argv[1]

    sintax=open(Sintax_file,'r')

    error_lst=[]
    matrix=[]
    taxaName=['Kingdom','Phylum','Class','Order','Family','Genus','Specie']
    #set total
    score_total=[{'True Positive':0,'True Negative':0,'False Positive':0,'False Negative':0},
                {'True Positive':0,'True Negative':0,'False Positive':0,'False Negative':0},
                {'True Positive':0,'True Negative':0,'False Positive':0,'False Negative':0},
                {'True Positive':0,'True Negative':0,'False Positive':0,'False Negative':0},
                {'True Positive':0,'True Negative':0,'False Positive':0,'False Negative':0},
                {'True Positive':0,'True Negative':0,'False Positive':0,'False Negative':0},
                {'True Positive':0,'True Negative':0,'False Positive':0,'False Negative':0}]


    for line in sintax:
        sintax_text=line.split('\t')
        sintax_exp=sintax_text[0]
        sintax_obs=sintax_text[1]
        try:
            number=getIndex(sintax_exp,'','|',0,0)
        except ValueError:
            number=getIndex(sintax_exp,'','.',0,0)

        print number,'\n',sintax_exp, '\n \n', sintax_obs, '\n\n'
        
        lst_sintax_exp=[0,1,0,1,0,1,0,1,0,1,0,1,0,1] #the cutoff for the reference pathway is set to 1.
        lst_sintax_obs=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        #EXPECTED LIST
        try:
            domain_exp=getIndex(sintax_exp,'k:',',',2,0)
        except ValueError:
            try:
                domain_exp=getIndex(sintax_exp,'k:',';',2,0)
            except ValueError:            
                domain_exp='None'
        lst_sintax_exp[0]=domain_exp
        
        try:
            phylum_exp=getIndex(sintax_exp,'p:',',',2,0)
        except ValueError:
            try:
                phylum_exp=getIndex(sintax_exp,'p:',';',2,0)
            except ValueError:            
                phylum_exp='None'
        lst_sintax_exp[2]=phylum_exp
        
        try:
            class_exp=getIndex(sintax_exp,'c:',',',2,0)
        except ValueError:
            try:
                class_exp=getIndex(sintax_exp,'c:',';',2,0)
            except ValueError:            
                class_exp='None'
        lst_sintax_exp[4]=class_exp
       
        try:
            order_exp=getIndex(sintax_exp,'o:',',',2,0)
        except ValueError:
            try:
                order_exp=getIndex(sintax_exp,'o:',';',2,0)
            except ValueError:            
                order_exp='None'
        lst_sintax_exp[6]=order_exp

        try:
            family_exp=getIndex(sintax_exp,'f:',',',2,0)
            
        except ValueError:
            try:
                family_exp=getIndex(sintax_exp,'f:',';',2,0)
            except ValueError:            
                family_exp='None'
        lst_sintax_exp[8]=family_exp

        try:
            genus_exp=getIndex(sintax_exp,'g:',',',2,0)
        except ValueError:
            try:
                genus_exp=getIndex(sintax_exp,'g:',';',2,0)
            except ValueError:            
                genus_exp='None'
        lst_sintax_exp[10]=genus_exp
        
        try:
            specie_exp=getIndex(sintax_exp,'s:',',',2,0)
        except ValueError:
            try:
                specie_exp=getIndex(sintax_exp,'s:',';',2,0)
            except ValueError:            
                specie_exp='None'
        lst_sintax_exp[12]=specie_exp


        #OBSERVED LIST
        try:
            domain_obs=getIndex(sintax_obs,'k:',',',2,0)
        except ValueError:
            try:
                domain_obs=getIndex(sintax_obs,'k:',';',2,0)
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


    
        print 'expected','\t',domain_exp,phylum_exp,class_exp,order_exp,family_exp,genus_exp,specie_exp,'\n\n'
        print 'Observed','\t',domain_obs,phylum_obs,class_obs,order_obs,family_obs,genus_obs,specie_obs,'\n\n'

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
        
        print lst_sintax_exp,'\n',lst_sintax_obs
        
        Counter(lst_sintax_exp,lst_sintax_obs,error_lst,cutoff)
        matrix.append(error_lst)

        scorePerLevel(error_lst, score_total)
        error_lst=[]
    sintax.close()


    #total score output
    for i in range(0,len(score_total)):
        print taxaName[i],'\n\t','%s' % (score_total[i])
    
    outName=sys.argv[3]

    with open(outName,"w") as output:
        for i in range(0,len(score_total)):
            print >> output, taxaName[i]
            output.writelines('{}\t{}\n'.format(k,v) for k,v in score_total[i].items())
            print >>output, '\n'
    output.close()



    
        
if __name__ == '__main__':
    main()
