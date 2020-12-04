buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

masukan = input("Nama buah yan dibeli :")
a = []
b = []
i = 0
for x,v in buah.items() :
    d = "%s %d" % (x,v)
    a.append(x)
    b.append(v)
while i != len(b) :  
    if masukan in a[i]:
        kg = int(input("Berapa kg : "))
        total = b[i] * kg
        print("Total harga : ", total)
    else :
        break
    i += 1
