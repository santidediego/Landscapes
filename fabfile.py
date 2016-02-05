from fabric.api import *
env.user = 'santiago'
env.hosts = '168.61.157.18'

def deploy():
    run('sudo apt-get update')
    run('sudo apt-get install -y git')
    run('cd /home/santiago && sudo git clone https://github.com/santidediego/Landscapes')
    #Install
    run('sudo apt-get install -y python3-pip')
    run('sudo apt-get install -y python-software-properties') #Necesario para que funciones add-apt-repository
    run('sudo apt-get install build-essential')
    run('sudo apt-get install python3-nose')
    run('cd /home/santiago/Landscapes && make install')

def execute():
    run('cd /home/santiago/Landscapes && python3 inicio.py')

#Instalacion de docker y descarga de imagen
def getDocker():
    run('sudo apt-get update')
    run('sudo apt-get install -y docker.io')
    run('mkdir /home/santiago/Contenedor')
    run('cd /home/santiago/Contenedor && sudo docker pull santidediego/landscapes')

def pull():
	run('cd /home/santiago/Landscapes && sudo git pull')

def test():
    run('cd /home/santiago/Landscapes && nosetests ./tests/test.py')
