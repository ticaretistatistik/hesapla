from dataclasses import dataclass
from typing import List, Literal
import json
import os


class DersTipi:
    ZORUNLU = "Zorunlu"
    SECMELI = "Seçmeli"


@dataclass
class Ders:
    """
    Ders bilgilerini tutan sınıf
    """

    ad: str  # Ders adı
    akts: int
    # Ders ağırlıkları: Vize + Final + Quiz = 1.0 olmalı
    vize: float = 0.4
    final: float = 0.6
    quiz: float = 0  # quiz veya ödev, aynı anlamda kullanıldı.
    type: Literal["Zorunlu", "Seçmeli"] = DersTipi.ZORUNLU  # Zorunlu veya Seçmeli


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
                    Ders(ad="Genel İngilizce 1", akts=2),
                    Ders(ad="Matematik 1", vize=0.3, final=0.7, akts=6),
                    Ders(ad="İstatistik 1", akts=6),
                    Ders(ad="Olasılık 1", akts=6),
                    Ders(ad="Doğrusal Programlama 1", akts=6),
                    Ders(ad="Türk Dili 1", akts=2),
                    Ders(ad="Atatürk İlkeleri ve İnkılap Tarihi 1", akts=2),
                ],
            ),
            DonemDersleri(
                donem="Bahar",
                dersler=[
                    Ders(ad="Genel İngilizce 2", akts=2),
                    Ders(ad="Matematik 2", vize=0.3, final=0.7, akts=6),
                    Ders(ad="İstatistik 2", akts=6),
                    Ders(ad="Olasılık 2", akts=6),
                    Ders(ad="Doğrusal Programlama 2", akts=6),
                    Ders(ad="Türk Dili 2", akts=2),
                    Ders(ad="Atatürk İlkeleri ve İnkılap Tarihi 2", akts=2),
                ],
            ),
        ],
        "2": [
            DonemDersleri(
                donem="Güz",
                dersler=[
                    Ders(ad="Veri Analizinde Bilgisayar Programlama 1", akts=5),
                    Ders(ad="İktisat", akts=5),
                    Ders(ad="Örnekleme 1", akts=6),
                    Ders(ad="Matematiksel İstatistik", akts=6),
                    Ders(ad="Yöneylem Araştırması", akts=6),
                    Ders(ad="Üniversite Seçmeli Ders", type=DersTipi.SECMELI, akts=2),
                ],
            ),
            DonemDersleri(
                donem="Bahar",
                dersler=[
                    Ders(
                        ad="Veri Analizinde Bilgisayar Programlama 2",
                        vize=0.2,
                        quiz=0.2,
                        final=0.6,
                        akts=5,
                    ),
                    Ders(ad="Örnekleme 2", akts=5),
                    Ders(ad="Kantitatif Karar Verme Teknikleri", akts=5),
                    Ders(ad="Optimizasyon", akts=5),
                    Ders(ad="Seçmeli Ders", type=DersTipi.SECMELI, akts=5),
                    Ders(ad="Seçmeli Ders", type=DersTipi.SECMELI, akts=5),
                ],
            ),
        ],
        "3": [
            DonemDersleri(
                donem="Güz",
                dersler=[
                    Ders(ad="Deney Düzenleme 1", akts=6),
                    Ders(ad="Uygulamalı İstatistil 1", akts=6),
                    Ders(ad="Regresyon Analizi 1", akts=6),
                    Ders(ad="Açıklayıcı Veri Analizi", akts=5),
                    Ders(ad="Seçmeli Ders", type=DersTipi.SECMELI, akts=5),
                    Ders(ad="Üniversite Seçmeli Ders", type=DersTipi.SECMELI, akts=2),
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
                        akts=4,
                    ),
                    Ders(ad="Zaman Serileri Analizi", vize=0.4, final=0.6, akts=4),
                    Ders(ad="Regresyon Analizi 2", vize=0.4, final=0.6, akts=5),
                    Ders(ad="Mesleki İngilizce", vize=0.4, final=0.6, akts=4),
                    Ders(ad="Seçmeli Ders", type=DersTipi.SECMELI, akts=5),
                    Ders(ad="Üniversite Seçmeli Ders", type=DersTipi.SECMELI, akts=2),
                ],
            ),
        ],
        "4": [
            DonemDersleri(
                donem="Güz",
                dersler=[
                    Ders(ad="Çok Değişkenli Analiz 1", akts=5),
                    Ders(ad="Ekonometri 1", akts=5),
                    Ders(ad="Kariyer Planlama", akts=0),
                    Ders(ad="Seçmeli Ders", type=DersTipi.SECMELI, akts=5),
                    Ders(ad="Seçmeli Ders", type=DersTipi.SECMELI, akts=5),
                    Ders(ad="Seçmeli Ders", type=DersTipi.SECMELI, akts=5),
                    Ders(ad="Seçmeli Ders", type=DersTipi.SECMELI, akts=5),
                ],
            ),
            DonemDersleri(
                donem="Bahar",
                dersler=[
                    Ders(ad="Çok Değişkenli Analiz 2", akts=4),
                    Ders(ad="Ekonometri 2", akts=4),
                    Ders(ad="Makine Öğrenmesi", akts=4),
                    Ders(ad="Bitirme Projesi", akts=3),
                    Ders(ad="Seçmeli Ders", type=DersTipi.SECMELI, akts=5),
                    Ders(ad="Seçmeli Ders", type=DersTipi.SECMELI, akts=5),
                    Ders(ad="Seçmeli Ders", type=DersTipi.SECMELI, akts=5),
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
                donem_data = {"donem": donem_obj.donem, "dersler": []}
                for ders in donem_obj.dersler:
                    donem_data["dersler"].append(
                        {
                            "ad": ders.ad,
                            "akts": ders.akts,
                            "vize": ders.vize,
                            "final": ders.final,
                            "quiz": ders.quiz,
                            "type": ders.type if hasattr(ders, "type") else None,
                        }
                    )
                result[yil][sinif_no].append(donem_data)

    return result


def export_mufredat_json():
    """Mufredat'ı JSON dosyasına kaydet"""
    data = mufredat_to_dict()
    output_path = os.path.join(os.path.dirname(__file__), "ui", "mufredat.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✓ mufredat.json oluşturuldu: {output_path}")


if __name__ == "__main__":
    export_mufredat_json()
