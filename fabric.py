from fabric.api import *
env.user = 'santiago'
env.hosts = '40.114.215.241'

def deploy():
    run('sudo apt-get update')
	run('sudo apt-get install -y git')
	run('cd /home && sudo git clone https://github.com/santidediego/Landscapes')
    #Install
    run('sudo apt-get install -y python3-pip')
    run('sudo apt-get install -y python-software-properties') #Necesario para que funciones add-apt-repository
    run('sudo apt-get install build-essential')
    run('make install')
    
def execute():
    run('cd /home && python3 inicio.py')
    
#Instalacion de docker y descarga de imagen
def getDocker():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull santidediego/landscapes')
