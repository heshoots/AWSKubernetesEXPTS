SCALING CLUSTER

kops edit ig nodes --name=$NAME

you will have a file open in your text editor

edit the lines

maxSize: X
and
minSize: Y

to the required values

now run

kops update cluster $NAME

to see the changes that will be made

then run

kops update cluster $NAME --yes

kops rolling-update cluster --name=$NAME

now wait for the nodes to spin up


SCALING CASSANDRA

scaling cassandra itself is more complicated

edit the number of pods with

helm upgrade --set config.cluster_size=4 cassandra incubator/cassandra

these however will often fail due to not having a persistent volume

you may see "Pending" as the node status
