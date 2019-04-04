# PyHub-PR
Command line tool written in Python to create a PR on github

usage:
```
usage: github_pr [-h] --organisation ORGANISATION --repo REPO --token TOKEN --title TITLE --body BODY [--base BASE] [--head HEAD]
                 [--github-url GITHUB_URL]

Create a PR

optional arguments:
  -h, --help            show this help message and exit
  --organisation ORGANISATION
                        GitHub organisation
  --repo REPO           GitHub repo
  --token TOKEN         GitHub token
  --title TITLE         Title of the Pull Request
  --body BODY           Body of the Pull Request
  --base BASE           Base branch to merge into
  --head HEAD           Head branch to merge from
  --github-url GITHUB_URL
                        Github API url
```