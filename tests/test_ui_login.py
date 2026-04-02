from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config import Config

def test_succesful_login_with_pom(driver):
    driver.get("https://saucedemo.com/")
    login_pg=LoginPage(driver)
    login_pg.enter_username(Config.USERNAME)
    login_pg.enter_password(Config.PASSWORD)
    login_pg.click_login()

    assert "inventory.html" in driver.current_url

def test_add_to_cart_with_pom(driver):
    driver.get("https://saucedemo.com/")

    login_pg=LoginPage(driver)
    login_pg.enter_username(Config.USERNAME)
    login_pg.enter_password(Config.PASSWORD)
    login_pg.click_login()

    inventory_pg=InventoryPage(driver)
    inventory_pg.add_backpack_to_cart()
    assert inventory_pg.get_cart_count()=="1"