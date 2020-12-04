a = []
def rataBuah(buah) :
    for x,v in buah.items() :
        d = "%s %d" % (x,v)
        a.append(v)
    rata = sum(a) / len(a)
    print("Rata-Rata harga satuan dari keseluruhan buah adalah :", rata)
    return d,rata

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
rataBuah(buah)

