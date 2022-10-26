""""
aplikasi deteksi gempa
modularisasi function
"""

def ekstraksi_data():

    """
    tanggal:26 Oktober 2022
    waktu: 08:34:01 WIB
    magnitudo: 2.8
    kedalaman: 10 km
    lokasi: LS= 7.27 - BT= 107.69
    Pusat gempa: berada di darat 23 km Barat Daya Kab. Garut
    Dirasakan:  (Skala MMI): II Cibereum, II Pengalengan, II Kertasari, II Pasirwangi, II Darajat
    """
    hasil = {}
    hasil['tanggal'] = '26 oktober 2022'
    hasil['waktu'] = '08:34:01 WIB'
    hasil['magnitudo'] = 2.8
    hasil['kedalaman'] = '10 km'
    hasil['lokasi'] = {'ls':7.27, 'bt': 107.69}
    hasil['pusat gempa'] = 'berada di darat 23 km Barat Daya Kab. Garut'
    hasil['dirasakan'] = '(Skala MMI): II Cibereum, II Pengalengan, II Kertasari, II Pasirwangi, II Darajat'

    return hasil

def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")
    print(f"magnitudo {result['magnitudo']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"pusat gempa {result['pusat gempa']}")
    print(f"dirasakan {result['dirasakan']}")

if __name__ == '__main__':
    print('aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
