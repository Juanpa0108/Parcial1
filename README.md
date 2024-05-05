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
<p>Se importan las librerias necesarias para el correcto funcionamiento del aplicativo y se comienza a tomar el tiempo que tardara en ejecutarse el aplicativo, posteriormente se crea la funcion llamada "descargarVideos" que recibe un canal, del cual se descarga los ultimos 5 videos y se obtienen los id haciendo uso de la aplicacion yt-dlp, los cuales se usaran para rearmar la url proveniente del video que se guarda en un arreglo llamado urlsVideos, seguido se buscan todos los archivos terminados en .mp4 que tengas en la carpeta, verifica si existe algun archivo terminado en .mp3 antes de hacer la conversion, en caso de ser así se borra e inicia el proceso de extraccion de audio usando "ffmpeg", al finalizar este proceso se borra el archivo.mp4, finalizando la funcion recorrermos el arreglo de url y con cada uno de ellos obtenemos el nombre, fecha de publicacion y fecha de descarga de los videos y los guardamos en el archivo "registro.txt", continuando con la funcion llamada "descargarVideosEnparalelo", la cual recibe como parametros el arreglo con los canales  y el numero de procesos con el cual se ejecuta la aplicacion, haciendo uso del current.futures indicamos el numero de hilos con el cual trabajara la aplicacion y ejecutamos la funcion "descargarVideos" sobre cada uno de los valores del array que recibe como parametro, la ultima funcion que encontramos en el archivo es "pedirUrls" que, como su nombre lo indica, solicita al usuario los canales a los cuales se le realiza la descarga de los videos, finalizando el aplicativo tenemos la llamada a las funciones "pedirUrls" y "descargarVideosParalelo", luego de esto se finaliza el tiempo de ejecucion. </p>

<h3>parcialMulti.py</h3>
<p>Se importan las librerias necesarias para el funcionamiento del apicativo y se inicia la cuenta del tiempo que tarda en ejecutarse la aplicacion, encontramos una funcion llamada "descargarVideo" la cual recibe como argumento un canal y descarga los ultimos 5 videos, posteriormente encontramos la funcion "convertirAudio", la cual recibe el nombre del archivo y haciendo uso de la aplicacion ffmpeg extrae el audio para despues borrar el archivo con extension .mp4, luego encontramos la funcion llamada "descargarVideos" que recibe un array con los canales y el numero de procesos con los cuales se ejecuta el aplicativo, haciendo uso de la libreria multiprocessing indicamos la cantidad de procesos a usar y estos procesos se encargan de la ejecucion de la funcion "descargarVideo" con cada uno de los canales que tiene en el arreglo que recibe como parametro, posteriormente se recorre el array de los canales para obtener el id de cada video y reestructurar las url pertienentes, las cuales seran guardadas en un arreglo llamado "urlVideos". Luego haciendo uso nuevamente de la libreria multiprocessing indicamos el numero de procesos y esta vez realiza la funcion "convertirAudio" sobre todos los archivos terminados en .mp4 de la carpeta, al fnializar la conversion se recorre el arreglo urlVideos y haciendo uso de la aplicacion tdlp obtenemos el titulo, la fecha de publicacion del video y la escribimos en el archivo "registro.txt", posteriormente con la libreria dateTime de python indicamos la fecha de descarga, la cual tambien sera escrita en el archivo. Posteriormente encontramos una funcion llamada "pedir_urls", que como su nombre lo indica solicita al usuario los url de los canales de youtube. Por ultimo hacemos el llamado a las funciones "pedir_urls" y "descargarVideos", para así dar por finalizado el tiempo de ejecucion. </p>


<pre>Cabe aclarar que el numero de nucleos de procesamiento de las versiones en paralelo de la aplicacion se define al finalizar el archivo cuando se hace el llamado a la funcion pertinente.</pre>
