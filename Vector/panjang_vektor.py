# Menghitung panjang atau norma suatu vektor
# Hasil berupa skalar

# Membuat fungsi akar dengan memangkatkan angka input dengan setengah
def akarDari(sebuahAngka):
    setengah = 1/2
    return sebuahAngka ** setengah
  
  # Membuat fungsi pemangkatan suatu angka dengan 2
def pangkat2Dari(sebuahAngka):
    return sebuahAngka*sebuahAngka
  
  def panjang_vektor(vektor):
    temp = 0 # variabel untuk menyimpan operasi iterasi
    panjang = range(len(vektor)) # panjang vektor
    # Menjumlahkan semua isi vektor yang telah dipangkat 2
    for i in panjang:
       temp = temp + pangkat2Dari(vektor[i])
    hasil = akarDari(temp)
    return hasil
  
vektorDummy = [1, 1, 4]
print(panjang_vektor(vektorDummy))
