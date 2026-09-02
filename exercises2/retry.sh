#!/usr/bin/env bash
count=0
while true
do
    count=$((count + 1))
    ./target.sh > out.log 2> err.log
    if [ $? -ne 0 ]; then
        echo "脚本发生失败，一共运行 ${count} 次"
        break
    fi
done
