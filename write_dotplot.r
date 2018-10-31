#file = commandArgs(trailingOnly=TRUE)[1]
ylabel = "Tbx5 RNA expression level"
file = "C:/Users/Yutaro/Dropbox/paper/revision3/thickness.txt"
df <- read.table(file=file, header=T, fileEncoding="utf-8",sep="\t")
library(ggplot2)
print(df)
means <- aggregate(x=df['value'], by=list(df$category), FUN=mean)
standard <- means$value[1]
#specify control category
means$value <- means$value / standard
df$value <- df$value / standard
p <- ggplot(df, aes(x=category, y=value)) + stat_summary(fun.data=mean_se, fun.args=list(mult=1), geom="errorbar", color="black", width=0.2) + geom_bar(stat="summary", fun.y="mean", width=0.4, colour="black", fill="white") +  geom_dotplot(binaxis='y', dotsize=0.8, stackdir='center') + coord_fixed(ylim=c(0, 1.3), ratio=1.5, expand=FALSE) + theme_classic(base_size = 20, base_family="Helvetica") + theme(axis.title.y=element_text(size=15), axis.title.x=element_blank(), axis.text.x = element_text(color="black"), axis.ticks.x=element_line(color="black") ,axis.text.y = element_text(color="black"), axis.ticks.y=element_line(color="black")) + labs(y=ylabel) + scale_x_discrete(limits=unique(df$category))
ggsave(file="C:/Users/Yutaro/Dropbox/paper/revision3/thickness.svg", plot=p)
