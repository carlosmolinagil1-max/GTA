"""
Generador de guiones virales para Shorts de GTA en Español e Inglés.
Diseñado para maximizar retención (Uso Legítimo y Fair Use).
"""

PLANTILLAS_GUIONES = {
    "reto_rampa": {
        "es": (
            "¿Será posible sobrevivir a esta caída imposible en GTA? "
            "Mira con atención la velocidad a la que va ese coche... Si toca el borde está completamente acabado. "
            "¡No me creo que lo haya conseguido! ¿Tú habrías frenado a tiempo?"
        ),
        "en": (
            "Can this car actually survive this impossible GTA ramp drop? "
            "Watch closely how fast it is going... If he hits the edge, it's completely over. "
            "I can't believe he made that landing! Would you have braked in time?"
        )
    },
    "tren_vs_todo": {
        "es": (
            "¿Qué pasa si ponemos a prueba el tren indestructible de GTA contra esto? "
            "Todo el mundo dice que nada puede detenerlo, pero mira lo que ocurre en tres, dos, uno... "
            "¡La física de este juego es una locura! Déjame en comentarios qué vehículo deberíamos probar después."
        ),
        "en": (
            "What happens when you put GTA's indestructible train against this? "
            "Everyone claims nothing can stop it, but watch what happens in three, two, one... "
            "The physics in this game are insane! Comment below which vehicle we should test next."
        )
    },
    "stunt_epico": {
        "es": (
            "Este es probablemente el truco más difícil jamás grabado en GTA 5. "
            "Le tomó más de trescientas horas lograr alinearse exactamente con esa barra. "
            "Espera al aterrizaje perfecto... Dale a me gusta si tú te habrías estrellado en el primer intento."
        ),
        "en": (
            "This is hands down the hardest stunt ever pulled off in GTA 5. "
            "It took over three hundred hours just to line up perfectly with that rail. "
            "Wait for the landing... Hit like if you would have crashed on your very first try!"
        )
    }
}

def obtener_guion(tipo="reto_rampa", personalizacion_es=None, personalizacion_en=None):
    """
    Devuelve un diccionario con guiones virales en español e inglés.
    """
    base = PLANTILLAS_GUIONES.get(tipo, PLANTILLAS_GUIONES["reto_rampa"])
    return {
        "es": personalizacion_es if personalizacion_es else base["es"],
        "en": personalizacion_en if personalizacion_en else base["en"]
    }
