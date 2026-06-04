"""
analiz.py
---------
Veri analizi modülü.
Pandas DataFrame işlemleri ve NumPy istatistiksel hesaplamaları içerir.
"""

import numpy as np
import pandas as pd


def verileri_dataframe_yap(gelirler: list, giderler: list) -> pd.DataFrame:
    """
    Gelir ve gider listelerini birleştirerek pandas DataFrame yapısına dönüştürür.

    Args:
        gelirler (list): Gelir Islem nesnelerinin listesi.
        giderler (list): Gider Islem nesnelerinin listesi.

    Returns:
        pd.DataFrame: Tüm işlemleri içeren DataFrame.
                      Sütunlar: id, tutar, tarih, aciklama, tip
    """
    tum_islemler = gelirler + giderler

    if not tum_islemler:
        print("⚠️  Analiz yapılacak veri bulunamadı.")
        return pd.DataFrame(columns=["id", "tutar", "tarih", "aciklama", "tip"])

    satirlar = [islem.to_dict() for islem in tum_islemler]
    df = pd.DataFrame(satirlar)

    # Tarih sütununu datetime tipine çevir ve ay sütunu ekle
    df["tarih"] = pd.to_datetime(df["tarih"])
    df["ay"] = df["tarih"].dt.to_period("M")

    return df


def toplam_gelir_gider(df: pd.DataFrame) -> dict:
    """
    DataFrame üzerinden toplam gelir, toplam gider ve net bakiye hesaplar.

    Args:
        df (pd.DataFrame): İşlemleri içeren DataFrame.

    Returns:
        dict: {'toplam_gelir', 'toplam_gider', 'net_bakiye'} anahtarlı sözlük.
    """
    if df.empty:
        return {"toplam_gelir": 0.0, "toplam_gider": 0.0, "net_bakiye": 0.0}

    toplam_gelir = df[df["tip"] == "gelir"]["tutar"].sum()
    toplam_gider = df[df["tip"] == "gider"]["tutar"].sum()
    net_bakiye   = toplam_gelir - toplam_gider

    print("\n📊 FİNANSAL ÖZET")
    print("-" * 35)
    print(f"  Toplam Gelir  : {toplam_gelir:>10.2f} TL")
    print(f"  Toplam Gider  : {toplam_gider:>10.2f} TL")
    print(f"  Net Bakiye    : {net_bakiye:>10.2f} TL  {'✅' if net_bakiye >= 0 else '⚠️'}")

    return {
        "toplam_gelir": float(toplam_gelir),
        "toplam_gider": float(toplam_gider),
        "net_bakiye":   float(net_bakiye),
    }


def aylik_analiz(df: pd.DataFrame) -> pd.DataFrame:
    """
    Verileri tarihe göre gruplayarak aylık bazda özet analiz oluşturur.

    Args:
        df (pd.DataFrame): İşlemleri içeren DataFrame.

    Returns:
        pd.DataFrame: Aylık gelir/gider/bakiye özetini içeren DataFrame.
    """
    if df.empty:
        print("⚠️  Aylık analiz için veri yok.")
        return pd.DataFrame()

    ozet = (
        df.groupby(["ay", "tip"])["tutar"]
        .sum()
        .unstack(fill_value=0)
        .rename(columns={"gelir": "Gelir (TL)", "gider": "Gider (TL)"})
    )

    # Eksik sütunları sıfır ile doldur
    for sutun in ["Gelir (TL)", "Gider (TL)"]:
        if sutun not in ozet.columns:
            ozet[sutun] = 0.0

    ozet["Net Bakiye (TL)"] = ozet["Gelir (TL)"] - ozet["Gider (TL)"]

    print("\n📅 AYLIK ANALİZ")
    print("-" * 55)
    print(ozet.to_string())

    return ozet


def numpy_istatistik(df: pd.DataFrame) -> dict:
    """
    NumPy kullanarak tutar verisi üzerinde temel istatistiksel
    hesaplamalar yapar (ortalama, min, max, standart sapma).

    Args:
        df (pd.DataFrame): İşlemleri içeren DataFrame.

    Returns:
        dict: {'ortalama', 'minimum', 'maksimum', 'std_sapma'} anahtarlı sözlük.
    """
    if df.empty:
        print("⚠️  İstatistik için veri yok.")
        return {}

    tutarlar = np.array(df["tutar"].tolist())

    ortalama  = np.mean(tutarlar)
    minimum   = np.min(tutarlar)
    maksimum  = np.max(tutarlar)
    std_sapma = np.std(tutarlar)

    print("\n📈 NUMPY İSTATİSTİKLERİ (Tüm İşlemler)")
    print("-" * 40)
    print(f"  Ortalama Tutar   : {ortalama:>10.2f} TL")
    print(f"  Minimum Tutar    : {minimum:>10.2f} TL")
    print(f"  Maksimum Tutar   : {maksimum:>10.2f} TL")
    print(f"  Standart Sapma   : {std_sapma:>10.2f} TL")

    return {
        "ortalama":  float(ortalama),
        "minimum":   float(minimum),
        "maksimum":  float(maksimum),
        "std_sapma": float(std_sapma),
    }
