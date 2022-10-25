# Kubernetes

pain.

## Manual management

Stuff is done locally in `minikube` so before doing stuff:

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

To make it work, gotta run `minikube tunnel` then `minikube service mongus`.
The latter command prints this:

```txt
|-----------|--------|-------------|---------------------------|
| NAMESPACE |  NAME  | TARGET PORT |            URL            |
|-----------|--------|-------------|---------------------------|
| default   | mongus |        8000 | http://192.168.49.2:32241 |
|-----------|--------|-------------|---------------------------|
```

Connecting to the link from the table (using browser) leads to the OG app. Most likely.

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
