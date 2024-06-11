import os

# Inisialisasi data
data_mahasiswa = []
data_inventaris = []
data_transaksi = []

def owner():
    print("=========================================")
    print("Nama         : Ilham Sheva Renggafiarto")
    print("Prodi        : Teknik Informatika")
    print("Mata Kuliah  : Bahasa Pemrograman")
    print("=========================================")
    

# Fungsi untuk menginput data mahasiswa
def input_mahasiswa():
    n = int(input("Masukkan Jumlah Mahasiswa: "))
    for i in range(n):
        print(f"Masukkan data mahasiswa ke-{i+1}")
        Nim = input("Masukkan Nim: ")
        Nama = input("Masukkan Nama: ")
        Prodi = input("Masukkan Prodi: ")
        nilai_absen = float(input("Masukkan Nilai Absen: "))
        nilai_tugas = float(input("Masukkan Nilai Tugas: "))
        nilai_uts = float(input("Masukkan Nilai UTS: "))
        nilai_uas = float(input("Masukkan Nilai UAS: "))
        print()
        mhs = {
            "Nim": Nim,
            "Nama": Nama,
            "Prodi": Prodi,
            "Nilai Absen": nilai_absen,
            "Nilai Tugas": nilai_tugas,
            "Nilai UTS": nilai_uts,
            "Nilai UAS": nilai_uas
        }
        data_mahasiswa.append(mhs)

# Fungsi untuk menampilkan data mahasiswa
def cetak_mahasiswa():
    for i, mhs in enumerate(data_mahasiswa):
        print(f"Mahasiswa ke-{i+1}:")
        print(f"Nim: {mhs['Nim']}")
        print(f"Nama: {mhs['Nama']}")
        print(f"Prodi: {mhs['Prodi']}")
        print(f"Nilai Absen: {mhs['Nilai Absen']}")
        print(f"Nilai Tugas: {mhs['Nilai Tugas']}")
        print(f"Nilai UTS: {mhs['Nilai UTS']}")
        print(f"Nilai UAS: {mhs['Nilai UAS']}")
        print()

# Fungsi untuk menghitung dan menampilkan rata-rata nilai mahasiswa
def rata_rata():
    total_nilai = 0
    total_mahasiswa = len(data_mahasiswa)
    for mhs in data_mahasiswa:
        total_nilai += mhs["Nilai Absen"] + mhs["Nilai Tugas"] + mhs["Nilai UTS"] + mhs["Nilai UAS"]
    rata_rata_nilai = total_nilai / (total_mahasiswa * 4)
    print(f"Nilai rata-rata: {rata_rata_nilai:.2f}")

# Fungsi untuk mencari dan menampilkan mahasiswa dengan nilai tertinggi dan terendah
def nilai_tertinggi_terendah():
    nilai_mahasiswa = [(mhs["Nama"], mhs["Nilai Absen"] + mhs["Nilai Tugas"] + mhs["Nilai UTS"] + mhs["Nilai UAS"]) for mhs in data_mahasiswa]
    nilai_mahasiswa.sort(key=lambda x: x[1])
    print(f"Mahasiswa dengan nilai tertinggi: {nilai_mahasiswa[-1][0]} ({nilai_mahasiswa[-1][1]:.2f})")
    print(f"Mahasiswa dengan nilai terendah: {nilai_mahasiswa[0][0]} ({nilai_mahasiswa[0][1]:.2f})")

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

# Fungsi untuk menginput transaksi
def input_transaksi():
    jenis_transaksi = input("Masukkan Jenis Transaksi (Pemasukan/Pengeluaran): ")
    if jenis_transaksi != "Pemasukan" and  jenis_transaksi != "Pengeluaran":
        print("Jenis transaksi tidak valid. Silakan pilih 'Pemasukan' atau 'Pengeluaran'.")
        return
    nominal = float(input("Masukkan Nominal Transaksi: "))
    transaksi = {
        "Jenis Transaksi": jenis_transaksi,
        "Nominal": nominal
    }
    data_transaksi.append(transaksi)

# Fungsi untuk menampilkan semua transaksi
def tampilkan_transaksi():
    for i, transaksi in enumerate(data_transaksi):
        print(f"Transaksi ke-{i+1}:")
        print(f"Jenis Transaksi: {transaksi['Jenis Transaksi']}")
        print(f"Nominal: {transaksi['Nominal']:.2f}")
        print()

