#6 kyu Find The Parity Outlier

def find_outlier(integers):
    odd = [0, 0]
    even = [0, 0]
    for i in integers:
        if i % 2 == 0 :
            even[0] += 1
            even[1] = i
        else:
            odd[0] += 1
            odd[1] = i
    if odd[0] == 1:
        return odd[1]
    else:
        return even[1]