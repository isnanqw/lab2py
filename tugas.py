nama = 'Maulana Isnan Ibrahim' #tipe string
nim = 312510355 #tipe integer
kelas = 5
tahun= 2025
usia = 19
tinggi_badan = 162.5 #tipe float
menyapa = 'halo semua'

#int("19") -->> 19
#str(19) --->> "19"
#float(165.5) ---->> 5.0

print(menyapa + ' kenalin saya '+ nama)
print('nim : '+str(nim))
print('kelas : TI.'+str(tahun)+'.C'+str(kelas))
print('usia : '+str(usia))
print('tinggi_badan : '+str(tinggi_badan))
print('belajar', end=' ')
print('python')

print('hello','saya sedang belajar python',sep='-')

a=8
b=6
c=a+b
d=a*b
e=a/b
print('variabel a='+str(a))
print('variabel b='+str(b))
print(c)
print(d)
print(e)

a = 8
b = 6

# Cetak nilai variabel dengan format sederhana

print("Variabel a = {}".format(a))
print("Variabel b = {}".format(b))
a=input ('masukan nilai a:')
b=input ('masukan nilai b:')

# Cetak hasil penggabungan string dengan String Format (sebelum konversi)
print("Hasil penggabungan {a} & {b} = {gabung}".format(a=a, b=b, gabung=str(a) + str(b)))

# Konversi nilai variabel ke integer (untuk aritmatika)
a = int(a)
b = int(b)

# Cetak hasil penjumlahan (langsung a + b, tanpa c)
print("Hasil penjumlahan {a} + {b} = {hasil}".format(a=a, b=b, hasil=a + b))
# Cetak hasil perkalian (langsung a * b, tanpa d)
print("Hasil perkalian {a} * {b} = {hasil}".format(a=a, b=b, hasil=a * b))

# Cetak hasil pembagian (langsung a / b, dengan format 2 desimal, tanpa e)
print("Hasil pembagian {a} / {b} = {hasil}".format(a=a, b=b, hasil=a / b))
