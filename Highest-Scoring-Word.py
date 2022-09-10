# 6 kyu Highest Scoring Word

def high(x):
    
    lst = x.split()
    sum = [0 for i in range(len(lst))]
    for word_indx in range(len(lst)):
        for letter in lst[word_indx]:
            sum[word_indx] += ord(letter) % 96 #ord(a) = 97, 97 % 96 = 1...
    return lst[sum.index(max(sum))]