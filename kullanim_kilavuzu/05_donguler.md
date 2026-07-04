# Döngüler: iken ve dek Döngülerinin Detaylı Analizi

TİLK dilinde döngüler, algoritmanın akışına göre iki farklı yapıda kurulur.

## 1. Koşullu Döngü (`iken`)
Belirtilen şart doğru olduğu sürece bloğu tekrarlar. Klasik `while` döngüsünün sondan eklemeli halidir:
```oz
sayaç = 1;
sayaç <= 3 iken {
    yazdır("Sayaç değeri:", sayaç);
    sayaç = sayaç + 1;
}
```

## 2. Aralık Döngüleri (`dek`)
Belli bir başlangıç değerinden bitiş değerine kadar artarak veya azalarak çalışır. Türkçe ek uyumuna göre `1'den 5'e dek` şeklinde yazılır:
```oz
// Artan aralık döngüsü (1, 2, 3, 4, 5)
i, 1'den 5'e dek artarak {
    yazdır(i);
}

// Azalan aralık döngüsü (5, 4, 3, 2, 1)
j, 5'ten 1'e dek azalarak {
    yazdır(j);
}
```
Kesme işareti (`'`) lexer tarafından yok sayıldığı için `1'den` ifadesi `1 den` olarak ayrıştırılır ve parser bu ekleri dinamik olarak yakalar.
