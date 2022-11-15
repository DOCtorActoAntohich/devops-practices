# Kubernetes

This file can help you deploy the app locally using `minikube` and `kubectl` (install them).

## Manual management

Stuff is done locally in `minikube` so before the start:

`minikube start`

### Deployment

Create deployment by running:

```bash
kubectl create deployment mongus --image=doctoractoantohich/make_your_time:latest
```

### Service

To expose the container, create a service:

```bash
kubectl expose deployment mongus --type=LoadBalancer --port=8000
```

### Finishing up

Run `minikube tunnel` and `minikube service mongus`, probably in different termilans.
That should run and expose the container

The first command repeatedly prints this heresy every couple of seconds:

```
Status:
        machine: minikube
        pid: 66666
        route: 10.96.0.0/12 -> 192.168.49.2
        minikube: Running
        services: [mongus]
    errors:
                minikube: no errors
                router: no errors
                loadbalancer emulator: no errors

```

The second command prints this:

```txt
|-----------|--------|-------------|---------------------------|
| NAMESPACE |  NAME  | TARGET PORT |            URL            |
|-----------|--------|-------------|---------------------------|
| default   | mongus |        8000 | http://192.168.49.2:32241 |
|-----------|--------|-------------|---------------------------|
```

Finally, as a proof that this monstrosity works:

