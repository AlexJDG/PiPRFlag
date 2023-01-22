from githubWatcher import repo_has_requested_reviews_for_user
from flagControl import FlagController

flag = FlagController()
if repo_has_requested_reviews_for_user():
    flag.setFlagUp()
else:
    flag.setFlagDown()