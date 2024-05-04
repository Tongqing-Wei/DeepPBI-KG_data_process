## G0富集分析
library(clusterProfiler)
library(patchwork)
DEGfile <- read.csv('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/my_degs.csv',header = T,row.names = NULL)
genes <- as.vector(DEGfile$gene_id)
go_anno <- read.csv("D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/go_annotation.txt",header = T,sep = "\t",row.names = NULL)
go2gene <- go_anno[, c(2, 1)]
go2name <- go_anno[, c(2, 3)]
ego <- enricher(genes, TERM2GENE = go2gene, TERM2NAME = go2name)
write.csv(ego@result,"D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/enrich.csv",row.names =FALSE)
#write.csv(go_anno, "C:/Users/未同庆/Desktop/go.txt",sep='\t',row.names =FALSE)
b <- dotplot(ego, showCategory = 15 ,title = "dotplot for enricher")
pdf("C:/Users/未同庆/Desktop/barplot.pdf",width = 12,height = 8)
b
dev.off()

##GO barplot
GOO <- read.csv("D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/enrich.csv")
GOO$gene <- gsub("^.*/","",GOO$GeneRatio)
GOO$gene <- as.numeric(GOO$gene)
GOO$Percentage <- GOO$Count/GOO$gene
GO_table <- GOO[,c(1,2,10,9,12,3,4,8,5,6,7)]
GO_col_name <- c("GO_ID","GO_term","GO_category","Num_of_symbols_in_list_in_GO","Percentage_of_symbols_in_list","GeneRatio","BgRatio","Symbols_in_list","pvalue","p.adjust","qvalue")
names(GO_table) <- GO_col_name
GO_table <- arrange(GO_table, GO_category, pvalue)
#write.csv(GO_table,file="table_human_6s_case_vs_con_FC1_GO_enrichment.csv",row.names = F)

#鍒朵綔鐢诲浘鏂囦欢
GO_BP <- GO_table[GO_table$GO_category=="biological_process",]
GO_CC <- GO_table[GO_table$GO_category=="cellular_component",]
GO_MF <- GO_table[GO_table$GO_category=="molecular_function",]
GO_BP_top10 <- GO_BP[1:10,]
GO_CC_top10 <- GO_CC[1:10,]
GO_MF_top10 <- GO_MF[1:10,]
go_draw <- rbind(GO_BP_top10,GO_CC_top10,GO_MF_top10)
go_draw$p <- -log(go_draw$pvalue,base = 10)

go_draw$GO_term <- factor(go_draw$GO_term,levels = go_draw$GO_term)
library(ggplot2)
###GO barplot
p2 <- ggplot(go_draw,aes(x=GO_term,y=p,fill=GO_category, order=GO_category))+
  geom_bar(stat = 'identity')+coord_flip()+
  scale_fill_manual(values = c('#FF6666','#33CC33','#3399FF'),limits = c('molecular_function','cellular_component','biological_process'),labels = c('molecular_function','cellular_component','biological_process'))+
  theme_bw()+theme(axis.text.x = element_text(size = 15), axis.text.y  = element_text(size = 15))+
  ylab("-log10pvalue") + theme(axis.title.y  = element_text(size = 15))+
  xlab("GO_Term") + theme(axis.title.x = element_text(size = 15)) + 
  labs(title='The Most Enriched GO Terms') + theme(plot.title = element_text(size = 15))  + 
  theme_bw() + theme_classic() + theme(panel.border = element_rect(fill=NA,color="black", size=0.5, linetype="solid"))
p2

p2 <- p2 + theme(axis.text.x=element_text(size = 12), axis.text.y=element_text(size = 12))
p2
#x3 <- x3 + theme(axis.line = element_line(size = 1.2), axis.ticks = element_line(size=1.2), axis.ticks.length = unit(0.1,'cm'))
#x3 <- x3 + theme(legend.text = element_text(size=17), legend.title = element_text(size=17))
pdf("D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/barplot_host_GO_0.00004.pdf",width = 12,height = 8)
p2
dev.off()


go_draw$GO_category <- factor(go_draw$GO_category, levels = c( "molecular_function","cellular_component","biological_process"))
##GO dotplot
go_dotplot=ggplot(go_draw,aes(p, GO_term))
d1 <- go_dotplot+geom_point(aes(size=Num_of_symbols_in_list_in_GO,shape = GO_category,color=p))
d2 <- d1+labs(color=expression(-log10pvalue),size="gene_number",x="-log10pvalue",y="GO_Term")
d3 <- d2 + labs(title='GO enrichment of test Genes') + theme(plot.title = element_text(size = 15))
d4 <- d3 + scale_color_gradient(high = "#FF00AAFF", low = "green")
d5 <- d4 + theme(panel.border = element_rect(fill=NA,color="black", size=1, linetype="solid"))
d6 <- d5 + theme_bw() + theme(axis.text.x = element_text(size = 12),
                              axis.text.y  = element_text(size = 12))
d6
pdf("D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/dotplot_host_GO_0.00004.pdf",width = 12,height = 8)
d6
dev.off()

##KEGG富集分析
library(clusterProfiler)
DEGfile <- read.csv('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/my_degs_kegg.csv',header = T,row.names = NULL)
genes <- as.vector(DEGfile$gene_id)
go_anno <- read.csv("D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/kegg_annotation.txt",header = T,sep = "\t",row.names = NULL)
go2gene <- go_anno[, c(2, 1)]
go2name <- go_anno[, c(2, 3)]
ego <- enricher(genes, TERM2GENE = go2gene, TERM2NAME = go2name)
write.csv(ego@result,"D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/enrich_kegg.csv",row.names =FALSE)
ego@result

