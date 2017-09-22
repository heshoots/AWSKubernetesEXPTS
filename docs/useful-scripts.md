create cluster
kops create cluster $NAME --zones eu-west-1b
kops edit ig nodes --name=$NAME
