import pandas as pd
data = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/phage_key_gene_importance.csv', header = 0)
data

phage = data['importance'].tolist()[:95]
phage = sorted(phage)[::-1]
host = data['importance'].tolist()[95:]
host = sorted(host)[::-1]
val = pd.DataFrame(phage + host)
val

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
rcParams['pdf.fonttype'] = 42 
rcParams['ps.fonttype'] = 42 

threshold_list = [1, 0.99, 0.95, 0.90, 0.85, 0.80, 0.75, 0.70, 0.65, 0.60, 0.55, 0.50]
colors = plt.cm.Greens(np.linspace(0.99,0.3,len(threshold_list)))
fig, ax1 = plt.subplots(figsize=(15,6))
ax1.plot(sorted(data['importance'].tolist())[::-1], color=colors[4], linewidth=3)
ax1.set_title('host key_gene importance', fontsize = 24, pad = 12.0)
ax1.set_ylabel('importance', fontsize=20)
#ax1.axvline(x=1310, color='grey', linestyle='--', lw = 4)
ax1.axhline(y=0.00004, color='red', linestyle='--', lw = 2)
#ax1.axhline(y=0.0002, color='red', linestyle='--', lw = 2)
#ax1.xaxis.set_major_formatter(ticker.NullFormatter())
plt.xticks([0, 10000, 20000, 30000], fontsize = 15)
plt.yticks([0.00004, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008], fontsize = 15)
ax1.set_xlim(0,32621)
#ax1.text(1.01, 0.008, 'contribution = 90%')
#ax1.set_xlabel('                                                                                                                 host                                                                                                                           ', fontsize=20)
fig.tight_layout()
#plt.savefig('C:/Users/未同庆/Desktop/RF_host_gene_importance.pdf', dpi = 400)

import matplotlib.pyplot as plt
import numpy as np
from brokenaxes import brokenaxes
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
rcParams['pdf.fonttype'] = 42 
rcParams['ps.fonttype'] = 42 

threshold_list = [1, 0.99, 0.95, 0.90, 0.85, 0.80, 0.75, 0.70, 0.65, 0.60, 0.55, 0.50]
colors = plt.cm.Greens(np.linspace(0.99,0.3,len(threshold_list)))
fig,ax1= plt.subplots(figsize=(10,5))
#bax = brokenaxes(xlims = ((0, 0.22), (0.78, 1)), despine = False, wspace=0.05, diag_color = '#1f78b4')
ax1.set_xlim(0,1110)
ax1.plot(sorted(data['importance'].tolist())[::-1][:1110], color=colors[4], linewidth=3)
ax1.set_title('phage key_gene importance', fontsize = 24, pad = 12.0)
ax1.set_ylabel('importance', fontsize=20)
#ax1.axvline(x=1310, color='grey', linestyle='--', lw = 4)
ax1.axhline(y=0.00004, color='red', linestyle='--', lw = 2)
#ax1.axhline(y=0.0002, color='red', linestyle='--', lw = 2)
#ax1.xaxis.set_major_formatter(ticker.NullFormatter())
plt.xticks([0, 400, 800, 1100], fontsize = 15)
plt.yticks([0.0001, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008], fontsize = 15)
#ax1.text(1.01, 0.008, 'contribution = 90%')
#ax1.set_xlabel('                                                                                                                 host                                                                                                                           ', fontsize=20)
fig.tight_layout()
plt.savefig('C:/Users/未同庆/Desktop/RF_phage_gene_importance_broken.pdf', dpi = 400)