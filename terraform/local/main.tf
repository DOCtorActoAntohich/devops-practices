terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.22.0"
    }
  }
}


provider "docker" {
  # windows bad. remove if it doesn't work on linux:
  host = "npipe:////.//pipe//docker_engine"
}


resource "docker_image" "make_your_time" {
  name         = "doctoractoantohich/make_your_time:latest"
  keep_locally = true
}


resource "docker_container" "make_your_time" {
  image = docker_image.make_your_time.latest
  name  = var.container_name
  ports {
    internal = 8000
    external = 8000
  }
}
