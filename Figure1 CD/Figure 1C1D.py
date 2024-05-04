import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rcParams

plt.figure(figsize = (16,8))
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42
#mpl.rcParams["font.sans-serif"] = ["SimHei"]
plt.rc('font', family = 'Arial')
mpl.rcParams['axes.unicode_minus'] = False

labels = ["Mycolicibacterium smegmatis MKD8 ... (1337)", 'Others (1407)', 'Streptomyces griseus subsp.... (59)', 
          "Salmonella enterica subsp. diarizonae (65)", "Propionibacterium acnes 6609 (67)", "Microbacterium foliorum strain 122 ...(84)",     
          "Staphylococcus aureus strain NMR08 ... (85)", "Escherichia coli CFT073 (90)", "Pseudomonas aeruginosa PA38182 (106)", 
          "Arthrobacter sp. NHB-10 myd gene ... (161)",  "Gordonia terrae strain NRRL ... (186)"]
    
values = [1337 / 3647,  1407 / 3647, 59 / 3647, 65 / 3647, 67 / 3647, 84 / 3647, 85 / 3647, 90 / 3647, 
          106 / 3647, 161 / 3647, 186 / 3647]
#colors = ['silver', 'mistyrose', 'peachpuff', 'cornsilk', 'gold', 'palegreen', 'aquamarine', 'lightskyblue', 'lavender', 
#          'thistle', 'pink']
colors = ['#8dd3c7', 'gainsboro', '#bc80bd', '#ccebc5', '#fccde5', '#b3de69', '#fdb462', '#80b1d3', '#fb8072', '#bebada', '#ffffb3']

plt.pie(values, labels = labels, autopct = "%3.1f%%", startangle = 20, pctdistance = 0.8, textprops = {'fontsize': 14}
        , labeldistance = 1.1, colors = colors)
plt.title("Host", fontsize = 18)
plt.savefig('C:\\Users\\admin\\Desktop\\扇形.pdf', dpi = 400)
plt.show()


import matplotlib as mpl
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from matplotlib import rcParams

grid = gridspec.GridSpec(1, 4)
fig = plt.figure(figsize = (16, 9))

plt.rc('font', family = 'Arial')
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42
mpl.rcParams['axes.unicode_minus'] = False

ax1 = fig.add_subplot(grid[0,0])
labels1 = ['top phage (68)', 'Others (3579)']
values1 = [68 / 3647, 3579 / 3647]
colors1 = ['thistle', 'gainsboro']
ax1.pie(values1, labels = labels1, autopct = "%3.1f%%", startangle = 20, pctdistance = 0.6, textprops = {'fontsize': 15}
        , labeldistance = 1.1, colors = colors1)
ax1.annotate('', xy=(1, 0.35), xytext = (2.8, -0.2), arrowprops = dict(arrowstyle = '<-', color = 'black'))

ax2 = fig.add_subplot(grid[0, 1:])
labels = ["Clostridium phage phiCD6356 (11)", "Clostridium phage phiMMP02 (10)", "Clostridium phage phiMMP04 (9)", "Clostridium phage phiCD38-2 (8)",
         "Listeria phage B025 (6)", "Enterobacteria phage Fels-2 (5)", "Streptococcus pyogenes phage 315.3 (5)", "Streptococcus prophage 315.5 (5)", 
          "Geobacillus phage GBSV1 (5)", 'Streptococcus prophage 315.1 (4)']
    
#values = [11 / 68 , 10 / 68, 9 / 68, 8 / 68, 6 / 68, 5 / 68, 5 / 68, 5 / 68, 5 / 68, 4 / 68]
values = [11, 10, 9, 8, 6, 5, 5, 5, 5, 4]
#colors = ['silver', 'mistyrose', 'peachpuff', 'cornsilk', 'gold', 'palegreen', 'aquamarine', 'lightskyblue', 'lavender', 
#          'thistle', 'pink']
colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd']

ax2.pie(values, labels = labels, autopct = "%3.1f%%", startangle = 20, pctdistance = 0.8, textprops = {'fontsize': 14}
        , labeldistance = 1.1, colors = colors)
plt.title("Phage", fontsize = 18)
plt.savefig('C:\\Users\\admin\\Desktop\\phage扇形.pdf', dpi = 400)
plt.show()