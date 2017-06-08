import sys
import csv

richness_file=sys.argv[1]
richness_table_file=open(richness_file,'rb')
richness_table=csv.reader(richness_table_file,delimiter='\t')

rank=[]
otu=[]

for line in richness_table:
    rank.append(line[0])
    otu.append(line[3])
del rank[0],otu[0]

ranks={}
for level in rank:
    ranks[level]={'occurrence':0 , 'otu':0}

for i in range(0,len(rank)):
    level=rank[i]
    if level==rank[i]:
        ranks[level]['occurrence']+=1
        ranks[level]['otu']+=int(otu[i])

outName=sys.argv[2]
with open(outName,"w") as output:
    print>> output, 'Ranks','\t','Occurrence','\t','OTUs'
    for i in ranks:
        print>> output, i,'\t', ranks[i]['occurrence'],'\t', ranks[i]['otu']
