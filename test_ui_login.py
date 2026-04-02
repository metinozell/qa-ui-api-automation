import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture
def setup_and_login():
    chrome_options=Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")

    driver=webdriver.Chrome(options=chrome_options)
    driver.get("https://saucedemo.com/")
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()   

    yield driver
    time.sleep(2)
    driver.quit()

def test_login(setup_and_login):
    driver=setup_and_login
    assert "inventory.html" in driver.current_url

def test_add_to_cart(setup_and_login):
    driver=setup_and_login
    driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    cart_count=driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
    assert cart_count=="1"

def test_go_to_checkout_step_one(setup_and_login):
    driver=setup_and_login
    driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    driver.find_element(By.ID,"checkout").click()
    assert "checkout-step-one.html" in driver.current_url
