#!/bin/bash

for file in *;do
    echo ${file}
    python /media/amelie/DATA/Anders_TFM/Script/Python/cpx_sintax.py  /media/amelie/DATA/Anders_TFM/Sintax\ DB/unite.fasta /media/amelie/DATA/Anders_TFM/LCA\ DB/unite.fasta ${file}
done


for file in *_db.fasta ;do
    usearch -makeudb_sintax ${file} -output ${file//.fasta}.udb
done

mkdir UDB
mv *.udb UDB/

for file in *_db.fasta; do
    taxon=${file//_db.fasta}
    
    usearch -sintax ${taxon}.fasta -db UDB/${taxon}_db.udb -tabbedout ${taxon}.sintax -strand both -sintax_cutoff 0.8

    cat ${taxon}.sintax >> evaluate_all.sintax
done

python /media/amelie/DATA/Anders_TFM/Script/Python/evaluate_sintax_bis.py evaluate_all.sintax 0.1 result_evaluate.txt


mkdir SINTAX
mv *.sintax SINTAX/

mkdir FASTA
mv *fasta FASTA/

mkdir EVALUATE
mv *.txt EVALUATE/