![image](https://user-images.githubusercontent.com/49134679/197895424-b2b02772-8b68-4afa-bf7f-9e27d82b4ad0.png)

### Outputs

`kubectl get deployments` yields:

```txt
NAME     READY   UP-TO-DATE   AVAILABLE   AGE
mongus   1/1     1            1           0s
```

`kubectl get pod,svc` yields:

```txt
NAME                          READY   STATUS    RESTARTS   AGE
pod/mongus-599fb5f495-v7vnx   1/1     Running   0          0s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1       <none>          443/TCP          16y
service/mongus       LoadBalancer   10.104.64.115   10.104.64.115   8000:32241/TCP   0s
```

### Cleaning up

Delete service and deployment:

```bash
kubectl delete service mongus
kubectl delete deployment mongus
```

Then destroy `minikube`

```bash
minikube tunnel --cleanup
minikube stop
```

Maybe you might want to `minikube delete` instead of `stop`.

## Using config files, a.k.a. YAML programming

Instead of manually entering commands to setup services each time, you can manually enter commands to read service configs from files.

## Setting up

From this directory, the commands are:

```bash
kubectl apply -f ./config/deployment.yaml
kubectl apply -f ./config/service.yaml
```

`kubectl get pods,svc` yields:

```txt
NAME                                  READY   STATUS    RESTARTS   AGE
pod/make-your-time-796d54b48d-5zl4l   1/1     Running   0          0s
pod/make-your-time-796d54b48d-77p8p   1/1     Running   0          0s
pod/make-your-time-796d54b48d-bpd6v   1/1     Running   0          0s

NAME                     TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes       ClusterIP      10.96.0.1      <none>        443/TCP          1.7sg
service/make-your-time   LoadBalancer   10.102.190.4   <pending>     8080:31337/TCP   0s
```

To launch everything execute `minikube service --all`.
I replaced silly emotes with text analogs just in case but tables remain the same:

```txt
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
:sadboi:  service default/kubernetes has no node port
|-----------|----------------|-------------|---------------------------|
| NAMESPACE |      NAME      | TARGET PORT |            URL            |
|-----------|----------------|-------------|---------------------------|
| default   | make-your-time | http/8080   | http://192.168.49.2:31337 |
|-----------|----------------|-------------|---------------------------|
:happyboi:  Opening service default/make-your-time in default browser...
```

Gladly, this funny thing works too:

![image](https://user-images.githubusercontent.com/49134679/197900125-c19ae32a-275a-48ec-8db1-2bcdb51b249b.png)

## Cleaning up

Similarly to manual work, here are the commands:

```bash
kubectl delete -f ./config/service.yaml
kubectl delete -f ./config/deployment.yaml
```

Then kill `minikube` if you want (I know you *really* want).

## Automating the automation with `helm`

Instead of manually entering commands to read service configs from files, you can manually enter commands to add the whole pod configuratuion.

For this luxury, install `helm` for `kubernetes` (careful here).

![helm](https://user-images.githubusercontent.com/49134679/199402117-12bf2c22-ce34-496b-8ed2-edf91028dbea.png)

### `helm` chart, a.k.a. package

I created a template using `helm create make-your-time`. In this template, I edited the following section in `values.yaml`:

```yaml
image:
  repository: doctoractoantohich/make_your_time
  pullPolicy: IfNotPresent
  tag: "latest"

service:
  type: NodePort
  container_port: 8000
  out_port: 8080
```

A couple more edits in `deployents.yaml`:

```yaml
ports:
  - name: http
    containerPort: {{ .Values.service.container_port }}
    protocol: TCP
```

And in `service.yaml`:

```yaml
ports:
  - port: {{ .Values.service.out_port }}
    targetPort: {{ .Values.service.container_port }}
    protocol: TCP
    name: http
```

Used `helm lint make-your-time` just in case.

Then I made a local package using `helm package make-your-time`.
That command creates an archive, which you can install using `helm install make-your-time make-your-time-0.1.0.tgz`.
The first parameter is a name for the local instance.
The second parameter is the created archive.
Note that version might be different.

Successful installation means the app is up and running.

`minikube service make-your-time` shows:

```txt
|-----------|----------------|-------------|---------------------------|
| NAMESPACE |      NAME      | TARGET PORT |            URL            |
|-----------|----------------|-------------|---------------------------|
| default   | make-your-time | http/8080   | http://192.168.49.2:32257 |
|-----------|----------------|-------------|---------------------------|
```

`kubectl get pods,svc` shows:

```txt
NAME                                  READY   STATUS    RESTARTS   AGE
pod/make-your-time-5f69cb9b97-m5vxn   1/1     Running   0          2m28s

NAME                     TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes       ClusterIP   10.96.0.1      <none>        443/TCP          16y
service/make-your-time   NodePort    10.97.52.109   <none>        8080:32257/TCP   2m28s
```

Indeed, it works:

![curl](https://user-images.githubusercontent.com/49134679/199409258-bdd85eb8-97e8-46f9-9213-3819e2b4d137.png)

There's also this cool green thing in `minikube dashboard`:

![green_thing](https://user-images.githubusercontent.com/49134679/199411582-c469d66e-9f44-4183-9a68-fb189d7c7826.png)

![dashboard](https://user-images.githubusercontent.com/49134679/199409316-2b5cfd18-e75d-4f91-a19a-5c5911c3d39c.png)

### Health checks

I edited these sections in `deployment.yaml`:

```yaml
livenessProbe:
  httpGet:
    path: /
    port: {{ .Values.service.container_port }}
  initialDelaySeconds: 10
  periodSeconds: 10
readinessProbe:
  httpGet:
    path: /
    port: {{ .Values.service.container_port }}
  initialDelaySeconds: 10
  periodSeconds: 10
```

Now there will be warnings if the container is not very alive.

However, in my case, `kubectl describe pod make-your-time` shows these lines:

```txt
Liveness:       http-get http://:8000/ delay=10s timeout=1s period=10s #success=1 #failure=3
Readiness:      http-get http://:8000/ delay=10s timeout=1s period=10s #success=1 #failure=3
```

And these lines in the end:

```txt
Events:
Type    Reason     Age   From               Message
----    ------     ----  ----               -------
Normal  Scheduled  31s   default-scheduler  Successfully assigned default/make-your-time-6557954df7-rqtxt to minikube
Normal  Pulled     30s   kubelet            Container image "doctoractoantohich/make_your_time:latest" already present on machine
Normal  Created    30s   kubelet            Created container make-your-time
Normal  Started    30s   kubelet            Started container make-your-time
```

In process of setting up, I noticed something like this in `kubectl get events`:

```txt
LAST SEEN   TYPE      REASON              OBJECT                                 MESSAGE
42m17s      Warning   Unhealthy           pod/make-your-time-dbc67b65d-zpb44     Readiness probe failed: Get "http://172.17.0.6:8000/": dial tcp 172.17.0.6:8000: connect: connection refused
```

It was caused by wrong settings, or wrong port, or for some other reason.
When I supplied it with the correct port, it stopped pestering me.

If the container had issues, it would spam me with such messages everywhere. However, everything was okay for me, which is very cool and epic.

### Clean up

Deleting via `helm` is done using `helm uninstall make-your-time`.

The rest is just `minikube` which you already know how to annihilate.

## Extras

### CPU/Memory limits

You can setup memory and cpu requests (what it should take) and limits (can't take more than that) for containers.

Refer to [`deployment.yaml`](make-your-time/templates/deployment.yaml) and [`values.yaml`](make-your-time/values.yaml) for examples.

After applying these values and reloading, `kubectl describe pod <>` prints these lines (many other lines were omitted):

```txt
Ready:          True
Restart Count:  0
Limits:
  cpu:          500m
  memory:       512Mi
Requests:
  cpu:          250m
  memory:       128Mi
```
