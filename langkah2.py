# --- 3. KONVERSI TIPE DATA (Type Casting) ---
nilai_algo = float(input("Nilai Algoritma: "))
nilai_bd = float(input("Nilai Basis Data: "))
nilai_web = float(input("Nilai Pemrograman Web: "))

# --- 4. KALKULASI MENGGUNAKAN VARIABEL ---
total_nilai = nilai_algo + nilai_bd + nilai_web
jumlah_matkul = 3
rata_rata_nilai = total_nilai / jumlah_matkul
sks_per_matkul = 3
total_sks_diambil = jumlah_matkul * sks_per_matkul

# Penentuan status kelulusan semester (Boolean)
# Lulus jika rata-rata >= 75.0 dan status mahasiswa aktif
is_aktif = True
is_lulus_semester = (rata_rata_nilai >= 75.0) and (is_aktif == True)

print("\n--- HASIL EVALUASI AVAL ---")
print("Total Nilai      :", total_nilai)
print("Rata-Rata Nilai  :", round(rata_rata_nilai, 2))
print("Total SKS        :", total_sks_diambil)
print("Status Lulus     :", is_lulus_semester)