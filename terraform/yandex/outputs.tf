output "name" {
  value = yandex_compute_instance.machine.name
}

output "address" {
  value = yandex_compute_instance.machine.network_interface.0.nat_ip_address
}
