#!/bin/bash


cat names.dat | awk '{CMD[$1]++;count++} END { for (a in CMD) { if (CMD[a] >= 5) {print CMD[a] " " CMD[a]/count*100 "% " a; }}}' | grep -v "./" | column -c3 -s " " -t | sort -nr | head -n30


