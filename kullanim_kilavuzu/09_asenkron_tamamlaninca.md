# Asenkron Programlama: arkaplanda_çalıştır ve tamamlanınca

TİLK, uzun süren işlemlerin ana thread'i bloke etmesini engellemek için yerleşik asenkron görev desteği barındırır.

## 1. Görev Oluşturma (`arkaplanda_çalıştır`)
Bir işlev çağrısı `arkaplanda_çalıştır` ile sarmalandığında, işletim sisteminde asenkron bir thread başlatılır ve bir `Task` nesnesi dönülür:
```oz
işlev api_istegi() {
    uyku(1500); // 1.5 saniye simüle et
    döndür "veri_geldi";
}

görev = arkaplanda_çalıştır(api_istegi);
```

## 2. Görev Sonucu (`tamamlanınca`)
Asenkron başlatılan görevin tamamlanmasını beklemek ve sonucunu işlemek için `tamamlanınca` deyimi kullanılır:
```oz
görev tamamlanınca {
    // Sonuç otomatik olarak 'sonuç' veya 'sonuc' değişkenine atanır.
    yazdır("İşlem tamamlandı, gelen sonuç:", sonuç);
}
```
