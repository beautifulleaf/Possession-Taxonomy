#!/bin/bash
for n in "$@"; do echo "#### $n"; sed -n '/Distribution/,/Name:/p' homa/$n.txt | tr -s ' \n' ' ' | cut -c1-1000; echo; done
