# Dosya Giriş/Çıkış (I/O) İşlemleri Kılavuzu

TİLK dilinin dosya sistemi ile iletişim kurmasını sağlayan yerleşik I/O fonksiyonları.

## 1. Dosyaya Yazma (`dosya_yaz`)
Belirtilen dosya yoluna metin içeriğini yazar. Dosya yoksa oluşturulur, varsa üzerine yazılır:
```oz
yol = "gunluk.txt";
dosya_yaz(yol, "TİLK dosya yazma testi.\nTarih: 2026.");
```

## 2. Dosyadan Okuma (`dosya_oku`)
Belirtilen dosyadaki tüm veriyi metin (`String`) olarak okur:
```oz
icerik = dosya_oku("gunluk.txt");
yazdır("Dosya İçeriği:\n", icerik);
```

## 3. Dosya Silme (`dosya_sil`)
Belirtilen yolu dosya sisteminden temizler:
```oz
dosya_sil("gunluk.txt");
```
Dosya işlemleri sırasında oluşabilecek OS hataları VM düzeyinde yakalanabilir.
