# 6 kyu Write Number in Expanded Form

def expanded_form(num):
    a = str(num)
    res = str()
    for i in range((len(a))):
        if a[i] != "0":
            res = res + a[i] + "0"*(len(a)-i - 1)
            if (len(a) - i) > 1:
                res += " + "
    if a[len(a) - 1] == "0":
        res = res[:-3]
    return res