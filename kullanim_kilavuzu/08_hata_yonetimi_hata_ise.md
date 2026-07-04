# Hata Yönetimi: hata_fırlat ve hata_ise Mekanizması

TİLK, programın çalışma zamanı hatalarında çökmesini önlemek için özgün bir hata yakalama mekanizması sunar.

## 1. Hata Fırlatma (`hata_fırlat`)
Çalışma zamanında beklenmeyen bir durumu belirtmek için `hata_fırlat` fonksiyonu kullanılır:
```oz
işlev böl(a, b) {
    b == 0 ise {
        hata_fırlat("Sıfıra bölme hatası oluştu!");
    }
    döndür a / b;
}
```

## 2. Hata Yakalama (`hata_ise`)
Bir ifade yürütülürken hata oluşursa alternatif bir blok (`hata_ise`) çalıştırılır. Hata mesajı otomatik olarak `hata_mesajı` değişkenine atanır:
```oz
sonuç = böl(10, 0) hata_ise {
    yazdır("Bir hata oluştu. Detay:", hata_mesajı);
    döndür 0;
};
// sonuç 0 olur ve program çökmek yerine çalışmaya devam eder.
```
