# 7 kyu Credit Card Mask

# return masked string
def maskify(cc):
    return "#" * (len(cc) - 4) + cc[-4:]