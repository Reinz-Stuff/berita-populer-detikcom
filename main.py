"""
Aplikasi Berita Terpopuler Detikcom
"""

from beritapopuler import NewsTrending

if __name__ == "__main__":  # -> kode hanya akan di eksekusi jika sebagai module utama bukan dari perintah import
    berita_populer = NewsTrending()
    berita_populer.run()


# Alternatif
# cara ini kurang, kita tidak tahu ektraksi data dari package yang mana


# from beritaterkini import ekstraksi_data, tampilkan_data
#
# if __name__ == "__main__":
#     print("Berita Terpopuler dan Terkini Detik.com\n")
#     result = ekstraksi_data()
#     tampilkan_data(result)

