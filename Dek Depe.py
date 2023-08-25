#Classifying Colours (kurang paham mksd class)

class color:
  red = '\033[31m' 
  blue = '\033[36m'
  reset = '\033[0m' 

M = color.red # Merah
B = color.blue # Biru (cerah)
R = color.reset # Reset warna

# Input checker (agar tidak terjadi error) (saya kurang paham dengan class/function/loop yg mendalam, 
# namun paham kegunaan dasar saja jadi mungkin perlu penjelasan/pertanyaan lebih lanjut)

def ada_angka(s):
  return any(i.isdigit() for i in s)

def input_checker(isian, ada_Angka=True):
  while True:
    input_User = input(isian)
    tipe = "huruf" if ada_Angka == True else "angka"
    if ada_angka(input_User) == True:
      print("Dimohon untuk hanya memasukkan", tipe)
    else:
      break
  

def input_checker(isian, hurufsaja=True):
  input_User = input(isian)
  tipe = "huruf" if hurufsaja == True else "angka"
  while ada_angka(input_User) == hurufsaja:
    print("Mohon untuk memasukkan " + tipe + " saja.")
    input_User = input(isian)

  return input_User

# Constants (agar mudah untuk diubah)

KALIMAT_PEMBUKA = "Welcome to Dek Depe\'s Name Tag Store!"
GARIS_PEMISAH = "----------------------------------------"
KALIMAT_PENUTUP = "Terima Kasih sudah berbelanja di Dek Depe\'s Name Tag Store!"
HARGA_MODAL = 100

print(KALIMAT_PEMBUKA)

print(GARIS_PEMISAH)

#Input variables

nama = input_checker("Nama: ")
tanggal_lahir = input("Tanggal Lahir: ")
jurusan = input_checker("Jurusan: ")
motto_hidup = input("Motto Hidup: ")
panjang_name_tag = input_checker("Masukkan panjang (cm): ", False)
lebar_name_tag = input_checker("Masukkan lebar (cm): ", False)

#print functions (agar mudah jika ingin diubah hanya dari input/calls) (kurang paham maksud function/kegunaan mendalam)

def printLine1(namanya, jurusannya):
  print("Halo", B, namanya, R, "dari", B + jurusannya + R + ".")

def printLine2(tgl_lahir, motto_hdp):
  print("Lahir pada", B, tgl_lahir, R, "dengan motto", "\"" + B + motto_hdp + R + "\"")

def printLine3(namanya, panjang, lebar):
  print("Luas name tag", B, namanya + R + ":", B, panjang * lebar, R, "cm\N{SUPERSCRIPT TWO}")

def printLine4(namanya, panjang, lebar, harga_modal):
  print("Harga name tag", B, namanya + R + ":", "Rp" + B + str(panjang * lebar * harga_modal) + R)

# Printing session 

print(GARIS_PEMISAH)

printLine1(nama, jurusan)
printLine2(tanggal_lahir, motto_hidup)
printLine3(nama, panjang_name_tag, lebar_name_tag)
printLine4(nama, panjang_name_tag, lebar_name_tag, HARGA_MODAL)

print(GARIS_PEMISAH)

#penutup

print(KALIMAT_PENUTUP)

# input terlalu sulit untuk dijadikan berwarna tanpa import..