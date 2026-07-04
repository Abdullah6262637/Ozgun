# Logos Lexer ve Token Yapılandırması

Sözcüksel analiz (lexing) aşamasının detayları.

## 1. Logos Entegrasyonu
`oz-lexer` modülü, Rust'ın compile-time DFA üreteci `logos` kütüphanesini kullanır. Bu sayede sıfır bellek kopyalamalı (zero-copy) kelime analizi yapılır.

## 2. Kesme İşareti Skip Kuralları
Türkçe sonekleri (`1'den`, `limit'e`) ayırmak için kesme işareti whitespace'ler gibi skip edilir:
```rust
#[logos(skip r"[ \t\n\f']+")]
```
Böylece `1'den` girdisi `1` (Sayı) ve `den` (Tanımlayıcı) olarak ayrışır.

## 3. String Escape Kuralları
Metin içindeki kaçış karakterleri (`\n`, `\t` vb.) lexer tarafından state-machine ile çözümlenerek String token'ına yazılır.
