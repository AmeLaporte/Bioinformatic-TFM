#!/bin/bash

for i in `seq 1 100`;
do
    python /media/amelie/DATA/Anders_TFM/Script/Python/random10sintax.py /media/amelie/DATA/Anders_TFM/Sintax\ DB/unite.fasta /media/amelie/DATA/Anders_TFM/LCA\ DB/unite.fasta ${i}
  echo ${i}
done

mkdir ART

for file in *_db.fasta; do
    taxon=${file//_db.fasta}

    art_illumina -ss MSv3 -amp -na -i ${taxon}.fasta -l 250 -f 1 -o ART/${taxon}_SE_FQ

    usearch --fastq_filter ART/${taxon}_SE_FQ.fq --fastaout ${taxon}_SE.fasta
    
    usearch -makeudb_sintax ${file} -output ${file//.fasta}.udb

done

mkdir UDB
mv *.udb UDB/

for file in *_db.fasta; do
    taxon=${file//_db.fasta}
    usearch -sintax ${taxon}_SE.fasta -db UDB/${file//.fasta}.udb -tabbedout ${taxon}.sintax -strand both -sintax_cutoff 0.8

    cat ${taxon}.sintax >> evaluate_all.sintax  
done


python /media/amelie/DATA/Anders_TFM/Script/Python/evaluate_sintax_bis.py evaluate_all.sintax 0.1 result_evaluate.txt


mkdir SINTAX
mv *.sintax SINTAX/

mkdir FASTA
mv *fasta FASTA/

mkdir EVALUATE
mv *.txt EVALUATE/

