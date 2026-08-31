#!/bin/bash
until "$@"; do
    echo "测试失败，正在重试……"
done
echo "测试执行成功！"

