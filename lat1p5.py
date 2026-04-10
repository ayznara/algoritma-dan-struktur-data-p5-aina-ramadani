data_mahasiswa = [
    [["10121001", "Asep"], [50, 70, 40, 80]],
    [["10121002", "Budi"], [78, 78, 80, 65]],
    [["10121003", "Cecep"], [57, 88, 67, 69]]
]

nama_paling_pintar = ""
nilai_rata_tertinggi = 0

for mhs in data_mahasiswa:
    nama = mhs[0][1]
    nilai = mhs[1]
    
    rata_rata_orang = (nilai[0] + nilai[1] + nilai[2] + nilai[3]) / 4
    
    if rata_rata_orang > nilai_rata_tertinggi:
        nilai_rata_tertinggi = rata_rata_orang
        nama_paling_pintar = nama

total_mk1 = data_mahasiswa[0][1][0] + data_mahasiswa[1][1][0] + data_mahasiswa[2][1][0]
total_mk2 = data_mahasiswa[0][1][1] + data_mahasiswa[1][1][1] + data_mahasiswa[2][1][1]
total_mk3 = data_mahasiswa[0][1][2] + data_mahasiswa[1][1][2] + data_mahasiswa[2][1][2]
total_mk4 = data_mahasiswa[0][1][3] + data_mahasiswa[1][1][3] + data_mahasiswa[2][1][3]

rata_mk1 = total_mk1 / 3
rata_mk2 = total_mk2 / 3
rata_mk3 = total_mk3 / 3
rata_mk4 = total_mk4 / 3

mk_terkecil_nama = "MK1"
mk_terkecil_nilai = rata_mk1

if rata_mk2 < mk_terkecil_nilai:
    mk_terkecil_nilai = rata_mk2
    mk_terkecil_nama = "MK2"

if rata_mk3 < mk_terkecil_nilai:
    mk_terkecil_nilai = rata_mk3
    mk_terkecil_nama = "MK3"

if rata_mk4 < mk_terkecil_nilai:
    mk_terkecil_nilai = rata_mk4
    mk_terkecil_nama = "MK4"

print("Mahasiswa Terpintar :", nama_paling_pintar, "(Nilai :", round(nilai_rata_tertinggi, 2), ")")
print("Mata Kuliah Nilai Terkecil :", mk_terkecil_nama, "(Nilai :", round(mk_terkecil_nilai, 2), ")")