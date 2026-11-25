# 🗺️ Hoja de Ruta (Roadmap) — Proyecto GTA

Este documento define las posibles vertientes y fases de desarrollo para la idea de **GTA** en este repositorio.

---

## 🎯 4 Posibles Enfoques del Proyecto

| Enfoque | Descripción | Tecnologías Clave |
| :--- | :--- | :--- |
| **1. Minijuego 2D Cenital (Estilo GTA 1 / 2)** | Simulación de vehículo, movimiento de peatones, conducción en vista superior, cámara y colisiones. | `pygame`, `math`, `Pillow` |
| **2. Modding & Servidores (FiveM / Alt:V)** | Creación de scripts de rol, sistemas de economía, garajes, trabajos o inventarios para GTA V. | `Lua`, `Python`, `JSON / SQLite` |
| **3. Automatización / Visión por Computador (Bot GTA)** | Detección automática de minimapa, lectura de barras de salud, autopilotaje o macros inteligentes. | `OpenCV`, `mss`, `PyTorch / YOLO` |
| **4. Análisis de Datos & Telemetría GTA** | Análisis estadístico de vehículos (aceleración, tracción), armas, misiones o economía del juego. | `pandas`, `matplotlib`, `seaborn` |

---

## 📌 Fases de Trabajo Recomendadas

1. **Fase 1: Configuración de la base (Completada)**
   - Estructuración de carpetas separadas de la búsqueda de empleo.
   - Creación del notebook de pruebas interactivo (`notebooks/gta_proyecto.ipynb`).
   - Definición de clases iniciales (`Jugador`, `Vehiculo`, `Mision`).

2. **Fase 2: Elección de Vertiente y Primer Módulo**
   - Decidir junto a Carlos si priorizamos desarrollo visual (Pygame/2D), scripting de servidor, o análisis/automatización.
   - Probar los primeros prototipos en el Jupyter Notebook.

3. **Fase 3: Expansión de Funcionalidades**
   - Guardado de partidas / estados en `data/`.
   - Lógica de eventos, misiones aleatorias o interfaz gráfica.
