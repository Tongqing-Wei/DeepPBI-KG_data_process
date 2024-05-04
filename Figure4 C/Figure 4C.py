import pandas as pd
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_curve, auc, confusion_matrix
from sklearn.metrics import roc_auc_score, precision_recall_curve
data = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/工具对比/PredPHI/external_kmeans_roc_new.csv', header = 0).iloc[ind['0'].tolist(),:]
#ind = pd.read_csv('C:/Users/未同庆/Desktop/index.csv', header = 0)
#data = data[data['pred'] != 0]
#data = data.iloc[ind['0'].tolist(), :]
data['score'] = 0
#data['one minus pred'] = 1 - data['pred']
#data['one minus pred'][1267:] = data['one minus pred'][1267:] / 1.005
for i in range(len(data)):
    if data.iloc[i, 1] < 0.5:
        data.iloc[i, -1] = 0
    else:
        data.iloc[i, -1] = 1
data

TP = confusion_matrix(data['label'], data['score'])[1, 1]
TN = confusion_matrix(data['label'], data['score'])[0, 0]
FP = confusion_matrix(data['label'], data['score'])[0, 1]
FN = confusion_matrix(data['label'], data['score'])[1, 0]
print('acc  ' + str(accuracy_score(data['label'], data['score'])))
print('pre  ' + str(precision_score(data['label'], data['score'])))
print('recall  ' + str(recall_score(data['label'], data['score'])))
print('f1  ' + str(f1_score(data['label'], data['score'])))
print('spe  ' + str(TN / float(TN + FP)))
print('sen  ' + str(TP / float(TP + FN)))

confusion_matrix(data['label'], data['score'])

y_label = data['label']
y_pred = data['pred']
fpr = dict()
tpr = dict() 
roc_auc = dict()
fpr[0], tpr[0], _ = roc_curve(y_label, y_pred)
roc_auc[0] = auc(fpr[0], tpr[0])
roc_auc[0]

precision, recall, _thresholds = precision_recall_curve(y_label, y_pred)
roc_auc= auc(recall, precision)
roc_auc

import matplotlib
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
rcParams['pdf.fonttype'] = 42 
rcParams['ps.fonttype'] = 42 

#matplotlib.rcParams['font.family']='Times New Roman'           
#matplotlib.rcParams['font.sans-serif']=['Times New Roman']
data_labels=np.array(['KGDeepPBI','VirHostMatcher','vHULK', 'DeepHost'])

n=5
radar_labels=np.array(['             accuracy','                   precision','recall         ',\
                     'F1   ','                  specificity', ' '])
    
data = np.array([[0.7478, 0.7296, 0.7571, 0.6343],
                 [0.7628, 0.9742, 1, 0.9831],
                 [0.7664, 0.5074, 0.5454, 0.3212],
                 [0.7646, 0.6674, 0.7058, 0.4842],
                 [0.7264, 0.9846, 1, 0.9937]]) 
data = np.concatenate((data, [data[0]]))    
angles=np.linspace(0,2*np.pi,n,endpoint=False)
angles=np.concatenate((angles,[angles[0]]))     
plt.figure(facecolor='white', figsize = (10, 10))
plt.subplot(111,polar=True)
#plt.figtext(0.52,0.95,'雷达图',ha='center',size=20)  
plt.thetagrids(angles*180/np.pi,radar_labels, fontsize = '20')
sam = ['r-', 'o-.', 'g--', 'b-.', 'p:']
plt.plot(angles,data,'o-',linewidth=1.5,alpha=0.2) #连线，画出不规则六边形
plt.fill(angles,data,alpha=0.15) 
legend=plt.legend(data_labels,loc=(0.94,0.80),labelspacing=0.1, fontsize = '20')
plt.setp(legend.get_texts(),fontsize='18')      
plt.grid(True)
plt.ylim(0, 1)
plt.savefig(r'C:/Users/未同庆/Desktop/rodar.pdf',dpi=400, bbox_inches = 'tight')
plt.show()
