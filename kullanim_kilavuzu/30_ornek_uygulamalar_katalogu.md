# Örnek Uygulamalar Kataloğu

TİLK dilinin özelliklerini gösteren kapsamlı kod örnekleri.

## 1. Fibonacci Dizisi Hesaplama
```oz
işlev fib(n) {
    n <= 1 ise {
        döndür n;
    }
    döndür fib(n - 1) + fib(n - 2);
}

yazdır(fib(10)); // 55
```

## 2. Güvenli Dosya Okuma
```oz
işlev oku_ve_yazdır(yol) {
    içerik = dosya_oku(yol) hata_ise {
        yazdır("Hata: Dosya okunamadı.");
        döndür "";
    };
    yazdır(içerik);
}
```
