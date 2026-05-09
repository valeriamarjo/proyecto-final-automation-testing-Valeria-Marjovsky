# Proyecto de Automatización QA Valeria Marjovsky 2026

## Propósito del Proyecto

Proyecto de automatización de pruebas hecho en python, selenium Webdriver y Pytest.
Este proyecto forma parte de la pre-entrega para el curso de Automation Testing. El objetivo principal es validar los flujos críticos de la plataforma **SauceDemo**, incluyendo la autenticación de usuarios, la visualización de productos en el catálogo y la funcionalidad del carrito de compras, de acuerdo a las consignas indicadas.


## Tecnologías
- Python: Versión-3.14.4
- Selenium WebDriver: Versión - 4.43.0
- Pytest HTML: versión - 4.2.0
- Git: versión 2.54.0.windows.1

# Instalación
  1. Clonar el repositorio: https://github.com/valeriamarjo/pre-entrega-automation-testing-Valeria-Marjovsky.git
  2. Instalar las dependencias: pip install -r requirements.txt
  3. Para ejecutar los tests y generar automáticamente el reporte de resultados en formato HTML, está configurado el pytest ini para que solo ejecutes el comando pytest en la raíz del proyecto. Esto ejecutará todos los tests y podrás ver el reporte en la carpeta Test_resultados


## Dependencias

pip install -r requirements.txt

## Funcionamiento Pruebas
   # Estructura de las Pruebas
   
    - tests/: Contiene los scripts de prueba (Login, Inventario, Carrito).
    - utils/: Funciones auxiliares para la lógica de inicio de sesión.
    - reports/: Carpeta destinada a guardar los reportes de ejecución.
    - pytest.ini: Configuración personalizada de Pytest.
 
 # Tests
    - Test Cart: Verifica el agregado de un producto al carrito, para lo cual el mismo debe existir y que el producto agregado sea el que fue seleccionado
    - Test Inventario: Verifica la existencia de los productos.

