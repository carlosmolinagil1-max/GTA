"""
Módulo de búsqueda y radar de Shorts virales de GTA en YouTube.
"""
from pathlib import Path
from typing import List, Dict

def buscar_tendencias_gta(termino_busqueda: str = "gta 5 stunts shorts", limite: int = 5) -> List[Dict]:
    """
    Busca Shorts populares y recientes de GTA en YouTube usando yt-dlp.
    """
    import yt_dlp

    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'default_search': f'ytsearch{limite}',
        'skip_download': True
    }

    resultados = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(termino_busqueda, download=False)
        if 'entries' in info:
            for entry in info['entries']:
                resultados.append({
                    'id': entry.get('id'),
                    'titulo': entry.get('title'),
                    'url': f"https://www.youtube.com/watch?v={entry.get('id')}",
                    'duracion': entry.get('duration', 0),
                    'vistas': entry.get('view_count', 'N/D')
                })
    return resultados

def descargar_video_sin_audio(url: str, ruta_salida_mp4: str) -> str:
    """
    Descarga el vídeo de YouTube en máxima resolución vertical.
    """
    import yt_dlp

    Path(ruta_salida_mp4).parent.mkdir(parents=True, exist_ok=True)
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': str(ruta_salida_mp4).replace('.mp4', '') + '.%(ext)s',
        'quiet': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return str(ruta_salida_mp4)
