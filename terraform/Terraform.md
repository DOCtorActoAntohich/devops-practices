# Terraform

Doing it for a project that small is cursed.

## Docker

~~Kind of same as `Docker Compose` but more annoying.~~

### How to

### Command outputs for Docker

- [terraform show](local/Command%20outputs/terraform%20show)
- [terraform state list](local/Command%20outputs/terraform%20state%20list)
- [terraform output](local/Command%20outputs/terraform%20output)

## Yandex Cloud

~~I mean, you know why I couldn't use AWS.~~

### Command outputs for Yandex

- [terraform show](yandex/Command%20outputs/terraform%20show)
- [terraform state list](yandex/Command%20outputs/terraform%20state%20list)
- [terraform output](yandex/Command%20outputs/terraform%20output)

## Good practices I used

- Separate workspaces (split local and production).
- Files are as small as possible.
- Use input variables.
- To initialize sensitive variables, use `terraform.tfvars` file, which is `.gitignore`d.
- Keep `.terraform.lock.hcl` file in the repository so that teammates have no problems managing dependencies.

## How to run this mess

### Locally

Inside `terraform` folder, where `Makefile` is located, run `make run_local`.
When you're done, run `make stop_local`.

You will have to confirm your actions, just follow the instructions.

If running for the first time, let it wait for 3-10 minutes because Terraform is stupid and slow.
After that you should be fine because it should cache.
~~If it doesn't cache then you can shoot me in my knee.~~

You might want to go to `main.tf` and comment out one line (you'll see) because of Windows.
I didn't test it on Linux.

### Yandex provider

First of all, good luck following the guide mentioned on [Yandex Docs](https://cloud.yandex.ru/docs/tutorials/infrastructure-management/terraform-quickstart)!
~~This guide was so disgustingly bad and unclear, if I start commenting on it, the censorship will say I was silent.~~

After you obtain your API key, cloud ID, and folder ID, copy contents of `terraform.tfvars.sample` into `terraform.tfvars` and change all variables accordingly.

If you have something to do with users and SSH, go to `machine-user.yml` and change the SSH key.
Mine is garbage, I don't even remember the passphrase, and I didn't link it to the account.

Finally, run `make run_yandex` to create VMs, and `make stop_yandex` to stop them.
