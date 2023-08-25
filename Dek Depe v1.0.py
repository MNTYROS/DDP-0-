import random
import math
import colorama #untuk warna input
import sys #agar semua warna tidak berubah jadi merah saat error

# Constants
KALIMAT_PEMBUKA = "Welcome to Dek Depe\'s Name Tag Store!"
KALIMAT_PENUTUP = "Terima kasih sudah berbelanja di Dek depe's Name Tag Store!"
GARIS_PEMISAH = "----------------------------------------"
HARGA_MODAL = 100

# Important Variables
jenis_bangun = ["segiempat", "segitiga", "lingkaran"] #input list pemilihan random
semua_kemungkinan = ["segiempat", "segitiga", "lingkaran", "random"] #untuk cek input
luas_total = 0

#Loop Functions
def ada_bentuk(x): #mengecek apakah yang ditulis ada di dalam list bentuk
	if x in semua_kemungkinan:
		return True

def bentuk_checker(): #dibuat func agar bisa recursive
	global bentuk_nametag, luas_total

	if bentuk_nametag == "segiempat":
		panjang = float(colored_input("Masukkan panjang (cm): ", colorama.Fore.RED))
		lebar = float(colored_input("Masukkan lebar (cm): ", colorama.Fore.RED))
		luas1 = panjang * lebar
		luas_total += luas1

	elif bentuk_nametag == "segitiga":
		alas = float(colored_input("Masukkan alas (cm): ", colorama.Fore.RED))
		tinggi = float(colored_input("Masukkan tinggi (cm): ", colorama.Fore.RED))
		luas2 = alas * tinggi / 2
		luas_total += luas2

	elif bentuk_nametag == "lingkaran":
		diameter = float(colored_input("Masukkan diameter (cm): ", colorama.Fore.RED))
		luas3 = math.pi * (diameter**2) 
		luas_total += luas3
		
	elif bentuk_nametag == "random":
		bentuk_nametag = random.choice(jenis_bangun) #random from list
		print(B + "Bentuk yang terpilih adalah " + bentuk_nametag + R)
		bentuk_checker() #recursion, biar di cek lagi untuk hasil dari random


#Colour Functions

#inputs
def hook(system, *argv):
    if system is KeyboardInterrupt:
        print(colorama.Fore.RESET)
        exit()

def colored_input(text: str, color):
    sys.excepthook = hook
    inp = input(text + color)
    print(colorama.Fore.RESET, end="", flush=True)
    sys.excepthook = sys.__excepthook__
    return inp
#format penulisan untuk warna input adalah
# nama = input("str", coloroma.Fore.Red)

#output variables
B = '\033[36m' #biru
R = '\033[0m' #reset
#format penulisan untuk warna output adalah
# print( B + "str" + R ), dimana B memberi warna biru, dan R mereset warna

print(KALIMAT_PEMBUKA)

jumlah_pelanggan = int(colored_input("Masukkan jumlah pelanggan: ", colorama.Fore.RED))

print(GARIS_PEMISAH)

for i in range(1, jumlah_pelanggan + 1):

	print("====== PELANGGAN " + B + str(i) + R)

	nama_pelanggan = colored_input("Masukkan nama pelanggan ke-" + B + str(i) + R + ": ", colorama.Fore.RED)
	jumlah_nametag = int(colored_input("Masukkan jumlah name tag yang ingin dibuat: ", colorama.Fore.RED))	
	print(" ")

	x = 0
	while x < jumlah_nametag:
		pra_bentuk_nametag = colored_input(("Bentuk nametag ke-" + B + str(x + 1) + R +
					 	" (segiempat/segitiga/lingkaran/random): "), colorama.Fore.RED)
		bentuk_nametag = pra_bentuk_nametag.lower() #di lower disini karena pra_bentuk_nametag berbentuk Tuple,
													#guna di lower agar bisa ignore caps/lowercase

		if ada_bentuk(bentuk_nametag) == True: #mengecek True for in list
			
			bentuk_checker()
			print(" ")

			x += 1

		else:
			print("Mohon masukkan salah satu dari bentuk yang telah disediakan.") #else, ulang input
			continue

	if x == jumlah_nametag:
		print("Total harga kertas yang diperlukan untuk membuat " + B + str(jumlah_nametag) + R +
		" name tag untuk pelanggan atas nama " + B + nama_pelanggan + R + " adalah Rp" +
		  B + str(round(luas_total * HARGA_MODAL, 3)) + R) #tambah 3 dibelakang koma untuk kembalian indomaret style
		print(" ")

print(GARIS_PEMISAH)

print(KALIMAT_PENUTUP)