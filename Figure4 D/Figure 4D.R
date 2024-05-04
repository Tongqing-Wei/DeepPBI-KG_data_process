#带数值标签的棒棒糖图
# 导入ggplot2包
library(ggplot2)

# 示例数据
data <- data.frame(
  Category = c("Mycolicibacterium smegmatis MKD8 chromosome", "Gordonia terrae strain NRRL B-16283 chromosome", 
               "Pseudomonas aeruginosa PA38182", "Escherichia coli CFT073",
               "Staphylococcus aureus strain NMR08 chromosome", "Microbacterium foliorum strain 122 genome",
               "Propionibacterium acnes 6609", "Salmonella enterica subsp. diarizonae serovar",
               "Lactococcus lactis subsp. cremoris IBB477 chromosome", "Rhodococcus erythropolis strain ATCC 15903 DVG80_1"),
  Value = c(0.90, 0.75, 0.98, 0.87, 0.99, 0.91, 0.66, 0.84, 0.99, 0.69),
  color = c("#a6cee3", "#1f78b4", "#b2df8a", "#33a02c", "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00", "#cab2d6", "#b79f00")
)
data$Category = factor(data$Category, levels = c("Mycolicibacterium smegmatis MKD8 chromosome", "Gordonia terrae strain NRRL B-16283 chromosome", 
                                                 "Pseudomonas aeruginosa PA38182", "Escherichia coli CFT073",
                                                 "Staphylococcus aureus strain NMR08 chromosome", "Microbacterium foliorum strain 122 genome",
                                                 "Propionibacterium acnes 6609", "Salmonella enterica subsp. diarizonae serovar",
                                                 "Lactococcus lactis subsp. cremoris IBB477 chromosome", "Rhodococcus erythropolis strain ATCC 15903 DVG80_1"))
data$color = factor(data$color, levels = c("#a6cee3", "#1f78b4", "#b2df8a", "#33a02c", "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00", "#cab2d6", "#b79f00"))
# 创建棒棒糖图
plt <- ggplot(data, aes(x = Category, y = Value, fill=Category)) +
  geom_segment(aes(xend = Category, yend = 0), color = "black", size = 0.5) +
  geom_point(size = 11, color = c("#a6cee3", "#1f78b4", "#b2df8a", "#33a02c", "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00", "#cab2d6", "#b79f00")) + 
  scale_color_manual(values = c('gold','pink')) + 
  geom_text(aes(label = Value), vjust = 0.5) +
  labs(title = "AUC of the different strains", x = "", y = "AUC",) + theme_bw() + 
  guides(color = guide_legend(override.aes = list(fill = data$color))) + 
  theme(panel.border = element_rect(fill=NA,color="black", size=1, linetype="solid")) + theme(legend.position="right") + 
  theme(plot.title = element_text(hjust = 0.5))
pdf("C:/Users/未同庆/Desktop/各菌种AUC_棒棒糖图.pdf",width = 12,height = 8)
plt
dev.off()