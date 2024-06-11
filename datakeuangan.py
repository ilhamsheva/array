# Inisialisasi data transaksi
data_transaksi = []

# Fungsi untuk menginput transaksi
def input_transaksi():
    jenis_transaksi = input("Masukkan Jenis Transaksi (Pemasukan/Pengeluaran): ")
    if jenis_transaksi != "Pemasukan" and jenis_transaksi != "Pengeluaran":
        print("Jenis transaksi tidak valid. Silakan pilih 'Pemasukan' atau 'Pengeluaran'.")
        return jenis_transaksi
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
        print(f"Nominal: {transaksi['Nominal']:.3f}")
        print()

# Fungsi untuk menghitung dan menampilkan total pemasukan
def total_pemasukan():
    total = sum(transaksi['Nominal'] for transaksi in data_transaksi if transaksi['Jenis Transaksi'] == 'Pemasukan')
    print(f"Total Pemasukan: {total:.3f}")

# Fungsi untuk menghitung dan menampilkan total pengeluaran
def total_pengeluaran():
    total = sum(transaksi['Nominal'] for transaksi in data_transaksi if transaksi['Jenis Transaksi'] == 'Pengeluaran')
    print(f"Total Pengeluaran: {total:.3f}")

# Fungsi untuk menghitung dan menampilkan saldo akhir
def saldo_akhir():
    total_pemasukan = sum(transaksi['Nominal'] for transaksi in data_transaksi if transaksi['Jenis Transaksi'] == 'Pemasukan')
    total_pengeluaran = sum(transaksi['Nominal'] for transaksi in data_transaksi if transaksi['Jenis Transaksi'] == 'Pengeluaran')
    saldo = total_pemasukan - total_pengeluaran
    print(f"Saldo Akhir: {saldo:.3f}")

# Main program
while True:
    print("\nMenu:")
    print("1. Tambah Transaksi")
    print("2. Tampilkan Semua Transaksi")
    print("3. Total Pemasukan")
    print("4. Total Pengeluaran")
    print("5. Saldo Akhir")
    print("6. Keluar")
    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        input_transaksi()
    elif pilihan == "2":
        tampilkan_transaksi()
    elif pilihan == "3":
        total_pemasukan()
    elif pilihan == "4":
        total_pengeluaran()
    elif pilihan == "5":
        saldo_akhir()
    elif pilihan == "6":
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.")
