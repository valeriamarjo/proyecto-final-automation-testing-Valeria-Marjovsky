# Proyecto de Automatización QA (E2E y API) - Valeria Marjovsky 2026

Repositorio de automatización para la Entrega Final de Automatización de Procesos de QA. Este proyecto implementa una solución utilizando Python, Selenium WebDriver y Pytest, estructurada bajo el patrón de diseño Page Object Model (POM) para la interfaz web, sumado a un set de pruebas funcionales para servicios de API REST.

---

## Repositorio y Clonación

Para obtener una copia local de este proyecto y ejecutar las pruebas, ejecutá los siguientes comandos en tu terminal:

git clone https://github.com/valeriamarjo/proyecto-final-automation-testing-valeria-marjovsky.git
cd proyecto-final-automation-testing-valeria-marjovsky

---

## Tecnologías y Librerías Utilizadas

- Lenguaje: Python 3.11+
- Testing Framework: Pytest 9.0.3
- Automatización Web: Selenium WebDriver 4.22.0
- Manejo de Drivers: WebDriver Manager 4.0.2 
- Reportes Visuales: Pytest-HTML 4.2.0
- Validaciones Fluidas: Pytest-Check 2.8.0 
- Peticiones HTTP: Requests 2.31.1

---

## Estructura del Proyecto

El diseño del framework, desacople de los selectores y las interacciones físicas de la lógica de negocio y los datos de prueba:

EntregaFinal/
│
├── .github/workflows/       # Configuración de Integración Continua (CI)
│   └── tests.yml            # Pipeline automatizado en GitHub Actions
│
├── data/                    # Orígenes de datos estáticos y dinámicos
│   └── users.csv            # Credenciales para pruebas basadas en datos (Data-Driven)
│
├── pages/                   #Pattern POM (Page Object Model)
│   ├── login_page.py        # Métodos de interacción y selectores del Login
│   ├── inventory_page.py    # Flujo de productos, filtros y catálogo
│   └── cart_page.py         # Lógica del carrito, validación de montos y checkout
│
├── tests/                   # Suite de Pruebas de Interfaz de Usuario (UI)
│   ├── test_inventory.py    # Suite de pruebas End-to-End integradas (Flujo de Compra)
│   └── test_login.py        # Pruebas dinámicas de Login basadas en datos (CSV)
│
├── tests_api/               # Suite de Pruebas de Servicios (API REST)
│   ├── test_login_api.py    # Pruebas funcionales sobre endpoints de autenticación
│   └── test_users_api.py    # Pruebas de CRUD completo sobre usuarios (ReqRes API)
│
├── utils/                   # Módulos utilitarios
│   └── data_reader.py       # Lector dinámico (CSV / JSON)
│
├── conftest.py              # Fixtures globales (set up de WebDriver y Hooks de reporte)
├── pytest.ini               # Configuración del entorno de ejecución y tags de Pytest
├── requirements.txt         # Lista de dependencias del proyecto
└── products.json            # Base de datos de productos para la suite E2E

---

## Instalación y Configuración
1. Instalar dependencias del entorno: Asegurate de tener las librerías necesarias ejecutando en la terminal de la raíz del proyecto: pip install -r requirements.txt

2. Preparación automatizada de Drivers: Este proyecto no requiere la descarga o configuración manual de ejecutables (como chromedriver). El módulo webdriver-manager se encarga de detectar la versión local de tu navegador y lo descargar en tiempo de ejecución.

---

## Ejecución de Pruebas y Reportes Avanzados

### Comando de Ejecución General
Para correr toda la suite de pruebas automatizadas (tanto la capa de UI web como las verificaciones de API) de forma simultánea y generar el reporte consolidado, ejecutá:
pytest

---

### Reportes Dinámicos y Evidencias Fotográficas

Como estrategia de calidad y visibilidad, el framework está configurado mediante hooks de Pytest en conftest.py para resolver flujos críticos post-ejecución de manera transparente:

1. Reportes HTML Centralizados: Cada ciclo genera un reporte visual indexado de forma automática dentro del directorio Test_resultados/ bajo la estructura de nombres repo_e2e_html_AAAAMMDD_HHMMSS.html. Este archivo es autocontenido (self-contained), lo que facilita su envío o revisión rápida en navegadores sin dependencias externas.

2. Capturas de Pantalla Automatizadas ante Fallos (Screenshots): Si un caso de prueba de interfaz de usuario falla, se toma una captura instantánea del estado exacto de la pantalla del navegador en ese preciso milisegundo.

3. Incrustación de Evidencias: Las imágenes no se guardan de forma aislada en carpetas del sistema. El hook del reporte HTML las adjunta e incrusta de manera directa en la fila correspondiente al test fallido. Esto permite realizar un análisis de causa raíz veloz e inmediato directamente desde el reporte visual.

Nota: La carpeta Test_resultados/ y las capturas temporales locales están protegidas en el archivo .gitignore para evitar la subida de archivos basura al historial del repositorio, garantizando un control de versiones limpio.

---

## Integración Continua (GitHub Actions)
Este repositorio cuenta con soporte de CI (Continuous Integration). Cada vez que se realiza un git push hacia la rama principal (main), una máquina virtual basada en Linux levanta el entorno de forma aislada en la nube de GitHub, instala las dependencias de manera limpia, ejecuta la suite de pruebas web y de servicios en paralelo, y disponibiliza los reportes HTML generados como artefactos descargables para la auditoría de calidad.