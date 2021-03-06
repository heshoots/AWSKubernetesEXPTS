For the last few weeks I have been experimenting with using cassandra on an AWS cluster, a lack of resources on setting this up was an issue, so here is a brief guide on setting htis up!

Before starting:

If you have no experience with kubernetes, you can try it out on your own machine without using AWS, try out minikube. I have had some stability issues using this on my machine with cassandra however, so moved over to AWS instead.

If you want to learn more about how this works you can follow a guide on how to set up a cassandra cluster from scratch here:

If you have done this or just want to set up a cluster feel free to follow along

Requirements:
  AWS cloud
  AWS account with the following permissions

  Installed:
    kubectl
    kops
    awscli
    helm

Begin by launching a cluster using kops
you can follow this guide

AAAAAAAAAAAAAAAAAAAAAAAAA

kops creates a new kubernetes "kind" called a cluster, this confused me due to my previous experiments in kubernetes. This is essentially what it says on the tin, a description of a cluster, not as I imaged, a description of a cluster and what to run on it.

Now you have your cluster set up, lets add cassandra to it.

First, you will need to add the helm "tiller" to the cluster, do this with `helm init`

You will also need to add the incubator repository to get access to the cassandra chart.

If using the default cluster set up by kops you may also want to edit some of the settings for the cassandra cluster since the defaults will leave a pod with no resources to function

fetch the chart using 

helm fetch --untar incubator/cassandra
cd cassandra

edit the values.yaml file in this folder with the following settings

run

helm install --namespace "cassandra" -n "cassandra" --values=values.yaml incubator/cassandra

this will create all of the services pods and statelessSets you need to run a cassandra cluster. these will be under the namespace "cassandra".

using 

`helm status "cassandra"`

you can see the state of the setup
you can use 

`kubectl get all --namespace "cassandra"`

to see the state of all the elements of the cassandra cluster, then when you are done, run

`BLAH BLAH nodetool status`

and if all is well, you should see a screen like this. 

Congratulations, your cassandra cluster is up and running.

Clean up

Deleting the cluster is as simple as kops delete cluster ${name}.

---

TESTING SCHEMA

If you want to find out the performance of the cluster for your data needs, I have created a docker image for that,
in deploy/cassandra-stress you will find a basic file (you may need to edit and reupload to dockerhub to add your own text editor)

delete your cassandra cluster with

helm delete --purge cassandra

start up the testcass instance

kubectl create -f cassandra-test.yaml --namespace=cassandra

install the cassandra cluster again as before, now when done, attach to the cassandra-test pod with

kubectl exec -it cassandra-test --namespace=cassandra -- bash

from here you can run cassandra-stress commands on your cluster

try    cassandra-stress write -node <cassandra-cassandra-0 ip>

to test your own schema edit stress.yaml and run with

cassandra-stress user profile=stress.yaml ops\(insert=1\) n=1000000 -rate threads=32

---

TO ADD

scaling cluster up and down

To add nodes to the cluster use

kops edit ig nodes --name=${NAME}
and change

minnodes=NUM
maxnodes=NUM

then run kops cluster upgrade 
kops cluster rolling-update

and wait for your cluster to come up with

kops validate cluster

when done, run 

helm 

decommisioning nodes


