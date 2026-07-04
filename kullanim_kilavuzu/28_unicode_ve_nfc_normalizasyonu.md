# Unicode ve NFC Harf Normalizasyonu Kuralları

Türkçe karakterlerin büyük/küçük harf dönüşümlerindeki kararsızlıkların çözümü.

## 1. Türkçe I/İ Harf Problemi
ASCII tabanlı sistemlerde büyük `İ` harfi küçük harfe dönüştürülürken noktalı `i` yapılamaz. TİLK bu sorunu özel `turkish_lowercase` fonksiyonu ile aşar.

## 2. Unicode Normalizasyonu
Karakterlerin uyuşmazlık yaratmaması için tüm kod metni sözcüksel analiz öncesinde `unicode-normalization` kütüphanesi kullanılarak NFC (Normalization Form Canonical Composition) formatına dönüştürülür.
