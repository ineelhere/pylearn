#-----importing the dataset and creation of list
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/ineelhere/pylearn/master/RGTE11_dataset/2010_RGTE11.csv", encoding="unicode_escape") #import the data
data=list(df["Popn_2010"])
#-----bubble sort
for i in range(0,len(data)):
    for j in range(0,len(data)-1):
        if (data[j]>data[j+1]):
            data[j],data[j+1] = data[j+1],data[j]
print(data)       
