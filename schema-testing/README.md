HOW TO USE

start cassandra-test.yaml before you start up the cassandra cluster, this ensures that cassandra-test has access to all the ports required for testing

you can start it with

kubectl create -f cassandra-test.yaml --namespace=cassandra

find the ip address <cass-ip> on a node on the kubernetes cluster with

kubectl get pods -o wide --namespace=cassandra

to run a test like "cassandra-stress write -node <cass-ip>" run

remote-stress write -node <cass-ip>

to push a file to the test pod use 

push filename

you can use this for pushing yaml based tests, for example

push stress.yaml
remote-stress user profile=stress.yaml ops\(insert=1\) n=1000000 -node <cass-ip>
