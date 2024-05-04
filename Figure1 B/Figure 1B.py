import pandas as pd
alldata = pd.read_excel('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/RF_all_sample.xlsx', sheet_name = 'ID', header = 0)
alldata

save = {}
for i in range(len(alldata[alldata['label'] == 1])):
    if 'MKD8' in alldata[alldata['label'] == 1].iloc[i,3]:
        save[alldata.iloc[i,0]] = alldata.iloc[i,2]
save

import re

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

walkfile = walkFile('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/phage_sequence')
f = open('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/Mycobacterium_phage.fasta', 'w')
for i in range(len(walkfile)):
    if walkfile[i][6:][walkfile[i][6:].find('_') + 1:-8] in save:
        ff = open('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/phage_sequence' + os.sep + walkfile[i], 'r')
        line = ff.readlines()
        ff.close()
        f.writelines(line)
f.close()

from Bio import Phylo
tree = Phylo.read('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/Mycobacterium_phage_new.phy', 'newick')
tree.ladderize()
#print(tree)
Phylo.draw_ascii(tree)

# from Bio import Phylo

# # 读取 Phylip 树文件
# tree_file_path = 'path/to/your/phylip_treefile.txt'
# with open(tree_file_path, 'r') as tree_file:
#     tree_text = tree_file.read()

# # 将 Newick 树文本解析为树对象
# tree = Phylo.read(tree_text, 'newick')

# 获取叶节点列表
leaves = tree.get_terminals()

# 创建一个距离矩阵
distance_matrix = {}

# 计算叶节点之间的距离
for i, leaf1 in enumerate(leaves):
    for leaf2 in leaves[i+1:]:
        distance = tree.distance(leaf1, leaf2)
        distance_matrix[(leaf1.name, leaf2.name)] = distance
        distance_matrix[(leaf2.name, leaf1.name)] = distance

# 打印距离矩阵
# for leaf1 in leaves:
#     row = [distance_matrix.get((leaf1.name, leaf2.name), 0) for leaf2 in leaves]
#     print(leaf1.name, row)

# 可以根据需要保存距离矩阵到文件
# 例如，将距离矩阵保存为 CSV 文件
csv_file_path = 'D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/distance_matrix.csv'
with open(csv_file_path, 'w') as csv_file:
    # 写入表头
    csv_file.write(','.join(leaf.name for leaf in leaves) + '\n')
    
    # 写入数据行
    for leaf1 in leaves:
        row = [str(distance_matrix.get((leaf1.name, leaf2.name), 0)) for leaf2 in leaves]
        csv_file.write(','.join(row) + '\n')

print("Distance matrix has been printed and saved to:", csv_file_path)

import pandas as pd
data = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/distance_matrix.csv', header = 0, index_col = 0)
data

cut = pd.read_csv("D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/cut.csv", header = 0)
cut

import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from scipy.spatial.distance import pdist, squareform

# 假设有一个随机数据集
#np.random.seed(42)
#data = np.random.rand(10, 4)

# 计算距离矩阵
dist_matrix = pdist(data)

# 进行层次聚类
Z = linkage(data, method='average')

# 基于聚类结果生成切割点，这里我们选择3个聚类
#clusters = fcluster(Z, t=3, criterion='maxclust')
clusters = np.asarray(cut['x']).flatten()
# 为了生成新的距离矩阵，我们需要按聚类结果对数据点分组并计算每个聚类的质心
centroids = pd.DataFrame(data).groupby(clusters).mean().values

# 计算质心之间的新距离矩阵
new_dist_matrix = pdist(centroids)

# 将新的距离矩阵转换为方阵形式以便更好地理解和展示
new_dist_matrix_square = squareform(new_dist_matrix)

# 将结果转换为DataFrame以提供更清晰的格式化输出
new_dist_df = pd.DataFrame(new_dist_matrix_square)

new_dist_df

# 为了生成新的距离矩阵，我们需要按聚类结果对数据点分组并计算每个聚类的质心
centroids = pd.DataFrame(data).groupby(clusters).mean().values

# 计算质心之间的新距离矩阵
new_dist_matrix = pdist(centroids)

# 将新的距离矩阵转换为方阵形式以便更好地理解和展示
new_dist_matrix_square = squareform(new_dist_matrix)

# 将结果转换为DataFrame以提供更清晰的格式化输出
new_dist_df = pd.DataFrame(new_dist_matrix_square)

new_dist_df

cut['name'] = data.index
name = []
for i in range(1, 144):
    if len(cut[cut['x'] == i]) == 1:
        name.append(cut[cut['x'] == i].iloc[0,1])
    else:
        name.append(len(cut[cut['x'] == i]))
new_dist_df.columns = name
new_dist_df.index = name
new_dist_df

new_dist_df.to_csv('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/distance_matrix_cutree.csv', index = True)