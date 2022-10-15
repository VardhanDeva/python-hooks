#!/usr/bin/python
from pygit2 import Repository
current_branch = (Repository('.').head.shorthand)
print(current_branch)
