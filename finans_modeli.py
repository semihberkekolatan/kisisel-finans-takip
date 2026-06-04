"""
finans_modeli.py
----------------
Bu modül, uygulamanın temel nesne modelini tanımlar.
Islem sınıfı; her gelir ve gider kaydını temsil eden nesneyi içerir.
"""


class Islem:
    """
    Bir finansal işlemi (gelir veya gider) temsil eden sınıf.

    Attributes:
        id (int): İşlemin benzersiz kimliği.
        tutar (float): İşlem tutarı.
        tarih (str): İşlem tarihi (YYYY-MM-DD formatında).
        aciklama (str): İşleme ait açıklama.
        tip (str): 'gelir' veya 'gider'.
    """

    def __init__(self, id: int, tutar: float, tarih: str, aciklama: str, tip: str):
        """
        Islem nesnesini başlatır.

        Args:
            id (int): Benzersiz işlem kimliği.
            tutar (float): İşlem tutarı.
            tarih (str): YYYY-MM-DD formatında tarih.
            aciklama (str): İşlem açıklaması.
            tip (str): 'gelir' veya 'gider'.
        """
        self.id = id
        self.tutar = float(tutar)
        self.tarih = tarih
        self.aciklama = aciklama
        self.tip = tip  # 'gelir' veya 'gider'

    def __str__(self) -> str:
        """Işlemi okunabilir formatta döndürür."""
        return (
            f"[{self.id}] {self.tip.upper():6} | "
            f"{self.tarih} | "
            f"{self.tutar:>10.2f} TL | "
            f"{self.aciklama}"
        )

    def to_dict(self) -> dict:
        """
        Işlem nesnesini sözlük (dict) formatına dönüştürür.
        CSV kaydetme işlemlerinde kullanılır.

        Returns:
            dict: İşlem verilerini içeren sözlük.
        """
        return {
            "id": self.id,
            "tutar": self.tutar,
            "tarih": self.tarih,
            "aciklama": self.aciklama,
            "tip": self.tip,
        }
