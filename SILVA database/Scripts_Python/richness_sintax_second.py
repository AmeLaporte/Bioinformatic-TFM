import sys
import csv

csv_file=open(sys.argv[1],'rb')
csv_data=csv.reader(csv_file,delimiter='\t')

domain_count=0
domains=[]
phylum_count=0
phyla=[]
class_count=0
classes=[]
order_count=0
orders=[]
family_count=0
families=[]
genus_count=0
genera=[]
specie_count=0
species=[]

lines=[]
for line in csv_data:
    print line
    lines.append(line)
    if line[0] not in domains and line[0]!='None ' and line[0]!='unidentified ' and line[0]!='None':
        domains.append(line[0])
    if line[0]!='None ' and line[0]!='unidentified ' and line[0]!='None':
        domain_count+=1
    
    if line[1] not in phyla and line[1]!='None ' and line[1]!='unidentified ' and line[1]!='None':
        phyla.append(line[1])
    if line[1]!='None ' and line[1]!='unidentified ' and line[1]!='None':
        phylum_count+=1

    if line[2] not in classes and line[2]!='None ' and line[2]!='unidentified ' and line[2]!='None':
        classes.append(line[2])
    if line[2]!='None ' and line[2]!='unidentified ' and line[2]!='None':
        class_count+=1

    if line[3] not in orders and line[3]!='None ' and line[3]!='unidentified ' and line[3]!='None':
        orders.append(line[3])
    if line[3]!='None ' and line[3]!='unidentified ' and line[3]!='None':
        order_count+=1

    if line[4] not in families and line[4]!='None ' and line[4]!='unidentified ' and line[4]!='None':
        families.append(line[4])
    if line[4]!='None ' and line[4]!='unidentified ' and line[4]!='None':
        family_count+=1

    if line[5] not in genera and line[5]!='None ' and line[5]!='unidentified ' and line[5]!='None':
        genera.append(line[5])
    if line[5]!='None ' and line[5]!='unidentified ' and line[5]!='None':
        genus_count+=1

    if line[6] not in species and line[6]!='None ' and line[6]!='unidentified ' and line[6]!='None':
        species.append(line[6])
    if line[6]!='None ' and line[6]!='unidentified ' and line[6]!='None':
        specie_count+=1

print len(lines)
print domain_count, phylum_count, class_count, order_count, family_count, genus_count, specie_count
print len(domains),len(phyla),len(classes),len(orders),len(families),len(genera),len(species)

with open('Richness_sintax.csv','w') as output:
    print >> output, 'Rank','\t','Occurrence','\t','OTUs'
    print >> output, 'domain','\t',len(domains),'\t',domain_count
    print >> output, 'phylum','\t',len(phyla),'\t',phylum_count
    print >> output, 'class','\t',len(classes),'\t',class_count
    print >> output, 'order','\t',len(orders),'\t',order_count
    print >> output, 'family','\t',len(families),'\t',family_count
    print >> output, 'genus','\t',len(genera),'\t',genus_count
    print >> output, 'specie','\t',len(species),'\t',specie_count
output.close()
