# Managing Secrets

> `minikube` should be running.

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
