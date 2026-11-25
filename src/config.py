"""
Configuración general y constantes del proyecto GTA.
"""
from pathlib import Path

# Rutas principales del proyecto GTA
BASE_DIR = Path(__file__).resolve().parent.parent
NOTEBOOKS_DIR = BASE_DIR / "notebooks"
DATA_DIR = BASE_DIR / "data"
DOCS_DIR = BASE_DIR / "docs"

# Ajustes generales de simulación / juego
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
FPS = 60
VELOCIDAD_MAX_VEHICULO = 120.0  # km/h simulados
ACELERACION = 2.5
FRICCION = 0.98
