# Terraform

Doing it for a project that small is cursed.

## How to run

You might want to go to `main.tf` and comment out one line (you'll see) because of Windows.
I didn't test it on Linux.

### Locally

Inside `terraform` folder, where `Makefile` is located, run `make run_local`.
When you're done, run `make stop_local`.

You will have to confirm your actions, just follow the instructions.

If running for the first time, let it wait for 3-10 minutes because Terraform is stupid and slow.
After that you should be fine because it should cache.
~~If it doesn't cache then you can shoot me in my knee.~~

## Docker

~~Kind of same as `Docker Compose` but more annoying.~~

### Command outputs

- [terraform show](local/Command%20outputs/terraform%20show)
- [terraform state list](local/Command%20outputs/terraform%20state%20list)
- [terraform output](local/Command%20outputs/terraform%20output)

## Yandex Cloud

~~I mean, you know why I won't use AWS.~~

Thanks to [Yandex Docs](https://cloud.yandex.ru/docs/tutorials/infrastructure-management/terraform-quickstart) for existing.
