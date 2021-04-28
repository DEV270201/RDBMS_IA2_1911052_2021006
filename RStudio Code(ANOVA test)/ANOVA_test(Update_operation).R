#Analysis of Variance(ANOVA)

mysql <- c(0.10,	0.16,	0.23,	1.40)
mongodb <- c(0.003,	0.024,	0.136,	0.319)

#combines data into a single data set.
Combined_grps <- data.frame(cbind(mysql,mongodb))
Combined_grps # shows spreadsheet like results

Stacked_grps <- stack(Combined_grps)
Stacked_grps  # shows the table Stacked_grps

Anova_results <- aov(values~ind,data = Stacked_grps)
summary(Anova_results) # shows Anova_results
#For displaying Graph
# Calculate range from 0 to max value of mysql and mongodb
g_range <- range(0, mysql, mongodb)

# Graph autos using y axis that ranges from 0 to max 
# value in mysql or mongodb vector.  Turn off axes and 
# annotations (axis labels) so we can specify them ourself
plot(mysql, type="o", col="blue", ylim=g_range, axes=FALSE, ann=FALSE)

# Make x axis using 100-10000 labels
axis(1, at=1:4, lab=c("100","1000","5000","10000"))

# Make y axis with horizontal labels that display ticks at 
# every 1 marks. 4*0:g_range[2] is equivalent to c(0,1,2,3).
axis(2, las=1, at=4*0:g_range[2])

# Create box around plot
box()

# Graph mongodb with red dashed line and square points
lines(mongodb, type="o", pch=22, lty=2, col="red")

# Create a title with a red, bold/italic font
title(main="UPDATE OPERATION", col.main="red", font.main=4)

# Label the x and y axes with dark green text
title(xlab="NUMBER OF RECORDS", col.lab=rgb(0,0.5,0))
title(ylab="EXECUTION TIME IN SECONDS", col.lab=rgb(0,0.5,0))

# Create a legend at (1, g_range[2]) that is slightly smaller  
# and uses the same line colors and points used by 
# the actual plots 
legend(1, g_range[2], c("mysql","mongodb"), cex=0.8, 
       col=c("blue","red"), pch=21:22, lty=1:2)