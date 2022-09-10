# 7 kyu Descending Order

def descending_order(num):
    num = str(num)
    num = sorted(num, reverse = True)
    return int("".join(num))