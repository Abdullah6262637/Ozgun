# Proje Yapılandırması: tilk.toml Manifest Kılavuzu

Her TİLK projesinin kök dizininde bulunması gereken yapılandırma dosyası.

## 1. tilk.toml Parametreleri
- **`ad`**: Projenin benzersiz ismi.
- **`surum`**: Semantık versiyonlama formatındaki sürüm numarası (örn: `0.1.0`).
- **`giris`**: Derleme veya çalıştırma işlemlerinde baz alınacak ana kaynak kodu yolu.

## 2. Örnek Manifest
```toml
[paket]
ad = "hesaplayıcı"
surum = "1.0.0"
giris = "kaynak/ana.oz"
```
