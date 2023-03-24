#!/usr/bin/env python3

from os import execlp

execlp('docker', 'docker', "build", "-t", "gremid/tei-stylesheets-action", ".")
