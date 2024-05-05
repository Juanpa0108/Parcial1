<h1>Integrantes</h1>
<h3>Nicole Narvaez - nicole.narvaez@correounivalle.edu.co - 202156947-3743</h3>
<h3>Juan Pablo Robayo - robayo.juan@correounivalle.edu.co - 202156743-3743</h3>

<h2>Requerimientos minimos</h2>
<ul>
  <li> yt-dlp instalado</li>
  <li> ffmpeg instalado</li>
  <li> python instalado</li>
  <li> Conexion estable a internet</li>
</ul>

<h2>Como ejecutar el programa</h2>

<pre>Este paso a paso sera suponiendo que ya tienes instalado el yt-dlp y ffmpeg</pre>
<ol>
  <li>Muevete a la carpeta donde descargaste o clonaste respositorio usando el comando "cd" en la consola</li>
  <li>Usa el comando "python" segudido del nombre del archivo que desees ejecutar, siendo así: 
    <ul>
      <li> parcialSecuencial.py la version secuencial del programa</li>
      <li> parcialThread.py la version paralela del programa usando multithreading </li>
      <li> parcialMulti.py la version paralela del programa usando multiprocessing </li>
    </ul>
  </li>
  <li> Administra las url de los 5 canales </li>
</ol>


<h2>Descripcion de la logica del aplicativo</h2>

<h3>parcialSecuencial.py</h3>
<p>Se importan las librerias necesarias para el funcionamiento del aplicativo, posteriormente se inicia la toma del tiempo que tardara en ejecutarse el archivo, seguido se crea la funcion descargarVideos la cual recibe como argumento un arreglo de canales sobre los cuales va a iterar mediante un ciclo for, en cada iteracion descargamos 5 videos de cada canal, obtenemos el id de cada video, creamos la url a la que pertenece el id y lo guardamos en un arreglo llamado urlVideos. Posteriormente buscamos en la carpeta donde nos encontramos todos los archivos que terminen en .mp4, verificamos si existe un archivo con extension .mp3 y en caso que exista se borra, luego con el programa ffmpeg se extrae el audio creando así un archivo .mp3 por cada video descargado, seguido de eso se borra el archivo con extension .mp4. Despues recorremos los url guardados al comienzo de la aplicacion mediante un ciclo for y en cada iteracion obtenemos el nombre, fecha de publicacion y fecha de descarga del mismo, estos datos los guardamos en un archivo llamado registro.txt, así dando por finalizada la funcion para descargar los videos. Continuando nos encontramos con otra funcion la cual se encarga de solicitar los url de los videos al usuario. Terminando el programa se llama a cada una de estas funciones y se toma el tiempo que tardo en ejecutarse la aplicacion. </p>

<h3>parcialThread.py</h3>
<p>Se importan las librerias necesarias para el correcto funcionamiento del aplicativo y se comienza a tomar el tiempo que tardara en ejecutarse el aplicativo </p></p>
