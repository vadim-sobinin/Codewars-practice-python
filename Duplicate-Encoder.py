# 6 kyu Duplicate Encoder

def duplicate_encode(word):
    
    newlst = ["(" if word.lower().count(i.lower()) == 1 else ")" for i in word]
        
    return "".join(newlst)