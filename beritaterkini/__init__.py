import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    try:
        page = requests.get('http://detik.com')
    except Exception:
        return None
    if page.status_code == 200:
        # Belum menemukan cara fetch tanggal upload karena tanggal berta menempel pada id berita,sedangkan yg
        # di fetch di berita terpopuler adalah rannking yang bisa berubah2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        soup = BeautifulSoup(page.text, 'html.parser')

        first_news = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '1'})
        first_news = first_news.text.strip()

        upload = soup.find('div', {'class': 'media'})
        # print(upload)

        second_news = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '2'})
        second_news = second_news.text.strip()
        # second_upload = soup.find('span', {'d-time': '1666849534'})
        # second_upload = second_upload.text
        #
        third_news = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '3'})
        third_news = third_news.text.strip()
        # third_upload = soup.find('span', {'d-time': '1666846941'})
        # third_upload = third_upload.text
        #
        fourth_news = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '4'})
        fourth_news = fourth_news.text.strip()
        # fourth_upload = soup.find('span', {'d-time': '1666849774'})
        # fourth_upload = fourth_upload.text
        #
        fifth_news = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '5'})
        fifth_news = fifth_news.text.strip()

        hasil = dict()
        hasil['first_news'] = {
            'isi': first_news,
            'diupload': 'first_upload'
        }
        hasil['second_news'] = {
            'isi': second_news,
            'diupload': 'second_upload'
        }
        hasil['third_news'] = {
            'isi': third_news,
            'diupload': 'third_upload'
        }
        hasil['fourth_news'] = {
            'isi': fourth_news,
            'diupload': 'fourth_upload'
        }
        hasil['fifth_news'] = {
            'isi': fifth_news,
            'diupload': '1 jam yang lalu'
        }

        return hasil


def tampilkan_data(result):
    if result is None:
        print('Tidak dapat menemukan data berita terkini')
        return None
    print(f"#1. {result['first_news']['isi']}. \n   Diupload {result['first_news']['diupload']}")
    print(f"#2. {result['second_news']['isi']}. \n   Diupload {result['second_news']['diupload']}")
    print(f"#3. {result['third_news']['isi']}. \n   Diupload {result['third_news']['diupload']}")
    print(f"#4. {result['fourth_news']['isi']}. \n   Diupload {result['fourth_news']['diupload']}")
    print(f"#5. {result['fifth_news']['isi']}. \n   Diupload {result['fifth_news']['diupload']}")


if __name__ == "__main__":
    print("Berita Terpopuler dan Terkini Detik.com\n")
    result = ekstraksi_data()
    tampilkan_data(result)
