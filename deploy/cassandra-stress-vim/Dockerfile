FROM quorauk/cassandra-stress:latest
RUN apt-get update && apt-get install -y \
    vim \
 && rm -rf /var/lib/apt/lists/*
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
