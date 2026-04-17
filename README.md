# Final Notu Hesap Makinesi

İstanbul Ticaret Üniversitesi İstatistik Bölümü için geliştirilmiş, ders hedeflerine göre gereken minimum final notunu ve dönem ortalamasını hesaplayan bir araçtır.

## Özellikler

- Geçiş notuna göre minimum final hesaplama
- Hedef harf notuna göre minimum final hesaplama
- Hedef ders ortalamasına göre minimum final hesaplama
- Dönem dersleri için 4'lük sistem dönem GPA hesaplama
- Müfredat verisini JSON üzerinden dinamik yükleme

## Proje Yapısı

- `ui/index.html`: Arayüz ve istemci tarafı hesaplama mantığı
- `ui/config.json`: Harf notları, not eşikleri ve temel ayarlar
- `ui/mufredat.json`: Yıl, sınıf, dönem ve ders/ağırlık verileri
- `main.py`: Uygulama başlatma/giriş noktası
- `hesaplama.py`: Hesaplama yardımcıları
- `mufredat.py`: Müfredat veri işleme yardımcıları

## Çalıştırma

### Yerel (statik arayüz)

1. Proje klasörüne girin.
2. `ui` klasörünü bir statik sunucu ile servis edin.
3. Tarayıcıdan açın.

Örnek:

```bash
cd ui
python3 -m http.server 8080
```

Ardından tarayıcıda `http://localhost:8080` adresini açın.

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır.

Detaylar için [LICENSE](LICENSE) dosyasına bakın.
