# 6 kyu Your order, please

import re
def order(sentence):
    orders = re.findall(r"\d", sentence)
    words = sentence.split()
    dic = dict(zip(orders,words))
    res = str()
    for i in range(1, len(dic) + 1):
        res = res + dic[str(i)] + " "
    res = res[:-1]

    return res