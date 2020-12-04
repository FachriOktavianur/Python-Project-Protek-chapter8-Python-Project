buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
a = []
b = []
c = []
i = 0
for x,v in buah.items() :
    d = "%s %d" % (x,v)
    a.append(x)
    b.append(v)

masukan = input("Nama buah yan dibeli :")
kg = int(input("Berapa kg : "))
total = b[i] * kg
c.append(total)
option = input("beli buah yang lain (y/n) ? ")

while option != 'n' :
    i += 1  
    if option == 'y':
        masukan = input("Nama buah yan dibeli :")
        kg = int(input("Berapa kg : "))
        total = b[i] * kg
        c.append(total)
    elif masukan not in a[i] :
            print("data buah tidak ada")
    option = input("beli buah yang lain (y/n) ? ")
else :
    print("------------------------")
    print("Total harga  : ",sum(c))
