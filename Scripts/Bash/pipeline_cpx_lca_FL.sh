#!/bin/bash

cd /home/amelie/Téléchargements/RESULTS_TESTS

mkdir Evaluate

for file in sequence_deleted_*; do
    taxa=${file//sequence_deleted_}

    QUERY=/home/amelie/Téléchargements/RESULTS_TESTS/sequence_deleted_${taxa}
    NEWDB=/home/amelie/Téléchargements/RESULTS_TESTS/troncated_database_${taxa}

    makeblastdb -in ${NEWDB} -dbtype nucl

    blastn -task megablast -query  ${QUERY} -db ${NEWDB} -num_alignments 100 -outfmt 5 -out ${QUERY//.fa*}_Unite.xml -num_threads 4

    gzip ${QUERY//.fa*}_Unite.xml

    
    XML=/home/amelie/Téléchargements/RESULTS_TESTS/sequence_deleted_${taxa//.fasta}_Unite.xml.gz

    classify -i  ${QUERY} -d unite -o CREST_RESULTS/CREST_${taxa//.fasta} -f ${XML}


    py-crest /home/amelie/Téléchargements/CREST-master/LCAClassifier/src/LCAClassifier/evaluate.py /home/amelie/Téléchargements/RESULTS_TESTS/CREST_RESULTS/CREST_${taxa//.fasta}/sequence_deleted_${taxa//.fasta}_Assigned.fasta /home/amelie/Téléchargements/RESULTS_TESTS/Evaluate/${taxa//.fasta}.txt

done

mkdir blast_db
mv *.fasta.n* /home/amelie/Téléchargements/RESULTS_TESTS/blast_db

mkdir Blastn
mv *.gz /home/amelie/Téléchargements/RESULTS_TESTS/Blastn
