# Kubernetes

pain.

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
