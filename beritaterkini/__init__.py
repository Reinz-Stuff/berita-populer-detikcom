def ekstraksi_data():
    """
    Berita Terpopuler
#1
Tangis Vera Saat Ungkap Yosua Curhat Masalah yang Ditanggung Sendiri
detikNews | 1 jam yang lalu
#2
Erick Thohir: Yang Jadi Presiden Pasti Bukan Saya, Berikutnya Orang Jawa
detikFinance | 1 jam yang lalu
#3
Penampakan Wanita Coba Terobos Istana Kini Diborgol di Kantor Polisi
detikNews | 2 jam yang lalu
#4
Adik Yosua: Saya Dilarang Kombes Pakaikan Baju dan Gendong Jenazah Kakak
detikNews | 45 menit yang lalu
#5
Rizaldi Sempat Jadi 'Pak Ogah' Usai Bunuh Anak Perempuan Pulang Ngaji
detikNews | 1 jam yang lalu
    :return:
    """
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
    print(f"#1. {result['pertama']['isi']}. \n   Diupload {result['pertama']['diupload']}")
    print(f"#2. {result['kedua']['isi']}. \n   Diupload {result['kedua']['diupload']}")
    print(f"#3. {result['ketiga']['isi']}. \n   Diupload {result['ketiga']['diupload']}")
    print(f"#4. {result['keempat']['isi']}. \n   Diupload {result['keempat']['diupload']}")
    print(f"#5. {result['kelima']['isi']}. \n   Diupload {result['kelima']['diupload']}")
