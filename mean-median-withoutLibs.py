import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/ineelhere/pylearn/master/RGTE11_dataset/2010_RGTE11.csv", encoding="unicode_escape") #import the data
length = len(df["Popn_2010"])
sum = 0
for i in range(0,len(df["Popn_2010"])):
    sum = sum + df["Popn_2010"][i]
print(f"Mean = {sum/length}")
data=df["Popn_2010"].values.tolist()
data.sort() #this could have been done manually, for example - bubble sort
if length % 2 == 0: 
    res1 = data[int(length/2)] #list indices must be integers or slices, not float
    res2 = data[int(length/2 - 1)] 
    median = (res1 + res2)/2
else: 
    median = data[int(length/2)] 
print(f"Median = {median}")
