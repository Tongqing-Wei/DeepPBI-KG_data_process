# 检查从NCBI找的RBP在不在phage_protein中, 并提取对应config的ID
import pandas as pd
import os
import re
import pandas as pd
import numpy as np
from Bio import Entrez
from Bio import SeqIO
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

def walkFile(file):
    phage_name = []
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        for f in files:
            phage_name.append(os.path.join(f))
    return phage_name



tail = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/receptor.txt', sep = '\t', header = None)
tail = tail.drop_duplicates()
xl = pd.read_excel('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/RF_all_sample.xlsx', sheet_name = 'ID', header = 0)
dic = {}
for i in range(len(tail)):
    p = xl[xl['host_name'] == tail.iloc[i,0]].index.tolist()[0]
    tail.iloc[i,0] = xl.iloc[p,1]
for i in range(len(tail)):
    if tail.iloc[i,0] not in dic.keys():
        dic[tail.iloc[i,0]] = [tail.iloc[i,1]]
    else:
        dic[tail.iloc[i,0]].append(tail.iloc[i,1])

        
# 文件输出路径
walkfile = walkFile('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/host_protein')
f = open('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/rbp_host.txt', 'w')
name = []
for k in dic.keys():
    for ls in walkfile:
        if ls[13:-6][ls[13:-6].find('_') + 1:] == k:
            res_dir = "D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/host_protein/" + ls
            records = (r for r in SeqIO.parse(res_dir, "fasta"))
            test = []
            for i in records:
                test.append(i)
            for v in dic[k]:
                for j in test:
                    if j.seq == v:
                        f.writelines('%s\t%s\n' % (ls[13:-6][ls[13:-6].find('_') + 1:], j.seq))
                        name.append(j.name)
name = pd.DataFrame(name)
name.to_csv('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/rbp_host.csv', index = False)
f.close()