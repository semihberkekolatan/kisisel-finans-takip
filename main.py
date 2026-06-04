"""
main.py
-------
Kişisel Finans ve Harcama Takip Sistemi — Ana Uygulama Modülü.

Bu dosya; tüm modülleri bir araya getirerek kullanıcının
konsol menüsü üzerinden sistemi kullanmasını sağlar.

Kullanım:
    python main.py
"""

from utils           import menu_goster, sayi_kontrol
from islem_yonetimi  import gelir_ekle, gider_ekle, islemleri_listele, islem_sil
from dosya_islemleri import csv_kaydet, csv_oku
from analiz          import (verileri_dataframe_yap, toplam_gelir_gider,
                              aylik_analiz, numpy_istatistik)
from gorsellestirme  import aylik_grafik, gelir_gider_bar, pasta_grafik

# --------------------------------------------------------------------------- #
# Uygulama başlangıcında CSV'den veri yükle (varsa)
CSV_DOSYASI = "finans_verileri.csv"

gelirler, giderler = csv_oku(CSV_DOSYASI)
# --------------------------------------------------------------------------- #


def csv_menu() -> None:
    """CSV alt menüsünü yönetir: kaydet veya yükle."""
    print("\n--- 💾 CSV İşlemleri ---")
    print("  1. Kaydet")
    print("  2. Dosyadan Yükle")
    secim = input("Seçiminiz: ").strip()

    if secim == "1":
        csv_kaydet(CSV_DOSYASI, gelirler, giderler)
    elif secim == "2":
        yeni_gelirler, yeni_giderler = csv_oku(CSV_DOSYASI)
        gelirler.clear()
        giderler.clear()
        gelirler.extend(yeni_gelirler)
        giderler.extend(yeni_giderler)
    else:
        print("⚠️  Geçersiz seçim.")


def grafik_menu(df) -> None:
    """Grafik alt menüsünü yönetir."""
    if df.empty:
        print("⚠️  Grafik için önce işlem ekleyin.")
        return

    print("\n--- 📊 Grafik Seç ---")
    print("  1. Aylık Çizgi Grafik")
    print("  2. Gelir/Gider Sütun Grafik")
    print("  3. Pasta Grafik")
    print("  4. Tüm Grafikler")
    secim = input("Seçiminiz: ").strip()

    if secim == "1":
        aylik_grafik(df)
    elif secim == "2":
        gelir_gider_bar(df)
    elif secim == "3":
        pasta_grafik(df)
    elif secim == "4":
        aylik_grafik(df)
        gelir_gider_bar(df)
        pasta_grafik(df)
    else:
        print("⚠️  Geçersiz seçim.")


def main() -> None:
    """Ana döngü: menüyü gösterir ve kullanıcı seçimine göre ilgili fonksiyonu çağırır."""
    print("\n🚀 Kişisel Finans Takip Sistemine Hoş Geldiniz!")

    while True:
        menu_goster()
        secim = input("Seçiminiz (1-7): ").strip()

        if secim == "1":
            gelir_ekle(gelirler)

        elif secim == "2":
            gider_ekle(giderler)

        elif secim == "3":
            islemleri_listele(gelirler, giderler)

        elif secim == "4":
            df = verileri_dataframe_yap(gelirler, giderler)
            toplam_gelir_gider(df)
            aylik_analiz(df)
            numpy_istatistik(df)

        elif secim == "5":
            df = verileri_dataframe_yap(gelirler, giderler)
            grafik_menu(df)

        elif secim == "6":
            csv_menu()

        elif secim == "7":
            # Çıkışta otomatik kaydet
            csv_kaydet(CSV_DOSYASI, gelirler, giderler)
            print("\n👋 Güle güle! Veriler kaydedildi.")
            break

        else:
            print("⚠️  Lütfen 1-7 arasında bir seçim yapın.")


# ------------------------------------------------------------------ #
if __name__ == "__main__":
    main()
