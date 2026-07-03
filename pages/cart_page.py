from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        
        # Selectores utilizando el patrón Page Object Model (POM)
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.cart_items_name = (By.CLASS_NAME, "inventory_item_name")
        self.cart_item_price = (By.CLASS_NAME, "inventory_item_price")
        self.btn_checkout = (By.ID, "checkout")

    def obtener_productos_carrito(self):
        """Recorre la lista de elementos en el carrito y retorna sus nombres y precios."""
        items = self.driver.find_elements(*self.cart_items)
        productos = []

        for item in items:
            nombre_item = item.find_element(*self.cart_items_name).text
            precio_item = item.find_element(*self.cart_item_price).text

            productos.append(
                {
                    "name": nombre_item,
                    "price": precio_item
                }
            )
            return productos

    def iniciar_checkout(self):
        elemento = self.driver.find_element(*self.btn_checkout)
        self.driver.execute_script("arguments[0].click();", elemento)