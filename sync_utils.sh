#!/bin/bash

shopt -s globstar

array=( "${@}" )
arraylength=${#array[@]}

for (( i=0; i < ${arraylength}; i++ )); do
   cp utils/* "${array[$i]}"
   [[ $? ]] && echo "Synced contents of utils to ${array[$i]} succesfully"
done

for d in */; do cp .gitignore "$d"; done
[[ $? ]] && echo "Succesfully synced .gitignore file"
