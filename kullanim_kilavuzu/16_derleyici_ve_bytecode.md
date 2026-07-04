# Bayt Kodu Derleyicisi (Compiler) Mimarisi

`oz-vm` içerisindeki `compiler.rs` modülü, AST'yi VM bayt kodlarına dönüştürür.

## 1. Değişken Çözümleme ve scopes Yığını
Derleyici, yerel değişkenlerin isimlerini `scopes: Vec<HashMap<String, u16>>` yığınında tutar. Bir değişken yazıldığında veya okunduğunda scope yığını taranarak yerel slot indeksi (`u16`) atanır. Bulunamazsa global olarak işaretlenir.

## 2. Kod Üretimi (Code Generation)
AST düğümleri özyinelemeli olarak taranarak doğrusal opkod listesine dönüştürülür:
- Koşul blokları için conditional jump'lar.
- Döngüler için geri atlama jump'ları.
- İşlev çağrıları için parametre hazırlama ve `Call` talimatları.
