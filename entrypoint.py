#!/usr/bin/env python3

from os import environ, execve
from sys import argv, stderr, exit

args = argv[1:]

if len(args) == 0:
    stderr.write('Missing args\n')
    exit(1)

cmd = '/stylesheets/bin/' + args[0]
args = [cmd] + args[1:]

execve(cmd, args, environ)
