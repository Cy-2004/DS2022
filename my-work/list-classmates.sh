#!/bin/bash

set -e

# move into people dir
cd ../people

# look for readme file
target_file="README.md"

# loop through all dirs and find target file
for dir in $( find . -type d ); do 
  if[ -f "$dir/$target_file" ]; then
    #echo "$dir/$target_file";
    name='head -n 1 "dir/$target_file"';
    echo $name;
  fi
done
