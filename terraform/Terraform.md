# Terraform

Doing it for a project that small is cursed.

## Docker

~~Kind of same as `Docker Compose` but more annoying.~~

### `terraform show` yields

```txt
# docker_container.make_your_time:
resource "docker_container" "make_your_time" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/bin/sh",
        "-c",
        "gunicorn -k uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 app_python.main:app",
    ]
    env                                         = []
    gateway                                     = "172.17.0.1"
    hostname                                    = "e21b503a7e57"
    id                                          = "e21b503a7e5725006af7708733beb7b49826560652433a3fc8c8c20d62425e83"
    image                                       = "sha256:d488f735284f0d1bc50dec15dc23d66d8b3889c294bdd065351aa633569c2a58"
    init                                        = false
    ip_address                                  = "172.17.0.2"
    ip_prefix_length                            = 16
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "make_your_time"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            network_name              = "bridge"
        },
    ]
    network_mode                                = "default"
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "floppa"
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.make_your_time:
resource "docker_image" "make_your_time" {
    id           = "sha256:d488f735284f0d1bc50dec15dc23d66d8b3889c294bdd065351aa633569c2a58doctoractoantohich/make_your_time:latest"
    image_id     = "sha256:d488f735284f0d1bc50dec15dc23d66d8b3889c294bdd065351aa633569c2a58"
    keep_locally = false
    latest       = "sha256:d488f735284f0d1bc50dec15dc23d66d8b3889c294bdd065351aa633569c2a58"
    name         = "doctoractoantohich/make_your_time:latest"
    repo_digest  = "doctoractoantohich/make_your_time@sha256:c9f1fad29fb315d661767530e485056b34b41a514e1c32bc1311307170de8f36"
}


Outputs:

container_id = "e21b503a7e5725006af7708733beb7b49826560652433a3fc8c8c20d62425e83"
container_name = "make_your_time"
image = "doctoractoantohich/make_your_time:latest"
ports = [
    "8000:8000",
]
```

### `terraform state list` yields

```txt
docker_container.make_your_time
docker_image.make_your_time
```

### `terraform output` yields

```txt
container_id = "e21b503a7e5725006af7708733beb7b49826560652433a3fc8c8c20d62425e83"
container_name = "make_your_time"
image = "doctoractoantohich/make_your_time:latest"
ports = [
  "8000:8000",
]
```
