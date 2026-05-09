from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_validation (login_in_driver):
  # Se recibe el driver ya logueado desde el fixture
  
      driver = login_in_driver

      assert "/inventory.html" in driver.current_url, 'No se redirigió al inventario'
      