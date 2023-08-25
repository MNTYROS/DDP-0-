"""
Mohon Maaf sebelumnya, saya kurang paham kalau tidak
memakai function, jadi melewati materi sedikit
"""
#Constants
KALIMAT_PEMBUKA = "Welcome to Dek Depe\'s Name Tag Store!"
GARIS_PEMISAH = "----------------------------------------"
KALIMAT_PENUTUP = ("Terima Kasih sudah berbelanja " +
                    "di Dek Depe\'s Name Tag Store!")
HARGA_MODAL = 100

print(KALIMAT_PEMBUKA)

print(GARIS_PEMISAH)

#Input variables
nama_User = input("Nama: ")
tanggal_lahir_User = input("Tanggal lahir: ")
jurusan_User = input("Jurusan: ")
motto_hidup_User = input("Motto Hidup: ")
jumlah_name_tag_User = int(input("Silahkan masukkan " 
                                 + "banyak name tag: "))

#More variables
luas_total = 0

#loop functions
def luas_segiempat():
  panjang = int(input("Masukkan panjang (cm): "))
  lebar = int(input("Masukkan lebar (cm): "))
  luas1 = panjang * lebar

  return luas1

def luas_segitiga():
  alas = int(input("Masukkan alas (cm): "))
  tinggi = int(input("Masukkan tinggi (cm): "))
  luas2 = alas * tinggi / 2

  return luas2

print(GARIS_PEMISAH)

#loops for user_input #jumlah_name_tag_User
for x in range(jumlah_name_tag_User):
  print("Name Tag", x + 1)
  bentuk = input("Silahkan masukkan bentuk name tag anda: ")
  if bentuk == "segiempat":
    luas_segiempat1 = luas_segiempat()
    luas_total += luas_segiempat1
  else:
    luas_segitiga1 = luas_segitiga()
    luas_total += luas_segitiga1

print(GARIS_PEMISAH)

#Print ending statement
print("Halo", nama_User, "dari", jurusan_User)

print("Lahir pada", tanggal_lahir_User, 
        "dengan motto", "\"" + motto_hidup_User + "\"")

print("Total biaya untuk memproduksi ke-" + 
        str(jumlah_name_tag_User), "name tag adalah ",
        "Rp" + str(luas_total * HARGA_MODAL))

print(GARIS_PEMISAH)

print(KALIMAT_PENUTUP)