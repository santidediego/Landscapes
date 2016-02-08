
# Landscapes
[![Build Status](https://travis-ci.org/santidediego/Landscapes.svg?branch=master)](https://travis-ci.org/santidediego/Landscapes)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://landscapes93.herokuapp.com)

[<img src="http://azuredeploy.net/deploybutton.png" alt="Azure" height=32>](http://landscapes-vagrantazure-service-fxpxh.cloudapp.net) 

Repositorio para el proyecto de una infraestructura virtual para complementar el proyecto de la asignatura de Diseño de Aplicaciones para Internet.


##Descripción

Dicho proyecto consiste en una aplicación web que constituye una red social para amantes de la fotografía. La aplicación permite al usuario crearse una cuenta y almacenar lugares con valor fotográfico marcándolos en un mapa. Además el usuario añade un título, descripción... (y más especificaciones aún por determinar). La idea es que esos lugares pueden ser vistos por el resto de usuarios, que al mismo tiempo pueden añadir sus lugares favoritos y así todos pueden compartirlos. Tenemos pensadas más especificaciones pero aún hay que concretarlas.

La idea del proyecto surge de una necesidad que me planteé en su día como fotógrafo aficionado que soy de una especie de red social que permita a la gente compartir sus lugares favoritos para sacar fotografías.

##Detalles en la elaboración

Mi proyecto de Infraestructura Virtual consiste en la automatización de la creación de toda la base de datos MongoDB en una máquina Virtual con Azure con los usuarios (datos personales) y sus lugares marcados, así como la foto correspondiente. Esta MV la he creado con MongoLab alojándola en Azure, después de hacerlo una vez para el prototipo en Azure pero instalándola yo en una máquina virtual pero me decanté por usar MongoLab ya que era mucho más sencillo de configurar. Podemos ver la forma tradicional de hacerlo [aquí](https://github.com/santidediego/Landscapes/blob/master/Instalacion_configuracion_bd_azure.md), creando la MV desde cero.

Además configuraré todo el despliegue automático de la aplicación completa, también en otra MV en Azure y en Heroku. Además he configurado el despliegue de otra máquina virtual en azure para producción.

Para el desarrollo de la aplicación web utilizaremos el framework [Flask](http://flask.pocoo.org)

##Colaboradores
Para la parte del diseño y puesta en marcha de la aplicación web colaboro con Javier Pérez (@neon520). La parte de la infraestructura virtual la hago yo enteramente (Despliegue, test, integración continua, BD´s...).

##Preparación del entorno Virtual

Entramos en nuestra carpeta y definimos nuestro entorno como `virtualenv landscapes` después lo activamos con `cd landscapes & source bin/activate`

#Integración continua

En esta segunda parte añadiré integración continua al repositorio. Para ello utilizaré [Travis](https://travis-ci.org).

Aquí podemos ver el archivo [.travis.yml](https://github.com/santidediego/Landscapes/blob/master/.travis.yml)

Sin añadir todavía ningún test, solamente con la configuración de las librerías vemos que travis da el visto bueno:

![Integración continua](http://i864.photobucket.com/albums/ab201/Santiago_de_Diego/Integracion%20continua%20flask_zps3r8smu6w.png)

##Archivo requirements

En python, podemos generar un archivo con lo requerimientos básicos de la aplicación. Esto lo hacemos sin más que ejecutar `pip3 freeze > requirements.txt`

##Makefile

Ejecutando la orden `make test` se pasan los test que he definido para el proyecto. El archivo makefile se encuentra dentro de la carpeta *Landscapes*. Una vez dentro ya se puede ejecutar `make test` para pasar los tests.

#Despliegue en Heroku
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

#Subiendo el proyecto a Docker

Podemos ver los pasos seguidos [aquí](https://github.com/santidediego/Landscapes/blob/master/PASOS.md)

###Posible problema
Al arrancar el contenedor me encuentro con que no tiene conexión a internet. En mi caso lo he solucionado editando el archivo `/etc/NetworkManager/NetworkManager.conf` y comentando la línea `dns=dnsmask`. Sin mas que ejecutar luego `sudo restart network-manager` ya funciona correctamente. Se puede ver el problema y la solución es [esta issue](https://github.com/docker/docker/issues/1809)

###Añadiéndolo a DockerHub

Primero de todo he tenido que asignar un tag a mi contenedor para que coincida con el repositorio que he creado en Docker Hub, que en mi caso era *santidediego/landscapes*. El tag se lo asigno con `docker tag b66ff6f57f2e santidediego/landscapes` . Una vez hecho esto ejecuto `docker push santidediego/landscapes` y comienza a subirse.

Para instalar el contenedor en local, basta ejecutar:

`docker pull santidediego/landscapes`

y el contenedor comienza a instalarse. No hace falta hacer nada más, una vez terminada la instalación, se ejecuta automáticamente la aplicación siguiendo las directrices del Dockerfile que a su vez enlaza con los scripts de instalación y configuración.

Se puede encontrar el docker de mi proyecto [aquí](https://hub.docker.com/r/santidediego/landscapes/)

#Despliegue automático con fabric
He decidido hacer un despliegue con fabric en una Máquina Virtual Azure con Ubuntu 15, para ello, utilizaré un fichero [fabfile.py](https://github.com/santidediego/Landscapes/blob/master/fabfile.py) en el que aparecen varias directivas para trabajar remotamente con nuestra MV. El proceso seguido es similar al utilizado para la [creación de la base MongoDB en Azure](https://github.com/santidediego/Landscapes/blob/master/Instalacion_configuracion_bd_azure.md) solo que con otra máquina virtual distinta. En este caso podemos conectarnos a nuestra máquina por ssh con `ssh 40.74.49.235 `


##Problema: Utilización de python 2.7
Fabric no está disponible para python 3.5, y por tanto he tenido que crearme aparte un entorno virtual con python 2.7, instalar fabric en él con `pip install fabric` y ejecutar el comando desde ese entorno virtual; es un poco engorroso pero es la única solución y además funciona.

Ahora, para hacer el despliegue, basta ejecutar `fab deploy` y comienza a desplegarse. [Aquí](https://github.com/santidediego/Landscapes/blob/master/Fabric.md) podemos ver los detalles.

#Creación de una MV en Azure con Vagrant y provisionamiento con Ansible

En mi caso lo he realizado en un equipo con Mac Os X. Para esta parte lo primero es instalar Vagrant de [aquí](https://www.vagrantup.com/downloads.html) y Ansible, que podemos hacerlo con `brew install ansible`. Una vez hecho esto, he seguido el [siguiente tutorial](https://github.com/Azure/vagrant-azure) para conectar mi cuenta de Azure con Vagrant y de ahí he elaborado el correspondiente [Vagrantfile](https://github.com/santidediego/Landscapes/blob/master/Vagrantfile).

##Cómo funciona
EL Vagrantfile se conecta con la MV en Azure después de crearla e instala todo lo que aparece en mi receta de Ansible que podemos encontrar en la carpeta ansible como [webservice.yml](https://github.com/santidediego/Landscapes/blob/master/ansible/webservice.yml). De esta manera se despliega la aplicación en la MV sin más que ejecutar `vagrant up`.

Además he configurado el despliegue y la configuración automática de una BD Mongo en otra MV de Azure. Para desplegarla, hay que entrar a la carpeta [vagrant-mongo](https://github.com/santidediego/Landscapes/tree/master/vagrant-mongo) y ejecutar `vagrant up` donde hay definido otro Vagrantfile que se encarga de esta parte. He decidido hacerlo de esta manera para que el usuario pueda elegir qué quiere desplegar por separado, y que no se desplieguen las dos cosas a la vez cuando se haga `vagrant up`
No obstante, la principal base de datos la monta automáticamente MongoLab, pero pongo el Vagrantfile por si se desea montarla en azure por cuenta propia.

Además he incluido otro Vagrantfile en la carpeta [Servidor de producción](https://github.com/santidediego/Landscapes/tree/master/Servidor_produccion) para crear otra MV que sirva para producción.

##Combinándolo con Fabric

Podemos utilizar Fabric para trabajar con nuestra MV en Azure creada con Vagrant desde un equipo remoto, sin más que utilizar la dirección `168.61.157.18` correspondiente a la dirección de la MV (Actualmente tengo puesta esta en el archivo de configuración para no tener que cambiarla). Para ver los comandos disponibles ver la sección de Fabric más atrás.