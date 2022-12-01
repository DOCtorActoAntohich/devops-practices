# Init Containers

## Kube Prometheus Stack

### Components

- Prometheus Operator - automates prometheus setup.
- Prometheus - a dude that pulls metrics from `/metrics`.
- Alertmanager - simply handles alerts sent by others and organizes them.
- Prometheus Node Exporter - exports metrics of the node (Linux kernel).
- Prometheus Adapter for Kubernetes Metrics API - collects kubernetes metrics.
- `kube-state-metrics` - preduces metrics for each running object in kubernetes.
- Grafana - a thing with fancy dashboards and graphs.

### Add GitHub repository

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

### Install

I will name it `fnnuy-stats`:

```bash
helm install fnnuy-stats prometheus-community/kube-prometheus-stack
```

I also installed my app using `make helm_install`.

### Check

Executing `kubectl get po,sts,svc,pvc,cm` yields lots of text that I split into blocks.
Basically this epic command shows status of many things, such as:

- Deployments:

```txt
NAME                                                         READY   STATUS    RESTARTS        AGE
pod/alertmanager-fnnuy-stats-kube-prometheu-alertmanager-0   2/2     Running   1 (3m36s ago)   3m54s
pod/fnnuy-stats-grafana-757d8b6549-92mqp                     3/3     Running   0               4m8s
pod/fnnuy-stats-kube-prometheu-operator-74ff8b675f-4k9j7     1/1     Running   0               4m8s
pod/fnnuy-stats-kube-state-metrics-567dbf8d54-9lqd6          1/1     Running   0               4m8s
pod/fnnuy-stats-prometheus-node-exporter-zdwg6               1/1     Running   0               4m8s
pod/make-your-time-0                                         1/1     Running   0               3m37s
pod/make-your-time-1                                         1/1     Running   0               3m37s
pod/make-your-time-2                                         1/1     Running   0               3m37s
pod/prometheus-fnnuy-stats-kube-prometheu-prometheus-0       2/2     Running   0               3m54s
```

- Stateful sets:

```txt
NAME                                                                    READY   AGE
statefulset.apps/alertmanager-fnnuy-stats-kube-prometheu-alertmanager   1/1     3m54s
statefulset.apps/make-your-time                                         3/3     3m37s
statefulset.apps/prometheus-fnnuy-stats-kube-prometheu-prometheus       1/1     3m54s
```

- Services:

```txt
NAME                                              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
service/alertmanager-operated                     ClusterIP   None             <none>        9093/TCP,9094/TCP,9094/UDP   3m54s
service/fnnuy-stats-grafana                       ClusterIP   10.97.33.203     <none>        80/TCP                       4m8s
service/fnnuy-stats-kube-prometheu-alertmanager   ClusterIP   10.108.204.179   <none>        9093/TCP                     4m8s
service/fnnuy-stats-kube-prometheu-operator       ClusterIP   10.107.92.118    <none>        443/TCP                      4m8s
service/fnnuy-stats-kube-prometheu-prometheus     ClusterIP   10.105.229.7     <none>        9090/TCP                     4m8s
service/fnnuy-stats-kube-state-metrics            ClusterIP   10.101.7.82      <none>        8080/TCP                     4m8s
service/fnnuy-stats-prometheus-node-exporter      ClusterIP   10.105.172.227   <none>        9100/TCP                     4m8s
service/kubernetes                                ClusterIP   10.96.0.1        <none>        443/TCP                      4m43s
service/make-your-time                            NodePort    10.100.78.96     <none>        8080:30734/TCP               3m37s
service/prometheus-operated                       ClusterIP   None             <none>        9090/TCP                     3m54s
```

- Persistent volumes (got none)

- Configmaps:

