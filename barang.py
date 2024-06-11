# Inisialisasi data inventaris
data_inventaris = []

# Fungsi untuk menginput data barang
def input_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    kode_barang = input("Masukkan Kode Barang: ")
    jumlah_barang = int(input("Masukkan Jumlah Barang: "))
    barang = {
        "Nama Barang": nama_barang,
        "Kode Barang": kode_barang,
        "Jumlah Barang": jumlah_barang
    }
    data_inventaris.append(barang)

# Fungsi untuk menampilkan semua barang
def tampilkan_barang():
    for i, barang in enumerate(data_inventaris):
        print(f"Barang ke-{i+1}:")
        print(f"Nama Barang: {barang['Nama Barang']}")
        print(f"Kode Barang: {barang['Kode Barang']}")
        print(f"Jumlah Barang: {barang['Jumlah Barang']}")
        print()

# Fungsi untuk mencari barang berdasarkan kode
def cari_barang(kode):
    for barang in data_inventaris:
        if barang["Kode Barang"] == kode:
            print(f"Barang dengan kode {kode}:")
            print(f"Nama Barang: {barang['Nama Barang']}")
            print(f"Jumlah Barang: {barang['Jumlah Barang']}")
            return
    print(f"Tidak ditemukan barang dengan kode {kode}.")

# Fungsi untuk menghapus barang berdasarkan kode
def hapus_barang(kode):
    for barang in data_inventaris:
        if barang["Kode Barang"] == kode:
            data_inventaris.remove(barang)
            print(f"Barang dengan kode {kode} telah dihapus.")
            return
    print(f"Tidak ditemukan barang dengan kode {kode}.")

# Main program
while True:
    print("\nMenu:")
    print("1. Tambah Barang")
    print("2. Tampilkan Semua Barang")
    print("3. Cari Barang")
    print("4. Hapus Barang")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        input_barang()
    elif pilihan == "2":
        tampilkan_barang()
    elif pilihan == "3":
        kode_cari = input("Masukkan Kode Barang yang ingin dicari: ")
        cari_barang(kode_cari)
    elif pilihan == "4":
        kode_hapus = input("Masukkan Kode Barang yang ingin dihapus: ")
        hapus_barang(kode_hapus)
    elif pilihan == "5":
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.")