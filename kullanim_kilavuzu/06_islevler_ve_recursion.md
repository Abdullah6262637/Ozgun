# İşlevler (Fonksiyonlar) ve Özyinelemeli (Recursive) Programlama

İşlevler, dildeki modüler kod bloklarıdır. `işlev` anahtar kelimesi ile bildirilirler.

## 1. İşlev Tanımlama ve Değer Döndürme
Bir işlev birden fazla parametre alabilir ve `döndür` ifadesiyle değer dönebilir:
```oz
işlev alan_hesapla(genişlik, yükseklik) {
    döndür genişlik * yükseklik;
}

sonuç = alan_hesapla(10, 5);
yazdır("Alan:", sonuç); // 50
```
Eğer `döndür` ifadesi kullanılmazsa, işlev varsayılan olarak `boş` (Bos) değerini döndürür.

## 2. Özyinelemeli (Recursive) İşlevler
TİLK, fonksiyonların kendi kendini çağırmasını (recursion) ve yığın yönetimini Call Frame mimarisi ile tam olarak destekler:
```oz
işlev faktöriyel(n) {
    n <= 1 ise {
        döndür 1;
    }
    döndür n * faktöriyel(n - 1);
}

yazdır(faktöriyel(5)); // 120
```
Özyinelemeli her çağrıda yeni bir sanal makine Frame'i oluşturulur ve yerel değişkenler bu frame içinde izole edilir.
