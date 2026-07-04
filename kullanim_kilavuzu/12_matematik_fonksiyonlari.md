# Yerleşik Matematiksel Fonksiyonlar Kılavuzu

TİLK sayısal analizler için optimize edilmiş dahili matematiksel opkodlara sahiptir.

## 1. Karekök (`kök`)
Bir sayının karekökünü hesaplar. Negatif değer verilirse çalışma zamanı hatası fırlatır:
```oz
yazdır(kök(9)); // 3.0
yazdır(karekok(100)); // 10.0 (karekok alias'ı mevcuttur)
```

## 2. Üs Alma (`üs`)
Tabanın, üs derecesinden kuvvetini hesaplar:
```oz
yazdır(üs(2, 8)); // 256.0
yazdır(ust(5, 3)); // 125.0 (ust alias'ı mevcuttur)
```

## 3. Mutlak Değer (`mutlak`)
Negatif veya pozitif sayıların işaretsiz mutlak değerini döner:
```oz
yazdır(mutlak(-42.5)); // 42.5
```
