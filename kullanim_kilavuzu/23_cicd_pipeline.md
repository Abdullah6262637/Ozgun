# CI/CD (Sürekli Entegrasyon) Süreç Belgesi

TİLK projesinin GitHub Actions üzerinde çalışan CI/CD otomasyonu.

## 1. Workflow Tetikleyicileri
Her `push` veya `pull_request` işlemi yapıldığında GitHub Actions sunucularında `.github/workflows/ci.yml` iş akışı tetiklenir.

## 2. Denetim Aşamaları
- **Biçimlendirme (`cargo fmt`)**: Kod stilinin standarda uygunluğunu denetler.
- **Kod Analizi (`cargo clippy`)**: Güvenlik ve performans uyarılarını denetler (`-D warnings` politikasıyla hiçbir uyarıya izin verilmez).
- **Testler (`cargo test`)**: Tüm birim ve golden entegrasyon testlerini koşturur.
