produk = {
    "laptop": 5500000,
    "smartphone": 3000000,
    "tablet": 2000000,
    "smartwatch": 1500000,
    "headphone": 5000000
}
pesanan = []

def buat_pesanan():
    for key, value in produk.items():
        n_produk = str(input("masukkan nama produk yang ingin dibeli: "))
        jumlah = int(input("masukkan jumlahnya: "))
        harga_sementara = jumlah * value
        # pesanan.append(n_produk,jumlah)
        return harga_sementara
    
    if n_produk not in produk.items():
        print("produk tidak tersedia")

def tampilkan_produk():
    for key, value in produk.items():
        print(f"{key.lower()} : {value}")

def cek_penawaran(tawaran, value):
    for key, value in produk.items():
        if tawaran <= 80/100 * value:
            hasil = value - tawaran
            return hasil
    else:
        print("penawaran ditolak.harga asli digunakan")


def hitung_diskon(member, total_pembelian):
    diskon = 0
    if member == 'y':
        if total_pembelian > 10000000:
            diskon += 10/100
        elif total_pembelian > 5000000:
            diskon += 5/100
    else:
        print("km g dpt diskon")
    return diskon

def transaksi(nama, produk, jumlah, harga, subtotal, diskon):
    print("=== STRUK PEMBELIAN ===")
    print(f"Nama pembeli: {nama}")
    print(f"Produk dibeli:{produk}\njumlah unit : {jumlah}\nHarga/unit : {harga}")
    subtotal = jumlah * harga
    print(f"subtotal : {subtotal}")
    print(f"diskon: {diskon}")
    total_akhir = subtotal *diskon
    print(f"total akhir: {total_akhir}")
    print("")

def main():
    tampilkan_produk()
    nama = str(input("masukkan nama: "))
    umur = int(input("masukkan umur: "))
    beli = str(input("apakah kamu ingin membeli?(y/n): "))
    while True:
        if beli == 'y':
            buat_pesanan()
            tawaran = str(input("apakah km mw nawar?(y/n): "))
            if tawaran == 'y':
                cek_penawaran(tawaran)
            member = str(input("apakah km member? (y/n): "))
            if member == 'y':
                hitung_diskon(member)
            # transaksi(nama,produk,jumlah, harga, subtotal, diskon)

        else:
            break

main()