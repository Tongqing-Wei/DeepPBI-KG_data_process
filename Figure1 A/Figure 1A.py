import pandas as pd
alldata = pd.read_excel('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/RF_all_sample.xlsx', sheet_name = 'ID', header = 0)
alldata

from collections import Counter
phage = list(set(alldata['phage_name'].tolist()))
pre = []
for i in range(len(phage)):
    pre.append(phage[i].split(' ')[0])
dic = Counter(pre)

dic = sorted(dic.items(), key = lambda x : x[1], reverse = True)
dic


from Bio import Entrez
from Bio import SeqIO
import pandas as pd
import re

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
    return ana + format_seq + "\n"

def NCBI_seq(key_words):
    
    Entrez.email = "20210700125@fudan.edu.cn"     # Always tell NCBI who you are
    # 查找相应ID    
    handle = Entrez.esearch(db="Nucleotide", term=key_words)
    record = Entrez.read(handle)
    gi_list = record["IdList"]

    # 获取Genbank信息
    gi_str = ",".join(gi_list)
    handle1 = Entrez.efetch(db="Nucleotide", id=gi_str, rettype="gb", retmode="text")
    records = SeqIO.parse(handle1, "gb")
    for i in records:
        if key_words in i.description:
            return str(i.seq)
        
    
if __name__ == '__main__':
    #xl = pd.read_excel('D:/我的文件/噬菌体数据/公共数据/公共数据final/PHI_final.xlsx', sheet_name = 'ID', header = 0)
    #target = data['Description'].tolist()
    for i in range(len(target)):
        file = open('D:/我的文件/噬菌体数据/公共数据/1062 database/' + str(target[i]) + '.fasta', 'w')
        result = NCBI_seq(target[i])
        res = format_fasta('>' + target[i] + '\n', result, 70)
        file.writelines(res)
        file.close()

def NCBI_seq(key_words, name):
    
    Entrez.email = "20210700125@fudan.edu.cn"     # Always tell NCBI who you are
    # 查找相应ID    
    handle = Entrez.esearch(db="Nucleotide", term=key_words)
    record = Entrez.read(handle)
    gi_list = record["IdList"]

    # 获取Genbank信息
    gi_str = ",".join(gi_list)
    handle1 = Entrez.efetch(db="Nucleotide", id=gi_str, rettype="gb", retmode="text")
    line = handle1.read()
    if line.split('DEFINITION')[1].split('ACCESSION')[0][2:-1].split(',')[0] == name.split(',')[0]:
        return line.split('ORGANISM ')[1].split('REFERENCE')[0][1:-1]
        
    
if __name__ == '__main__':
    #xl = pd.read_excel('D:/我的文件/噬菌体数据/公共数据/公共数据final/PHI_final.xlsx', sheet_name = 'ID', header = 0)
    #target = data['Description'].tolist()
    dic = {}
    for i in range(len(alldata)):
        dic[alldata.iloc[i,1]] = alldata.iloc[i,3]
    for k, v in dic.items():
        dic[k] = NCBI_seq(k, v)


query = {}
for i in range(len(res)):
    if res.iloc[i,-1] not in query:
        if res.iloc[i,1].split(' ')[0] == 'MAG':
            query[res.iloc[i,-1]] = [res.iloc[i,1].split(' ')[1]]
        else:
            query[res.iloc[i,-1]] = [res.iloc[i,1].split(' ')[0]]
    else:
        if res.iloc[i,1].split(' ')[0] == 'MAG':
            query[res.iloc[i,-1]].append(res.iloc[i,1].split(' ')[1])
        else:
            query[res.iloc[i,-1]].append(res.iloc[i,1].split(' ')[0])
query


for k, v in query.items():
    query[k] = sorted(v, key = lambda x : x[1], reverse = True)
query


ans = pd.DataFrame(index = list(range(162)), columns = ['phylum', 'phage kill host', 'num'])
n = 0
for k, v in query.items():
    for i in range(len(v)):
        ans.iloc[n, 0] = k
        ans.iloc[n, 1] = v[i][0]
        ans.iloc[n, 2] = v[i][1]
        n += 1
ans.to_csv('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/phage_host_phylum.csv', index = False)

