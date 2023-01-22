from github import Github
import config


def repo_has_requested_reviews_for_user() -> bool:
    # Create GitHub api instance with access token
    github = Github(config.GH_TOKEN)

    # Grab repo
    repo = github.get_repo(config.GH_REPO)

    reviewers = []
    for pull in repo.get_pulls('open'):
        for reviewer in pull.requested_reviewers:
            if reviewer.login == config.GH_USER:
                return True

    return False
