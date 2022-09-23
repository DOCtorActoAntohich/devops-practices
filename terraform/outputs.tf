output "image" {
  description = "Docker Image Name"
  value       = docker_image.make_your_time.name
}

output "container_id" {
  description = "Docker Container ID"
  value       = docker_container.make_your_time.id
}

output "container_name" {
  description = "Docker Container ID"
  value       = docker_container.make_your_time.name
}

output "ports" {
  description = "Docker Container mapped ports (external:internal)"
  value       = [for port in docker_container.make_your_time.ports : "${port.external}:${port.internal}"]
}
