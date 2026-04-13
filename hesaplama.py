import json
from pathlib import Path
from dataclasses import dataclass
from mufredat import DonemDersleri, Ders


@dataclass
class DersNotu:
    """
    Ders notlarını tutan sınıf
    """

    vize: float
    final: float | None = None
    quiz: float | None = None


@dataclass
class HarfNotu:
    """
    Harf notları ile sayısal karşılıklarının eşleştirilmesi
    """

    harf: str
    geçiş_notu: float
    açıklama: str


# Harf notları eşleştirilmesi (100'lük sistem)
def _load_ui_config() -> dict:
    """UI tarafındaki ortak config dosyasını yükle."""
    config_path = Path(__file__).resolve().parent / "ui" / "config.json"
    if not config_path.exists():
        return {}

    with config_path.open("r", encoding="utf-8") as f:
        return json.load(f)


_HARF_ACIKLAMALARI = {
    "AA": "Mükemmel",
    "BA": "Çok İyi",
    "BB": "İyi",
    "CB": "Ortalamanın Üstü",
    "CC": "Orta",
    "CD": "Tatmin Edici",
    "DD": "Şartlı Başarılı",
    "DF": "Şartlı Başarılı",
    "F": "Başarısız",
}

CONFIG = _load_ui_config()
GECIS_NOTU = float(CONFIG.get("gecisNotu", 41))
SARTLI_GECIS_NOTU = float(CONFIG.get("sartliGecisNotu", 31))

harf_notu_eslestirmesi = [
    HarfNotu(harf, float(puan), _HARF_ACIKLAMALARI.get(harf, ""))
    for harf, puan in CONFIG.get("harfNotlari", {
        "AA": 91,
        "BA": 81,
        "BB": 71,
        "CB": 61,
        "CC": 51,
        "CD": 41,
        "DD": 36,
        "DF": 31,
        "F": 0,
    }).items()
]


def _validate_score(value: float, name: str) -> None:
    """Puanın 0 ile 100 arasında olduğunu doğrula."""
    if not 0 <= value <= 100:
        raise ValueError(f"{name} değeri 0 ile 100 arasında olmalıdır: {value}")


def ders_ortalama(
    ders: Ders,
    vize: float,
    final: float,
    quiz: float | None = None,
) -> float:
    """Ders notunu ağırlıklı puanlarla hesapla."""
    _validate_score(vize, "Vize")
    _validate_score(final, "Final")

    ortalama = vize * ders.vize + final * ders.final

    if quiz is not None:
        _validate_score(quiz, "Quiz")
        ortalama += quiz * ders.quiz

    return ortalama


def minimum_final_hesapla(
    ders: Ders,
    vize: float,
    gecis_notu: float,
) -> float:
    """
    Verilen vize puanı ve geçiş notu için gerekli minimum final puanını hesapla.

    Args:
        ders: Dersin ağırlıklandırması
        vize: Vize puanı
        gecis_notu: Geçiş notu

    Returns:
        Gerekli minimum final puanı
    """
    _validate_score(vize, "Vize")
    _validate_score(gecis_notu, "Geçiş notu")

    # final_puan * ders.final = gecis_notu - (vize * ders.vize)
    required = (gecis_notu - vize * ders.vize) / ders.final

    # Sonuç 0-100 arasında olmalı
    return max(0, min(100, required))


def harf_notu_bul(puan: float) -> str:
    """Sayısal puanı harf notuna çevir."""
    for harf in sorted(
        harf_notu_eslestirmesi, key=lambda x: x.geçiş_notu, reverse=True
    ):
        if puan >= harf.geçiş_notu:
            return harf.harf
    return "FF"


def minimum_final_harf_icin(
    ders: Ders,
    vize: float,
    hedef_harf: str,
) -> tuple[float | None, bool]:
    """
    Verilen vize puanı için hedef harf notunu almak için gerekli minimum final puanını hesapla.

    Args:
        ders: Dersin ağırlıklandırması
        vize: Vize puanı
        hedef_harf: Hedef harf notu (ör: "BB")

    Returns:
        (gerekli_final_puanı, imkansız_mı) - imkansızsa gerekli_final_puanı None olur
    """
    _validate_score(vize, "Vize")

    # Harf notunun minimum puanını bul
    hedef_puan = None
    for harf in harf_notu_eslestirmesi:
        if harf.harf == hedef_harf:
            hedef_puan = harf.geçiş_notu
            break

    if hedef_puan is None:
        raise ValueError(f"Geçersiz harf notu: {hedef_harf}")

    # Gereken final puanını hesapla
    required = (hedef_puan - vize * ders.vize) / ders.final

    # İmkansız mı diye kontrol et
    if required > 100:
        return (None, True)

    # Negatif olursa 0'a ayarla
    return (max(0, required), False)


