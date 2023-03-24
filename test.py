#!/usr/bin/env python3

from os import execlp, getcwd
from subprocess import check_output

uid = check_output(['id', '-u'], text=True).strip()
gid = check_output(['id', '-g'], text=True).strip()

execlp(
    'docker', 'docker',
    'run', '-it', '--rm',
    '-u', ':'.join([uid, gid]),
    '-v', f'{getcwd()}:/work',
    'gremid/tei-stylesheets-action',
    'teitorelaxng', '/work/tei_lite.odd', '/work/tei_lite.rng'
)
