# Examen final

Este proyecto es un sistema de asistencia para aulas que utiliza reconocimiento facial usando `face_recognition` y WebRTC.

## Integrantes
 1. Delgado Pérez, José Alexis 
 2. Espinoza Huaman, Diego Alexhander
 3. Linares Rojas, Ander Rafael
 4. Ramirez Chero, Alejandro David
 5. Pozo Hernandez, Jhanilde Selenne del Pilar

## Requisitos previos

* Docker
* Node.js
* npm

## Instalación

1. Clona este repositorio: `git clone https://github.com/ElBromasMC/final-exam.git`
2. Ingresa al directorio: `cd final-exam`
3. Construye la imagen de Docker: `docker build -f Dockerfile -t elbromasmc/final-exam .`
4. Ejecuta el contenedor: `docker compose -f docker-compose.dev.yml up --build`
5. Abre tu navegador en [http://127.0.0.1:8080](http://127.0.0.1:8080)

## Uso

1. Haz clic en el botón "Iniciar" para comenzar a transmitir video desde tu cámara web.
2. El sistema reconocerá las caras en el video y mostrará los nombres de los estudiantes identificados.
3. Haz clic en el botón "Registrar Asistencia" para generar un archivo CSV con la asistencia.
4. Haz clic en el enlace "Descargar Asistencia" para descargar el archivo CSV.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una rama con tu función: `git checkout -b mi-funcion`
3. Haz commit de tus cambios: `git commit -am 'Agrega mi función'`
4. Haz push a la rama: `git push origin mi-funcion`
5. Abre un pull request.

## Definición de entorno

Ejemplo del contenido del archivo `.env`

```bash
USER_UID=1000
```


## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más información.
