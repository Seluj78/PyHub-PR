#! /usr/bin/env python3
import argparse
import json

try:
    import requests
except ImportError:
    print(
        "Module 'requests' is required to run this script. Please install and try again."
    )

from pyhub_pr._git import get_base_branch_name, get_current_branch_name


def create_pull_request(
    token, title, body, base, head, github_url, organisation, repository
):
    headers = {"Authorization": f"token {token}", "Content-Type": "application/json"}
    data = {
        "title": str(title),
        "body": str(body),
        "base": str(base),
        "head": str(head),
    }

    response = requests.post(
        github_url + "/repos/" + organisation + "/" + repository + "/pulls",
        headers=headers,
        data=json.dumps(data),
        verify=True,
    )

    if response.status_code not in range(200, 299):
        raise Exception("Response %d: %s" % (response.status_code, response.content))
    return response.json()


def main():
    parser = argparse.ArgumentParser(prog="github_pr", description="Create a PR")

    parser.add_argument(
        "--organisation", type=str, help="GitHub organisation", required=True
    )
    parser.add_argument("--repo", type=str, help="GitHub repo", required=True)

    parser.add_argument("--token", type=str, help="GitHub token", required=True)

    parser.add_argument(
        "--title", type=str, help="Title of the Pull Request", required=True
    )
    parser.add_argument(
        "--body", type=str, help="Body of the Pull Request", required=True
    )

    parser.add_argument(
        "--base",
        type=str,
        default=get_base_branch_name(),
        help="Base branch to merge into",
    )

    parser.add_argument(
        "--head",
        type=str,
        default=get_current_branch_name(),
        help="Head branch to merge from",
    )

    parser.add_argument(
        "--github-url",
        type=str,
        default="https://api.github.com",
        help="Github API url",
    )

    args = parser.parse_args()
    create_pull_request(
        args.token,
        args.title,
        args.body,
        args.base,
        args.head,
        args.github_url,
        args.organisation,
        args.repo,
    )
    # TODO: Across forks
    # TODO: Check if current branch has any changes
