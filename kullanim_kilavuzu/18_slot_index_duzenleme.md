# Lokal Değişken Slot-Index Optimizasyon Belgesi

Yerel değişken erişimlerindeki performans artışının detayları.

## 1. Eski HashMap Tabanlı Çözüm
Eski mimaride, her fonksiyon çağrısında yerel değişkenler string anahtarlı bir `HashMap` içinde saklanıyordu. Bu durum:
- Her değişken okuma/yazma işleminde string hashing maliyetine yol açıyordu.
- Değişkenlerin Heap üzerinde sürekli tahsis edilmesini (allocation) gerektiriyordu.

## 2. Yeni Slot-Index Çözümü
- Derleme aşamasında yerel değişkenlere `0`, `1`, `2` gibi slot numaraları atanır.
- VM Frame yapısında `slots: Vec<Val>` tutulur.
- Değişken erişimleri `LoadLocal(slot)` ve `StoreLocal(slot)` opkodları ile doğrudan dizi erişimi hızında O(1) olarak gerçekleştirilir.
