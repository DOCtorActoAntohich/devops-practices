# Metrics

I was forced to use Prometheus to obtain some metrics for my app. ![](https://steamcommunity-a.akamaihd.net/economy/emoticon/:ohh_yeah:)

## Loki

First, I added a job to obtain metrics from Loki (and from Prometheus itself).

On `http://127.0.0.1:9090/targets` there are these jobs:

![loki](https://user-images.githubusercontent.com/49134679/195821249-e3effe62-c7bd-4145-bf1a-492ad95012b4.png)