# Fungsi untuk menghitung dan menampilkan total pemasukan
def total_pemasukan():
    total = sum(transaksi['Nominal'] for transaksi in data_transaksi if transaksi['Jenis Transaksi'] == 'Pemasukan')
    print(f"Total Pemasukan: {total:.2f}")

# Fungsi untuk menghitung dan menampilkan total pengeluaran
def total_pengeluaran():
    total = sum(transaksi['Nominal'] for transaksi in data_transaksi if transaksi['Jenis Transaksi'] == 'Pengeluaran')
    print(f"Total Pengeluaran: {total:.2f}")

# Fungsi untuk menghitung dan menampilkan saldo akhir
def saldo_akhir():
    total_pemasukan = sum(transaksi['Nominal'] for transaksi in data_transaksi if transaksi['Jenis Transaksi'] == 'Pemasukan')
    total_pengeluaran = sum(transaksi['Nominal'] for transaksi in data_transaksi if transaksi['Jenis Transaksi'] == 'Pengeluaran')
    saldo = total_pemasukan - total_pengeluaran
    print(f"Saldo Akhir: {saldo:.2f}")

# Main program
while True:
    print("\nMenu Utama:")
    print("1. Penulis")
    print("2. Manajemen Data Mahasiswa")
    print("3. Manajemen Inventaris Barang")
    print("4. Manajemen Transaksi Keuangan")
    print("5. Keluar")
    pilihan = input("Pilih menu utama : ")
    os.system('cls')

    if pilihan == "1":
        owner()
        os.system('pause')
        os.system('cls')
    elif pilihan == "2":
        while True:
            print("1. Tambah Data Mahasiswa")
            print("2. Tampilkan Data Mahasiswa")
            print("3. Hitung Rata-rata Nilai Mahasiswa")
            print("4. Tampilkan Nilai Tertinggi dan Terendah")
            print("5. Kembali ke Menu Utama")
            sub_pilihan = input("Pilih menu mahasiswa : ")
            os.system('cls')

            if sub_pilihan == "1":
                input_mahasiswa()
                os.system('pause')
                os.system('cls')
            elif sub_pilihan == "2":
                cetak_mahasiswa()
                os.system('pause')
                os.system('cls')
            elif sub_pilihan == "3":
                rata_rata()
                os.system('pause')
                os.system('cls')
            elif sub_pilihan == "4":
                nilai_tertinggi_terendah()
                os.system('pause')
                os.system('cls')
            elif sub_pilihan == "5":
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang benar.")
    elif pilihan == "3":
        while True:
            print("1. Tambah Barang")
            print("2. Tampilkan Semua Barang")
            print("3. Cari Barang")
            print("4. Hapus Barang")
            print("5. Kembali ke Menu Utama")
            sub_pilihan = input("Pilih menu inventaris : ")
            os.system('cls')

            if sub_pilihan == "1":
                input_barang()
                os.system('pause')
                os.system('cls')
            elif sub_pilihan == "2":
                tampilkan_barang()
                os.system('pause')
                os.system('cls')
            elif sub_pilihan == "3":
                kode_cari = input("Masukkan Kode Barang yang ingin dicari: ")
                cari_barang(kode_cari)
                os.system('pause')
                os.system('cls')
            elif sub_pilihan == "4":
                kode_hapus = input("Masukkan Kode Barang yang ingin dihapus: ")
                hapus_barang(kode_hapus)
                os.system('pause')
                os.system('cls')
            elif sub_pilihan == "5":
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang benar.")
    elif pilihan == "4":
        while True:
            print("1. Tambah Transaksi")
            print("2. Tampilkan Semua Transaksi")
            print("3. Total Pemasukan")
            print("4. Total Pengeluaran")
            print("5. Saldo Akhir")
            print("6. Kembali ke Menu Utama")
            sub_pilihan = input("Pilih menu transaksi : ")
            os.system('cls')

            if sub_pilihan == "1":
                input_transaksi()
                os.system('pause')
                os.system('cls')
            elif sub_pilihan == "2":
                tampilkan_transaksi()
                os.system('pause')
                os.system('cls')
            elif sub_pilihan == "3":
                total_pemasukan()
                os.system('pause')
                os.system('cls')
            elif sub_pilihan == "4":
                total_pengeluaran()
                os.system('pause')
                os.system('cls')
            elif sub_pilihan == "5":
                saldo_akhir()
                os.system('pause')
                os.system('cls')
            elif sub_pilihan == "6":
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang benar.")
    elif pilihan == "5":
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.")