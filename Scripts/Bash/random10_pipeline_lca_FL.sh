#!/bin/bash

cd /home/amelie/Téléchargements/RESULTS_TESTS


while [ `ls | wc -l` -lt 200 ];
do
    py-crest /home/amelie/Téléchargements/TFM_Anders/Script/Python/random10.py /home/amelie/Téléchargements/TFM_Anders/LCA\ DB/unite.fasta `ls | wc -l`
 echo `ls | wc -l`
done


mkdir Evaluate
mkdir CREST_RESULTS
mkdir ART

for file in random-*; do

    NB=${file//random-}
    QUERY=/home/amelie/Téléchargements/RESULTS_TESTS/random-${NB}
    NEWDB=/home/amelie/Téléchargements/RESULTS_TESTS/removed_random-${NB}

    
    makeblastdb -in ${NEWDB} -dbtype nucl


    blastn -task megablast -query  ${QUERY} -db ${NEWDB} -num_alignments 100 -outfmt 5 -out ${QUERY//.fa*}_Unite.xml -num_threads 4


    gzip ${QUERY//.fa*}_Unite.xml

    
    XML=${QUERY//.fasta}_Unite.xml.gz

    classify -i  ${QUERY} -d unite -o CREST_RESULTS/CREST_${NB//.fasta} -f ${XML}


    py-crest /home/amelie/Téléchargements/CREST-master/LCAClassifier/src/LCAClassifier/evaluate.py /home/amelie/Téléchargements/RESULTS_TESTS/CREST_RESULTS/CREST_${NB//.fasta}/random-${NB//.fasta}_Assigned.fasta /home/amelie/Téléchargements/RESULTS_TESTS/Evaluate/${NB//.fasta}.txt

done

mkdir blast_db
mv *.fasta.n* /home/amelie/Téléchargements/RESULTS_TESTS/blast_db

mkdir Blastn
mv *.gz /home/amelie/Téléchargements/RESULTS_TESTS/Blastn
