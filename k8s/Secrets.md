# Managing Secrets

> `minikube` should be running.

## Manually with `kubectl`

One can create secrets using `kubectl`. I will create a mock user `susso` with password `imp0stre` using command CLI:

```bash
kubectl create secret generic make-your-secret \
    --from-literal=user=susso \
    --from-literal=pass=imp0stre
```

In process of creating that, managed to mess up and create an empty secret.
You can delete it with `kubectl delete secret make-your-secret`.

But if you don't mess up, `kubectl describe secret make-your-secret` should show this:

```txt
Name:         make-your-secret
Namespace:    default
Labels:       <none>
Annotations:  <none>

Type:  Opaque

Data
====
pass:  8 bytes
user:  5 bytes
```

To see if it works, execute the following cursed command:

```bash
kubectl get secret make-your-secret -o jsonpath={.data.user} | base64 --decode && \
echo -n " " && \
kubectl get secret make-your-secret -o jsonpath={.data.pass} | base64 --decode
```

The output should be `susso imp0stre` (no `\n` though).
That means secrets kinda work although `base64` isn't super cool.

## Manually but with `helm`

> Automating the automatic automation.

### Encrypt the data

First, install some random `helm` plugin:

```bash
helm plugin install https://github.com/jkroepke/helm-secrets
```

Install `sops`, and and `gpg --gen-key` key if you didn't.

I created `mock-data.yaml` file with the following contents:

```yaml
user: susso
pass: imp0stre
```

Contents of this file will behave as if they appeared in [`make-your-time/values.yaml`](make-your-time/values.yaml) after decryption.
However, we won't add them right there because they're supposed to be _sensitive data_.

So let's encrypt them as follows:

```bash
sops --encrypt --pgp A22F38390EFECC181E97A83D5648BC556C85961C --in-place mock-data.yaml
```

I added `--in-place` because I don't care about original file.
Remove it, and the command will print the encrypted data which you can save to file using `>`.

### Helm chart configuration

Time to become yaml programmer again and add a new file [`templates/secrets.yaml`](./make-your-time/templates/secrets.yaml).

I changed the name of the secret to `make-your-secret` and added two data fields that should be "encrypted" to `base64`.
`user` and `pass` will be taken from `Values` after decryption.

Next step is to pass the sensitive data to pods.
This is done by adding a couple of lines to [`templates/deployment.yaml`](make-your-time/templates/deployment.yaml).
The following lines should go to `spec.template.spec.containers.env`:

```yaml
env:
  - name: HELM_USER
    valueFrom:
      secretKeyRef:
        name: make-your-secret
        key: user
  - name: HELM_PASS
    valueFrom:
      secretKeyRef:
        name: make-your-secret
        key: pass
```

Here it's simple - the pod will grab data keys `user` and `pass` from secret `make-your-secret` and put them into pod environment under specific names.

### Install the chart

Now it's time to install the app, this time no archives:

```bash
helm secrets install make-your-time ./make-your-time -n default -f ./mock-data.yaml
```

It'll install app named `make-your-time` (can be any name) from `./make-your-time` and decrypt `./mock-data.yaml`.

`kubectl get secret make-your-secret -o yaml` should print something like this (I omitted `metadata`):

```txt
apiVersion: v1
data:
  pass: aW1wMHN0cmU=
  user: c3Vzc28=
kind: Secret
metadata:
  ...
type: Opaque
```

Execute this messy scary command again:

```bash
kubectl get secret make-your-secret -o jsonpath={.data.user} | base64 --decode && \
echo -n " " && \
kubectl get secret make-your-secret -o jsonpath={.data.pass} | base64 --decode
```

And it'll print `susso imp0stre` once again.

### Checking pod environment.

`kubectl get pods` shows that there's a pod named `make-your-time-7c5d876cbd-l7nh6`.

Then let's execute the following command:

```bash
kubectl exec make-your-time-7c5d876cbd-l7nh6 -- printenv
```

Should print these lines (I again omitted many unrelated lines):

```txt
HOSTNAME=make-your-time-7c5d876cbd-l7nh6
HELM_USER=susso
HELM_PASS=imp0stre
MAKE_YOUR_TIME_PORT_8080_TCP_PORT=8080
```

As you see, credentials made their way to the container environment, and they are decrypted there.


## ConfigMaps

Instead of using environment variables, there's a way to use config files of any format.

You can encrypt them with `sops` and then decrypt when calling `helm secrets install ...` but I'll skip that step now.

### Volume mounts

Go inside [`deployment.yaml`](make-your-time/templates/deployment.yaml) template.
Add the following lines to the path `spec.template.spec.containers.volumeMounts`:

```yaml
volumeMounts:
  - name: mogusconf
    mountPath: /app/mogusconf.yaml
    subPath: mogusconf.yaml
```

To `spec.template.spec.volumes` add:

```yaml
volumes:
  - name: mogusconf
    configMap:
      name: make-your-time-configpain
```

Then create [`configmap.yaml`](make-your-time/templates/configmap.yaml).
This file (in my implementation) will read lines from `mogusconf.yaml`.

`mogusconf.yaml` have to reside in the package root folder because template files cannot read other templates or `.helmignore`d files.

This entire monstrousity will basically map `mogusconf.yaml` from chart root into `/app/mogusconf.yaml`, which can then be used by the app inside container.
There might be an entire directory instead of one file.

### Results

Let's see if it works. `kubectl exec <pod> -- ls` shows:

```txt
app_python
mogusconf.yaml
requirements.txt
```

It mapped successfully. Then `kubectl exec <pod> -- cat mogusconf.yaml` shows the following but with messed up newlines:

```txt
mosugconf:  imposter:    - red  susso: true  lore:    - "MANKIND IS DEAD."    - "BLOOD IS FUEL."    - "HELL IS FULL."
```
