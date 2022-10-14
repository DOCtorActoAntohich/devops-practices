# Metrics

I was forced to use Prometheus to obtain some metrics for my app. ![](https://steamcommunity-a.akamaihd.net/economy/emoticon/:ohh_yeah:)

## Scraping

In [Prometheus Config](./config/prometheus.yaml) there are jobs to collect metrics from all services.
It is done by going to `/metrics/` path in web on each service. That's what Prometheus will do for me, instead of me.

### Python App

I honestly had no idea which metrics I could add (and how), so I used this funny Python library called [Prometheus FastAPI Instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator).

Going to `http://127.0.0.1:8080/metrics` shows this (not full output because it's too long and useless):

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

### Result

Prometheus collects all metrics and shows everything is okay.

![metrics](https://user-images.githubusercontent.com/49134679/195829047-ba08bbe3-89e4-4918-9422-f0636d5b9b14.png)

## Grafana

Using some funny Grafana [provisioning configs](./config/grafana/), you can automagically add datasources and dashboards to it on startup.

![datasources](https://user-images.githubusercontent.com/49134679/195840954-9415d186-ac92-474b-8334-4010d52eb669.png)

![dashboards](https://user-images.githubusercontent.com/49134679/195841018-a8e59a3a-85b0-4548-ad5e-a97491966fe2.png)

Below there are dashboards that I used. They look pretty cool but I don't understand anything ![](https://steamcommunity-a.akamaihd.net/economy/emoticon/:ohh_yeah:)

I imported them by IDs [13407](https://grafana.com/grafana/dashboards/13407-loki2-0-global-metrics/) and [3662](https://grafana.com/grafana/dashboards/3662-prometheus-2-0-overview/), then exported as JSONs which I load back on startup. It's cool that JSONs will keep the structure of dashboard if I change something.

![loki](https://user-images.githubusercontent.com/49134679/195841107-5693dfe5-3ee7-4b62-83a8-bed4fb000629.png)

![prometheus](https://user-images.githubusercontent.com/49134679/195841121-1b61aa30-ae10-4688-a1e6-8f51a7495d05.png)
