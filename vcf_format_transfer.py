# -*- coding: utf-8 -*-
"""
Created on 20240220

@author: xiaokl
"""

# 1.导入所需模块
import sys
import random
import numpy as np
import pandas as pd

# 2.数据输入
file_path=sys.argv[1]              # 
filename=sys.argv[2]               # 
data=pd.read_table(file_path+filename,sep="\t",header="infer")
wangyi=pd.read_table(file_path+filename,header='infer',index_col=False,dtype=object) # wangyi=pd.read_table(file_path+filename,header='infer',index_col=False,dtype=object)
f = open(file_path+filename,'r')
geno = ["0/0","0/1","1/1"]
t=f.readline()

# 2. content内容格式转换
def p_random(arr1,arr2):
    assert len(arr1) == len(arr2), "Length does not match."
    assert sum(arr2) == 1, "Total rate is not 1."

    sup_list = [len(str(i).split(".")[-1]) for i in arr2]
    top = 10 ** max(sup_list)
    new_rate = [int(i*top) for i in arr2]
    rate_arr = []
    for i in range(1,len(new_rate)+1):
        rate_arr.append(sum(new_rate[:i]))
    rand = random.randint(1,top)
    data = None
    for i in range(len(rate_arr)):
        if rand <= rate_arr[i]:
            data = arr1[i]
            break
    return data

###P VALU matrix Part 'A'
pvalue1 = []
PWeights1 = 1/9
            ##Weighted probability value
PWeights2 = 4/9
PWeights3 = 4/9
pvalue1.append(PWeights1)
pvalue1.append(PWeights2)
pvalue1.append(PWeights3)
plistA = []
for i in range(100000):
    plistA.append(p_random([0,1,2],pvalue1))

###P VALU matrix Part 'B'
pvalue2 = []
PWeights11 = 4/9
##Weighted probability value
PWeights22 = 4/9
PWeights33 = 1/9
pvalue2.append(PWeights11)
pvalue2.append(PWeights22)
pvalue2.append(PWeights33)
plistB = []
for i in range(100000):
    plistB.append(p_random([0,1,2],pvalue2))

########
m=0
wangyi_list=[]
for site in f.readlines():
    s = site.strip().split()
    s[8]='GT:DS:GP'
    s[7] = '.'
    o1 = s[9:]
    res = s[:9]
    #print(o1)
## Weights
    choices, counts = np.unique(o1, return_counts=True)
    choices = choices.tolist()
    for j in o1:
        a = [int(k) for k in j]
        GP = [a[0]/9, a[1]/9,a[2]/9]
        GP = [str(k) for k in GP]
        DS = a[1]/9 + 2*(a[2]/9)
        ff = str(DS)+":"+",".join(GP[0:]) 
        # Cluster 1
        if j == '441':
            index = int(random.choice(plistB))
            GT = geno[index]
            ft = GT+":"+ff
            res.append(ft)
        elif j =='144':
            index = int(random.choice(plistA))
            GT = geno[index]
            ft = GT+":"+ff 
            res.append(ft)
        else:
            K=a.index(max(a))
            GT = geno[K]
            ft = GT+":"+ff
            res.append(ft)
#    print('\t'.join(res))
    wangyi_list.append(res)
    m=m+1
# print(m,len(res))
wangyi_df=pd.DataFrame(wangyi_list)
wangyi_df.columns=wangyi.columns
data=wangyi_df

# 3.对格式进行统一
data_part1=data.iloc[:,0:9]
data_part2=data.iloc[:,9:]
#data_content=data_part2.applymap(lambda x:str.join("",x.split(":")[0].split("/")))
#data_content=data_part2.applymap(lambda x:str.join("",x.split(":")[0]))
data_unify=pd.concat([data_part1,data_part2],axis=1)

# 6.结果输出
filename_out=sys.argv[3]              # 'wangyi_unify.vcf'
data_unify.to_csv(file_path+filename_out,sep='\t',index=False,header=True)
