a = ["Bayam", "Kangkung", "Wortel", "Selada"]
print("""
        MENU :
        A.  Tambah data Sayur
        B.  Hapus data Sayur
        C.  Tampilkan data Sayur""")

masukan = input("Pilihan Anda:")
while masukan != 'C' :
    if masukan == 'A' :
        input_sayur = input("Masukkan nama sayur yang akan ditambahkan :")
        if input_sayur in a :
            print("data sudah ada")
        else :
            a.append(input_sayur)
    elif masukan == 'B' :
        hapus_sayur = input("Masukkan nama sayur yang akan dihapus :")
        if hapus_sayur not in a :
            print("data tidak ditemukan")
        else :
            a.remove(hapus_sayur)
    masukan = input("Pilihan Anda:")
else :
    if masukan == 'C' :
        print(a)

