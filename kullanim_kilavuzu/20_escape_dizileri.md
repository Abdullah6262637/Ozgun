# Metin İçinde Kaçış (Escape) Karakterleri Desteği

TİLK dize literallerinde (String literals) kullanılan standart kaçış dizilimleri.

## 1. Desteklenen Karakterler
- `\n`: Yeni satıra geçiş (Line Feed)
- `\t`: Yatay sekme (Tab)
- `\r`: Satır başı (Carriage Return)
- `\"`: Çift tırnak karakteri
- `\\`: Ters eğik çizgi karakteri

## 2. Çözümleme Mantığı
Lexer, çift tırnaklar arasındaki metni tararken ters eğik çizgi (`\`) karakterini algıladığında bir sonraki karakteri kontrol eder ve bunu karşılık gelen kontrol byte'ına dönüştürür. Hatalı kaçış dizilimleri derleme zamanında tespit edilir.
