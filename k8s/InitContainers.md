# Init Containers

A helpful guys that run before the start of the container itself.

I will download an image as an example, but there can be literally any job.

## Implementation

I will work only with [`statefulset.yaml`](make-your-time/templates/statefulset.yaml).

Add the following text to `spec.template.spec.containers.initContainers` path:

```yaml
initContainers:
  - name: ohh-yeah
    image: busybox:1.28
    command:
    - wget
    - "-O"
    - "/app/ohh_yeah/ohh_yeah.png"
    - "https://steamcommunity-a.akamaihd.net/economy/emoticon/:ohh_yeah:"
    volumeMounts:
      - name: ohh-yeah
        mountPath: "/app/ohh_yeah/"
```

This will create an Init Container from `busybox` image.
The container will download an image by the URL and put it to `/app/ohh_yeah/ohh_yeah.png`.

Init container also mounts a volume, so go add one at `spec.template.spec.containers.volumes`:

```yaml
volumes:
  - name: ohh-yeah  # <-- here.
    emptyDir: {}
```

Then, to test if it works, mount that volume to real container together with other volumes if you need.
Add the following to `spec.template.spec.containers.volumeMounts`:

```yaml
volumeMounts:
  - name: ohh-yeah
    mountPath: /app/ohh_yeah/
```

## Test if it works

Now just `helm install` your chart.
First time it might get stuck at Initialization stage because it probably needs to download the `busybox` image.
Next lunch runs should be faster though.

Now to see if it works, execute the following command:

```bash
kubectl exec pod/make-your-time-0 -- ls /app/ohh_yeah
```

The output is as follows:

```txt
Defaulted container "make-your-time" out of: make-your-time, ohh-yeah (init)
ohh_yeah.png
```
