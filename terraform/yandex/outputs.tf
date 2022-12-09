output "machine_user" {
  value = var.machine_user
}

output "machine_name" {
  value = yandex_compute_instance.machine.name
}

output "machine_ipv4" {
  value = yandex_compute_instance.machine.network_interface.0.nat_ip_address
}
