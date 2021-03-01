data = [34,54,11,42,12,1,78,997,32234,54531,3344,43,78,97,11] #example data
for i in range(1, len(data)):
    a = data[i]
    j = i
    while j>0 and data[j-1]>a:
        data[j]=data[j-1]
        j=j-1
    data[j]=a
data        
