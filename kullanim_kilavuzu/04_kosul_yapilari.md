# Koşullu İfadeler: ise, se ve değilse Yapısı

TİLK koşul yapıları, dilde Türkçe mantığının en belirgin olduğu yerlerden biridir.

## 1. Temel Yapı ve Sözdizimi
Şart cümleleri `ise` veya `se` ekiyle sonlanır:
```oz
sayı = 8;
sayı > 5 ise {
    yazdır("Sayı 5'ten büyüktür.");
} değilse {
    yazdır("Sayı 5 veya daha küçüktür.");
}
```

## 2. Değilse İse Zinciri
Koşullar `değilse` bloğu üzerinden yeni bir `ise` ile zincirlenebilir:
```oz
sıcaklık = 25;

sıcaklık > 30 ise {
    yazdır("Hava çok sıcak.");
} sıcaklık > 15 ise {
    yazdır("Hava ılık.");
} değilse {
    yazdır("Hava soğuk.");
}
```

## 3. VM Düzeyinde Çalışma Mantığı
Derleyici, koşullu ifadeyi derlerken:
1. Koşul ifadesini derler (sonuç stack tepesine gelir).
2. `JumpIfFalse(target)` opkodunu üretir. Eğer koşul yanlış ise target etiketine atlanır.
3. Koşul doğru ise gövde (`then_block`) çalıştırılır, ardından `Jump(end)` ile `değilse` bloğu atlanır.
