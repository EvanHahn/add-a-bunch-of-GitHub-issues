#!/usr/bin/env python
from github3 import login
from time import sleep
from random import randint

print("go to https://github.com/settings/tokens/new to get an access token")
gh_token = raw_input("what's your access token? ")

owner = raw_input("what user owns the repo? ")
reponame = raw_input("what's the repo called? ")

filename = raw_input("what file has all of the issues? ")

with open(filename, "r") as file:
    for unstripped_line in file:
        line = unstripped_line.strip()

        if len(line) != 0:
            gh = login(token=gh_token)
            repo = gh.repository(owner, reponame)

            print("adding " + line),
            repo.create_issue(line)

            print("- added. sleeping for"),
            sleeping_time = randint(10, 45)
            print(sleeping_time),
            print("seconds")
            sleep(sleeping_time)
