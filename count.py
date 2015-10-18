#!/usr/bin/python

import os
import os.path
import re
from helpers import *

# Populated list from:
# https://api.worldoftanks.eu/wot/encyclopedia/arenas/?application_id=demo&fields=name_i18n
# count: 43

mapNames = {
    "00_tank_tutorial": "Training area",
    "01_karelia": "Karelia",
    "02_malinovka": "Malinovka",
    "03_campania": "Province",
    "04_himmelsdorf": "Himmelsdorf",
    "05_prohorovka": "Prokhorovka",
    "06_ensk": "Ensk",
    "07_lakeville": "Lakeville",
    "08_ruinberg": "Ruinberg",
    "10_hills": "Mines",
    "11_murovanka": "Murovanka",
    "13_erlenberg": "Erlenberg",
    "14_siegfried_line": "Siegfried Line",
    "17_munchen": "Widepark",
    "18_cliff": "Cliff",
    "19_monastery": "Abbey",
    "22_slough": "Swamp",
    "23_westfeld": "Westfield",
    "28_desert": "Sand River",
    "29_el_hallouf": "El Halluf",
    "31_airfield": "Airfield",
    "33_fjord": "Fjords",
    "34_redshire": "Redshire",
    "35_steppes": "Steppes",
    "36_fishing_bay": "Fisherman's Bay",
    "37_caucasus": "Mountain Pass",
    "38_mannerheim_line": "Arctic Region",
    "39_crimea": "South Coast",
    "44_north_america": "Live Oaks",
    "45_north_america": "Highway",
    "47_canada_a": "Serene Coast",
    "63_tundra": "Tundra",
    "73_asia_korea": "Sacred Valley",
    "83_kharkiv": "Kharkov",
    "84_winter": "Windstorm",
    "86_himmelsdorf_winter": "Winter Himmelsdorf",
    "92_stalingrad": "Stalingrad",
    "95_lost_city": "Ghost Town",
    "96_prohorovka_defense": "Fiery Salient",
    "100_thepit": "Mittengard",
    "101_dday": "Overlord",
    "103_ruinberg_winter": "Winterberg",
    "111_paris": "Icebound"
}

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
        print "%-35s %5s" % (mapNames.get(mapName), count)
else:
    print "There are no replays available for processing...\n" \
          "Are you sure that you have enabled replay recording?"
