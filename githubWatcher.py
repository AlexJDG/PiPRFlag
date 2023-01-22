from github import Github
import config


def repo_has_requested_reviews_for_user(token, repo, username):
    # Create GitHub api instance with access token
    github = Github(token)

    # Grab repo
    repo = github.get_repo(repo)

    reviewers = []
    for pull in repo.get_pulls('open'):
        for reviewer in pull.requested_reviewers:
            reviewers.append(reviewer.login)

    return username in reviewers


if repo_has_requested_reviews_for_user(config.GH_TOKEN, config.GH_REPO, config.GH_USER):
    print('yes')
