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

import pandas as pd
#MLPg = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/工具对比/My-result/key_gene_MLP_test_kmeans.csv', header = 0)
#MLPr = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/工具对比/My-result/RBP_MLP_test_kmeans.csv', header = 0)
#RFg = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/工具对比/My-result/key_gene_RF_test_kmeans.csv', header = 0)
RFr = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/Pipeline/result/key_gene_external_new.csv', header = 0)
predphi = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/工具对比/PredPHI/external_key_gene_roc_new.csv', header = 0)
deephost = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/工具对比/DeepHost/external_key_gene_roc_new.csv', header = 0)
wish = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/工具对比/WIsH/external_key_gene_roc_new.csv', header = 0)
vhm = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/工具对比/VirHostMatcher-Net/external_key_gene_roc_new.csv', header = 0)
php = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/工具对比/PHP/external_key_gene_roc_new.csv', header = 0)
vhulk = pd.read_csv('D:/我的文件/噬菌体数据/公共数据/工具对比/vHULK/external_key_gene_roc_new.csv', header = 0)


'''
prob = [MLPg['prob'].values.tolist(), MLPr['pred'].values.tolist(), RFg['prob'].values.tolist(), RFr['pred'].values.tolist(),
       predphi['pred'].values.tolist(), deephost['score'].values.tolist(), wish['pred'].values.tolist(), vhm['score'].values.tolist(),
       php['pred'].values.tolist(), vhulk['pred'].values.tolist()]
trues = [MLPg['label'].values.tolist(), MLPr['label'].values.tolist(), RFg['label'].values.tolist(), RFr['label'].values.tolist(),
       predphi['label'].values.tolist(), deephost['label'].values.tolist(), wish['label'].values.tolist(), vhm['label'].values.tolist(),
       php['label'].values.tolist(), vhulk['label'].values.tolist()]
sample = ['key_gene_MLP', 'RBP_MLP', 'key_gene_RF', 'RBP_RF', 'PredPHI', 'DeepHost', 'WIsH', 'VirHostMatcher', 'PHP', 'vHULK']
'''
prob = [RFr['prob'].values.tolist(),
       predphi['pred'].values.tolist(), deephost['pred'].values.tolist(), wish['pred'].values.tolist(), vhm['pred'].values.tolist(),
       php['pred'].values.tolist(), vhulk['pred'].values.tolist()]
trues = [RFr['label'].values.tolist(),
       predphi['label'].values.tolist(), deephost['label'].values.tolist(), wish['label'].values.tolist(), vhm['label'].values.tolist(),
       php['label'].values.tolist(), vhulk['label'].values.tolist()]
sample = ['KGDeepPBI', 'PredPHI', 'DeepHost', 'WIsH', 'VirHostMatcher', 'PHP', 'vHULK']

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score
import csv
import sys
import numpy as np
from matplotlib import rcParams
fig = plt.figure(figsize = (6, 4))
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
rcParams['pdf.fonttype'] = 42 
rcParams['ps.fonttype'] = 42 

def ro_curve(num, y_pred, y_label, figure_file, method_name):
    '''
        y_pred is a list of length n.  (0,1)
        y_label is a list of same length. 0/1
        https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#sphx-glr-auto-examples-model-selection-plot-roc-py  
    '''
    y_label = np.array(y_label)
    y_pred = np.array(y_pred)    
    fpr = dict()
    tpr = dict() 
    roc_auc = dict()
    fpr[0], tpr[0], _ = roc_curve(y_label, y_pred)
    roc_auc[0] = auc(fpr[0], tpr[0])
    lw = 0.8
    if num <= 0:
        plt.plot(fpr[0], tpr[0],
             lw=lw, label= method_name + ' (AUC = %0.4f)' % roc_auc[0])
    else:
        plt.plot(fpr[0], tpr[0],
             lw=lw, linestyle = '--', label= method_name + ' (AUC = %0.4f)' % roc_auc[0])        
    plt.plot([0, 1], [0, 1], color='gainsboro', lw=1, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    # plt.xticks(font="Times New Roman",size=18,weight="bold")
    # plt.yticks(font="Times New Roman",size=18,weight="bold")
    fontsize = 4
    plt.xlabel('False Positive Rate', fontsize = '13.5')
    plt.ylabel('True Positive Rate', fontsize = '13.5')
    #plt.title('KP_train', fontdict={'weight':'normal','size': 20})
    #plt.title('Receiver Operating Characteristic Curve', fontsize = fontsize)
    plt.legend(loc="lower right", fontsize = '11.2')
    plt.savefig(figure_file + ".pdf")
    return 

def col_pic():
    plt.figure(figsize=(6, 6), dpi=400)
    for i in [0, 2, 6, 4, 5, 3, 1]:
        #ro_curve(i, prob[i],trues[i],"D:/我的文件/噬菌体数据/公共数据/工具对比/My-result/工具比对AUC",sample[i])
        ro_curve(i, prob[i],trues[i],"C:/Users/未同庆/Desktop/工具比对AUC.pdf",sample[i])
col_pic()

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score, precision_recall_curve
import csv
import sys
import numpy as np
from matplotlib import rcParams
fig = plt.figure(figsize = (6, 4))
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
rcParams['pdf.fonttype'] = 42 
rcParams['ps.fonttype'] = 42 

def ro_curve(num, y_pred, y_label, figure_file, method_name):
    '''
        y_pred is a list of length n.  (0,1)
        y_label is a list of same length. 0/1
        https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#sphx-glr-auto-examples-model-selection-plot-roc-py  
    '''
    y_label = np.array(y_label)
    y_pred = np.array(y_pred)    
    precision, recall, _thresholds = precision_recall_curve(y_label, y_pred)
    roc_auc= auc(recall, precision)
    lw = 0.8
    if num <= 0:
        plt.plot(recall, precision,
             lw=lw, label= method_name + ' (AUPR = %0.4f)' % roc_auc)
    else:
        plt.plot(recall, precision,
             lw=lw, linestyle = '--', label= method_name + ' (AUPR = %0.4f)' % roc_auc)   
    #plt.plot([1, 0], [0, 1], color='gainsboro', lw=1, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    # plt.xticks(font="Times New Roman",size=18,weight="bold")
    # plt.yticks(font="Times New Roman",size=18,weight="bold")
    fontsize = 14
    plt.xlabel('Recall', fontsize = '13.5')
    plt.ylabel('Precision', fontsize = '13.5')
    #plt.title('KP_train', fontdict={'weight':'normal','size': 20})
    #plt.title('Receiver Operating Characteristic Curve', fontsize = fontsize)
    plt.legend(loc="lower left", fontsize = '11.2')
    plt.savefig(figure_file + ".pdf")
    return 

def col_pic():
    plt.figure(figsize=(6, 6), dpi=400)
    for i in [6, 2, 4, 0, 5, 3, 1]:
        #ro_curve(i, prob[i],trues[i],"D:/我的文件/噬菌体数据/公共数据/工具对比/My-result/工具比对AUPR",sample[i])
        ro_curve(i, prob[i],trues[i],"C:/Users/未同庆/Desktop/工具比对AUPR",sample[i])
col_pic()

