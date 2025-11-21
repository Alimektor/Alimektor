#!/usr/bin/env python3

import json
import subprocess
from jinja2 import Template
import toml
from datetime import date
import argparse


def main(debug):
    today = date.today()
    markdown_template = open("config/TEMPLATE.md").read()
    template = Template(markdown_template)
    config = toml.load("config/config.toml")
    config.update({"public_projects": get_public_github_projects()})
    config.update({"archive_projects": get_archive_github_projects()})
    readme_content = template.render(config)
    if debug:
        # print(f"Config: {config}")
        print(f"Archived Projects: {config['archive_projects']}")
    with open("README.md", "w", encoding="utf-8") as readme_file:
        print(readme_content, file=readme_file)


def get_github_projects():
    gh_command = (
        "gh repo list --json owner,name,description,url,isArchived,isPrivate,isFork"
    )
    result = subprocess.run(gh_command.split(" "), capture_output=True, text=True)
    projects = json.loads(result.stdout)
    return projects


def get_public_github_projects():
    projects = get_github_projects()
    return [
        project
        for project in projects
        if not project["isArchived"]
        and not project["isPrivate"]
        and not project["isFork"]
        and not project["name"] == "Alimektor"
        and not project["name"] == "alimektor.github.io"
    ]


def get_archive_github_projects():
    projects = get_github_projects()
    return [
        project
        for project in projects
        if project["isArchived"] and not project["isPrivate"] and not project["isFork"]
    ]


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser("run.py")
        parser.add_argument("--debug", "-d", action="store_true")
        args = parser.parse_args()
        main(args.debug)
    except json.decoder.JSONDecodeError:
        print("Error: Need to be logged in to GitHub or something is wrong!")
