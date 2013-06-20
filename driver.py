#!/usr/bin/env python

import sys,argparse,bs
from bs.engine import *

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--players", help="number of players", type=int)
args = parser.parse_args()

print "Starting " + str(args.players) + " player game..."
egn = Engine(args.players)
