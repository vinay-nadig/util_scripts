#!/usr/bin/env python

from urllib import urlretrieve
from time import sleep
import json

KEY = "FDBAB7A134AB406B355E07680120A8C1"
MYID = "76561198064204624"
UNDESIRABLEIDS = ["76561198095275944", "76561198037811837", "76561198065838844", "76561198066966102"]

def getjobj(steamid, key):
    url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={0}&steamids={1}".format(key, steamid)
    fname = urlretrieve(url)[0]
    jobj = json.load(open(fname, "r"))
    return jobj

flag = 1
for idey in UNDESIRABLEIDS:
    x = getjobj(idey, KEY)
    state = x["response"]["players"][0]["personastate"]
    if(state):
        flag = 0

if flag:
    print "Yep, safe to go online"
else:
    print "Nope, you are better off in the alt account"

sleep(5)

