# Ansible

## Used materials

I DID NOT USE ANSIBLE DOCS BECAUSE THEY SUCK.

- [Docker role](https://medium.com/@knoldus/how-to-install-docker-on-rhel-using-ansible-role-62728c098351)
- [apt install](https://stackoverflow.com/questions/54944080/installing-multiple-packages-in-ansible) and [apt remove](https://stackoverflow.com/questions/29914253/remove-package-ansible-playbook)
- [Docker repo in apt](https://gist.github.com/rbq/886587980894e98b23d0eee2a1d84933)
- [Config example](https://gist.github.com/wbcurry/f38bc6d8d1ee4a70ee2c)

## Commands

### `ansible-playbook -i inventory/yandex.yaml playbooks/main.yaml --diff`

```txt
PLAY [Install Docker] **************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [red]

TASK [docker : include_tasks] ******************************************************************************************
included: */dev-ops-labs/ansible/roles/docker/tasks/docker_group.yaml for red

TASK [docker : Create Docker group] ************************************************************************************
changed: [red]

TASK [docker : Add users to Docker group] ******************************************************************************
changed: [red] => (item=floppa)

TASK [docker : include_tasks] ******************************************************************************************
included: */dev-ops-labs/ansible/roles/docker/tasks/install_docker.yaml for red

TASK [docker : D E S T R O Y old versions of Docker] *******************************************************************
ok: [red]

TASK [docker : Update requirements] ************************************************************************************
ok: [red]

TASK [docker : Add GPG key for Docker repo] ****************************************************************************
changed: [red]

TASK [docker : Add Docker APT repository] ******************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable

changed: [red]

TASK [docker : Install Docker] *****************************************************************************************
The following additional packages will be installed:
  containerd.io docker-ce-cli docker-ce-rootless-extras docker-scan-plugin git
  git-man libcurl3-gnutls liberror-perl libgdbm-compat4 libperl5.30 patch perl
  perl-modules-5.30 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite git-daemon-run | git-daemon-sysvinit
  git-doc git-el git-email git-gui gitk gitweb git-cvs git-mediawiki git-svn
  diffutils-doc perl-doc libterm-readline-gnu-perl
  | libterm-readline-perl-perl make libb-debug-perl liblocale-codes-perl
The following NEW packages will be installed:
  containerd.io docker-ce docker-ce-cli docker-ce-rootless-extras
  docker-scan-plugin git git-man libcurl3-gnutls liberror-perl libgdbm-compat4
  libperl5.30 patch perl perl-modules-5.30 pigz slirp4netns
0 upgraded, 16 newly installed, 0 to remove and 36 not upgraded.
changed: [red] => (item=docker-ce)
ok: [red] => (item=containerd.io)

TASK [docker : Start Docker service] ***********************************************************************************
ok: [red]

PLAY RECAP *************************************************************************************************************
red                        : ok=11   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### `ansible-inventory -i inventory/yandex.yaml --list`

```json
{
    "_meta": {
        "hostvars": {
            "red": {
                "ansible_host": "127.0.0.2",
                "ansible_ssh_private_key_file": "files/ssh/id_ed25519",
                "ansible_user": "floppa"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yandex_vms"
        ]
    },
    "yandex_vms": {
        "hosts": [
            "red"
        ]
    }
}
```
