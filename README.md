# Limpute —— A Novel Efficient Algorithm for Common Variants Genotyping from Low-Coverage Sequencing Data


## Installation
```
Prerequisites: cget, cmake.
git clone https://github.com/jue-hen/Limpute

cd Limpute/turtor
bash step0_script_setup.sh
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



### Second step, imputation through Limpute：
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
