
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver

def test_login_validation_title(driver_logged):
    title = driver_logged.title == "Swag Labs"
    assert title == "Swag Labs", "El título de la página no es correcto"

def test_productos_visibles(driver_logged):
    productos = driver_logged.find_elements(By.CLASS_NAME,"inventory_item")
    assert len(productos) > 0, "No se encontraron elementos"

def test_ui_elements(driver_logged):
    menu = driver_logged.find_element(By.ID, "react -burguer-menu-btn")
    filtro = driver_logged.find_element(By.CLASS_NAME, "product_sort_container")
    assert menu.is_displayed(), "el ícono del menú no está disponbile"
    assert filtro.is_displayed(), "el filtro del catálogo no está disponbile"


#faltan cosas, revisar clase práctica del 3/5