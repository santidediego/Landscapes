
# Landscapes
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

