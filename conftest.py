import pytest
import os
from datetime import datetime
from selenium import webdriver

MARCA_TIEMPO_SUITE = datetime.now().strftime("%Y%m%d_%H%M%S")

def pytest_configure(config):
    carpeta_reportes = "Test_resultados"
    os.makedirs(carpeta_reportes, exist_ok=True)
    
    nombre_reporte = f"repo_e2e_html_{MARCA_TIEMPO_SUITE}.html"
    config.option.htmlpath = os.path.join(carpeta_reportes, nombre_reporte)
    config.option.self_contained_html = True

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    local_driver = webdriver.Chrome(options=options)
    local_driver.implicitly_wait(10)
    
    yield local_driver
    local_driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver")
        
        if driver_fixture:
            carpeta_reportes = "Test_resultados"
            marca_tiempo_error = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            #screenshots
            nombre_archivo = f"repo_e2e_scrshts_{marca_tiempo_error}.png"
            ruta_completa = os.path.join(carpeta_reportes, nombre_archivo)
            
            driver_fixture.save_screenshot(ruta_completa)
            
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html is not None:
                extra = getattr(report, "extra", [])
                html_evidencia = f'<div><img src="{nombre_archivo}" alt="Screenshot Error" style="width:300px;height:200px;" ' \
                                 f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html_evidencia))
                report.extra = extra