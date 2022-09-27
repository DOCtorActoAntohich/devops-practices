terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "5.2.0"
    }
  }
}


# Gotta save access token to `GITHUB_TOKEN`.
provider "github" {}


resource "github_repository" "repo" {
  name        = "dev-ops-labs"
  description = "Linux, pain, existential dread - all that we love in DevOps you can find here."
  visibility  = "public"

  allow_squash_merge = false
  allow_rebase_merge = false
}

resource "github_branch_default" "master" {
  repository = github_repository.repo.name
  branch     = "master"
}

resource "github_branch_protection" "master" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.master.branch

  required_pull_request_reviews {
    required_approving_review_count = 0
    dismiss_stale_reviews = true
  }
}
