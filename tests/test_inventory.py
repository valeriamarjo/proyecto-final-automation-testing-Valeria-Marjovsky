
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver

def test_login_validation_title(driver_logged):
    title = driver_logged.title
    assert title == "Swag Labs", "El título de la página no es correcto"

def test_productos_visibles(driver_logged):
    productos = driver_logged.find_elements(By.CLASS_NAME,"inventory_item")
    assert len(productos) > 0, "No se encontraron elementos"

def test_ui_elements(driver_logged):
    try:
        menu = driver_logged.find_element(By.ID, "react-burger-menu-btn")
        assert menu.is_displayed(), "El icono del menú no está disponible"
    except Exception as e:
        # Si falla, saca una captura antes de mostrar el error
        driver_logged.save_screenshot("Test_resultados/error_menu.png")
        raise e #El test siga fallando("Failed") en el reporte