import pandas as pd
phy = pd.read_excel('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/phage_host_phylum.xlsx', sheet_name='plot', header = 0)
phy

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties
%matplotlib inline
# 数据
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
rcParams['pdf.fonttype'] = 42 
rcParams['ps.fonttype'] = 42 
np.random.seed(123)
groups1 = phy[phy['phylum'] == 'Actinobacteria']['num'].tolist()
groups2 = phy[phy['phylum'] == 'Bacillota']['num'].tolist()
groups3 = phy[phy['phylum'] == 'Pseudomonadota']['num'].tolist()
groups4 = phy[phy['phylum'] == 'Campylobacterota']['num'].tolist()
groups5 = phy[phy['phylum'] == 'Cyanobacteriota']['num'].tolist()
groups6 = phy[phy['phylum'] == 'Mycoplasmatota']['num'].tolist()
groups7 = phy[phy['phylum'] == 'Firmicutes']['num'].tolist()
groups8 = phy[phy['phylum'] == 'Chlamydiota']['num'].tolist()
groups9 = phy[phy['phylum'] == 'Thermoproteota']['num'].tolist()
groups10 = phy[phy['phylum'] == 'Euryarchaeota']['num'].tolist()
groups11 = phy[phy['phylum'] == 'Bacteroidota']['num'].tolist()
groups12 = phy[phy['phylum'] == 'Bdellovibrionota']['num'].tolist()
groups13 = phy[phy['phylum'] == 'Crenarchaeota']['num'].tolist()
groups14 = phy[phy['phylum'] == 'Discosea']['num'].tolist()
groups15 = phy[phy['phylum'] == 'Deinococcota']['num'].tolist()
groups16 = phy[phy['phylum'] == 'Other phylum']['num'].tolist()
 
groups = [groups1, groups2, groups3, groups4, groups5, groups6, groups7, groups8, groups9, groups10, groups11, groups12, groups13, groups14,
          groups15, groups16]
group_names = phy['phylum'].drop_duplicates().tolist()
group_colors = ['#A6CEE3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#b79f00', '#ffd700', 
                '#ff706d', '#7baf06', '#01bfc5', '#cb7bf6', '#dda0dd']
 
# 画图
#a4_w = 210 / 4 / 25.4
#a4_h = 210 / 4 / 25.4
fig = plt.figure(figsize=(8.27 / 2, 11.69 / 2), dpi=300, facecolor='white')
ax = fig.add_subplot(projection='polar')
 
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
 
radii = [0]
colors = ['white']
for g, c in zip(groups, group_colors):
    radii.extend(g)
    colors.extend([c]*len(g))
    radii.append(0)
    colors.append('white')
radii.pop()
colors.pop()


N = len(radii)
r_lim = 80
scale_lim = 200
scale_major = 40
bottom = 140
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
width = 2 * np.pi / (N + 9)
 
# 画出柱状图
ax.bar(theta, radii, width=width, bottom=bottom, color=colors)
 
# # 画出刻度
# def scale(ax, bottom, scale_lim, theta, width):
#     t = np.linspace(theta-width/2, theta+width/2, 6)
#     for i in range(int(bottom), int(bottom+scale_lim+scale_major), scale_major):
#         ax.plot(t, [i]*6, linewidth=0.25, color='gray', alpha=0.8)

# 画出刻度值
def scale_value(ax, bottom, theta, scale_lim):
    for i in range(int(bottom), int(bottom+scale_lim+scale_major), scale_major):
        ax.text(theta,
                i,
                f'{i-bottom}',
                fontsize=3.5,
                alpha=0.8,
                va='center',
                ha='center'
                )

s_list = []
g_no = 0
aa = phy['phage kill host'].tolist()
for t, r in zip(theta, radii):
    if r == 0:
        s_list.append(t)
        if t == 0:
            scale_value(ax, bottom, t, scale_lim)
        else:
            #scale(ax, bottom, scale_lim, t, width)
            pass
    else:
        t2 = np.rad2deg(t)
        # 标出每根柱的名称
        ax.text(t, r + bottom + scale_major*0.1,
                aa[g_no],
                fontsize=3,
                rotation=90-t2 if t < np.pi else 270-t2,
                rotation_mode='anchor',
                va='center',
                ha='left' if t < np.pi else 'right',
                color='black',
                clip_on=False,
                weight = 10
                )
        if g_no == (len(aa)-1):
            g_no = 0
        else:
            g_no += 1
 
 
s_list.append(2 * np.pi)
 
for i in range(len(s_list)-1):
    t = np.linspace(s_list[i]+width / 2, s_list[i+1]-width / 2, 50)
    ax.plot(t, [bottom-scale_major*0.2]*50, linewidth=0.1, color='black')
    '''
    ax.text(s_list[i]+(s_list[i+1]-s_list[i])/2,
            bottom-scale_major*1.2,
            group_names[i],
            va='center',
            ha='center',
            fontsize=3,
            )
    '''
ax.set_rlim(0, bottom+scale_lim+scale_major)
ax.axis('off')
font_properties = FontProperties(family = 'Arial', weight=1, size = 3)
legend = ax.legend(group_names, loc = 'lower center', ncol = 4, prop = font_properties, borderaxespad = 0.5)
frame = legend.get_frame()
frame.set_linewidth(0.5)
plt.savefig('C:/Users/未同庆/Desktop/correspond_host_phylum.pdf', dpi = 200, format = 'pdf')
plt.show()
