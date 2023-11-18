umur = int(input("Masukkan umur Anda: "))

if umur < 18:
    kategori = "Anak-anak"
elif 18 <= umur < 65:
    kategori = "Dewasa"
else:
    kategori = "Lanjut usia"
    
print("Anda masuk dalam kategori", kategori)
