#! /bin/bash

chmod +x Limpute_phoenix
chmod +x Limpute_fq2depth
chmod +x vcf_format_transfer.py

pip install gdown
gdown --fuzzy "https://drive.google.com/file/d/1W7oIAFN8PATjzNbrwG_MejtMtNuEGFT6/view?usp=drive_link"
gdown --fuzzy "https://drive.google.com/file/d/1rsGkFGItKth4TVQ74U01_e1xB9iOrkjd/view?usp=drive_link"
gunzip site.probe.gz

###if you have some double-end sequencing reads file, for example
###sample1_r1.fq.gz    sample2_r2.fq.gz
###sample2_r1.fq.gz    sample2_r2.fq.gz
###sample3_r1.fq.gz    sample2_r2.fq.gz
##etc...

##you can use this script to extract ALT/REF info from sequencing reads 
for i in *
do
    j=$(basename $i | cut -d "_" -f 1 | uniq)
    ../fq2depth ../site.probe.avx2 ./${j}.depth ${j}*.gz
done;


####To make things easier, we've already uploaded the processed depth files. So, during testing, you can start directly from step2.

