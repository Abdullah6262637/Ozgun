# Ariadne ile Görsel Hata Raporlama Sistemi

TİLK dilinin hata raporlama yeteneklerinin detaylı analizi.

## 1. Ariadne Entegrasyonu
Hataların terminalde görsel olarak sunulması için Rust'ın popüler `ariadne` diagnostik raporlama kütüphanesi kullanılmıştır.

## 2. Görsel Hata Yapısı
Hata oluştuğunda terminale şu şablonda çıktı üretilir:
- Hatanın kısa açıklaması ve hata kodu.
- Hatanın oluştuğu dosya adı, satır ve sütun numaraları.
- Hatalı kod bloğunun görselleştirilmiş hali ve hatanın tam yerini işaret eden oklar.

Bu sayede geliştirici karmaşık hata logları arasında kaybolmadan hatayı saniyeler içinde düzeltebilir.
