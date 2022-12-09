# Logging

It is done with the power of Grafana, Promtail, and Loki.

If you need to run and test it yourself (locally), in the root folder run `make monitoring_compose_up` or `make monitoring_compose_down` to enable or disable the system respectively.

## How it works

1. In `docker-compose-pull.yaml` you can see configurations for containers.
2. One of the things is `x-logging` that I basically copy-paste to every container's logging system. It adds contaner name as tag.
3. I expose the list of running docker containers to `promtail` using `volumes`
4. Loki is a web server so it has some ports exposed too.
5. In `monitoring/promtail.yaml` there are settings for promtail that are sent to containers using volumes too.
6. In the config, I told `promtail` to read tags from containers attributes and parse logs as JSONs. Here it also adds labels.

Finally, after all this pain, `promtail` sends everything to `loki` where you can see it "in more organized way" (it's actually messed up but you can solve it by parsing JSONSs in special way ~~which I didn't~~).

## Results

To see these results, I had to connect to `http://127.0.0.1:3100` which is Grafana's server. Here I added the data source as follows:

![data source](https://user-images.githubusercontent.com/49134679/195428803-35318460-895e-4647-b564-05511f8c5446.png)

The host name is `loki` because that's how I named the container, and both Grafana and Loki are in the same network.

Then I went to the Explore tab and added a query as follows (must be for Loki):

![explore](https://user-images.githubusercontent.com/49134679/195429094-f00dfdf2-eeba-4a49-a2a0-58fd641b07f6.png)

After refreshing, it showed me whatever this is:

![whatever this is](https://user-images.githubusercontent.com/49134679/195429420-efdb3bd9-22ee-46dc-9bf2-dfa1e032b099.png)

That looks like poorly parsed JSON of `make_your_time` container logs, so this abomination basically works. These are not exactly application logs, because I haven't added any, but I could add, make them different from web server logs, and parse them somehow.
