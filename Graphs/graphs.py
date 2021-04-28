import numpy as np
from matplotlib import pyplot as plt
width = 0.20



#For inserting the records

x1 = [100,1000,5000,10000]
y1 = [0.016,0.021,0.144,0.277]
x2 = [100,1000,5000,10000]
y2 = [0.13,0.60,3.07,4.36]
x_indexes = np.arange(len(x1))  
plt.title("Inserting Records")
plt.xlabel("No. of Records")
plt.ylabel("Time Taken (in seconds)")
plt.style.use("dark_background")  
plt.bar(x_indexes-width,y1,width=width,color="#5acd34",linewidth=2,label="MongoDB")  
plt.bar(x_indexes,y2,width=width,color="#aa1d32",linewidth=2,label="MySQL")
plt.xticks(ticks=x_indexes,labels=x1)  
plt.legend() 
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#For Selecting the records

x1 = [100,1000,5000,10000]
y1 = [0.0,0.0,0.002,0.011]
x2 = [100,1000,5000,10000]
y2 = [0.0,0.0,0.01,0.01]
x_indexes = np.arange(len(x1))  
plt.title("Selecting Records")
plt.xlabel("No. of Records")
plt.ylabel("Time Taken (in seconds)")
plt.style.use("dark_background")  
plt.bar(x_indexes-width,y1,width=width,color="#5acd34",linewidth=2,label="MongoDB")  
plt.bar(x_indexes,y2,width=width,color="#aa1d32",linewidth=2,label="MySQL")
plt.xticks(ticks=x_indexes,labels=x1)  
plt.legend() 
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#For updating the records

x1 = [100,1000,5000,10000]
y1 = [0.003,0.024,0.136,0.319]
x2 = [100,1000,5000,10000]
y2 = [0.10,0.16,0.23,1.40]
x_indexes = np.arange(len(x1))  
plt.title("Updating Records")
plt.xlabel("No. of Records")
plt.ylabel("Time Taken (in seconds)")
plt.style.use("dark_background")  
plt.bar(x_indexes-width,y1,width=width,color="#5acd34",linewidth=2,label="MongoDB")  
plt.bar(x_indexes,y2,width=width,color="#aa1d32",linewidth=2,label="MySQL")
plt.xticks(ticks=x_indexes,labels=x1)  
plt.legend() 
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------------
