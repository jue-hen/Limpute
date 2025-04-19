#! /bin/bash

###if you have some double-end sequencing reads file, for example
###sample1_r1.fq.gz    sample2_r2.fq.gz
###sample2_r1.fq.gz    sample2_r2.fq.gz
###sample3_r1.fq.gz    sample2_r2.fq.gz
##etc...

##you can use this script to extract ALT/REF info from sequencing reads 
#for i in *
#do
#    j=$(basename $i | cut -d "_" -f 1 | uniq)
#    ../fq2depth ../site.probe.avx2 ./${j}.depth ${j}*.gz
#done;


####To make things easier, we've already uploaded the processed depth files. So, during testing, you can start directly from step2.

