FROM cassandra:latest
ADD . /home/
WORKDIR /home/
EXPOSE 9042
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
