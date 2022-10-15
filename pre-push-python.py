#!/usr/bin/python
from pygit2 import Repository
print(Repository('.').head.shorthand)