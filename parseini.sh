#!/bin/bash

set +a
while read p; do
  reSec='^\[(.*)\]$'
  #reNV='[ ]*([^ ]*)+[ ]*=(.*)'     #Remove only spaces around name
  reNV='[ ]*([^ ]*)+[ ]*=[ ]*(.*)'  #Remove spaces around name and spaces before value
  if [[ $p =~ $reSec ]]; then
      section=${BASH_REMATCH[1]}
  elif [[ $p =~ $reNV ]]; then
    sNm=${section}_${BASH_REMATCH[1]}
    sVa=${BASH_REMATCH[2]}
    set -a
    eval "$(echo "$sNm"=\""$sVa"\")"
    set +a
  fi
done < $1
