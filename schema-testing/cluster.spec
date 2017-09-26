metadata:
  creationTimestamp: 2017-09-26T06:55:20Z
  name: epicass.k8s.local
spec:
  api:
    loadBalancer:
      type: Public
  authorization:
    alwaysAllow: {}
  channel: stable
  cloudProvider: aws
  clusterDNSDomain: cluster.local
  configBase: s3://whisky-cass-state-store/epicass.k8s.local
  configStore: s3://whisky-cass-state-store/epicass.k8s.local
  docker:
    bridge: ""
    ipMasq: false
    ipTables: false
    logDriver: json-file
    logLevel: warn
    logOpt:
    - max-size=10m
    - max-file=5
    storage: overlay,aufs
    version: 1.12.6
  etcdClusters:
  - etcdMembers:
    - instanceGroup: master-eu-west-1b
      name: b
    name: main
  - etcdMembers:
    - instanceGroup: master-eu-west-1b
      name: b
    name: events
  keyStore: s3://whisky-cass-state-store/epicass.k8s.local/pki
  kubeAPIServer:
    address: 127.0.0.1
    admissionControl:
    - NamespaceLifecycle
    - LimitRanger
    - ServiceAccount
    - PersistentVolumeLabel
    - DefaultStorageClass
    - DefaultTolerationSeconds
    - ResourceQuota
    allowPrivileged: true
    anonymousAuth: false
    apiServerCount: 1
    authorizationMode: AlwaysAllow
    cloudProvider: aws
    etcdServers:
    - http://127.0.0.1:4001
    etcdServersOverrides:
    - /events#http://127.0.0.1:4002
    image: gcr.io/google_containers/kube-apiserver:v1.7.2
    insecurePort: 8080
    kubeletPreferredAddressTypes:
    - InternalIP
    - Hostname
    - ExternalIP
    logLevel: 2
    securePort: 443
    serviceClusterIPRange: 100.64.0.0/13
    storageBackend: etcd2
  kubeControllerManager:
    allocateNodeCIDRs: true
    attachDetachReconcileSyncPeriod: 1m0s
    cloudProvider: aws
    clusterCIDR: 100.96.0.0/11
    clusterName: epicass.k8s.local
    configureCloudRoutes: true
    image: gcr.io/google_containers/kube-controller-manager:v1.7.2
    leaderElection:
      leaderElect: true
    logLevel: 2
    useServiceAccountCredentials: true
  kubeDNS:
    domain: cluster.local
    image: gcr.io/google_containers/kubedns-amd64:1.3
    replicas: 2
    serverIP: 100.64.0.10
  kubeProxy:
    clusterCIDR: 100.96.0.0/11
    cpuRequest: 100m
    hostnameOverride: '@aws'
    image: gcr.io/google_containers/kube-proxy:v1.7.2
    logLevel: 2
  kubeScheduler:
    image: gcr.io/google_containers/kube-scheduler:v1.7.2
    leaderElection:
      leaderElect: true
    logLevel: 2
  kubelet:
    allowPrivileged: true
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    hostnameOverride: '@aws'
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    networkPluginMTU: 9001
    networkPluginName: kubenet
    nonMasqueradeCIDR: 100.64.0.0/10
    podInfraContainerImage: gcr.io/google_containers/pause-amd64:3.0
    podManifestPath: /etc/kubernetes/manifests
    requireKubeconfig: true
  kubernetesApiAccess:
  - 0.0.0.0/0
  kubernetesVersion: 1.7.2
  masterInternalName: api.internal.epicass.k8s.local
  masterKubelet:
    allowPrivileged: true
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    hostnameOverride: '@aws'
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    networkPluginMTU: 9001
    networkPluginName: kubenet
    nonMasqueradeCIDR: 100.64.0.0/10
    podInfraContainerImage: gcr.io/google_containers/pause-amd64:3.0
    podManifestPath: /etc/kubernetes/manifests
    registerSchedulable: false
    requireKubeconfig: true
  masterPublicName: api.epicass.k8s.local
  networkCIDR: 172.20.0.0/16
  networking:
    kubenet: {}
  nonMasqueradeCIDR: 100.64.0.0/10
  secretStore: s3://whisky-cass-state-store/epicass.k8s.local/secrets
  serviceClusterIPRange: 100.64.0.0/13
  sshAccess:
  - 0.0.0.0/0
  subnets:
  - cidr: 172.20.32.0/19
    name: eu-west-1b
    type: Public
    zone: eu-west-1b
  topology:
    dns:
      type: Public
    masters: public
    nodes: public
