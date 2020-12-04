n = 5
m = 0
a = []
while m != n :
    masukan = int(input("Masukkan bilangan bulat :"))
    a.append(masukan)
    m += 1
else :
    pass
a.sort()
a.reverse()
print(a)
