# 6 kyu Mexican Wave

def wave(people):
    newline = list()
    if people != "":
        for i in range(len(people)):
            
            if people[i] != " ":
                newline.append(people[:i] + people[i].upper() + people[i+1:])
    
    return newline