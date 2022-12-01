# Transitioning from `Deployment` to `StatefulSet`

`StatefulSet` allows deploying stateful applications.

## Transition

1. Rename `template/deployment.yaml` to [`statefulset.yaml`](make-your-time/templates/statefulset.yaml).
2. Replace `kind: Deployment` with `kind: StatefulSet`

Unironically, running `helm install --dry-run --debug make-your-time make-your-time/` resulted in no errors.

Check if it's running using ``:

```txt
NAME                   READY   STATUS    RESTARTS   AGE
pod/make-your-time-0   1/1     Running   0          9h17m
pod/make-your-time-1   1/1     Running   0          9h17m
pod/make-your-time-2   1/1     Running   0          9h17m

NAME                              READY   AGE
statefulset.apps/make-your-time   3/3     9h17m

NAME                     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP          10h35m
service/make-your-time   NodePort    10.106.254.191   <none>        8080:32208/TCP   9h17m
```

## Epic testing

The app writes to file each time a user requests time in any time zone.
Statistics can be found in `/visits` endpoint.

`minukube service make-your-time` opened my app in browser where I could see stats.

> Due to stupid design, I do health checks by accessing app's root (`httpain://<ip:port>/`), so it adds extra visits
> That's why I disabled probes.

I accessed the root endpoint 20 times by slowly spamming F5.
Then I tried to catch different visits by opening `http://<ip:port>/visits` in different tabs.
Since there are 3 replicas, I expect different numbers of visits, ideally close-to-equal.
However, no matter the results, the total amount of visits shall remain 20.

Let's check them. Instead of visiting `/visits`, it's easier to access each pod's filesystem by executing this:

```bash
kubectl exec pod/make-your-time-X -- cat /app/data/visits.txt
```

Nota that X is the number of pod from 0 to 2 (3 replicas total).

Outputs format: first line is total number of visits, second line is last access time.

Pod 0:

```
<Еггог: No such file or directory>
```

Pod 1:

```
14
2022-11-23 19:57:20.299569
```

Pod 2:

```
6
2022-11-23 19:57:24.418718
```

Total number of visits is 20, which is correct.
The 0th pod doesn't have that file because apparently it was never accessed.

The `visits` file is local to each pod.
Also, `kubernetes` should have smart scheduling, so not always the same pod will respond to user requests.
Thus, each local file will have different numbers.
I expected results to be more equal, however on the larger scale that difference will be negligible.

## Ordering and Parallel creation

Kubernetes also guarantees ordering, but this is not necessary for such a small application.
Simply no need for it in a simple get-only app.
Might be useful on a larger scale, but here it's just one poor laptop, and no possible race conditions.

For me it doesn't take much time to create a pod.
However, three quick subsequent `kubectl get po` calls show that pods are created sequentally:

First call:

```
NAME                   READY   STATUS              RESTARTS   AGE
pod/make-your-time-0   0/1     ContainerCreating   0          1s
```

Second call:

```
NAME                   READY   STATUS              RESTARTS   AGE
pod/make-your-time-0   1/1     Running             0          2s
pod/make-your-time-1   0/1     ContainerCreating   0          1s
```

Third call:

```
NAME                   READY   STATUS              RESTARTS   AGE
pod/make-your-time-0   1/1     Running             0          3s
pod/make-your-time-1   1/1     Running             0          2s
pod/make-your-time-2   0/1     ContainerCreating   0          1s
```

This is because there is ordered pod management policy.
Let us then switch to Parallel policy.
Add this line to `spec.podManagementPolicy` path in [`statefulset.yaml`](make-your-time/templates/statefulset.yaml):

```yaml
podManagementPolicy: "Parallel"
```

With this, pods will start up simultaneously.
It doesn't mean they'll finish it at the same time (because of processor scheduling).
At least they should appear in the list together.
Check it with `kubectl get po` again:

```
NAME                   READY   STATUS              RESTARTS   AGE
pod/make-your-time-0   0/1     ContainerCreating   0          1s
pod/make-your-time-1   0/1     ContainerCreating   0          1s
pod/make-your-time-2   0/1     ContainerCreating   0          1s
```
