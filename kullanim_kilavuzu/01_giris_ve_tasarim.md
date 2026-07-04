# TİLK Dili Giriş ve Dil Tasarım Felsefesi

TİLK (Türkçe İşlevsel Logotetik Kod), programlama dilleri tarihindeki "kelime çevirisi yerelleştirme" yaklaşımını tamamen reddeden özgün bir dil tasarımı felsefesine sahiptir.

## 1. Dilbilimsel Temeller ve Sondan Eklemeli Yapı
Türkçe, sondan eklemeli (aglütinatif) bir dil ailesine mensuptur. Bu dilde yeni kavramlar ve mantıksal ilişkiler, köklere getirilen yapım ve çekim ekleri ile kurulur. Klasik diller (C, Java, Python) ise bükümlü veya analitik dil ailelerinin düşünce yapısına (SVO: Özne-Yüklem-Nesne) göre tasarlanmıştır.

TİLK, Türkçenin bu sondan eklemeli gücünü programlama mantığının merkezine yerleştirir:
- **Şart Kipi (`-ise / -se`)**: Koşul blokları, cümlenin sonunda yer alan şart eki ile tetiklenir.
- **Zarf-Fiiller (`-iken`)**: Eylemin devamlılığı ve döngüsel süreçler `-iken` ekiyle yönetilir.
- **Yönelme/Ayrılma (`-den ... -e dek`)**: Aralık döngüleri, sayıların yönünü ve sınırını eklerle belirler.

## 2. Neden Kelime Çevirisi Değil?
Mevcut Türkçe dil denemeleri (TPD, Karamel vb.) sadece anahtar kelimeleri Türkçeleştirir:
```python
# Diğer diller (İngilizce mantıklı Türkçe kelimeler)
eğer x > 5 ise:
    döndür doğru
```
TİLK ise tümce yapısını Türkçe düşünme şekline göre kurar:
```oz
# TİLK Mantığı
x > 5 ise {
    döndür doğru;
}
```
Bu tasarım, yazılımcının algoritmayı kafasında kurarken Türkçe iç konuşma diline en yakın şekilde kodlamasına olanak tanır.
