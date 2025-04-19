#! /bin/bash

cd ..
chmod +x Limpute_phoenix
chmod +x Limpute_fq2depth
chmod +x vcf_format_transfer.py

pip install gdown
gdown --fuzzy "https://drive.google.com/file/d/1W7oIAFN8PATjzNbrwG_MejtMtNuEGFT6/view?usp=drive_link"
gdown --fuzzy "https://drive.google.com/file/d/1rsGkFGItKth4TVQ74U01_e1xB9iOrkjd/view?usp=drive_link"
gunzip site.probe.gz
