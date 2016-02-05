#Detalles del despliegue automático
En mi caso he utilizado una MV virgen en Azure como podemos ver en la imagen

![imagen](http://i864.photobucket.com/albums/ab201/Santiago_de_Diego/Captura%20de%20pantalla%202016-01-03%20a%20las%2020.34.11_zpshbek0cmh.png)

Ahora ejecutamos `fab deploy` y esperamos. Una vez se ha terminado el despliegue, podemos ver como se ha instalado todo:

![imagen](http://i864.photobucket.com/albums/ab201/Santiago_de_Diego/Captura%20de%20pantalla%202016-01-03%20a%20las%2020.38.59_zpshhedqw5z.png)

Podemos ejecutar otros comandos como:

- execute: para ejecutarlo
- getDocker: para instalar el contenedor
- test: para pasar los test
- pull: para descargar la última versión de la aplicación