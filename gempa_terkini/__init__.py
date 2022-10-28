import requests
from bs4 import BeautifulSoup


def ekstraksi_data(content=None):
    """
    tanggal:26 Oktober 2022
    waktu: 08:34:01 WIB
    magnitudo: 2.8
    kedalaman: 10 km
    lokasi: LS= 7.27 - BT= 107.69
    Pusat gempa: berada di darat 23 km Barat Daya Kab. Garut
    Dirasakan:  (Skala MMI): II Cibereum, II Pengalengan, II Kertasari, II Pasirwangi, II Darajat
    """

    content = requests.get('https://www.bmkg.go.id/')
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        title = soup.find('title')
        print(title.text)

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')

        tanggal = None
        waktu = None
        magnitudo = None
        ls = None
        bt = None
        kedalaman = None
        koordinat = None
        lokasi = None
        dirasakan = None

        x = 0
        for res in result:
            print(x, res)

            if x == 0:
                waktu  = res.text.split(',')
                tanggal = waktu[0]
                waktu = waktu[1]
            elif x == 1:
                magnitudo = res.text
            elif x == 2:
                kedalaman = res.text
            elif x == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif x == 4:
                lokasi = res.text
            elif x == 5:
                dirasakan = res.text
            x = x + 1
        hasil = dict()
        hasil['Tanggal'] = tanggal
        hasil['Waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['Tanggal']}")
    print(f"Waktu {result['Waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat: LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Dirasakan {result['dirasakan']}")
