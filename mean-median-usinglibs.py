# using the pandas library
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/ineelhere/pylearn/master/RGTE11_dataset/2010_RGTE11.csv", encoding="unicode_escape")
print(df["Popn_2010"].mean()) #mean
print(df["Popn_2010"].median()) #median

#using the statistics library
import statistics
print(statistics.mean(df["Popn_2010"])) #mean
print(statistics.median(df["Popn_2010"])) #median
