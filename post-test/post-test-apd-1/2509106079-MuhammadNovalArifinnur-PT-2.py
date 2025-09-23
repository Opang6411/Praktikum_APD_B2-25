nama_lengkap = input("Masukkan nama lengkap: ")
nim = input("Masukkan NIM: ")
harga_pecel_lele = float(input("Masukkan harga pecel lele: "))
harga_mie_ayam = float(input("Masukkan harga mie ayam: "))
harga_nasi_padang = float(input("Masukkan harga nasi padang: "))
pajak_pecel_lele = harga_pecel_lele * (5 / 100)
pajak_mie_ayam = harga_mie_ayam  * (8 / 100)
pajak_nasi_padang = harga_nasi_padang * (10 / 100)
total_harga_pecel_lele = harga_pecel_lele + pajak_pecel_lele
total_harga_mie_ayam = harga_mie_ayam + pajak_mie_ayam
total_harga_nasi_padang = harga_nasi_padang + pajak_nasi_padang
total_bayar = total_harga_pecel_lele + total_harga_mie_ayam + total_harga_nasi_padang
print(nama_lengkap + " dengan NIM " + nim + " ingin membeli makanan seharga: Rp." + str(total_bayar))
