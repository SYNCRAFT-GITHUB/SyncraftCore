#!/bin/bash

# Executes all files within folders in the same script directory.

dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

for folder in "$dir"/*; do
    if [ -d "$folder" ]; then
        if [ -f "$folder/apply.sh" ]; then
            echo "RUNNING: $folder"
            (cd "$folder" && sudo bash apply.sh)
        fi
    fi
done
