#!/bin/bash

# 如果没有传参，默认使用当前目录
if [ $# -eq 0 ]; then
    dir="."
else
    dir="$1"
fi

find "$dir" -type f 2>/dev/null | awk -F '.' '
{
    if (NF >= 2) {
        ext = $NF
        cnt[ext]++
    } else {
        cnt["(no suffix)"]++
    }
}
END {
    for(k in cnt) {
        printf "%-15s %d\n", k, cnt[k]
    }
}
'

