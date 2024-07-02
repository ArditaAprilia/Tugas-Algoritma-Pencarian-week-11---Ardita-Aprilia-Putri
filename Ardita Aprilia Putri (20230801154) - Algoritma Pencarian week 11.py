buku = [
    {"judul": "Cara Cepat Kaya", "tahun": 2020, "penulis": "Budi ", "stok": 5},
    {"judul": "5 Kebiasaan Mengubah Hidup", "tahun": 2019, "penulis": "Agus", "stok": 2},
    {"judul": "Belajar Python", "tahun": 2019, "penulis": "Bambang", "stok": 3},
    {"judul": "Diet Singkat", "tahun": 2021, "penulis": "Siti", "stok": 4},
    {"judul": "Cara Mengatur Uang", "tahun": 2024, "penulis": "Ardit", "stok": 6},
]

def cari_buku(kata_kunci):
    hasil = []
    for buku_item in buku:
        if kata_kunci.lower() in buku_item["judul"].lower():
            hasil.append(buku_item)
    return hasil

def tampilkan_buku():
    print("\nDaftar Buku:")
    for buku_item in buku:
        print(f"Judul: {buku_item['judul']}, Tahun: {buku_item['tahun']}, Penulis: {buku_item['penulis']}, Stok: {buku_item['stok']}")

def pencarian():
    kata = input("Masukkan judul buku yang ingin dicari: ")
    hasil = cari_buku(kata)
    
    if hasil:
        print("\nHasil pencarian:")
        for buku_item in hasil:
            print(f"Judul: {buku_item['judul']}, Tahun: {buku_item['tahun']}, Penulis: {buku_item['penulis']}, Stok: {buku_item['stok']}")
    else:
        print("\nBuku tidak ditemukan.")

def tambah_buku():
    judul = input("Masukkan judul buku: ")
    tahun = int(input("Masukkan tahun terbit: "))
    penulis = input("Masukkan nama penulis: ")
    stok = int(input("Masukkan jumlah stok: "))
    buku_baru = {"judul": judul, "tahun": tahun, "penulis": penulis, "stok": stok}
    buku.append(buku_baru)
    print(f"\nBuku '{judul}' berhasil ditambahkan.")

def menu():
    while True:
        print("===========================================")
        print("Selamat Datang di Program Pencarian Buku")
        print("===========================================")
        print("| 1. Menampilkan semua buku |")
        print("| 2. Cari buku |")
        print("| 3. Tambah stock buku |")
        print("| 4. Keluar |")
        print("===========================================")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == '1':
            tampilkan_buku()
        elif pilihan == '2':
            pencarian()
        elif pilihan == '3':
            tambah_buku()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

menu()
