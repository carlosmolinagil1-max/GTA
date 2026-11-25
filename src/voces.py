"""
Módulo de generación de voces neuronales gratuitas con edge-tts.
No requiere claves API ni suscripciones de pago.
"""
import asyncio
from pathlib import Path

# Voces recomendadas por calidad y naturalidad
VOCES = {
    "es": "es-ES-AlvaroNeural",       # Voz masculina dinámica en español
    "es_mujer": "es-ES-ElviraNeural", # Voz femenina en español
    "en": "en-US-ChristopherNeural",  # Voz masculina en inglés nativo
    "en_mujer": "en-US-JennyNeural"   # Voz femenina en inglés nativo
}

async def _generar_audio_async(texto: str, voz: str, ruta_salida: str):
    import edge_tts
    comunicador = edge_tts.Communicate(texto, voz)
    await comunicador.save(ruta_salida)

def sintetizar_voz(texto: str, idioma: str = "es", ruta_salida: str = "locucion.mp3") -> str:
    """
    Sintetiza texto a voz en MP3 usando voces neuronales gratuitas de Microsoft.
    """
    voz_seleccionada = VOCES.get(idioma, VOCES["es"])
    Path(ruta_salida).parent.mkdir(parents=True, exist_ok=True)
    asyncio.run(_generar_audio_async(texto, voz_seleccionada, str(ruta_salida)))
    return str(ruta_salida)
