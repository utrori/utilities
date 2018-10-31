#file = commandArgs(trailingOnly=TRUE)[1]
ylabel = "Relative RNA expression level"
file = "C:/Users/Yutaro/Dropbox/paper2/figs/Fig2d.txt"
df <- read.table(file=file, header=T, fileEncoding="utf-8",sep="\t")
library(ggplot2)
print(df)
#specify control category
p <- ggplot(df, aes(x=category2, y=value, fill=category)) + stat_summary(fun.data=mean_se, fun.args=list(mult=1), geom="errorbar", width=0.2, position=position_dodge(0.4)) + geom_bar(stat="summary", fun.y=mean, width=0.4, position=position_dodge(0.4)) + scale_fill_manual(values=c("#7f878f", "#c8c8cb")) + geom_dotplot(binaxis='y', dotsize=0.5, stackdir='center', position=position_dodge(0.4)) + coord_fixed(ylim=c(0, 1.5), ratio=1.5, expand=FALSE) + theme_classic(base_size = 20, base_family="Helvetica") + theme(axis.title.y=element_text(size=15), axis.title.x=element_blank(), axis.text.x = element_text(color="black"), axis.ticks.x=element_line(color="black") ,axis.text.y = element_text(color="black"), axis.ticks.y=element_line(color="black")) + labs(y=ylabel) + scale_x_discrete(limits=unique(df$category2))
ggsave(file="C:/Users/Yutaro/Dropbox/paper2/figs/Fig2D.svg", plot=p)
