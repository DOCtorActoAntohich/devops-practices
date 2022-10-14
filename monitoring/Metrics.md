# Metrics

I was forced to use Prometheus to obtain some metrics for my app. ![](https://steamcommunity-a.akamaihd.net/economy/emoticon/:ohh_yeah:)

## Loki

First, I added a job to obtain metrics from Loki (and from Prometheus itself).

On `http://127.0.0.1:9090/targets` there are these jobs:

![loki](https://user-images.githubusercontent.com/49134679/195821249-e3effe62-c7bd-4145-bf1a-492ad95012b4.png)

## Python App

I honestly have no idea which metrics I could add (and how).

So I used this funny Python library called [Prometheus FastAPI Instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator).

Goint to `http://127.0.0.1:8080/metrics` shows this (not full output because it's too long and useless):

```txt
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 1057.0
python_gc_objects_collected_total{generation="1"} 495.0
python_gc_objects_collected_total{generation="2"} 134.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 127.0
python_gc_collections_total{generation="1"} 11.0
python_gc_collections_total{generation="2"} 1.0
```
