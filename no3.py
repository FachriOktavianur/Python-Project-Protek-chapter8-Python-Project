n = 4
m = 0
a = []
b = []
while m != n :
    masukan = input("Masukkan nama :")
    c = len(masukan)
    a.append(masukan)
    b.append(c)
    m += 1
else :
    q = 0
    a.sort()
    for x in a :
        print(x,"(",b[q],"karakter",")")
        q += 1
