#! /bin/bash

cd ./test_data
ls sample_{1..5}.depth | sort -V > ./target.list  ####target.list is the list of dep files, this part is the list of samples you want to get
ls sample_{6..10}.depth | sort -V > ./reference.list ###reference.list is the list of dep files, this is the list of samples you want to use as reference

cd ..
mkdir impute

cd ./test_data
../../phoenix ../impute/target_ori.vcf ./target.list ./reference.list 1028

cd ../impute
zless target_ori.vcf | sed '1s/.depth//g' | paste ../../site.probe - -d "\t" > target.vcf
rm -r target_ori.vcf
