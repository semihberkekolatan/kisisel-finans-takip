"""
utils.py
--------
Yardımcı (utility) fonksiyonlar modülü.
ID üretimi, tarih/sayı doğrulama ve menü gösterimi gibi
genel amaçlı fonksiyonları içerir.
"""

from datetime import datetime


def yeni_id_olustur(liste: list) -> int:
    """
    Verilen listedeki en büyük ID'yi bulup 1 artırarak
    yeni ve benzersiz bir ID döndürür.

    Args:
        liste (list): Islem nesnelerinden oluşan liste.

    Returns:
        int: Yeni benzersiz ID değeri.
    """
    if not liste:
        return 1
    return max(islem.id for islem in liste) + 1


def tarih_kontrol(tarih: str) -> bool:
    """
    Girilen tarihin YYYY-MM-DD formatında olup olmadığını kontrol eder.

    Args:
        tarih (str): Kontrol edilecek tarih dizgesi.

    Returns:
        bool: Format doğruysa True, değilse False.
    """
    try:
        datetime.strptime(tarih, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def sayi_kontrol(deger: str) -> bool:
    """
    Kullanıcıdan alınan değerin sayıya (float) dönüştürülüp
    dönüştürülemeyeceğini kontrol eder.

    Args:
        deger (str): Kontrol edilecek değer.

    Returns:
        bool: Sayıya çevrilebiliyorsa True, değilse False.
    """
    try:
        float(deger)
        return True
    except ValueError:
        return False


def menu_goster() -> None:
    """
    Programın ana menüsünü ekrana yazdırır.
    """
    print("\n" + "=" * 45)
    print("   💰  KİŞİSEL FİNANS TAKİP SİSTEMİ  💰")
    print("=" * 45)
    print("  1. Gelir Ekle")
    print("  2. Gider Ekle")
    print("  3. İşlemleri Listele")
    print("  4. Analiz Yap")
    print("  5. Grafik Göster")
    print("  6. CSV Kaydet / Yükle")
    print("  7. Çıkış")
    print("=" * 45)
