# Tip Sistemi ve Hindley-Milner Algoritması

TİLK statik tip doğruluğunu garanti altına almak için HM tip çıkarım algoritmasını kullanır.

## 1. Unification (Birleştirme)
Tip denetleyicisi, programdaki ifadelerin tiplerini denklemler kurarak çözümler. Örneğin:
- `a + b` işleminde `a` ve `b` tiplerinin birbiriyle uyuşması gerekir.
- Koşullu ifadelerin (`ise`) koşul tipi her zaman `Boolean` olmak zorundadır.

## 2. Tip Çıkarımı Örneği
```oz
x = 5; // Tip: Number
y = "test"; // Tip: String
z = x + y; // HATA: Tip Hatası: Toplama işlemi uyuşmayan tipler arasında yapılamaz.
```
Tip denetimi hatası oluştuğunda program derlenmez ve VM'e gönderilmez.
