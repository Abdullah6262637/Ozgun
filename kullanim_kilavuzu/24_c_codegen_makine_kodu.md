# C Kod Üretimi ve Makine Koduna Derleme (AOT)

TİLK kodlarının yerel makine koduna dönüştürülmesi aşaması.

## 1. C Transpiler
`oz-cli` derleme aracı, AST'yi standart bir C koduna dönüştürür. `c_codegen.rs` modülü, dildeki dinamik tipleri, dizileri ve haritaları taklit eden optimize edilmiş bir C runtime başlığı (`TilkVal`) üretir.

## 2. Yerel Derleme (Ahead-Of-Time)
Üretilen `program.c` kodu, sistemde bulunan C derleyicisi (gcc, clang, msvc) çağrılarak doğrudan makine koduna (executable `.exe` veya ELF) derlenir:
```bash
cargo run --bin oz-cli -- derle --yerel
```
