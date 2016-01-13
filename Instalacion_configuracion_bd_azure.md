#Configuración de la MV en Azure

Primero de todo nos logeamos con `azure login`

Después seleccionamos la suscripción por defecto que queremos, en mi caso: `azure account set "Pase de azure"`

Después ejecutamos `azure vm create landscapes-bd -o vmdepot-63471-1-32 -l "West Europe" santiago ***** --ssh`

###Si lo anterior no funciona
Creamos una MV desde la página de azure con Ubuntu Server y nos conectamos por ssh, en mi caso: `ssh santiago@40.114.251.112` y una vez dentro ya podemos instalar lo que queramos manualmente.

Para instalar MongoDB en un Ubuntu Server seguimos el siguiente [tutorial](http://www.mongodbspain.com/es/2014/08/30/install-mongodb-on-ubuntu-14-04/)

###Credenciales de Mongo:
user: mongouser

password: 09021993

Conexión: `mongo --host 40.121.141.129 --port 27017 -u mongouser -p 09021993 --authenticationDatabase admin`