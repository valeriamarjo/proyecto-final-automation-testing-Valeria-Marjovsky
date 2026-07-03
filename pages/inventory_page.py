from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import CartPage

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.contador_carrito = (By.CLASS_NAME, "shopping_cart_badge")
        self.link_carrito = (By.CLASS_NAME, "shopping_cart_link")
        self.nombres_productos = (By.CLASS_NAME, "inventory_item_name")
        self.btn_agregar_primer_producto = (By.ID, "add-to-cart-sauce-labs-backpack")

    def obtener_titulo(self):
        return self.driver.title

    def obtener_contador(self):
        try:
            return self.driver.find_element(*self.contador_carrito).text
        except:
            return "0"

    def esperar_actualizacion_contador(self, valor_esperado):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element(self.contador_carrito, str(valor_esperado))
            )
            return True
        except:
            return False

    def agregar_primer_producto_al_carrito(self):
        elemento = self.driver.find_element(*self.btn_agregar_primer_producto)
        self.driver.execute_script("arguments[0].click();", elemento)
    
    def obtener_nombre_primer_producto(self):
        return self.driver.find_elements(*self.nombres_productos)[0].text

    def ir_al_carrito(self):
        elemento = self.driver.find_element(*self.link_carrito)
        self.driver.execute_script("arguments[0].click();", elemento)
        return CartPage(self.driver)