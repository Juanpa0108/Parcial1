import subprocess
import os
from datetime import datetime
import time
import concurrent.futures


tiempoInicio = time.time()

def descargarVideos(canal):
    urlsVideos = []
    fechaDescarga = []
    datosTotales = []

    with open(os.devnull, 'w') as null:
        subprocess.run(['yt-dlp', '--max-downloads', '5', '--format', 'mp4', canal], stdout=null, stderr=null)
        salida = os.popen(f'yt-dlp --get-id --max-downloads 5 {canal}').read().strip()
        idVideos = salida.split('\n')
        for videoId in idVideos:
            urlsVideos.append(f'https://www.youtube.com/watch?v={videoId}')

        for nombreArchivo in os.listdir('.'):
            if nombreArchivo.endswith('.mp4'):
                nombreAudio = nombreArchivo.replace('.mp4', '.mp3')
                if os.path.exists(nombreAudio):
                    os.remove(nombreAudio)
                subprocess.run(['ffmpeg', '-i', nombreArchivo, nombreAudio], stdout=null, stderr=null)
                os.remove(nombreArchivo)

        for video in urlsVideos:
            salida2 = os.popen(f'yt-dlp --get-title --print upload_date "{video}').read().strip()
            fechaTitulo = datetime.now()
            fechaDescarga = fechaTitulo.strftime('%Y-%m-%d')
            datosTotales.append('\n')
            datosTotales.append(salida2)
            datosTotales.append(fechaDescarga)

        with open('registro.txt', 'a') as data:
            data.write('\n'.join(datosTotales))

def descargarVideosParalelo(canales, numeroProcesos):
    with concurrent.futures.ThreadPoolExecutor(max_workers=numeroProcesos) as executor:
        executor.map(descargarVideos, canales)

def pedirUrls():
    print("Ingresa los URLs de los 5 canales de YouTube:")
    canales = []
    for i in range(5):
        canal = input(f"Canal {i+1}: ")
        canales.append(canal)
    return canales

canales = pedirUrls()
descargarVideosParalelo(canales, 16)

print("Proceso completado. Se han descargado los últimos 5 videos de cada canal y se ha extraído el audio.")

tiempoFin = time.time() - tiempoInicio
print(f"Tiempo de finalizacion {tiempoFin}")
