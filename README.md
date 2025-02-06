# Limpute
A Novel Efficient Algorithm for Common Variants Genotyping from Low-Coverage Sequencing Data


## Installation
```
Prerequisites: cget, cmake.
git clone https://github.com/jue-hen/Limpute

###Download Large File
pip install gdown
gdown “https://drive.google.com/file/d/1W7oIAFN8PATjzNbrwG_MejtMtNuEGFT6/view?usp=drive_link”

gdown “https://drive.google.com/file/d/1rsGkFGItKth4TVQ74U01_e1xB9iOrkjd/view?usp=drive_link”
gzip site.probe.gz
```

## Usage

For example, you have some sequencing reads file,
```
sample1.gz 
sample2.gz
sample3.gz
..............
```

### First step, transfer these file to depth file：
```
for     i       in      *
do
        j=$(basename $i | cut -d “.” -f 1)
        ./fq2depth site.probe.avx2 ./$j.depth $i
done;
```


### Second step：
#### a.prepare target sample list
```
cat target.list
target1.depth
target2.depth
target3.depth
......
```

#### b.prepare reference sample list
```
cat reference.list
reference1.depth
reference2.depth
reference3.depth
.....
```

#### c.imputation
```
./phoenix ./target_ori.vcf ./target.list ./reference.list 1024
zcat target_ori.vcf | sed '1s/.depth//g' | paste ./site.probe - -d "\t" > ./target_ori.vcf
```

### Third step, produce vcf file:
```
python ./vcf_format_transfer.py  ./target_ori.vcf ./target.vcf
```
