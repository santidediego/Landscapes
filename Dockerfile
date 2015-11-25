FROM ubuntu
RUN apt-get install -y git  #Primero de todo instalamos git
RUN cd /home && git clone https://github.com/santidediego/Landscapes
#COPY ./ /home/Landscapes
RUN cd /home/Landscapes && chmod a+x docker_run
RUN cd /home/Landscapes/ && ./docker_run
CMD python3 /home/Landscapes/inicio.py
