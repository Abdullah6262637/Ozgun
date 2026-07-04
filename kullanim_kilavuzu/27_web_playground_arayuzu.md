# Web Oyun Alanı (Playground) ve Görsel Arayüz

TİLK dilini web tarayıcısında denememizi sağlayan playground altyapısı.

## 1. İstemci Taraflı Çalışma
Playground (`playground/index.html`), sunucuya bağımlı olmadan çalışır. Tüm yorumlama işlemleri JavaScript tabanlı lexer ve parser ile tarayıcı içinde koşturulur.

## 2. Görsel Bileşenler
- **AST Visualizer**: Kodun oluşturduğu soyut sözdizimi ağacını canlı olarak gösterir.
- **Token Stream**: Metnin hangi sözcüklere ayrıldığını gösterir.
- **Konsol Paneli**: Kodun çıktılarını gösterir.
