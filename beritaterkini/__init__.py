import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    try:
        page = requests.get('http://detik.com')
    except Exception:
        return None
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        judul = soup.find('title')
        print(judul.string)

        hasil = dict()  # perintah/cara lain agar otomatis mengubah menjadi tipe data dictionary
        hasil['pertama'] = {
            'isi': 'Tangis Vera Saat Ungkap Yosua Curhat Masalah yang Ditanggung Sendiri',
            'diupload': '1 jam yang lalu'
        }
        hasil['kedua'] = {
            'isi': 'Erick Thohir: Yang Jadi Presiden Pasti Bukan Saya, Berikutnya Orang Jawa',
            'diupload': '1 jam yang lalu'
        }
        hasil['ketiga'] = {
            'isi': 'Penampakan Wanita Coba Terobos Istana Kini Diborgol di Kantor Polisi',
            'diupload': '2 jam yang lalu'
        }
        hasil['keempat'] = {
            'isi': 'Adik Yosua: Saya Dilarang Kombes Pakaikan Baju dan Gendong Jenazah Kakak',
            'diupload': '45 menit yang lalu'
        }
        hasil['kelima'] = {
            'isi': "Rizaldi Sempat \'Jadi Pak Ogah\' Usai Bunuh Anak Perempuan Pulang Ngaji",
            'diupload': '1 jam yang lalu'
        }

        return hasil


def tampilkan_data(result):
    if result is None:
        print('Tidak dapat menemukan data berita terkini')
        return None
    print(f"#1. {result['pertama']['isi']}. \n   Diupload {result['pertama']['diupload']}")
    print(f"#2. {result['kedua']['isi']}. \n   Diupload {result['kedua']['diupload']}")
    print(f"#3. {result['ketiga']['isi']}. \n   Diupload {result['ketiga']['diupload']}")
    print(f"#4. {result['keempat']['isi']}. \n   Diupload {result['keempat']['diupload']}")
    print(f"#5. {result['kelima']['isi']}. \n   Diupload {result['kelima']['diupload']}")


# if __name__ == "__main__":
#     print("Berita Terpopuler dan Terkini Detik.com\n")
#     result = ekstraksi_data()
#     tampilkan_data(result)
