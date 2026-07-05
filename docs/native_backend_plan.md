# TİLK Native Backend (Makine Kodu) Mimari Tasarımı

Bu doküman, TİLK programlama dilinin C derleyicisine (GCC/Clang) veya Sanal Makineye (Bytecode VM) ihtiyaç duymadan doğrudan işletim sistemi üzerinde çalışan gerçek makine kodu (.exe, ELF, Mach-O) üretecek Cranelift (veya LLVM) arka ucunun tasarımını detaylandırmaktadır.

## Neden Şu An Cranelift/LLVM'e Geçilmiyor?
Şu anda dilin AST'si, typechecker katmanı ve parser mekanizması henüz hızla değişmekte olup yeni sözdizimi ve semantik özellikler eklenmektedir (ör. Closure'lar, Pattern Matching, Struct'lar). 
Native arka uç geliştirmek çok daha stabil bir ara temsil (Intermediate Representation - IR) gerektirir. Eğer şimdiden Cranelift arka ucuna başlarsak, dildeki her ufak tasarım değişikliği (örneğin closure capture mantığının değişmesi) Cranelift IR (clif) ve assembly üretim mantığında muazzam bir yeniden yazım gerektirecektir. Önce ön ucu (frontend) sağlamlaştırmak stratejik olarak en doğrusudur.

## Gerekli Olan Ara Temsil (IR) Katmanı
Bytecode veya doğrudan AST'den Cranelift'e derleme yapmak mümkündür ancak optimize edici bir derleyici için SSA (Static Single Assignment) formunda bir TİLK IR (TIR) tanımlanması faydalı olacaktır.
**Akış:**
`TİLK Kaynak Kodu -> AST -> HM Type Inference -> TİLK IR (TIR) -> Cranelift IR -> Native Executable`

## Runtime Veri Gösterimi (Representation)
Native ortamda TİLK değişkenlerinin (dinamik olarak veya statik tiplemeyle) bellekte nasıl tutulacağına dair stratejiler:
- **Number:** Doğrudan `f64` registerlarda veya stack'te taşınabilir.
- **String:** Heap üzerinde tahsis edilen ve kapasite/uzunluk/pointer taşıyan basit bir yapı (struct). `(ptr, len, cap)`.
- **Bool:** 1 baytlık `i8`.
- **Array:** Dinamik olarak büyüyebilen bir heap allocation buffer'ı.
- **Map:** HashMap veya BTreeMap'in native C-style struct implementasyonu.
- **Struct:** Field'ların offsetlerine göre hesaplanan bitişik bellek bloğu (struct layout).
- **Closure:** Fonksiyon pointer'ı ve environment (yakalanan değişkenler) struct'ını barındıran bir "fat pointer".

## Çöp Toplama (Garbage Collection) vs. Referans Sayımı
Native hedefler için tam teşekküllü bir GC yazmak (veya Boehm GC gibi bir şey bağlamak) karmaşıktır.
Modern dillerde olduğu gibi **Reference Counting (ARC / Rc)** stratejisi ile başlamak:
1. Her heap tahsisli TİLK nesnesinin (Metin, Dizi, Harita) başında bir `ref_count` baytı olur.
2. Scope sonlarında veya atamalarda derleyici otomatik olarak `retain` (artırma) ve `release` (azaltma) Cranelift instruction'ları üretir.

## AOT ve JIT Kararı
- **AOT (Ahead-of-Time):** Kod tamamen önceden Cranelift Object Module üzerinden derlenir. Windows için `.exe` oluşturmak adına `cranelift-object` kullanılarak statik objeler üretilir, sonra sistem linkleyici (gcc/lld/msvc) kullanılarak executable bağlanır.
- **JIT (Just-in-Time):** Kod bellekte derlenir ve hemen anında çalıştırılır (REPL veya çok hızlı test süreçleri için harikadır).

TİLK için birincil hedef **AOT** derleme olmalıdır.

## Hedef Platformlar
- **Windows:** `.exe` (COFF object format, x86_64 hedeflenerek MSVC linkleyici ile)
- **Linux:** ELF formatı, GCC veya LLD ile.
- **macOS:** Mach-O formatı (AArch64 ve x86_64 hedefleri).

## Native Backend Geliştirme Yol Haritası (Milestones)

1. **Sayısal Aritmetik ve Temel Akış:**
   Sadece `f64` hesaplamaları, temel register atamaları ve if/else Cranelift EBB (Extended Basic Block) yönlendirmelerinin yapılması. (Hello World of Compilers)
2. **Local Variables & Scoping:**
   Stack slot tahsisleri, değişkenlerin belleğe (veya register'a) alınması ve güncellenmesi.
3. **Fonksiyon Çağrıları (Function Calls):**
   ABI uyumlu fonksiyon üretim ve Cranelift çağrıları (call_indirect dahil).
4. **String & Heap Runtime:**
   Native kodun C standart kütüphanesi `malloc/free` ile haberleşmesi ve String concat, alloc işlevlerinin eklenmesi.
5. **Diziler, Haritalar ve Yapılar (Struct Runtime):**
   Dinamik diziler için bellek kurgusu ve struct alan (field offset) erişimleri.
6. **Closure Runtime:**
   Fonksiyon argümanı olarak çevre barındıran yapıların oluşturulup aktarılması.
7. **Standart Kütüphane Köprüsü (Stdlib Bridge):**
   TİLK native kodundan dış C API'lerini (syscall, file IO) çağırabilmek için Cranelift FFI interface'inin bağlanması.
