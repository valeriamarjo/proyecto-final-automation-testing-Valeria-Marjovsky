from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_cart(login_in_driver):
    driver = login_in_driver

    #Agrega al carrito
    
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    cuenta_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

   #Verifica contador del carrito para corroboar que se agregó el prodcuto a través del tag de texto
    assert cuenta_carrito.text == "1", "no se agregó correctamente la cantidad del producto seleccionado"

    #Conseguir el nombre del primer producto
    nombre_primer_producto =  driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

    driver.find_elements(By.CLASS_NAME, "shopping_cart_link")[0].click()
    
    #Nombre del producto dentro del carrito
    item_Del_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    assert item_Del_carrito == nombre_primer_producto, "El producto no coincide"