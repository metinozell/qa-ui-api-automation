import requests

def test_update_user():
    # SENARYO 1: 2 Numaralı kullanıcının mesleğini (job) güncellemek istiyoruz.
    url = "https://reqres.in/api/users/2"
    
    payload = {
        "name": "Metin QA",
        "job": "Senior Automation Engineer"
    }
    
    # HATA BÖLGESİ 1: Güncelleme işlemi için sence doğru metodu (GET, POST, PUT, DELETE) mu kullandım? 
    response = requests.put(url, json=payload)
    
    updated_data = response.json()
    print(f"\nGüncelleme Cevabı: {updated_data}")
    
    # HATA BÖLGESİ 2: reqres.in sitesinde başarılı bir "güncelleme" işlemi genelde 200 OK döner. 
    # Ama ben aşağıda ne yazmışım bir kontrol et.
    assert response.status_code == 200
    
    # Doğrulama: Meslek gerçekten güncellendi mi?
    assert updated_data["job"] == "Senior Automation Engineer"


def test_user_not_found():
    # SENARYO 2: Sistemde olmayan bir kullanıcıyı aradığımızda uygulamanın çökmeyip 
    # bize "Bulunamadı" (Not Found) hatası vermesi gerekir. (Negatif Test)
    
    # reqres.in veritabanında 23 numaralı bir kullanıcı yok.
    url = "https://reqres.in/api/users/23"
    
    response = requests.get(url)
    
    print(f"\nOlmayan Kullanıcı Durum Kodu: {response.status_code}")
    
    # HATA BÖLGESİ 3: Olmayan bir şeyi aradığımızda sence sunucu 200 (Her şey yolunda) döner mi?
    # İnternette "Sayfa Bulunamadı" hatasının kodu nedir, onu düşün ve burayı değiştir.
    assert response.status_code == 404