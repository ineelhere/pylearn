import array as arr
a=arr.array('d', [11,22,44,55,33,77,66,99,2345,1122,34])
print(f"a.pop(1) takes the index of the element in the array and prints the array element that has been removed - {a.pop(1)}")
print(f"The array now - {a}")
print(f"a.pop(9) prints the array element that has been removed - {a.pop(9)}")
print(f"The array now - {a}")
print(f"a.remove(77) does not print the array element that has been removed but actually removes that element mentioned - {a.remove(77)}")
print(f"The array after using a.remove(77) - {a}")
