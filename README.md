# Pruebas
Repositorio de prueba con la libreria OpenCV para Python 3
## Integrantes/Colaboradores
- Kevin Meza A01639770
- Marco Antonio Camalich Pérez A01351725
- Rogelio Guzman Cruzado a01639914
- Alejandro Paredes Balgañon A01351746
- Diego Navarro Aguilar A01640436
## Descripción
El proyecto consta del uso del Lenguaje de Programación Python con su herramienta OpenCv, el cuál utiliza la cámara del dispositivo para realizar diferentes modificaciones visuales. Este se utiliza por medio de una interfaz generada por la consola del IDLE que genera un ingreso de datos equivalente a un número entre el 0 y el 6 dependiendo de la acción que se desee ejecutar. El código ejecutable lleva de nombre 'proyecto.py'. Las actividades realizadas por la aplicación y su respectivo número son las siguientes:
- 1: Deteccion de figuras: por medio de la delimitacion de siluetas, el calculo de los vertices de estas y su relacion de aspecto es posible identificar de que figura se trata.
- 2: Detección de Movimientos: El código de detección de movimientos se encarga de observar cambios en el exacto lugar de movimiento de un cuadro de video en contraste con el fotograma anterior, denotando esa sección por medio de cuadrículas color verde que van cambiando con el tiempo si la cuadrícula de video observada por la cámara del dispositivo sigue viéndose modificada por la constante alteración de colores, sombras y figuras.
- 3: Deteccion de objetos en una imagen: Este programa detecta el número de objetos en una imagen usando un sistema de delineación y acentuación de bordes que define si se está mostrando en pantalla un objeto o no, el proceso se resume en lectura de imagen, conversion a escala de grises, delineación de bordes, y conteo del número de bordes detectados.
- 4: Detector de Rasgos Faciales: Para generar el código de detección de rasgos faciales, se integraron el programa de detección de caras, detección de ojos y detección de sonrisas. Por lo que el código a ejecutar es el Detector_Rasgos_Faciales.py. Lo que hace el programa es generar cuadros que identifican la sonrisa, los ojos y la cara de las personas.
- 5: Detección de colores: Por medio de la definicion de rangos de colores es posible identificar objetos con un color dentro de esos rangos, por medio de la detección de su silueta, para luego esta ser suavisada e impresa sobre la imagen con el color que corresponte al grupo que pertenece, por ultimo se circunscribe un circulo a su silueta, y con el centro del circulo cinscurcrito de calcula el centro de la figura, imprimiendose su valor en color verde apartir del centro de la figura.
- 6: Filtro Gaussiano y Canny para detección de Bordes
- 0: No ejecutar ningún proceso y salir.
## Referencias
- 1: Deteccion de figuras: https://omes-va.com/detectando-figuras-geometricas-con-opencv-python/
- 2: Detección de Movimiento: https://www.youtube.com/watch?v=kcmJQzu_q6M
- 3: Contador de objetos: https://www.youtube.com/watch?v=jYSdkLBzD88&ab_channel=OMES
- 4.1: Detección de caras: https://www.youtube.com/watch?v=J1jlm-I1cTs&t=225s
- 4.2: https://github.com/opencv/opencv/tree/master/data/haarcascades
- 5: Detección de colores: https://www.youtube.com/watch?v=CFuyXw-pfPY
