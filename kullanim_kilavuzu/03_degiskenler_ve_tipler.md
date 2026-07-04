# Değişkenler, Değerler ve Tilk Tip Sistemi

TİLK, dinamik tipli bir dil olmakla birlikte arka planda güçlü bir statik tip çıkarım ve unification (birleştirme) mekanizması barındırır.

## 1. Değişken Tanımlama ve Kapsam (Scope)
Değişkenler ilk atama yapıldıkları anda declare edilirler. Değişken isimleri Unicode uyumludur:
```oz
sayı = 100;
metin = "Tilk Dili";
noktalı_sayı = 3.14;
```
Yerel değişkenler fonksiyon scope'u içinde geçerlidir. `compiler.rs` yerel değişkenleri slot indekslerine çözümlerken, global değişkenler çalışma zamanında isim tabanlı aranır.

## 2. Veri Tipleri (Val Tipleri)
VM ve Yorumlayıcı düzeyinde şu temel veri tipleri işlenir:
1. **Sayı (`Number`)**: 64-bit kayan noktalı (double-precision) IEEE 754 sayılarıdır.
2. **Metin (`String`)**: UTF-8 formatında byte dizileridir. Kaçış karakterlerini (`\n`, `\t` vb.) destekler.
3. **Boolean**: Mantıksal `doğru` ve `yanlış` değerleridir.
4. **Boş (`Bos`)**: Değerin olmadığını veya fonksiyonun hiçbir şey döndürmediğini ifade eder.
5. **Dizi (`Array`)**: Dinamik yığın bellek (heap) üzerinde Rc<RefCell<Vec<Val>>> olarak tutulan koleksiyonlardır.
6. **Harita (`Map`)**: Anahtarları metin olan Rc<RefCell<HashMap<String, Val>>> koleksiyonlarıdır.
