// TİLK Metin İçi Değişken (String Interpolation) Testi
ad = "Ali";
yas = 22;

yazdır("Merhaba {ad}, demek {yas} yaşındasın!");
yazdır("5 yıl sonra {yas + 5} yaşında olacaksın.");

doğru_mu = doğru;
yazdır("Mantıksal değer: {doğru_mu}");

dizi_boyutu = boyut([1, 2, 3]);
yazdır("Dizide {dizi_boyutu} eleman var.");

sayi = 10;
yazdır("Eğer istersen \\{\\} gibi kaçış yapabilirsin veya {sayi * 2} diyebilirsin.");

// Hatalı kullanımları test etmek istersen alttakini aç:
// yazdır("Boş { } ve kapatılmamış {hata");
