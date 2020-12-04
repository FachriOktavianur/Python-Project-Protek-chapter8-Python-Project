nama_buah = []
harga_buah = []
def buahMahal(buah) :
    for x,v in buah.items() :
        d = "%s : %d" % (x,v)
        nama_buah.append(x)
        harga_buah.append(v)
    nilai_max = max(harga_buah)
    i = 0
    while i != len(harga_buah) :
        list_harga = [harga_buah[i]]
        if nilai_max in list_harga :
            print(nama_buah[i])
        i += 1
    return d

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
buahMahal(buah)
