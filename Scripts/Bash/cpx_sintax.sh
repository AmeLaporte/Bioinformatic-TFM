#!bin/bash

#aller dans le dossier où sont les fichiers avec le nom


#changer le level taxonomique dans le script python

for file in *;do
    echo ${file}
    python /home/amelie/Téléchargements/TFM_Anders/Sintax\ DB/cpx_sintax.py /home/amelie/Téléchargements/TFM_Anders/Sintax\ DB/unite.fasta /home/amelie/Téléchargements/TFM_Anders/LCA\ DB/unite.fasta ${file}
done

#changer le nom du dossier
mv *.fasta ../class_files

    
