# Zaman Yönetimi: şimdi ve uyku

TİLK dilinde zaman ölçümü ve thread duraklatma işlemleri.

## 1. Unix Zaman Damgası (`şimdi`)
`şimdi()` veya `simdi()` fonksiyonu, sistemin o anki milisaniye cinsinden Unix epoch zaman damgasını döner:
```oz
baslangic = şimdi();
uyku(500); // yarım saniye duraklat
bitis = şimdi();

yazdır("Geçen süre:", bitis - baslangic, "milisaniye");
```

## 2. Geciktirme (`uyku`)
Milisaniye cinsinden belirtilen süre boyunca thread yürütmesini tamamen duraklatır:
```oz
yazdır("Başlatılıyor...");
uyku(2000); // 2 saniye bekler
yazdır("2 saniye geçti.");
```