```txt
NAME                                                                     DATA   AGE
configmap/fnnuy-stats-grafana                                            1      4m8s
configmap/fnnuy-stats-grafana-config-dashboards                          1      4m8s
configmap/fnnuy-stats-kube-prometheu-alertmanager-overview               1      4m8s
configmap/fnnuy-stats-kube-prometheu-apiserver                           1      4m8s
configmap/fnnuy-stats-kube-prometheu-cluster-total                       1      4m8s
configmap/fnnuy-stats-kube-prometheu-controller-manager                  1      4m8s
configmap/fnnuy-stats-kube-prometheu-etcd                                1      4m8s
configmap/fnnuy-stats-kube-prometheu-grafana-datasource                  1      4m8s
configmap/fnnuy-stats-kube-prometheu-grafana-overview                    1      4m8s
configmap/fnnuy-stats-kube-prometheu-k8s-coredns                         1      4m8s
configmap/fnnuy-stats-kube-prometheu-k8s-resources-cluster               1      4m8s
configmap/fnnuy-stats-kube-prometheu-k8s-resources-namespace             1      4m8s
configmap/fnnuy-stats-kube-prometheu-k8s-resources-node                  1      4m8s
configmap/fnnuy-stats-kube-prometheu-k8s-resources-pod                   1      4m8s
configmap/fnnuy-stats-kube-prometheu-k8s-resources-workload              1      4m8s
configmap/fnnuy-stats-kube-prometheu-k8s-resources-workloads-namespace   1      4m8s
configmap/fnnuy-stats-kube-prometheu-kubelet                             1      4m8s
configmap/fnnuy-stats-kube-prometheu-namespace-by-pod                    1      4m8s
configmap/fnnuy-stats-kube-prometheu-namespace-by-workload               1      4m8s
configmap/fnnuy-stats-kube-prometheu-node-cluster-rsrc-use               1      4m8s
configmap/fnnuy-stats-kube-prometheu-node-rsrc-use                       1      4m8s
configmap/fnnuy-stats-kube-prometheu-nodes                               1      4m8s
configmap/fnnuy-stats-kube-prometheu-nodes-darwin                        1      4m8s
configmap/fnnuy-stats-kube-prometheu-persistentvolumesusage              1      4m8s
configmap/fnnuy-stats-kube-prometheu-pod-total                           1      4m8s
configmap/fnnuy-stats-kube-prometheu-prometheus                          1      4m8s
configmap/fnnuy-stats-kube-prometheu-proxy                               1      4m8s
configmap/fnnuy-stats-kube-prometheu-scheduler                           1      4m8s
configmap/fnnuy-stats-kube-prometheu-workload-total                      1      4m8s
configmap/kube-root-ca.crt                                               1      4m29s
configmap/make-your-time-configpain                                      1      3m37s
configmap/prometheus-fnnuy-stats-kube-prometheu-prometheus-rulefiles-0   29     3m54s
```

### Opening Grafana

> Everyone who made `kube-prometheus-stack` must burn in hell for having 0.001% useful documentation - everything besides _How to install_ section is utterly useless.

Minikube was crying in despair because Grafana had "no node port" :tm:.
Googling shows no real solutions except this one:

![gods](https://user-images.githubusercontent.com/49134679/205097550-7db4aa0d-647f-4772-8441-9e935952484d.png)

Doesn't give much hope? Same. But it just works even though it's cursed, so I'll thank [these Chinese dudes](https://www.cnblogs.com/shanghai1918/p/16328628.html) for solving the problem... Which could be avoided if these tools didn't suck.

Run `KUBE_EDITOR="nano" kubectl edit svc fnnuy-stats-grafana` and change `type: ClusterIP` to `type: NodePort`. Using `nano` because it's the only linux editor that _works_.

Now wait for a couple of minutes till this skunk applies changes and does some cursed magic, and only then `minikube service fnnuy-stats-grafana` will _finally_ open that goddamn browser.

### Logging in

Now another challenge - sign in into Grafana.

If you're wondering, credentials aren't `admin:admin` because Grafana is cancer.

You can see default settings by running `helm show values prometheus-community/kube-prometheus-stack`.
Be ready because it will print lots of trash, AMONG which you'll find the following Yaml thing (I omittted unnecessary lines):

```yaml
grafana:
  adminPassword: prom-operator
```

You can of course save a new `values.yaml` and go like `helm install -f grafanus-values.yaml prometheus-community/kube-prometheus-stack` if you want but I bet it'll break something and I don't even want to try.

So I just used `admin:prom-operator` as credentials.

### Checking stats

In existing dashboards you can see different stats.

- Memory and CPU usage on the whole node in `Kubernetes / Compute Resources / Node (Pods)`:

![](https://user-images.githubusercontent.com/49134679/205106524-7942648b-e8bc-412d-9d98-51b7767407f7.png)

- Total resource usage by cluster in `Kubernetes / Compute Resources / Cluster`:

![](https://user-images.githubusercontent.com/49134679/205104435-f96ead4e-3a7d-4be8-8599-983c7ab3b250.png)

- StatefulSet Memory and CPU consumption in `Kubernetes / Compute Resources / Namespace (Workloads)`:

![](https://user-images.githubusercontent.com/49134679/205105010-d280fbbb-41c5-485d-9493-c62d27b78eae.png)

- CPU and Memory usage of each pod in `Kubernetes / Compute Resources / Pod`:

![](https://user-images.githubusercontent.com/49134679/205107208-6d642d46-541b-4dab-98ea-dbc720d1bf89.png)

- Alerts in `Alert Manager / Overview`:

![](https://user-images.githubusercontent.com/49134679/205103446-19647c90-97b1-4513-a73c-7beb9c887236.png)

- Kubelet stats in `Kubernetes / Kubelet`:

![](https://user-images.githubusercontent.com/49134679/205107516-5f5f418b-34d0-46bd-a73f-25690ab6fe39.png)
