# Sanal Makine (VM) Yığın ve Yürütme Mimarisi

TİLK Sanal Makinesi (VM) yığın tabanlı bir sanal makinedir.

## 1. VM Yapısı
```rust
pub struct VM {
    instructions: Vec<Instruction>, // Çalıştırılacak opkodlar
    ip: usize,                      // Program sayacı
    stack: Vec<Val>,               // Veri yığını
    globals: HashMap<String, Val>, // Global değişkenler
    frames: Vec<Frame>,            // Çağrı çerçeveleri
}
```

## 2. Yürütme Döngüsü
Sanal makine, `ip` adresindeki talimatı okur (fetch), çözer (decode) ve yürütür (execute). `Return` opkodu gelene veya program sonlanana kadar döngü devam eder. Aritmetik operasyonlar doğrudan stack üzerinde pop/push ile yapılır.
