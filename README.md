# E-Commerce & API QA Automation Portfolio

Bu proje, modern yazılım test otomasyonu yeteneklerimi sergilemek amacıyla hazırlanmıştır. Proje kapsamında hem web arayüzü (UI) hem de web servis (API) testleri uçtan uca (E2E) otomatize edilmiş ve GitHub Actions ile Sürekli Entegrasyon (CI) sürecine dahil edilmiştir.

## 🚀 Teknolojiler ve Araçlar
* **Programlama Dili:** Python 3.10
* **UI Otomasyonu:** Selenium WebDriver
* **API Otomasyonu:** Requests kütüphanesi
* **Test Çatısı (Framework):** Pytest
* **CI/CD:** GitHub Actions (Headless mod ve otomatik tetikleme)
* **Versiyon Kontrolü:** Git & GitHub

## ⚙️ Test Senaryoları
1. **API Testleri (`test_user.py`):**
   * GET istekleri ile veri doğrulama (Data Validation)
   * POST istekleri ile yeni kayıt oluşturma (201 Created kontrolü)
2. **UI Testleri (`test_ui_login.py`):**
   * Başarılı kullanıcı girişi (Login)
   * Sepete ürün ekleme ve sepet rozeti doğrulama
   * Uçtan uca ödeme (Checkout) ekranına geçiş senaryosu
   * *Not: Testler Pytest Fixture mimarisiyle ve Implicit Wait senkronizasyonuyla stabil hale getirilmiştir.*

## 💻 Kurulum ve Çalıştırma (Lokal Cihazda)
Projeyi kendi bilgisayarınızda çalıştırmak için:
1. Repoyu klonlayın: `git clone https://github.com/metinozell/qa-ui-api-automation.git`
2. Gerekli kütüphaneleri yükleyin: `pip install -r requirements.txt`
3. Tüm testleri çalıştırın: `pytest -v -s`