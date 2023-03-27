#!/usr/bin/env python3

from subprocess import check_call, check_output
from pathlib import Path
from os import execlp

tag = check_output(['git', 'describe', '--tags', '--always'], text=True)
tag = tag.strip().lstrip('v')

image_name = 'gremid/tei-stylesheets-action'
image_tag = f'{image_name}:{tag}'

check_call(['docker', 'build', '-t', image_name, '.'])
check_call(['docker', 'tag', image_name, image_tag])
check_call(['docker', 'push', image_tag])
