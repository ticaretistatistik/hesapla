from dataclasses import dataclass, asdict
from typing import List, Literal
import json
import os


@dataclass
class Ders:
    """
    Ders bilgilerini tutan sınıf
    """

    ad: str  # Ders adı
    # Ders ağırlıkları: Vize + Final + Quiz = 1.0 olmalı
    vize: float = 0.4
    final: float = 0.6
    quiz: float = 0


@dataclass
class DonemDersleri:
    """
    Bir dönemdeki dersleri tutan sınıf
    """

    donem: Literal["Güz", "Bahar"]
    dersler: List[Ders]


mufredat = {
    # https://ticaret.edu.tr/istatistik/wp-content/uploads/sites/30/2025/10/2025-2026-Istatistik-Bolumu-Mufredat.pdf
    "2025-2026": {
        "1": [
            DonemDersleri(
                donem="Güz",
                dersler=[
                    Ders(ad="Genel İngilizce 1"),
                    Ders(ad="Matematik 1"),
                    Ders(ad="İstatistik 1"),
                    Ders(ad="Olasılık 1"),
                    Ders(ad="Doğrusal Programlama 1"),
                    Ders(ad="Türk Dili 1"),
                    Ders(ad="Atatürk İlkeleri ve İnkılap Tarihi 1"),
                ],
            ),
            DonemDersleri(
                donem="Bahar",
                dersler=[
                    Ders(ad="Genel İngilizce 2"),
                    Ders(ad="Matematik 2"),
                    Ders(ad="İstatistik 2"),
                    Ders(ad="Olasılık 2"),
                    Ders(ad="Doğrusal Programlama 2"),
                    Ders(ad="Türk Dili 2"),
                    Ders(ad="Atatürk İlkeleri ve İnkılap Tarihi 2"),
                ],
            ),
        ],
        "2": [
            DonemDersleri(
                donem="Güz",
                dersler=[
                    Ders(ad="Veri Analizinde Bilgisayar Programlama 1"),
                    Ders(ad="İktisat"),
                    Ders(ad="Örnekleme 1"),
                    Ders(ad="Matematiksel İstatistik"),
                    Ders(ad="Yöneylem Araştırması"),
                ],
            ),
            DonemDersleri(
                donem="Bahar",
                dersler=[
                    Ders(ad="Veri Analizinde Bilgisayar Programlama 2"),
                    Ders(ad="Örnekleme 2"),
                    Ders(ad="Kantitatif Karar Verme Teknikleri"),
                    Ders(ad="Optimizasyon"),
                ],
            ),
        ],
        "3": [
            DonemDersleri(
                donem="Güz",
                dersler=[
                    Ders(ad="Deney Düzenleme 1"),
                    Ders(ad="Uygulamalı İstatistil 1"),
                    Ders(ad="Regresyon Analizi 1"),
                    Ders(ad="Açıklayıcı Veri Analizi"),
                ],
            ),
            DonemDersleri(
                donem="Bahar",
                dersler=[
                    Ders(
                        ad="Parametrik Olmayan İstatistiksel Yöntemler",
                        vize=0.3,
                        final=0.5,
                        quiz=0.2,
                    ),
                    Ders(
                        ad="Zaman Serileri Analizi",
                        vize=0.4,
                        final=0.6,
                    ),
                    Ders(ad="Regresyon Analizi 2", vize=0.4, final=0.6),
                    Ders(ad="Mesleki İngilizce", vize=0.4, final=0.6),
                ],
            ),
        ],
        "4": [
            DonemDersleri(
                donem="Güz",
                dersler=[
                    Ders(ad="Çok Değişkenli Analiz 1"),
                    Ders(ad="Ekonometri 1"),
                    Ders(ad="Kariyer Planlama"),
                ],
            ),
            DonemDersleri(
                donem="Bahar",
                dersler=[
                    Ders(ad="Çok Değişkenli Analiz 2"),
                    Ders(ad="Ekonometri 2"),
                    Ders(ad="Makine Öğrenmesi"),
                    Ders(ad="Bitirme Projesi"),
                ],
            ),
        ],
    }
}

def mufredat_to_dict():
    """Mufredat'ı JSON'a uygun dict'e çevir"""
    result = {}
    
    for yil, siniflar in mufredat.items():
        result[yil] = {}
        for sinif_no, donemler in siniflar.items():
            result[yil][sinif_no] = []
            for donem_obj in donemler:
                donem_data = {
                    "donem": donem_obj.donem,
                    "dersler": []
                }
                for ders in donem_obj.dersler:
                    donem_data["dersler"].append({
                        "ad": ders.ad,
                        "vize": ders.vize,
                        "final": ders.final,
                        "quiz": ders.quiz
                    })
                result[yil][sinif_no].append(donem_data)
    
    return result

def export_mufredat_json():
    """Mufredat'ı JSON dosyasına kaydet"""
    data = mufredat_to_dict()
    output_path = os.path.join(os.path.dirname(__file__), 'ui', 'mufredat.json')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ mufredat.json oluşturuldu: {output_path}")

if __name__ == '__main__':
    export_mufredat_json()
