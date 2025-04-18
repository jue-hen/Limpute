#! /bin/bash
cd ../impute
python ../../vcf_format_transfer.py ./ target.vcf target.vcf

bgzip target.vcf 
