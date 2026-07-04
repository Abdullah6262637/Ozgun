# Golden File Test Altyapısı ve Harness Mimarisi

TİLK ekosisteminin kararlılık testleri.

## 1. Golden Test Nedir?
Golden testler, programın ürettiği tüm standart çıktıyı (stdout) önceden kaydedilmiş referans çıktılarla (`.stdout` uzantılı golden dosyaları) karşılaştıran entegrasyon testleridir.

## 2. Test Harness Tasarımı
- `tests/golden/` dizininde her örnek program için beklenen çıktılar tutulur.
- `oz-vm/src/tests.rs` içindeki test harness'ı, VM'in `stdout` yazıcısını geçici bir bellek tamponuna (RefCell buffer) yönlendirir.
- VM çalıştıktan sonra tamponun içeriği ile golden dosyasındaki metin karşılaştırılır. Boşluklar ve satır sonları normalize edilerek doğrulama yapılır.
