from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def login(driver):
    driver.get("https://www.saucedemo.com/")

    espera = WebDriverWait(driver, 10)  #Espera de 10 segundos. Explicita

    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user") 

    clave = driver.find_element(By.ID, "password")
    clave.send_keys("secret_sauce")

    boton = driver.find_element(By.ID, "login-button").click()

