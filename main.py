"""
Aplikasi Berita Terpopuler Detikcom
"""
from beritaterkini import ekstraksi_data, tampilkan_data

if __name__ == "__main__":  # -> kode hanya akan di eksekusi jika sebagai module utama bukan dari perintah import
    print("Berita Terpopuler dan Terkini Detik.com\n")
    result = ekstraksi_data()
    tampilkan_data(result)
