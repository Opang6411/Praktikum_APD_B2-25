nama=("Muhammad Noval Arifinnur")
nim=("2509106079")

inputnama=input("Masukkan nama anda: ")
inputnim=input("Masukkan nim anda: ")

if (inputnama==nama and inputnim==nim):
    ukt=6000000
    print("Login berhasil")
    print("Menampilkan Pilihan Pembayaran: ")
    print("Lunas (Administrasi 1%)")
    print("Cicilan 2x (Administrasi 5%)")
    print("Cicilan 4x (Administrasi 8%)")
    print("Cicilan 6x (Administrasi 12%)")
    inputbayar=input("Masukkan pembayaran 'Lunas','Cicilan 2x','Cicilan 4x', atau 'Cicilan 6x'(Salin saja pilihannya) : ")
    if (inputbayar=="Lunas"):
        print("Total pembayaran anda: Rp.", (ukt+ukt*0.01))
    elif (inputbayar=="Cicilan 2x"):
        print("Total pembayaran anda: Rp.", (ukt+ukt*0.05))
        print("Dengan pembayaran perbulan: Rp.", ((ukt+ukt*0.05)/2))
    elif (inputbayar=="Cicilan 4x"):
        print("Total pembayaran anda: Rp.", (ukt+ukt*0.08))
        print("Dengan pembayaran perbulan: Rp.", ((ukt+ukt*0.08)/4))
    elif (inputbayar=="Cicilan 6x"):
        print("Total pembayaran anda: Rp.", (ukt+ukt*0.12))
        print("Dengan pembayaran perbulan: Rp.", ((ukt+ukt*0.12)/6))
    else:
        print ("Anda masukin apa?")
else:
    print("Login gagal")
