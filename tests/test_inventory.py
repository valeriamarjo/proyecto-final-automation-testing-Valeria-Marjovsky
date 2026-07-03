import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.ui
def test_end2end(driver):
    """Caso de prueba integral de punta a punta para el flujo de compra."""
    login_page = LoginPage(driver)
    login_page.ejecutar_login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    
    assert inventory_page.obtener_titulo() == "Swag Labs", "No se encontró el título esperado"
    assert inventory_page.obtener_contador() == "0", "El carrito de compras no está en cero"
    
    nombre_esperado = inventory_page.obtener_nombre_primer_producto()
    inventory_page.agregar_primer_producto_al_carrito()
    
    inventory_page.esperar_actualizacion_contador("1")
    assert inventory_page.obtener_contador() == "1", "El contador no se incrementó a '1'"
    
    cart_page = inventory_page.ir_al_carrito()
    
    productos_en_carrito = cart_page.obtener_productos_carrito()
    nombres_en_carrito = [producto["name"] for producto in productos_en_carrito]
    
    assert nombre_esperado in nombres_en_carrito, f"El producto '{nombre_esperado}' no está en el carrito"
    
    cart_page.iniciar_checkout()