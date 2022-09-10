# 6 kyu Equal Sides Of An Array

def find_even_index(arr):
    
    l = [i for i in range(len(arr)) if sum(arr[(i+1):]) == sum(arr[:i])]
    
    try:
        return l[0]
    except IndexError:
        return -1