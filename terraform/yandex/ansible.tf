resource "local_file" "ansible_inventory" {
  content = templatefile("${var.ansible_inventory_templates_dir}/yandex.tpl",
    {
      machine_name = yandex_compute_instance.machine.name,
      machine_user = var.machine_user,
      machine_ipv4 = yandex_compute_instance.machine.network_interface.0.nat_ip_address
    }
  )
  filename = "${var.ansible_dynamic_inventory_out_dir}/yandex.yaml"
}
