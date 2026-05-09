import pytest
from selenium import webdriver
from utils.loginpage import login


@pytest.fixture
def driver(): #inicalización del navegador para las pruebas
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver= webdriver.Chrome(options= options)

    yield driver #pausa el código hasta aca

    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return (driver)
