#!/bin/bash

echo 'File analysis....'

for file in *.txt; do

    sed '2,5!d' ${file}> ${file//.txt}_domain.txt 
    sed '9,12!d' ${file} > ${file//.txt}_kingdom.txt 
    sed '16,19!d' ${file} > ${file//.txt}_phylum.txt 
    sed '23,26!d' ${file} > ${file//.txt}_class.txt 
    sed '30,33!d' ${file} > ${file//.txt}_order.txt 
    sed '37,40!d' ${file} > ${file//.txt}_family.txt 
    sed '44,47!d' ${file} > ${file//.txt}_genus.txt 
    sed '51,54!d' ${file} > ${file//.txt}_specie.txt
done

for file in *_domain.txt;do
    sed '1!d' ${file} > TN_${file}
    sed '2!d' ${file} > FP_${file}
    sed '3!d' ${file} > FN_${file}
    sed '4!d' ${file} > TP_${file}
done

cat TN_*_domain.txt > all_TN_domain.txt
cat TP_*_domain.txt > all_TP_domain.txt
cat FN_*_domain.txt > all_FN_domain.txt
cat FP_*_domain.txt > all_FP_domain.txt


for file in *_kingdom.txt;do
    sed '1!d' ${file} > TN_${file}
    sed '2!d' ${file} > FP_${file}
    sed '3!d' ${file} > FN_${file}
    sed '4!d' ${file} > TP_${file}
done

cat TN_*_kingdom.txt > all_TN_kingdom.txt
cat TP_*_kingdom.txt > all_TP_kingdom.txt
cat FN_*_kingdom.txt > all_FN_kingdom.txt
cat FP_*_kingdom.txt > all_FP_kingdom.txt


for file in *_phylum.txt;do
    sed '1!d' ${file} > TN_${file}
    sed '2!d' ${file} > FP_${file}
    sed '3!d' ${file} > FN_${file}
    sed '4!d' ${file} > TP_${file}
done

cat TN_*_phylum.txt > all_TN_phylum.txt
cat TP_*_phylum.txt > all_TP_phylum.txt
cat FN_*_phylum.txt > all_FN_phylum.txt
cat FP_*_phylum.txt > all_FP_phylum.txt


for file in *_class.txt;do
    sed '1!d' ${file} > TN_${file}
    sed '2!d' ${file} > FP_${file}
    sed '3!d' ${file} > FN_${file}
    sed '4!d' ${file} > TP_${file}
done

cat TN_*class.txt > all_TN_class.txt
cat TP_*_class.txt > all_TP_class.txt
cat FN_*_class.txt > all_FN_class.txt
cat FP_*_class.txt > all_FP_class.txt


for file in *_order.txt;do
    sed '1!d' ${file} > TN_${file}
    sed '2!d' ${file} > FP_${file}
    sed '3!d' ${file} > FN_${file}
    sed '4!d' ${file} > TP_${file}
done

echo '...'

cat TN_*_order.txt > all_TN_order.txt
cat TP_*_order.txt > all_TP_order.txt
cat FN_*_order.txt > all_FN_order.txt
cat FP_*_order.txt > all_FP_order.txt


for file in *_family.txt;do
    sed '1!d' ${file} > TN_${file}
    sed '2!d' ${file} > FP_${file}
    sed '3!d' ${file} > FN_${file}
    sed '4!d' ${file} > TP_${file}
done

cat TN_*_family.txt > all_TN_family.txt
cat TP_*_family.txt > all_TP_family.txt
cat FN_*_family.txt > all_FN_family.txt
cat FP_*_family.txt > all_FP_family.txt


for file in *_genus.txt;do
    sed '1!d' ${file} > TN_${file}
    sed '2!d' ${file} > FP_${file}
    sed '3!d' ${file} > FN_${file}
    sed '4!d' ${file} > TP_${file}
done

echo '...'

cat TN_*_genus.txt > all_TN_genus.txt
cat TP_*_genus.txt > all_TP_genus.txt
cat FN_*_genus.txt > all_FN_genus.txt
cat FP_*_genus.txt > all_FP_genus.txt


for file in *_specie.txt;do
    sed '1!d' ${file} > TN_${file}
    sed '2!d' ${file} > FP_${file}
    sed '3!d' ${file} > FN_${file}
    sed '4!d' ${file} > TP_${file}
done

cat TN_*_specie.txt > all_TN_specie.txt
cat TP_*_specie.txt > all_TP_specie.txt
cat FN_*_specie.txt > all_FN_specie.txt
cat FP_*_specie.txt > all_FP_specie.txt

echo 'Calculation in progress'

cat all_TN_domain.txt | awk '{total+=$3}END{print total}' > total_TN_domain.txt
cat all_TP_domain.txt | awk '{total+=$3}END{print total}' > total_TP_domain.txt
cat all_FN_domain.txt | awk '{total+=$3}END{print total}' > total_FN_domain.txt
cat all_FP_domain.txt | awk '{total+=$3}END{print total}' > total_FP_domain.txt

cat all_TN_kingdom.txt | awk '{total+=$3}END{print total}' > total_TN_kingdom.txt
cat all_TP_kingdom.txt | awk '{total+=$3}END{print total}' > total_TP_kingdom.txt
cat all_FN_kingdom.txt | awk '{total+=$3}END{print total}' > total_FN_kingdom.txt
cat all_FP_kingdom.txt | awk '{total+=$3}END{print total}' > total_FP_kingdom.txt

cat all_TN_phylum.txt | awk '{total+=$3}END{print total}' > total_TN_phylum.txt
cat all_TP_phylum.txt | awk '{total+=$3}END{print total}' > total_TP_phylum.txt
cat all_FN_phylum.txt | awk '{total+=$3}END{print total}' > total_FN_phylum.txt
cat all_FP_phylum.txt | awk '{total+=$3}END{print total}' > total_FP_phylum.txt

cat all_TN_class.txt | awk '{total+=$3}END{print total}' > total_TN_class.txt
cat all_TP_class.txt | awk '{total+=$3}END{print total}' > total_TP_class.txt
cat all_FN_class.txt | awk '{total+=$3}END{print total}' > total_FN_class.txt
cat all_FP_class.txt | awk '{total+=$3}END{print total}' > total_FP_class.txt

cat all_TN_order.txt | awk '{total+=$3}END{print total}' > total_TN_order.txt
cat all_TP_order.txt | awk '{total+=$3}END{print total}' > total_TP_order.txt
cat all_FN_order.txt | awk '{total+=$3}END{print total}' > total_FN_order.txt
cat all_FP_order.txt | awk '{total+=$3}END{print total}' > total_FP_order.txt

cat all_TN_family.txt | awk '{total+=$3}END{print total}' > total_TN_family.txt
cat all_TP_family.txt | awk '{total+=$3}END{print total}' > total_TP_family.txt
cat all_FN_family.txt | awk '{total+=$3}END{print total}' > total_FN_family.txt
cat all_FP_family.txt | awk '{total+=$3}END{print total}' > total_FP_family.txt

cat all_TN_genus.txt | awk '{total+=$3}END{print total}' > total_TN_genus.txt
cat all_TP_genus.txt | awk '{total+=$3}END{print total}' > total_TP_genus.txt
cat all_FN_genus.txt | awk '{total+=$3}END{print total}' > total_FN_genus.txt
cat all_FP_genus.txt | awk '{total+=$3}END{print total}' > total_FP_genus.txt

cat all_TN_specie.txt | awk '{total+=$3}END{print total}' > total_TN_specie.txt
cat all_TP_specie.txt | awk '{total+=$3}END{print total}' > total_TP_specie.txt
cat all_FN_specie.txt | awk '{total+=$3}END{print total}' > total_FN_specie.txt
cat all_FP_specie.txt | awk '{total+=$3}END{print total}' > total_FP_specie.txt

echo  'TN' `cat total_TN_specie.txt` 'TP'  `cat total_TP_specie.txt` 'FN'  `cat total_FN_specie.txt` 'FP'  `cat total_FP_specie.txt` > specieTotal.txt

echo 'TN' `cat total_TN_kingdom.txt` 'TP'  `cat total_TP_kingdom.txt` 'FN'  `cat total_FN_kingdom.txt` 'FP'  `cat total_FP_kingdom.txt` > kingdomTotal.txt

echo 'TN' `cat total_TN_domain.txt` 'TP'  `cat total_TP_domain.txt` 'FN'  `cat total_FN_domain.txt` 'FP'  `cat total_FP_domain.txt` > domainTotal.txt

echo 'TN' `cat total_TN_phylum.txt` 'TP'  `cat total_TP_phylum.txt` 'FN'  `cat total_FN_phylum.txt` 'FP'  `cat total_FP_phylum.txt` > phylumTotal.txt

echo 'TN' `cat total_TN_class.txt` 'TP'  `cat total_TP_class.txt` 'FN'  `cat total_FN_class.txt` 'FP'  `cat total_FP_class.txt` > classTotal.txt

echo 'TN' `cat total_TN_order.txt` 'TP'  `cat total_TP_order.txt` 'FN'  `cat total_FN_order.txt` 'FP'  `cat total_FP_order.txt` > orderTotal.txt

echo 'TN' `cat total_TN_family.txt` 'TP'  `cat total_TP_family.txt` 'FN'  `cat total_FN_family.txt` 'FP'  `cat total_FP_family.txt` > familyTotal.txt

echo 'TN' `cat total_TN_genus.txt` 'TP'  `cat total_TP_genus.txt` 'FN'  `cat total_FN_genus.txt` 'FP'  `cat total_FP_genus.txt` > genusTotal.txt

rm *_*.txt

echo -e 'Domain \n' `cat domainTotal.txt` '\n Kingdom \n' `cat kingdomTotal.txt` '\n Phylum \n' `cat phylumTotal.txt` '\n Class \n' `cat classTotal.txt` '\n Order \n' `cat orderTotal.txt` '\n Family \n' `cat familyTotal.txt` '\n Genus \n' `cat genusTotal.txt` '\n Specie \n' `cat specieTotal.txt`  > EvaluateSummarized.txt

rm *Total.txt

cat EvaluateSummarized.txt
