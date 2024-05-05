import subprocess
import os
from datetime import datetime
import time

timepoInicio= time.time()

def descargarVideos(canales):
    urlsVideos = []
    fechaDescarga = []
    datosTotales = []

    for canal in canales:
        subprocess.run(['yt-dlp', '--max-downloads', '5', '--format', 'mp4', canal])
        salida = os.popen(f'yt-dlp --get-id --max-downloads 5 {canal}').read().strip()
        idsVideos = salida.split('\n')
        for videoId in idsVideos:
            urlsVideos.append(f'https://www.youtube.com/watch?v={videoId}')

        
        for nombreArchivo in os.listdir('.'):
            if nombreArchivo.endswith('.mp4'):
                audioArchivo = nombreArchivo.replace('.mp4', '.mp3')
                if os.path.exists(audioArchivo):
                    os.remove(audioArchivo)
                subprocess.run(['ffmpeg', '-i', nombreArchivo, audioArchivo])
                os.remove(nombreArchivo)

    for video in urlsVideos: 
        salida2 = os.popen(f'yt-dlp --get-title --print upload_date "{video}').read().strip()
        fechaTitulo = datetime.now()
        fechaDescarga = fechaTitulo.strftime('%Y-%m-%d')
        datosTotales.append('\n')
        datosTotales.append(salida2)
        datosTotales.append(fechaDescarga)

    with open('registro.txt', 'a') as datos:
        datos.write('\n' .join(datosTotales) )

# Pedir al usuario que ingrese los URLs de los canales
def pedir_urls():
    print("Ingresa los URLs de los 5 canales de YouTube:")
    canales = []
    for i in range(5):
        canal = input(f"Canal {i+1}: ")
        canales.append(canal)
    return canales

# Obtener URLs de los canales del usuario y descargar los videos
canales = pedir_urls()
descargarVideos(canales)

print("Proceso completado. Se han descargado los últimos 5 videos de cada canal y se ha extraído el audio.")

tiempoFin = time.time() - timepoInicio

print(f"Tiempo de finalizacion {tiempoFin}")
