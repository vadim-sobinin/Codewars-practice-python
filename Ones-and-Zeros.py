# 7 kyu Ones and Zeros

def binary_array_to_number(arr):
    a = str()
    for i in arr:
        a += str(i)
    return int(a, 2)