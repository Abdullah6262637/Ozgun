# Chumsky Parser ve AST Span Yönetimi

TİLK parser mimarisi ve Soyut Sözdizimi Ağacı.

## 1. Chumsky Kombinatörleri
`oz-parser` modülü, Chumsky parser combinator kütüphanesini kullanır. Hata toleransı (error recovery) ve dinamik sonek filtrelemesi (`suffix_parser`) bu aşamada koşturulur.

## 2. Span Sarmalı (`Spanned`)
Her bir AST ifadesi ve deyimi, kaynak kodundaki karakter aralığını (`Span`) taşıyan `Spanned<T>` yapısı ile sarmalanır:
```rust
pub type Span = std::ops::Range<usize>;

pub struct Spanned<T> {
    pub node: T,
    pub span: Span,
}
```
Bu sayede tip denetleyici veya derleyici bir hata fırlattığında hatanın kaynak kodunda tam olarak nerede oluştuğu tespit edilebilir.
