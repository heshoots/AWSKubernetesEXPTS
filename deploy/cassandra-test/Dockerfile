FROM cassandra:latest
ADD . /home/
RUN apt-get update && apt-get install -y \
    vim \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /home/
EXPOSE 9042
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
