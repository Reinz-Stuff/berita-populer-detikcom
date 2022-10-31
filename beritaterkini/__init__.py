import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    try:
        page = requests.get('http://detik.com')
    except Exception:
        return None
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')

        first_news = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '1'})
        first_news = first_news.text.strip()

        second_news = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '2'})
        second_news = second_news.text.strip()

        third_news = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '3'})
        third_news = third_news.text.strip()

        fourth_news = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '4'})
        fourth_news = fourth_news.text.strip()

        fifth_news = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '5'})
        fifth_news = fifth_news.text.strip()

        hasil = dict()
        hasil['first_news'] = {
            'isi': first_news
        }
        hasil['second_news'] = {
            'isi': second_news
        }
        hasil['third_news'] = {
            'isi': third_news
        }
        hasil['fourth_news'] = {
            'isi': fourth_news
        }
        hasil['fifth_news'] = {
            'isi': fifth_news
        }

        return hasil


def tampilkan_data(result):
    if result is None:
        print('Tidak dapat menemukan data berita terkini')
        return None
    print(f"#1. {result['first_news']['isi']}.")
    print(f"#2. {result['second_news']['isi']}.")
    print(f"#3. {result['third_news']['isi']}.")
    print(f"#4. {result['fourth_news']['isi']}.")
    print(f"#5. {result['fifth_news']['isi']}.")


if __name__ == "__main__":
    print(" Detikcom - Informasi Berita Terkini dan Terpopuler Hari Ini")
    result = ekstraksi_data()
    tampilkan_data(result)
