library(ggtree)
library(ggnewscale)
library(ggplot2)
library(tidyverse)
library(ape)
library(treeio)
library(ggtreeExtra)
phyfile <- system.file('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data', 'Mycobacterium_phage.phy', package='ggtree')
phylip <- read.tree('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/Mycobacterium_phage_cut.phy')
ggtree(phylip, branch.length = '0.01', layout = 'circular', linetype=1, size = 0.01, ladderize=F)
ggtree(phylip) + geom_tiplab(aes(size=branch.length), offset=0.5) + scale_size_continuous(range = c(0,0.1),guide='none')

distance <- read.csv('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/distance_matrix_cutree.csv',header = T,row.names = NULL)
distance <- distance[,-1]
name <- colnames(distance)
distance <- as.numeric(unlist(distance))
distance <- matrix(distance, nrow = 143, byrow=TRUE)
hc <- hclust(as.dist(distance_matrix), method='complete')
cut <- cutree(hc, h = 0.2)
plot(hc, hang = -1)
rect.hclust(hc, k = 243)


write.csv(cut,"D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/cut.csv",row.names =FALSE)
write.tree(as.phylo(hc), file = 'D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/Mycobacterium_phage_cut_order.phy')
ggtree(ape::as.phylo(hc), linetype='dashed', color='#487AA1', layout = 'fan')

for (i in 1:143) {
  name_[i] <- name[hc$order[i]]
}
hc$labels <- name_

for (i in 1:143) {
   if (substring(name[i],1,1) == 'X') {
      name[i] <- substring(name[i], 2, )
   }
}

for (i in 1:143) {
   name[i] <- strsplit(name[i], ".", fixed = T)[[1]][1]
}
name_ <- name

tree <- ggtree(phylip, branch.length = 'none', layout = 'circular', size = 0.1) + 
  geom_strip(taxa1 = "175",
             taxa2 = "NC_023607",
             offset = 2.7,
             barsize = 11,
             extend = 0.5,
             color="#A6CEE3",
             label = "Group1",
             offset.text = 4,
             fontsize = 1.5) + 
  geom_strip(taxa1 = "NC_031080",
             taxa2 = "MG099948",
             offset = 2.7,
             barsize = 11,
             extend = 0.5,
             color="#b2df8a",
             label = "Group2",
             offset.text = 7,
             fontsize = 1.5) +
  geom_strip(taxa1 = "75",
             taxa2 = "NC_031253",
             offset = 2.7,
             barsize = 11,
             extend = 0.5,
             color="#cab2d6",
             label = "Group4",
             offset.text = 4,
             fontsize = 1.5) + 
  geom_strip(taxa1 = "MH834613",
             taxa2 = "NC_023738",
             offset = 2.7,
             barsize = 11,
             extend = 0.5,
             color="#fdbf6f",
             label = "Group3",
             offset.text = 7,
             fontsize = 1.5)  + geom_tiplab(size=1, linesize = 0.2, align=T, offset = 1) + 
  theme(text = element_text(family = "Arial")) 
  #geom_tiplab(size=1, align=T, offset = 2) + 
  #theme(text = element_text(family = "Arial"))
tree
pdf("C:/Users/未同庆/Desktop/ggtree.pdf",width = 8.27 / 2,height = 11.69 / 2)
tree
dev.off()