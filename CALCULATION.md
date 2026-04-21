# AGNO Hesaplama Mantığı ve Algoritma Akışı

## 1. Giriş Verileri (Input)

Her ders için kullanıcıdan iki değer alınır:

- 100'lük sistemde ders puanı (örnek: 75)
- Dersin AKTS kredisi (örnek: 5)

## 2. Puan Dönüşüm Tablosu (100'lük -> 4'lük)

| Not Aralığı | 4'lük Sistem Karşılığı | Harf Notu |
| ----------- | ---------------------- | --------- |
| 91 - 100    | 4.00                   | AA        |
| 81 - 90     | 3.75                   | BA        |
| 71 - 80     | 3.50                   | BB        |
| 61 - 70     | 3.00                   | CB        |
| 51 - 60     | 2.50                   | CC        |
| 41 - 50     | 2.00                   | CD        |
| 36 - 40     | 1.50                   | DD        |
| 31 - 35     | 1.00                   | DF        |
| 0 - 30      | 0.00                   | F         |

## 3. Matematiksel Formül

Her ders için önce katsayı bulunur, ardından ağırlıklı puan hesaplanır:

- Ağırlıklı Puan = Katsayı x AKTS
- Toplam Ağırlıklı Puan = tum derslerin ağırlıklı puanlarının toplamı
- Toplam AKTS = tum derslerin AKTS toplamı

Son adım:

- AGNO = Toplam Ağırlıklı Puan / Toplam AKTS

## 4. Örnek Senaryo (Doğrulama)

- Ders 1: 85 puan (BA = 3.75), 6 AKTS -> 3.75 x 6 = 22.5
- Ders 2: 55 puan (CC = 2.50), 4 AKTS -> 2.50 x 4 = 10.0
- Toplam Ağırlıklı Puan: 22.5 + 10.0 = 32.5
- Toplam AKTS: 6 + 4 = 10
- Sonuç (AGNO): 32.5 / 10 = 3.25

## 5. Uygulama Notu

- Ders puanı 0-100 aralığında olmalıdır.
- AKTS 0'dan büyük olmalıdır.
- Girilen dersler için AGNO hesaplaması mutlaka AKTS ağırlıklı yapılmalıdır.
