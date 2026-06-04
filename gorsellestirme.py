"""
gorsellestirme.py
-----------------
Veri görselleştirme modülü.
Matplotlib & Seaborn kullanarak çizgi, sütun ve pasta grafikleri üretir.
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import pandas as pd

# Genel stil ayarları
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (10, 5)
plt.rcParams["font.family"] = "DejaVu Sans"


def _grafik_kaydet(dosya_adi: str) -> None:
    """Grafiği PNG olarak kaydeder ve ekranda gösterir."""
    plt.tight_layout()
    plt.savefig(dosya_adi, dpi=150, bbox_inches="tight")
    plt.show()
    print(f"💾 Grafik '{dosya_adi}' olarak kaydedildi.")


def aylik_grafik(df: pd.DataFrame) -> None:
    """
    Aylık gelir ve giderleri karşılaştıran çizgi grafiği oluşturur.
    Her ay için gelir (yeşil) ve gider (kırmızı) çizgilerini gösterir.

    Args:
        df (pd.DataFrame): Analiz modülünün oluşturduğu aylık özet DataFrame
                           ya da ham işlem DataFrame'i.
    """
    if df.empty:
        print("⚠️  Çizgi grafik için yeterli veri yok.")
        return

    ozet = (
        df.groupby(["ay", "tip"])["tutar"]
        .sum()
        .unstack(fill_value=0)
    )

    fig, ax = plt.subplots()
    if "gelir" in ozet.columns:
        ax.plot(ozet.index.astype(str), ozet["gelir"],
                marker="o", color="#2ecc71", linewidth=2.5, label="Gelir")
    if "gider" in ozet.columns:
        ax.plot(ozet.index.astype(str), ozet["gider"],
                marker="s", color="#e74c3c", linewidth=2.5, label="Gider")

    ax.set_title("Aylık Gelir & Gider Karşılaştırması", fontsize=14, fontweight="bold")
    ax.set_xlabel("Ay")
    ax.set_ylabel("Tutar (TL)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    ax.legend()
    plt.xticks(rotation=30)
    _grafik_kaydet("aylik_grafik.png")


def gelir_gider_bar(df: pd.DataFrame) -> None:
    """
    Toplam gelir ve gider değerlerini karşılaştıran sütun (bar) grafiği oluşturur.

    Args:
        df (pd.DataFrame): İşlemleri içeren ham DataFrame.
    """
    if df.empty:
        print("⚠️  Sütun grafik için yeterli veri yok.")
        return

    toplam = df.groupby("tip")["tutar"].sum().reindex(["gelir", "gider"], fill_value=0)
    renkler = ["#2ecc71", "#e74c3c"]
    etiketler = ["Gelir", "Gider"]

    fig, ax = plt.subplots()
    bars = ax.bar(etiketler, toplam.values, color=renkler, width=0.4, edgecolor="white")

    # Çubuk üstüne değer yaz
    for bar, deger in zip(bars, toplam.values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max(toplam.values) * 0.01,
            f"{deger:,.2f} TL",
            ha="center", va="bottom", fontsize=11, fontweight="bold"
        )

    ax.set_title("Toplam Gelir & Gider", fontsize=14, fontweight="bold")
    ax.set_ylabel("Tutar (TL)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    _grafik_kaydet("gelir_gider_bar.png")


def pasta_grafik(df: pd.DataFrame) -> None:
    """
    Gelir ve gider oranlarını gösteren pasta (pie) grafiği oluşturur.

    Args:
        df (pd.DataFrame): İşlemleri içeren ham DataFrame.
    """
    if df.empty:
        print("⚠️  Pasta grafik için yeterli veri yok.")
        return

    toplam = df.groupby("tip")["tutar"].sum().reindex(["gelir", "gider"], fill_value=0)

    if toplam.sum() == 0:
        print("⚠️  Toplam tutar sıfır; pasta grafik oluşturulamadı.")
        return

    renkler  = ["#2ecc71", "#e74c3c"]
    etiketler = ["Gelir", "Gider"]
    patlama  = [0.05, 0.05]  # hafif çıkıntı efekti

    fig, ax = plt.subplots()
    ax.pie(
        toplam.values,
        labels=etiketler,
        colors=renkler,
        autopct="%1.1f%%",
        startangle=90,
        explode=patlama,
        shadow=True,
        textprops={"fontsize": 12}
    )
    ax.set_title("Gelir / Gider Oranları", fontsize=14, fontweight="bold")
    _grafik_kaydet("pasta_grafik.png")
