# Diziler ve Haritalar: Veri Yapıları Kılavuzu

TİLK, dinamik veri yapılarını referans tipleri olarak yönetir.

## 1. Diziler (Arrays)
Diziler köşeli parantezler `[...]` ile tanımlanır ve sıfır tabanlı indeksleme kullanır:
```oz
dizi = [10, 20, 30];
yazdır(dizi[0]); // 10

// Eleman güncelleme
dizi[1] = 99;

// Dahili fonksiyonlar
ekle(dizi, 40); // dizi sonuna 40 ekler
yazdır("Boyut:", boyut(dizi)); // 4
```

## 2. Haritalar (Maps)
Haritalar anahtar-değer (key-value) çiftlerini depolar. Anahtarlar her zaman metindir:
```oz
harita = {"ad": "Tilk", "surum": "1.0"};
yazdır(harita["ad"]); // Tilk

// Yeni anahtar ekleme veya güncelleme
harita["yas"] = 4;
yazdır(boyut(harita)); // 3
```
Harita ve diziler Heap üzerinde barındırılır ve `Rc<RefCell<...>>` ile paylaşımlı referans olarak yönetilirler.
