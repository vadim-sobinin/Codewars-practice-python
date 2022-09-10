# 6 kyu Persistent Bugger

def persistence(n):
    count = 0
    
    while len(str(n)) > 1:
        
        lst = [int(x) for x in str(n)]
        n = 1
        for i in lst:
            n *= i
        count += 1
        print(n)
    
    return count