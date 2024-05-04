import os
import pandas as pd
import numpy as np
import re
from Bio import SeqIO

def format_fasta(ana, seq, num):
    """
    格式化文本为 fasta格式
    :param ana: 注释信息
    :param seq: 序列
    :param num: 序列换行时的字符个数
    :return: fasta格式文本
    """
    format_seq = ""
    for i, char in enumerate(seq):
        format_seq += char
        if (i + 1) % num == 0:
            format_seq += "\n"
    return '>' + ana + '\n' + format_seq + "\n"


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



if __name__ == '__main__':
    rbp = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/rbp_phage.csv', header = 0)
    dic = {}
    for i in range(len(rbp)):
        pre = rbp.iloc[i,0].split('.')[0]
        if pre in dic:
            dic[pre].append(rbp.iloc[i,0])
        else:
            dic[pre] = [rbp.iloc[i,0]]


    walkfile = walkFile('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/phage_protein')
    gene = []
    for ls in walkfile:
        if ls[14:-6][ls[14:-6].find('_') + 1:] in dic:
            target = dic[ls[14:-6][ls[14:-6].find('_') + 1:]]
        else:
            continue
        f = open('D:/我的文件/噬菌体数据/公共数据/Pipeline/tmp_file/phage_rbp_protein/' + os.sep + ls, 'w')
        cds_fasta = ''
        res_dir = "D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/phage_protein/" + ls
        records = (r for r in SeqIO.parse(res_dir, "fasta"))  
        for i in records:
            if i.description.split(' ')[0] in target:
                cds_fasta += format_fasta(i.description, i.seq, 70)
                if re.findall(r'\[(.+?)\]', i.description)[0][:4] == 'gene':
                    gene.append(re.findall(r'\[(.+?)\]', i.description)[0])
                elif re.findall(r'\[(.+?)\]', i.description)[1] != 'protein=hypothetical protein':
                    gene.append(re.findall(r'\[(.+?)\]', i.description)[1])
        f.write(cds_fasta)
        f.close()

    gene = pd.DataFrame(list(set(gene))).to_csv('D:/我的文件/噬菌体数据/公共数据/Pipeline/tmp_file/phage_gene.csv', index = False)