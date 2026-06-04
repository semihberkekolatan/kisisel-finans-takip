"""
dosya_islemleri.py
------------------
CSV dosyası okuma ve yazma işlemlerini yöneten modül.
Verilerin kalıcı olarak saklanmasını ve geri yüklenmesini sağlar.
"""

import csv
from finans_modeli import Islem


# CSV dosyasındaki sütun başlıkları
SUTUNLAR = ["id", "tutar", "tarih", "aciklama", "tip"]


def csv_kaydet(dosya_adi: str, gelirler: list, giderler: list) -> None:
    """
    Tüm gelir ve gider verilerini belirtilen CSV dosyasına kaydeder.

    Args:
        dosya_adi (str): Kaydedilecek CSV dosyasının adı (örn. 'veriler.csv').
        gelirler (list): Gelir Islem nesnelerinin listesi.
        giderler (list): Gider Islem nesnelerinin listesi.
    """
    try:
        tum_islemler = gelirler + giderler

        with open(dosya_adi, mode="w", newline="", encoding="utf-8") as dosya:
            yazici = csv.DictWriter(dosya, fieldnames=SUTUNLAR)
            yazici.writeheader()

            for islem in tum_islemler:
                yazici.writerow(islem.to_dict())

        print(f"✅ {len(tum_islemler)} işlem '{dosya_adi}' dosyasına kaydedildi.")

    except IOError as e:
        print(f"❌ Dosya yazma hatası: {e}")


def csv_oku(dosya_adi: str) -> tuple[list, list]:
    """
    CSV dosyasındaki verileri okuyarak gelir ve gider listelerini oluşturur.

    Args:
        dosya_adi (str): Okunacak CSV dosyasının adı.

    Returns:
        tuple[list, list]: (gelirler, giderler) şeklinde iki liste döndürür.
                           Dosya bulunamazsa boş listeler döner.
    """
    gelirler = []
    giderler = []

    try:
        with open(dosya_adi, mode="r", newline="", encoding="utf-8") as dosya:
            okuyucu = csv.DictReader(dosya)

            for satir in okuyucu:
                islem = Islem(
                    id=int(satir["id"]),
                    tutar=float(satir["tutar"]),
                    tarih=satir["tarih"],
                    aciklama=satir["aciklama"],
                    tip=satir["tip"]
                )

                if islem.tip == "gelir":
                    gelirler.append(islem)
                elif islem.tip == "gider":
                    giderler.append(islem)

        print(f"✅ '{dosya_adi}' dosyasından {len(gelirler)} gelir, "
              f"{len(giderler)} gider yüklendi.")

    except FileNotFoundError:
        print(f"⚠️  '{dosya_adi}' bulunamadı. Boş listeler ile devam ediliyor.")
    except Exception as e:
        print(f"❌ Dosya okuma hatası: {e}")

    return gelirler, giderler
