# Logging

It is done with the power of Grafana, Promtail, and Loki.

## How it works

1. In `docker-compose-pull.yaml` you can see configurations for containers.
2. One of the things is `x-logging` that I basically copy-paste to every container's logging system. It adds contaner name as tag.
3. I expose the list of running docker containers to `promtail` using `volumes`
4. Loki is a web server so it has some ports exposed too.
5. In `monitoring/promtail.yaml` there are settings for promtail that are sent to containers using volumes too.
6. In the config, I told `promtail` to read tags from containers attributes and parse logs as JSONs. Here it also adds labels.

Finally, after all this pain, `promtail` sends everything to `loki` where you can see it "in more organized way" (it's actually messed up but you can solve it by parsing JSONSs in special way ~~which I didn't~~).

## Results
