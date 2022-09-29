yandex_vms:
  hosts:
    ${ machine_name }:
      ansible_user: ${ machine_user }
      ansible_ssh_private_key_file: files/ssh/id_ed25519
      ansible_host: ${ machine_ipv4 }
