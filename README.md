
# Landscapes
[![Build Status](https://travis-ci.org/santidediego/Landscapes.svg?branch=master)](https://travis-ci.org/santidediego/Landscapes)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://landscapes93.herokuapp.com)

Repositorio para el proyecto de una infraestructura virtual para complementar el proyecto de la asignatura de Diseño de Aplicaciones para Internet.


##Descripción

Dicho proyecto consiste en una aplicación web que constituye una red social para amantes de la fotografía. La aplicación permite al usuario crearse una cuenta y almacenar lugares con valor fotográfico marcándolos en un mapa. Además el usuario añade un título, descripción... (y más especificaciones aún por determinar). La idea es que esos lugares pueden ser vistos por el resto de usuarios, que al mismo tiempo pueden añadir sus lugares favoritos y así todos pueden compartirlos. Tenemos pensadas más especificaciones pero aún hay que concretarlas.

La idea del proyecto surge de una necesidad que me planteé en su día como fotógrafo aficionado que soy de una especie de red social que permita a la gente compartir sus lugares favoritos para sacar fotografías.

##Detalles en la elaboración

Mi proyecto de Infraestructura Virtual consiste en la automatización de la creación de toda la base de datos gestionada con mySQL con los usuarios y sus lugares marcados en un servidor en la nube. El despliegue lo haré casi seguramente en Bluemix, aunque también me planteo utilizar otro servidor como por ejemplo Azure para realizar réplicas de la base de datos como seguridad ante fallos.

Para el desarrollo de la aplicación web utilizaremos el framework [Flask](http://flask.pocoo.org)

##Colaboradores
Para la parte del diseño y puesta en marcha de la aplicación web colaboro con Javier Pérez (@neon520).

##Preparación del entorno Virtual

Entramos en nuestra carpeta y definimos nuestro entorno como `virtualenv landscapes` después lo activamos con `cd landscapes & source bin/activate`

#Segundo hito

En esta segunda parte añadiré integración continua al repositorio. Para ello utilizaré [Travis](https://travis-ci.org).

Aquí podemos ver el archivo [.travis.yml](https://github.com/santidediego/Landscapes/blob/master/.travis.yml)

Sin añadir todavía ningún test, solamente con la configuración de las librerías vemos que travis da el visto bueno:

![Integración continua](http://i864.photobucket.com/albums/ab201/Santiago_de_Diego/Integracion%20continua%20flask_zps3r8smu6w.png)

##Archivo requeriments

En python, podemos generar un archivo con lo requerimientos básicos de la aplicación. Esto lo hacemos sin más que ejecutar `pip3 freeze > requeriments.txt`

##Makefile

Ejecutando la orden `make test` se pasan los test que he definido para el proyecto. El archivo makefile se encuentra dentro de la carpeta *Landscapes*. Una vez dentro ya se puede ejecutar `make test` para pasar los tests.

#Tercer hito
En esta tercera parte voy a integrar mi proyecto con Heroku. Para ello lo configuraré para que cuando se haga un *push* en el repositorio directamente se suba a Heroku.

Primero de todo ejecutamos `pip3 install gunicorn`.  Después ejecutamos `heroku keys:add` y selecionamos la clave ssh que hemos utilizado para Github. Ahora ya podemos conectarnos a Heroku por ssh. Ahora ya vamos a la página de heroku, le damos a nueva aplicación y le ponemos un nombre.


Ahora vamos a hacer uso de un fichero Procfile. Este fichero debemos definirlo en nuestro directorio raíz y es donde declaramos los comandos que deberían ser ejecutados al arrancar nuestra aplicación. 

Lo creamos y dentro escribimos:

```
web: gunicorn inicio:app --log-file=logs
```

ya que *inicio.py* es el nombre de nuestro archivo python que carga la aplicación.

Una vez hecho esto, desde el propio Heroku podemos configurar el despliegue automático desde Github. Además es conveniente que marquemos la casilla de despliegue sólo si se han pasado los test. La configuración queda como aparece en la imagen:

![Github-Heroku](http://i864.photobucket.com/albums/ab201/Santiago_de_Diego/Githu-Heroku_zpskiwpnetq.png)

Y ya tenemos configurado nuestro despliegue automático, una vez se haga *git push* al repositorio. Se puede visitar mi aplicación [aquí](https://landscapes93.herokuapp.com)

##Runtime.txt
He tenido varios problemas para el despliegue en Heroku. El motivo era que no tenía creado un [fichero runtime.txt](https://devcenter.heroku.com/articles/python-runtimes) que es necesario para especificar la versión de python que estás utilizando.

#Cuarto hito
En esta parte vamos a configurar un Docker para almacenar el proyecto. Primero de todo he instalado Docker en un equipo en el que tengo Ubuntu. He instalado Docker mediante el comando: `wget -qO- https://get.docker.com/ | sh`	

Después basta ejecutar `sudo usermod -aG docker santiago` para no tener que estar haciendo `sudo` todo el rato cada vez que instalemos algo dentro de nuestro contenedor. Con `sudo nohup docker -d&` arrancamos el demonio de Docker y probamos que efectivamente funciona con `docker run hello-world`

Ahora falta descargar una imagen para Docker, he elegido la de [este repositorio](https://github.com/harbur/docker-workshop/). Sin más que hacer lo que nos dice: primero hacemos un `git clone` y luego un `docker pull ubuntu` tenemos una imagen de Docker lista para empezar a trabajar.

Una vez hecho esto, creamos un [Dockerfile](https://github.com/santidediego/Landscapes/blob/master/Dockerfile) en nuestro repo del proyecto donde tenemos todas las tareas de construcción del contenedor, así como la copia de los archivos desde nuestro repositorio al contenedor. Además en el fichero se hace referencia a un archivo [docker_run](https://github.com/santidediego/Landscapes/blob/master/docker_run) que no es más que un script que se encarga de instalar todo lo necesario para preparar el contenedor. Después el propio script llama al [makefile](https://github.com/santidediego/Landscapes/blob/master/makefile) que instala todas las dependencias necesarias.

Sin más que ejecutar `sudo docker build -t landscapes .` comienza todo el proceso. Con `build -t` le decimos que utilice el Dockerfile situado en `.` y `landscapes` es el nombre que tendrá el contenedor.

Una vez está todo instalado, podemos ver el contenedor en su [repositorio correspondiente de DockerHub]()  ¡AVISO: AUN NO HAY REPOSITORIO!