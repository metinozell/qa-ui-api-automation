import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import Config
import os
from datetime import datetime

@pytest.fixture
def driver():
    options=Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080") 

    driver=webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    driver.get(Config.BASE_URL)

    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    # Eğer test çalıştırıldıysa ve başarısız olduysa (Failed)
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures.txt") else "w"
        try:
            # Driver'a erişiyoruz
            if "driver" in item.funcargs:
                driver = item.funcargs["driver"]
                # Screenshots klasörü yoksa oluştur
                if not os.path.exists("screenshots"):
                    os.makedirs("screenshots")
                
                # Dosya adı: test_adı_tarih.png
                file_name = f"screenshots/{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                driver.save_screenshot(file_name)
                print(f"\n Hata yakalandı! Ekran görüntüsü kaydedildi: {file_name}")
        except Exception as e:
            print(f"Ekran görüntüsü alınırken hata oluştu: {e}")