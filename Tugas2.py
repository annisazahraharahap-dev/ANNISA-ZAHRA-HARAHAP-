
# Input nilai mahasiswa
tugas = float(input("Nilai tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))
kehadiran = float(input("Kehadiran: "))

# Menghitung nilai akhir
nilai = (20/100 * tugas) + (30/100 * uts) + (50/100 * uas)

print("Nilai Akhir:", nilai)

# Menentukan status mahasiswa
if nilai >= 85 and kehadiran >= 90 and nilai % 2 == 0:
    print("Status: LULUS DENGAN PREDIKAT")
elif nilai >= 60 and kehadiran >= 80:
    print("Status: LULUS")
else:
    print("Status: BELUM LULUS")
