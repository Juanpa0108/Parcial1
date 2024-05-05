import subprocess
import os
from datetime import datetime
import time
import multiprocessing

tiempoInicio = time.time()

def descargarVideo(canal):
    subprocess.run(['yt-dlp', '--max-downloads', '5', '--format', 'mp4', canal])

def convertirAudio(nombreArchivo):
    if nombreArchivo.endswith('.mp4'):
        archivoAudio = nombreArchivo.replace('.mp4', '.mp3')
        if os.path.exists(archivoAudio):
            os.remove(archivoAudio)
        subprocess.run(['ffmpeg', '-i', nombreArchivo, archivoAudio])
        os.remove(nombreArchivo)

def descargarVideos(canales, numProcesos):
    urlsVideos = []

    # Descargar videos en paralelo
    with multiprocessing.Pool(processes=numProcesos) as pool:
        pool.map(descargarVideo, canales)

    for canal in canales:
        salida = os.popen(f'yt-dlp --get-id --max-downloads 5 {canal}').read().strip()
        idVideos = salida.split('\n')
        for videoId in idVideos:
            urlsVideos.append(f'https://www.youtube.com/watch?v={videoId}')

    # Convertir videos descargados a audio en paralelo
    with multiprocessing.Pool(processes=numProcesos) as pool:
        pool.map(convertirAudio, os.listdir('.'))

    # Escribir datos en el registro.txt
    datosTotales = []
    for video in urlsVideos: 
        salida2 = os.popen(f'yt-dlp --get-title --print upload_date "{video}"').read().strip()
        fechaTitulo = datetime.now()
        fechaDescarga = fechaTitulo.strftime('%Y-%m-%d')
        datosTotales.append('\n')
        datosTotales.append(salida2)
        datosTotales.append(fechaDescarga)

    with open('registro.txt', 'a') as datos:
        datos.write('\n' .join(datosTotales))

def pedir_urls():
    print("Ingresa los URLs de los 5 canales de YouTube:")
    canales = [input(f"Canal {i+1}: ") for i in range(5)]
    return canales

if __name__ == "__main__":
    canales = pedir_urls()
    descargarVideos(canales, 16)

    print("Proceso completado. Se han descargado los últimos 5 videos de cada canal y se ha extraído el audio.")

    tiempoFin = time.time() - tiempoInicio
    print(f"Tiempo de finalización: {tiempoFin}")