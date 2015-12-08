#Pasos de creación y configuración del contenedor

En esta parte vamos a configurar un Docker para almacenar el proyecto. Primero de todo he instalado Docker en un equipo en el que tengo Ubuntu. He instalado Docker mediante el comando: `wget -qO- https://get.docker.com/ | sh`

Después basta ejecutar `sudo usermod -aG docker santiago` para no tener que estar haciendo `sudo` todo el rato cada vez que instalemos algo dentro de nuestro contenedor. Con `sudo nohup docker -d&` arrancamos el demonio de Docker y probamos que efectivamente funciona con `docker run hello-world`

Ahora falta descargar una imagen para Docker, he elegido la de [este repositorio](https://github.com/harbur/docker-workshop/). Sin más que hacer lo que nos dice: primero hacemos un `git clone` y luego un `docker pull ubuntu` tenemos una imagen de Docker lista para empezar a trabajar.

Una vez hecho esto, creamos un [Dockerfile](https://github.com/santidediego/Landscapes/blob/master/Dockerfile) en nuestro repo del proyecto donde tenemos todas las tareas de construcción del contenedor, así como la copia de los archivos desde nuestro repositorio al contenedor. Además en el fichero se hace referencia a un archivo [docker_run](https://github.com/santidediego/Landscapes/blob/master/docker_run) que no es más que un script que se encarga de instalar todo lo necesario para preparar el contenedor. Después el propio script llama al [makefile](https://github.com/santidediego/Landscapes/blob/master/makefile) que instala todas las dependencias necesarias.

Sin más que ejecutar `sudo docker build -t landscapes .` comienza todo el proceso. Con `build -t` le decimos que utilice el Dockerfile situado en `.` y `landscapes` es el nombre que tendrá el contenedor.