def minimum_final_ortalama_icin(
    ders: Ders,
    vize: float,
    hedef_ortalama: float,
) -> tuple[float | None, bool]:
    """
    Verilen vize puanı için hedef ortalamayı almak için gerekli minimum final puanını hesapla.

    Args:
        ders: Dersin ağırlıklandırması
        vize: Vize puanı
        hedef_ortalama: Hedef ortalama puanı (ör: 70.0)

    Returns:
        (gerekli_final_puanı, imkansız_mı) - imkansızsa gerekli_final_puanı None olur
    """
    _validate_score(vize, "Vize")
    _validate_score(hedef_ortalama, "Hedef Ortalama")

    # Gereken final puanını hesapla
    required = (hedef_ortalama - vize * ders.vize) / ders.final

    # İmkansız mı diye kontrol et
    if required > 100:
        return (None, True)

    # Negatif olursa 0'a ayarla
    return (max(0, required), False)


def donem_ortalama(donem: DonemDersleri, notlar: dict[str, DersNotu]) -> float:
    """Dönem ortalamasını ders notlarından hesapla."""
    if not donem.dersler:
        return 0.0

    toplam = sum(
        ders_ortalama(
            ders,
            notlar[ders.ad].vize,
            notlar[ders.ad].final or 0,
            notlar[ders.ad].quiz,
        )
        for ders in donem.dersler
        if ders.ad in notlar and notlar[ders.ad].final is not None
    )

    return toplam / len(donem.dersler)


if __name__ == "__main__":
    # Örnek senaryo
    ders = Ders(ad="Örnek Ders", vize=0.4, final=0.6, quiz=0)
    vize_puani = 20

    print("=" * 60)
    print("FINAL NOTU HESAP MAKİNESİ")
    print("=" * 60)
    print(f"Vize Puanı: {vize_puani}\n")

    # 1. Geçiş notu için gereken minimum final
    print("1. GEÇİŞ NOTU İÇİN GEREKEN MİNİMUM FİNAL")
    print("-" * 60)
    min_final_gecis = minimum_final_hesapla(ders, vize_puani, GECIS_NOTU)
    print(f"   Geçiş Notu: {GECIS_NOTU}")
    print(f"   Gerekli Minimum Final: {min_final_gecis:.2f}")
    print(f"   Harf Notu: {harf_notu_bul(GECIS_NOTU)}\n")

    print("1.1 ŞARTLI GEÇİŞ NOTU İÇİN GEREKEN MİNİMUM FİNAL")
    print("-" * 60)
    min_final_sartli = minimum_final_hesapla(ders, vize_puani, SARTLI_GECIS_NOTU)
    print(f"   Şartlı Geçiş Notu: {SARTLI_GECIS_NOTU}")
    print(f"   Gerekli Minimum Final: {min_final_sartli:.2f}")
    print(f"   Harf Notu: {harf_notu_bul(SARTLI_GECIS_NOTU)}\n")

    # 2. BB (71) için gereken minimum final
    print("2. BB NOTU İÇİN GEREKEN MİNİMUM FİNAL")
    print("-" * 60)
    min_final_bb, imkansiz_bb = minimum_final_harf_icin(ders, vize_puani, "BB")
    if imkansiz_bb:
        print("   ❌ İMKANSIZ - Final 100'den fazla puan gerekli!")
        print("   Teorik olarak gerekli final: ∞")
    else:
        print("   Hedef Harf Notu: BB (71+)")
        print("   Gerekli Minimum Final: {min_final_bb:.2f}")
    print()

    # 3. 70 üstü ortalama için gereken minimum final
    print("3. 70 ÜSTÜ ORTALAMA İÇİN GEREKEN MİNİMUM FİNAL")
    print("-" * 60)
    min_final_70, imkansiz_70 = minimum_final_ortalama_icin(ders, vize_puani, 70.0)
    if imkansiz_70:
        print("   ❌ İMKANSIZ - Final 100'den fazla puan gerekli!")
        print("   Final'de 100 alsanız bile ortalama 70'e ulaşamaz.")
    else:
        print("   Hedef Ortalama: 70+")
        print("   Gerekli Minimum Final: {min_final_70:.2f}")
    print()

    print("=" * 60)
