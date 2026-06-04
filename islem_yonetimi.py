"""
islem_yonetimi.py
-----------------
Gelir ve gider işlemlerinin yönetildiği modül.
Kayıt ekleme, listeleme ve silme fonksiyonlarını içerir.
"""

from finans_modeli import Islem
from utils import yeni_id_olustur, tarih_kontrol, sayi_kontrol


def gelir_ekle(gelirler: list) -> None:
    """
    Kullanıcıdan alınan bilgileri doğrulayarak yeni bir gelir kaydı
    oluşturur ve gelirler listesine ekler.

    Args:
        gelirler (list): Mevcut gelir işlemlerinin listesi.
    """
    print("\n--- 💚 Gelir Ekle ---")

    # Tutar al ve doğrula
    while True:
        tutar_str = input("Tutar (TL): ").strip()
        if sayi_kontrol(tutar_str) and float(tutar_str) > 0:
            tutar = float(tutar_str)
            break
        print("⚠️  Geçerli bir pozitif sayı girin.")

    # Tarih al ve doğrula
    while True:
        tarih = input("Tarih (YYYY-MM-DD): ").strip()
        if tarih_kontrol(tarih):
            break
        print("⚠️  Tarih formatı hatalı. Örnek: 2026-06-01")

    # Açıklama al
    aciklama = input("Açıklama: ").strip()
    if not aciklama:
        aciklama = "Açıklama yok"

    # Yeni ID üret ve nesne oluştur
    yeni_id = yeni_id_olustur(gelirler)
    yeni_islem = Islem(
        id=yeni_id,
        tutar=tutar,
        tarih=tarih,
        aciklama=aciklama,
        tip="gelir"
    )
    gelirler.append(yeni_islem)
    print(f"✅ Gelir kaydedildi → {yeni_islem}")


def gider_ekle(giderler: list) -> None:
    """
    Kullanıcıdan alınan bilgileri doğrulayarak yeni bir gider kaydı
    oluşturur ve giderler listesine ekler.

    Args:
        giderler (list): Mevcut gider işlemlerinin listesi.
    """
    print("\n--- 🔴 Gider Ekle ---")

    while True:
        tutar_str = input("Tutar (TL): ").strip()
        if sayi_kontrol(tutar_str) and float(tutar_str) > 0:
            tutar = float(tutar_str)
            break
        print("⚠️  Geçerli bir pozitif sayı girin.")

    while True:
        tarih = input("Tarih (YYYY-MM-DD): ").strip()
        if tarih_kontrol(tarih):
            break
        print("⚠️  Tarih formatı hatalı. Örnek: 2026-06-01")

    aciklama = input("Açıklama: ").strip()
    if not aciklama:
        aciklama = "Açıklama yok"

    yeni_id = yeni_id_olustur(giderler)
    yeni_islem = Islem(
        id=yeni_id,
        tutar=tutar,
        tarih=tarih,
        aciklama=aciklama,
        tip="gider"
    )
    giderler.append(yeni_islem)
    print(f"✅ Gider kaydedildi → {yeni_islem}")


def islemleri_listele(gelirler: list, giderler: list) -> None:
    """
    Tüm gelir ve gider kayıtlarını düzenli bir formatta ekrana yazdırır.
    Listelerin her ikisi de boşsa bilgi mesajı gösterir.

    Args:
        gelirler (list): Gelir işlemlerinin listesi.
        giderler (list): Gider işlemlerinin listesi.
    """
    print("\n" + "=" * 55)
    print(" 📋 TÜM İŞLEMLER")
    print("=" * 55)

    if gelirler:
        print("\n💚 GELİRLER:")
        print("-" * 55)
        for islem in gelirler:
            print(f"  {islem}")
    else:
        print("\n💚 Henüz gelir kaydı yok.")

    if giderler:
        print("\n🔴 GİDERLER:")
        print("-" * 55)
        for islem in giderler:
            print(f"  {islem}")
    else:
        print("\n🔴 Henüz gider kaydı yok.")

    # Özet satırı
    toplam_gelir = sum(i.tutar for i in gelirler)
    toplam_gider = sum(i.tutar for i in giderler)
    bakiye = toplam_gelir - toplam_gider
    print("\n" + "=" * 55)
    print(f"  Toplam Gelir : {toplam_gelir:>10.2f} TL")
    print(f"  Toplam Gider : {toplam_gider:>10.2f} TL")
    print(f"  Net Bakiye   : {bakiye:>10.2f} TL  {'✅' if bakiye >= 0 else '⚠️'}")
    print("=" * 55)


def islem_sil(gelirler: list, giderler: list, islem_id: int) -> bool:
    """
    Verilen ID'ye sahip işlemi ilgili listeden siler.

    Args:
        gelirler (list): Gelir işlemlerinin listesi.
        giderler (list): Gider işlemlerinin listesi.
        islem_id (int): Silinecek işlemin ID'si.

    Returns:
        bool: Silme başarılıysa True, kayıt bulunamazsa False.
    """
    # Önce gelirlerde ara
    for islem in gelirler:
        if islem.id == islem_id:
            gelirler.remove(islem)
            print(f"✅ Gelir kaydı silindi → ID: {islem_id}")
            return True

    # Bulunamazsa giderlerde ara
    for islem in giderler:
        if islem.id == islem_id:
            giderler.remove(islem)
            print(f"✅ Gider kaydı silindi → ID: {islem_id}")
            return True

    print(f"⚠️  ID {islem_id} ile eşleşen kayıt bulunamadı.")
    return False
