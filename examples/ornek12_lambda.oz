// TİLK Lambda / İsimsiz Fonksiyon Testi
yazdır("--- Lambda Testleri ---");

// Değişkene atanan isimsiz fonksiyon
iki_katı = işlev(x) {
    döndür x * 2;
};

yazdır("5'in iki katı:", iki_katı(5));

// Başka bir isimsiz fonksiyon
topla = işlev(a, b) {
    döndür a + b;
};

yazdır("3 + 4 =", topla(3, 4));

// İşlevi başka bir işleve geçirme
işlem_yap = işlev(f, x) {
    döndür f(x);
};

sonuc = işlem_yap(iki_katı, 10);
yazdır("işlem_yap sonucu:", sonuc);

yazdır("Lambda testleri tamamlandı.");
