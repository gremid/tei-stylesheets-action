#!/usr/bin/env python3

from os import environ, execve
from sys import argv, stderr, exit

cmd = environ.get('INPUT_TRANSFORM')
source = environ.get('INPUT_SOURCE')
target = environ.get('INPUT_TARGET')
odd2odd = environ.get('INPUT_ODD2ODD')

args = argv[1:]

if cmd is None and len(args) > 1:
    cmd = args[0]
    args = args[1:]

if cmd is None:
    stderr.write('Missing transform command\n')
    exit(1)

if (odd2odd is not None) and (odd2odd.lower() in ['yes', 'true', '1']):
    args.append('--odd')

if source is not None:
    args.append(source)
if target is not None:
    args.append(target)

cmd = '/stylesheets/bin/' + cmd
args = [cmd] + args
execve(cmd, args, environ)
