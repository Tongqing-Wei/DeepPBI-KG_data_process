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


import re
import os
from Bio import SeqIO
import argparse

#将参数定义好并封装
parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help = 'input phage(host) cds protein fasta file path')
parser.add_argument('--type', type=str, help = 'phage or host')
parser.add_argument('--output', type=str, help = 'output phage(host) all key gene seq fasta file')
opt = parser.parse_args()     
walkfile = walkFile(opt.input) 
lt = []
for ls in walkfile:
    if ls[-5:] == 'fasta':
        gb = list(SeqIO.parse(opt.input + os.sep + ls, 'fasta'))
        for i in gb:
            if re.findall(r'\[(.+?)\]', i.description)[0][:4] == 'gene':
                lt.append(re.findall(r'\[(.+?)\]', i.description)[0])
            elif re.findall(r'\[(.+?)\]', i.description)[1] != 'protein=hypothetical protein':
                lt.append(re.findall(r'\[(.+?)\]', i.description)[1])

ll = list(set(lt))

dic = {}
for i in range(len(ll)):
    dic[ll[i]] = ll[i]

import re
import os
from Bio import SeqIO
walkfile = walkFile(opt.input) 
#f = open('/bios-store1/home/TongqingWei/database/host.txt', 'w')
for ls in walkfile:
    if ls[-5:] == 'fasta':
        gb = list(SeqIO.parse(opt.input + os.sep + ls, 'fasta'))
        for i in gb:
            if re.findall(r'\[(.+?)\]', i.description)[0][:4] == 'gene' and re.findall(r'\[(.+?)\]', i.description)[0] in dic:
                dic[re.findall(r'\[(.+?)\]', i.description)[0]] = str(i.seq)
                #f.writelines('>%s\n' % re.findall(r'\[(.+?)\]', i.description)[0])
                #f.writelines('%s\n' % i.seq)
            elif re.findall(r'\[(.+?)\]', i.description)[1] in dic:
                dic[re.findall(r'\[(.+?)\]', i.description)[1]] = str(i.seq)
                #f.writelines('>%s\n' % re.findall(r'\[(.+?)\]', i.description)[1])
                #.writelines('%s\n' % i.seq)
                
#f.close()

f = open(opt.output + os.sep + opt.type + '_key_gene.txt', 'w')
for k, v in dic.items():
    f.writelines('>%s\n' % k)
    f.writelines('%s\n' % v)   
f.close()