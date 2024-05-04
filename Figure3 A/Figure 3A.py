#  KP
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib import rcParams


rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
rcParams['pdf.fonttype'] = 42 
rcParams['ps.fonttype'] = 42 
plt.rc('font', family = 'Arial')
#mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.arange(6)
y = [0.89, 0.90, 0.89, 0.89, 0.93, 0.90]
y1 = [0.83, 0.84, 0.83, 0.83, 0.87, 0.82]
#y = [0.61, 0.67, 0.66, 0.66]
#y1 = [0.68, 0.81, 0.75, 0.76]

#y = [0.85, 0.66, 0.72, 0.72]
#y1 = [0.94, 0.80, 0.81, 0.82]

bar_width = 0.35
tick_label = ['accuracy', 'precision', 'recall', 'F1', 'AUC', 'AUPR']

plt.figure(figsize =(10, 6))
plt.bar(x, y, bar_width, color = 'darkturquoise', align = 'center', label = 'Kmeans', alpha = 0.5)
plt.bar(x + bar_width, y1, bar_width, color = 'blue', align = 'center', label = 'Random', alpha = 0.5)
for a, b, c in zip(x, y, y1):
    plt.text(a, b, b, ha='center', va= 'bottom', fontsize=14)
    plt.text(a + bar_width, c, c, ha='center', va= 'bottom', fontsize=14)
#plt.xlabel('feature')
#plt.ylabel('percent')
plt.title('KGDeepPBI Model Performance', fontsize = 18)
#plt.title('SVM', fontsize = 18)
#plt.title('MLP', fontsize = 18)
plt.xticks(x + bar_width / 2, tick_label, fontsize = 15)
plt.yticks(fontsize = 15)
plt.ylim(0.5, 1.03)
plt.legend(loc = 'upper right', prop = {'size':15})
#plt.show()
plt.savefig('C:/Users/未同庆/Desktop/Model_performance.pdf', dpi = 400)
#plt.savefig('C:/Users/未同庆/Desktop/SVM.pdf', dpi = 400)
#plt.savefig('C:/Users/未同庆/Desktop/MLP.pdf', dpi = 400)