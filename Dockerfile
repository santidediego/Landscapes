FROM ubuntu
RUN mkdir /home/Landscapes
COPY ./ /home/Landscapes
RUN cd /home/Landscapes && chmod a+x docker_run
RUN cd /home/Landscapes/ && ./docker_run
CMD python3 /home/Landscapes/inicio.py
