# Kısa Devre (Short-Circuit) Optimizasyonu

Mantıksal VE/VEYA operatörlerinin performansı artırmak için kısa devre değerlendirilmesi.

## 1. Çalışma Mantığı
TİLK derleyicisi mantıksal operatörleri derlerken şu stratejiyi izler:
- **VE (`ve`)**: Sol taraftaki ifade yanlış (false) ise, sağ taraftaki ifadenin sonucuna bakılmaksızın tüm mantıksal işlem yanlıştır.
- **VEYA (`veya`)**: Sol taraftaki ifade doğru (true) ise, sağ tarafın sonucuna bakılmaksızın tüm işlem doğrudur.

## 2. VM Opcodları
Bu kısa devre akışını yönetmek için yığındaki değeri pop etmeden kontrol eden `JumpIfFalseKeep` ve `JumpIfTrueKeep` opkodları kullanılır. Bu sayede sol tarafın sonucu yığında korunarak doğrudan atlama sağlanır.
