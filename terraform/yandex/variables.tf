variable "zone" {
  type    = string
  default = "ru-central1-a"
}

variable "network_name" {
  type    = string
  default = "greg-net"
}

variable "subnetwork_name" {
  type    = string
  default = "greg-subnet"
}

variable "subnet_v4_cidr_blocks" {
  type    = list(string)
  default = ["192.168.10.0/16"]
}

variable "nat" {
  type    = bool
  default = true
}

variable "machine_name" {
  type    = string
  default = "red"
}

variable "image_id" {
  type    = string
  default = "fd80jdh4pvsj48qftb3d"
}

variable "image_family" {
  type    = string
  default = "ubuntu-1804-lts"
}

variable "cores" {
  type    = number
  default = 2
}

variable "memory" {
  type    = number
  default = 2
}

variable "timeout_create" {
  default = "10m"
}

variable "timeout_delete" {
  default = "10m"
}

variable "yandex_token" {
    type = string
}

variable "yandex_cloud_id" {
    type = string
}

variable "yandex_folder_id" {
    type = string
}