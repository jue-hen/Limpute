# Limpute 
A Novel Efficient Algorithm for Common Variants Genotyping from Low-Coverage Sequencing Data


## Installation
```
Prerequisites: cget, cmake.
git clone https://github.com/jue-hen/Limpute

cd Limpute/turtor
bash step0_script_setup.sh
```



## Usage

To generate VCF files from second-generation sequencing data using Limpute, the following three-step pipeline is employed:

Step 1: Extract reference (REF) and alternative (ALT) allele information for SNP sites using pre-defined virtual probes. This step generates highly compressed depth files. The corresponding script can be found at:
Limpute/turtor/step1_script_extract_reads_info.sh


Step 2: Perform genotype imputation by using the samples as mutual references to estimate genotype probabilities. This step is executed using the script:
Limpute/turtor/step2_script_impute.sh


Step 3: Convert the genotype probability files into sample-specific VCF files. This is accomplished with the script:
Limpute/turtor/step3_script_transfer.sh


For quick testing and demonstration purposes, preprocessed depth files are included in the test_data directory. These allow researchers to initiate the workflow directly from Step 2, bypassing the read extraction process.
