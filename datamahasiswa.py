# Inisialisasi data mahasiswa
data_mahasiswa = []

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

# Main program
input_mahasiswa()
cetak_mahasiswa()
rata_rata()
nilai_tertinggi_terendah()