#!/bin/bash

csvfile="$1"

if [ ! -f "$csvfile" ]; then
    echo "Error: file $csvfile does not exist" >&2
    exit 1
fi

awk -F',' 'NR>1 && $4 ~ /^5/ {print $3}' "$csvfile" \
| sort | uniq -c \
| sort -k1,1nr -k2,2 \
| head -n 2

awk -F',' 'NR>1 {sum += $5; cnt++} END {print sum, cnt}' "$csvfile" \
| awk '{printf "%.2f\n", $1 / $2}'
