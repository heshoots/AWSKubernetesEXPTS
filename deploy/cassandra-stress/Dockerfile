FROM openjdk:latest
RUN wget http://mirror.ox.ac.uk/sites/rsync.apache.org/cassandra/3.11.0/apache-cassandra-3.11.0-bin.tar.gz
RUN tar -xzf apache-cassandra-3.11.0-bin.tar.gz
RUN cp apache-cassandra-3.11.0/tools/bin/cassandra-stress /bin
EXPOSE 9042
WORKDIR /home
ADD . /home
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
