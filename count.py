#!/usr/bin/python

import os
import os.path
import re
import json
from helpers import *

with open('./helpers/maps.json') as data_file:
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
