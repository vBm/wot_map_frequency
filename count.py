#!/usr/bin/python

import os
import os.path
import re
import sys
import json
from helpers import *


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# got resource_path from http://stackoverflow.com/a/13790741

with open(resource_path('helpers/wot-maps.json'), 'rb') as data_file:
    mapNames = json.load(data_file)

files = [name for name in os.listdir('.') if os.path.isfile(name) and not
         name.startswith('temp') and name.endswith('.wotreplay')]

if len(files) > 0:
    print "%-35s %s" % ("Number of replays processed:\t", len(files))
    print "\n"
    nameRegex = r"(\d+)\_\d+\_(.*)\_(\d+\_\D+)\.wotreplay"
    maps = []
    for replays in files:
        replay = re.match(nameRegex, replays).groups()
        maps.append(replay[2])

    for count, mapName in sorted(((maps.count(e), e) for e in set(maps)),
                                 reverse=True):
        print "%-35s %5s" % (mapNames["maps"][mapName], count)
else:
    print "There are no replays available for processing...\n" \
          "Are you sure that you have enabled replay recording?"
