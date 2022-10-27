import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    try:
        page = requests.get('http://detik.com')
    except Exception:
        return None
    if page.status_code == 200:
        # Belum direvisi apakah sudah betul menunjukan berita populer berdasarkan ranking. Kemungkinan menunjukan
        # id berita saja!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        soup = BeautifulSoup(page.text, 'html.parser')

        first_news = soup.find('a', {'dtr-id': '6372097'})
        first_news = first_news.text.strip()
        first_upload = soup.find('span', {'d-time': '1666848035'})
        first_upload = first_upload.text.strip()

        second_news = soup.find('a', {'dtr-id': '6372158'})
        second_news = second_news.text.strip()
        second_upload = soup.find('span', {'d-time': '1666849534'})
        second_upload = second_upload.text

        third_news = soup.find('a', {'dtr-id': '6372043'})
        third_news = third_news.text.strip()
        third_upload = soup.find('span', {'d-time': '1666846941'})
        third_upload = third_upload.text

        fourth_news = soup.find('a', {'dtr-id': '6372175'})
        fourth_news = fourth_news.text.strip()
        fourth_upload = soup.find('span', {'d-time': '1666849774'})
        fourth_upload = fourth_upload.text

        fifth_news = soup.find('a', {'dtr-id': '6372043'})
        fifth_news = fifth_news
        print(fifth_news)

        hasil = dict()
        hasil['first_news'] = {
            'isi': first_news,
            'diupload': first_upload
        }
        hasil['kedua'] = {
            'isi': second_news,
            'diupload': second_upload
        }
        hasil['ketiga'] = {
            'isi': third_news,
            'diupload': third_upload
        }
        hasil['keempat'] = {
            'isi': fourth_news,
            'diupload': fourth_upload
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
    print(f"#1. {result['first_news']['isi']}. \n   Diupload {result['first_news']['diupload']}")
    print(f"#2. {result['kedua']['isi']}. \n   Diupload {result['kedua']['diupload']}")
    print(f"#3. {result['ketiga']['isi']}. \n   Diupload {result['ketiga']['diupload']}")
    print(f"#4. {result['keempat']['isi']}. \n   Diupload {result['keempat']['diupload']}")
    print(f"#5. {result['kelima']['isi']}. \n   Diupload {result['kelima']['diupload']}")


if __name__ == "__main__":
    print("Berita Terpopuler dan Terkini Detik.com\n")
    result = ekstraksi_data()
    tampilkan_data(result)
