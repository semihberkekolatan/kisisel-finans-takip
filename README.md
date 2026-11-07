# 💰 Kişisel Finans ve Harcama Takip Sistemi

**Öğrenci Adı Soyadı:** Semih Berke Kolatan  
**Öğrenci Numarası:** 24097002  
**Bölüm:** Bilişim Sistemleri Ve Teknolojileri  
**Ders:** BGY210 – Python Programlama II  
**Öğretim Elemanı:** Dr. Öğr. Üyesi Tohid YOUSEFİ  
**Dönem:** 2025–2026 Bahar  

---

## 🔗 GitHub Repo
https://github.com/semihberkekolatan/kisisel-finans-takip

---

## 📋 Proje Açıklaması

Bu uygulama, kullanıcıların gelir ve giderlerini kolayca kayıt altına almasını,
tüm işlemleri listelemesini, Pandas & NumPy ile finansal analiz yapmasını
ve Matplotlib/Seaborn grafikleriyle sonuçları görselleştirmesini sağlayan
konsol tabanlı bir Python uygulamasıdır.

---

## 📁 Proje Yapısı

```
AdSoyad_24097002_Bolum/
├── main.ipynb            ← Jupyter Notebook (ana çalıştırma dosyası)
├── main.py               ← Konsol uygulaması
├── finans_modeli.py      ← Islem sınıfı (OOP)
├── utils.py              ← Yardımcı fonksiyonlar
├── islem_yonetimi.py     ← Gelir/gider işlemleri
├── dosya_islemleri.py    ← CSV okuma/yazma
├── analiz.py             ← Pandas & NumPy analizleri
├── gorsellestirme.py     ← Grafikler
├── finans_verileri.csv   ← Veri çıktısı
├── aylik_grafik.png      ← Grafik çıktısı
├── gelir_gider_bar.png   ← Grafik çıktısı
├── pasta_grafik.png      ← Grafik çıktısı
└── README.md             ← Bu dosya
```

---

## ⚙️ Kurulum ve Çalıştırma

```bash
# Gerekli kütüphaneleri yükle
pip install numpy pandas matplotlib seaborn

# Uygulamayı başlat
python main.py
```

---

## 🏗️ Kullanılan Veri Yapıları

| Yapı | Kullanım Yeri |
|---|---|
| `list` (gelirler, giderler) | İşlem nesnelerini saklamak |
| `Islem` nesnesi (OOP) | Her gelir/gider kaydı |
| `pandas.DataFrame` | Analiz ve gruplama |
| `numpy.ndarray` | İstatistiksel hesaplamalar |
| `dict` | CSV satırı ve JSON benzeri veri |
| `csv.DictReader/Writer` | Dosya okuma/yazma |

---

## 📊 Özellikler

- ✅ Gelir & gider ekleme (doğrulama ile)
- ✅ İşlem listeleme ve silme
- ✅ CSV kaydet / yükle
- ✅ Aylık analiz (Pandas)
- ✅ İstatistik (NumPy: ort, min, max, std)
- ✅ 3 farklı grafik türü (çizgi, sütun, pasta)
- ✅ Hata yönetimi (try-except)
- ✅ Modüler yapı (7 dosya)
- ✅ Clean Code & docstring
