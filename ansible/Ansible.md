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

PLAY [U p d a t i n g . . .] **********************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************
ok: [red]

TASK [system_update : Apt update/upgrade] *********************************************************************************************************
Calculating upgrade...
The following NEW packages will be installed:
  linux-headers-5.4.0-126 linux-headers-5.4.0-126-generic
  linux-image-5.4.0-126-generic linux-modules-5.4.0-126-generic
  linux-modules-extra-5.4.0-126-generic
The following packages will be upgraded:
  base-files bind9-dnsutils bind9-host bind9-libs curl intel-microcode
  language-pack-en language-pack-en-base language-pack-gnome-en
  language-pack-gnome-en-base libcurl4 libnss-systemd libpam-systemd
  libpcre2-8-0 libsqlite3-0 libsystemd0 libudev1 linux-generic
  linux-headers-generic linux-image-generic python-apt-common python3-apt
  python3-distupgrade rsync systemd systemd-sysv systemd-timesyncd tzdata
  ubuntu-advantage-tools ubuntu-release-upgrader-core udev vim vim-common
  vim-runtime vim-tiny xxd
36 upgraded, 5 newly installed, 0 to remove and 0 not upgraded.
changed: [red]

PLAY [Install Docker] *****************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************
ok: [red]

TASK [docker : include_tasks] *********************************************************************************************************************
included: */dev-ops-labs/ansible/roles/docker/tasks/docker_group.yaml for red

TASK [docker : Create Docker group] ***************************************************************************************************************
changed: [red]

TASK [docker : Add users to Docker group] *********************************************************************************************************
changed: [red] => (item=floppa)

TASK [docker : include_tasks] *********************************************************************************************************************
included: */dev-ops-labs/ansible/roles/docker/tasks/install_python.yaml for red

TASK [docker : Install Python 3.not_10] ***********************************************************************************************************
ok: [red] => (item=python3.8)
The following packages were automatically installed and are no longer required:
  linux-headers-5.4.0-42 linux-headers-5.4.0-42-generic
  linux-image-5.4.0-42-generic linux-modules-5.4.0-42-generic
  linux-modules-extra-5.4.0-42-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  binutils binutils-common binutils-x86-64-linux-gnu build-essential cpp cpp-9
  dpkg-dev fakeroot g++ g++-9 gcc gcc-9 gcc-9-base libalgorithm-diff-perl
  libalgorithm-diff-xs-perl libalgorithm-merge-perl libasan5 libatomic1
  libbinutils libc-dev-bin libc6-dev libcc1-0 libcrypt-dev libctf-nobfd0
  libctf0 libdpkg-perl libexpat1-dev libfakeroot libfile-fcntllock-perl
  libgcc-9-dev libgdbm-compat4 libgomp1 libisl22 libitm1 liblsan0 libmpc3
  libmpfr6 libperl5.30 libpython3-dev libpython3.8-dev libquadmath0
  libstdc++-9-dev libtsan0 libubsan1 linux-libc-dev make manpages-dev patch
  perl perl-modules-5.30 python-pip-whl python3-dev python3-wheel
  python3.8-dev zlib1g-dev
Suggested packages:
  binutils-doc cpp-doc gcc-9-locales debian-keyring g++-multilib
  g++-9-multilib gcc-9-doc gcc-multilib autoconf automake libtool flex bison
  gdb gcc-doc gcc-9-multilib glibc-doc git bzr libstdc++-9-doc make-doc
  diffutils-doc perl-doc libterm-readline-gnu-perl
  | libterm-readline-perl-perl libb-debug-perl liblocale-codes-perl
The following NEW packages will be installed:
  binutils binutils-common binutils-x86-64-linux-gnu build-essential cpp cpp-9
  dpkg-dev fakeroot g++ g++-9 gcc gcc-9 gcc-9-base libalgorithm-diff-perl
  libalgorithm-diff-xs-perl libalgorithm-merge-perl libasan5 libatomic1
  libbinutils libc-dev-bin libc6-dev libcc1-0 libcrypt-dev libctf-nobfd0
  libctf0 libdpkg-perl libexpat1-dev libfakeroot libfile-fcntllock-perl
  libgcc-9-dev libgdbm-compat4 libgomp1 libisl22 libitm1 liblsan0 libmpc3
  libmpfr6 libperl5.30 libpython3-dev libpython3.8-dev libquadmath0
  libstdc++-9-dev libtsan0 libubsan1 linux-libc-dev make manpages-dev patch
  perl perl-modules-5.30 python-pip-whl python3-dev python3-pip python3-wheel
  python3.8-dev zlib1g-dev
0 upgraded, 56 newly installed, 0 to remove and 0 not upgraded.
changed: [red] => (item=python3-pip)
ok: [red] => (item=python3-setuptools)

TASK [docker : include_tasks] *********************************************************************************************************************
included: */dev-ops-labs/ansible/roles/docker/tasks/install_docker.yaml for red

TASK [docker : D E S T R O Y old versions of Docker] **********************************************************************************************
ok: [red]

TASK [docker : Update requirements] ***************************************************************************************************************
ok: [red]

TASK [docker : Add GPG key for Docker repo] *******************************************************************************************************
changed: [red]

TASK [docker : Add Docker APT repository] *********************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable

changed: [red]

TASK [docker : Install Docker] ********************************************************************************************************************
The following packages were automatically installed and are no longer required:
  linux-headers-5.4.0-42 linux-headers-5.4.0-42-generic
  linux-image-5.4.0-42-generic linux-modules-5.4.0-42-generic
  linux-modules-extra-5.4.0-42-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  containerd.io docker-ce-cli docker-ce-rootless-extras docker-scan-plugin git
  git-man libcurl3-gnutls liberror-perl pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite git-daemon-run | git-daemon-sysvinit
  git-doc git-el git-email git-gui gitk gitweb git-cvs git-mediawiki git-svn
The following NEW packages will be installed:
  containerd.io docker-ce docker-ce-cli docker-ce-rootless-extras
  docker-scan-plugin git git-man libcurl3-gnutls liberror-perl pigz
  slirp4netns
0 upgraded, 11 newly installed, 0 to remove and 0 not upgraded.
changed: [red] => (item=docker-ce)
ok: [red] => (item=containerd.io)

TASK [docker : Install Docker Module for Python] **************************************************************************************************
changed: [red]

TASK [docker : Start Docker service] **************************************************************************************************************
ok: [red]

PLAY [Deploy Docker] ******************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************
ok: [red]

TASK [app_python : Run Docker Container from an image] ********************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "exists": false,
-    "running": false
+    "exists": true,
+    "running": true
 }

changed: [red]

PLAY RECAP ****************************************************************************************************************************************
red                        : ok=18   changed=9    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