library(ggplot2)
KEGG <- read.csv("D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/enrich_kegg.csv")
KEGG$gene <- gsub("^.*/","",KEGG$GeneRatio)
KEGG$gene <- as.numeric(KEGG$gene)
KEGG$Percentage <- KEGG$Count/KEGG$gene
KEGG_table <- KEGG[,c(1,2,9,11,3,4,8,5,6,7)]
KEGG_col_name <- c("ID","Path_term","Num_of_symbols_in_list_in_KEGG","Percentage_of_symbols_in_list","GeneRatio","BgRatio","Symbols_in_list","pvalue","p.adjust","qvalue")
names(KEGG_table) <- KEGG_col_name
KEGG_table <- arrange(KEGG_table, pvalue)
kegg_draw <- KEGG_table

#鍒朵綔鐢诲浘鏂囦欢
KEGG_part <- KEGG_table[KEGG_table$pvalue<0.99,]
if (nrow(KEGG_part) < 30){kegg_draw <- KEGG_part} else {kegg_draw <- KEGG_part[1:30,]}
kegg_draw$p <- -log(kegg_draw$pvalue,base = 10)
##KEGG barplot 
order <- sort(kegg_draw$p,index.return=TRUE,decreasing = TRUE)
kegg_draw$Path_term <- factor(kegg_draw$Path_term, levels = kegg_draw$Path_term[order$ix])
x2 <- ggplot(data=kegg_draw,aes(x=Path_term,y=p))
x2 <- x2 + geom_bar(stat = "identity",fill="#ff7575")+coord_flip() + ylab("-log10pvalue") + theme(axis.title.y  = element_text(size = 20))
x2 <- x2 + theme_classic() + theme(panel.border = element_rect(fill=NA,color="black", size=0.5, linetype="solid"))
x2 <- x2 + labs(title='The Most Enriched KEGG Terms') + theme(plot.title = element_text(size = 15))
x2 <- x2 + theme(axis.text.x=element_text(size = 12), axis.text.y=element_text(size = 12))
#x2 <- x2 + theme(axis.line = element_line(size = 1.2), axis.ticks = element_line(size=1.2), axis.ticks.length = unit(0.1,'cm'))
#x2 <- x2 + theme(legend.text = element_text(size=17), legend.title = element_text(size=17))
x2
pdf("D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/barplot_host_KEGG_0.00004.pdf",width = 12,height = 8)
x2
dev.off()
##KEGG dotplot
kegg_dotplot=ggplot(kegg_draw,aes(p, Path_term))
y1 <- kegg_dotplot+geom_point(aes(size=Num_of_symbols_in_list_in_KEGG,color=p))
y2 <- y1 + labs(color=expression(-log10pvalue),size="gene_number",x="-log10pvalue",y="pathway")
y3 <- y2 + labs(title='KEGG enrichment of test Genes') + theme(plot.title = element_text(size = 15))
y4 <- y3 + scale_color_gradient(high = "#FF00AAFF", low = "green")
y5 <- y4 + theme(panel.border = element_rect(fill=NA,color="black", size=1, linetype="solid"))
y6 <- y5 + theme_bw()
y6 <- y6 + theme(axis.text.x=element_text(size = 12), axis.text.y=element_text(size = 12))
y6
#y5 <- y4 + theme(axis.title = element_text(size = 22), axis.text.x=element_text(size = 20), axis.text.y=element_text(size = 19))
#y6 <- y5 + theme(axis.line = element_line(size = 1.2), axis.ticks = element_line(size=1.2), axis.ticks.length = unit(0.1,'cm'))
#y7 <- y6 + theme(legend.text = element_text(size=17), legend.title = element_text(size=17))
pdf("D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/dotplot_host_KEGG_0.00004.pdf",width = 12,height = 8)
y6
dev.off()


# GSEA
library(data.table)
library(clusterProfiler)
library(dplyr)
library(ggplot2)
library(enrichplot)
library(org.Hs.eg.db)
all <- read.gmt('D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/rbp_host_gsea.gmt')
genelist <- read.csv("D:/我的文件/噬菌体数据/公共数据/Pipeline/raw_Data/富集分析/host_key_gene_importance.csv")
genefc<-genelist$importance
names(genefc)<-genelist$gene
genefc<-sort(genefc,decreasing = T)
#gene <- genelist[,2]
#rownames(genelist) <- genelist[,1]
#genelist <- genelist[,-1]
gsea <- GSEA(genefc, TERM2GENE = all, pvalueCutoff = 1, pAdjustMethod = 'BH', scoreType = 'pos')
x <- gseaplot2(gsea, geneSetID = 'gene', pvalue_table = TRUE)+ labs(title='host gene GSEA', hjust = 0.5) + theme(plot.title = element_text(hjust = 0.5, vjust = 100, size = 16))
pdf("C:/Users/未同庆/Desktop/gsea_host_gene.pdf",width = 12,height = 8)
x
dev.off()
gseaplot(gsea, geneSetID = 'gene', pvalue_table = TRUE)+ labs(title='host gene GSEA', hjust = 0.5) + theme(plot.title = element_text(hjust = 0.5, vjust = 100, size = 16))
ids <- gsea@result$ID[1]
gseadist(gsea, IDs = ids, type = 'density')
gsearank(gsea, geneSetID = 1)
