z = []
def dataStat(x) :
    a = sum(x) / len(x)
    b = max(x)
    c = min(x)
    z.append(a)
    z.append(b)
    z.append(c)
    return a,b,c
print(dataStat(x=[4,5,6,12,14]))

