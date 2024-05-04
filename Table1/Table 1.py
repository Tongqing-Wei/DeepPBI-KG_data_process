from Bio import Entrez
from Bio import SeqIO
import pandas as pd
import re

def NCBI_seq(key_words):
    
    Entrez.email = "20210700125@fudan.edu.cn"     # Always tell NCBI who you are
    # 查找相应ID    
    handle = Entrez.esearch(db="protein", term="%s tail" % key_words)
    record = Entrez.read(handle)
    gi_list = record["IdList"]

    # 获取Genbank信息
    test = []
    seqindex = []
    seq = []
    label = []
    dic = []
    gi_str = ",".join(gi_list)
    handle1 = Entrez.efetch(db="protein", id=gi_str, rettype="gb", retmode="text")
    records = SeqIO.parse(handle1, "gb")
    for i in records:
        test.append(i)
    for i in test:
        if 'tail' in re.findall(r'(.+?)\ ', i.description):
            label.append(i.description)
    label = list(set(label))
    for i in label:
        dic.append({j:len(ls.seq) for j,ls in enumerate(test) if ls.description == i})
    for i in dic:
        seqindex.append(max(i, key = i.get))
    for i in seqindex:
        seq.append(test[i].seq)
        
    return seq
        
    
if __name__ == '__main__':
    xl = pd.read_excel('D:/我的文件/噬菌体数据/公共数据/公共数据final/PHI_final.xlsx', sheet_name = 'ID', header = 0)
    file = open('C:/Users/未同庆/Desktop/tail.txt', 'w')
    phage = []
    for i in range(len(xl)):
        phage.append(xl.iloc[i][2])
    phage = list(set(phage))
    
    for i in range(len(phage)):
        result = NCBI_seq(phage[i].split(',')[0])
        for j in result:
            file.writelines('%s\t%s\n' % (phage[i], j))
    file.close()


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



tail = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/external/receptor.txt', sep = '\t', header = 0)
tail = tail.drop_duplicates()
xl = pd.read_excel('D:/我的文件/噬菌体数据/公共数据/external/external_PHI.xlsx', sheet_name = 'ID', header = 0)
dic = {}
for i in range(len(tail)):
    p = xl[xl['host_species'] == tail.iloc[i,0]].index.tolist()[0]
    tail.iloc[i,0] = xl.iloc[p,1].split('.')[0]
for i in range(len(tail)):
    if tail.iloc[i,0] not in dic.keys():
        dic[tail.iloc[i,0]] = [tail.iloc[i,1]]
    else:
        dic[tail.iloc[i,0]].append(tail.iloc[i,1])

        
# 文件输出路径
walkfile = walkFile('E:/protein')
f = open('D:/我的文件/噬菌体数据/公共数据/external/rbp_host.txt', 'w')
name = []
for k in dic.keys():
    for ls in walkfile:
        if ls[8:-8] == k:
            res_dir = "E:/protein/" + ls
            records = (r for r in SeqIO.parse(res_dir, "fasta"))
            test = []
            for i in records:
                test.append(i)
            for v in dic[k]:
                for j in test:
                    if j.seq == v:
                        f.writelines('%s\t%s\n' % (ls[8:-8], j.seq))
                        name.append(j.name)
name = pd.DataFrame(name)
name.to_csv('D:/我的文件/噬菌体数据/公共数据/external/rbp_host.csv', index = False)
f.close()