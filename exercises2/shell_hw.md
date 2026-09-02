# Shell第二周练习（共11题）

## 练习1：特殊参数 `--`
问题：`--` 后面的所有内容都会被当作位置参数,作用是？


回答：`--` 告诉程序不再解析选项，后续全部作为文件名。


代码：
```bash
touch -- -myfile
# 删除：不能 rm -myfile，要写
rm -- -myfile
```

## 练习2：`ls`组合参数
问题：让`ls`按下面的方式列出文件：


1. 包含所有文件，包括隐藏文件


2. 文件大小以易读格式显示（例如 454M，而不是 454279954）


3. 按最近修改时间排序


4. 输出带颜色


代码：
```bash
ls -Ahltr --color=auto
```

解释：


 `-A`：全部隐藏文件，排除 `.` `..`
 `-h`：易读单位
 `-l`：长格式
 `-t`：按修改时间
 `-r`：逆序，旧文件放上面

## 练习3：进程替换比较 `printenv` 和 `export`
问题：进程替换 `<(command)` 可以把一个命令的输出当成文件来用。配合 `diff` 和进程替换，比较 `printenv` 与 `export` 的输出。它们为什么不一样？


代码：
```bash
diff <(printenv | sort) <(export | sort)
```

回答：


区别：


`printenv`：只输出环境变量


`export`：输出所有导出变量，会附带 `declare -x` shell 元信息，输出内容比 `printenv` 多


## 练习 4：`marco` `&` `polo` 保存切换目录
问题：写两个 `bash` 函数 `marco` 和 `polo`，行为如下：


1. 每次执行 `marco` 时，都要以某种方式保存当前工作目录；


2. 之后无论切到哪个目录，只要执行 `polo`，它都应该把 `cd` 回执行 `marco` 时所在的目录。


3. 为了方便调试，可以把代码写进 `marco.sh`，然后通过执行 `source marco.sh` 把这些定义重新加载到当前 shell。


代码：
```bash
cat > marco.sh <<'EOF'
#!/usr/bin/env bash
marco(){
    export SAVED_DIR=$(pwd)
}
polo(){
    cd "$SAVED_DIR"
}
EOF

```

## 练习 5：脚本循环直到命令失败
问题：脚本 `retry.sh`循环运行，统计运行多少次才出错，`stdout/stderr` 分开保存


代码：
```bash
#!/usr/bin/env bash
count=0
while true; do
    count=$((count+1))
    ./target.sh > out.log 2> err.log
    if [ $? -ne 0 ];then
        echo "失败！一共运行 $count 次"
        break
    fi
done
```
输出结果：
```bash
./retry.sh
脚本发生失败，一共运行 25次

ls
err.log  marco.sh  out.log  retry.sh  shell_hw.md  target.sh
```


## 练习6：任务控制，后台`sleep`，`pgrep`+`pkill`杀掉
问题：在终端里启动一个`sleep 10000`任务，用`Ctrl-Z`把它挂起，再用`bg`让它继续在后台运行。然后使用`pgrep`找到它的`pid`，再用`pkill` 把它杀掉，整个过程都不要手动输入这个 `pid`。


代码：
```bash
sleep 10000
# Ctrl‑z挂起
bg
pgrep -af sleep
pkill sleep
```
输出结果：
```bash
^Z
[1]+  Stopped                    sleep 10000

[1]+ sleep 10000 &

27723 sleep 10000

[1]+  Terminated                 sleep 10000
```

## 练习 7：`pidwait` 函数，等待指定进程结束
问题：写一个叫`pidwait`的`bash`函数，接收一个`pid`，并一直等待到该进程结束。用`sleep`来避免空转浪费 CPU。


代码：
```bash
pidwait(){
    local pid=$1
    while kill -0 "$pid" 2>/dev/null; do
        sleep 0.2
    done
}
# 使用 pidwait 1234
```

解释：`kill -0` 不发信号，仅检测进程是否存活。


输出结果：
```bash
sleep 5 &
pid=$!
pidwait $pid
echo "sleep结束，执行后续代码"

[1] 30137
[1]+  Done                       sleep 5
进程 30137 已经结束
sleep结束，执行后续代码
```

## 练习 8：递归查找目录最近修改文件
问题：写一个命令或脚本，递归找出某个目录中最近修改过的文件。更一般一点，你能不能按“最近修改时间”列出所有文件？


代码：
```bash
find . -type f -printf "%T@ %p\n" | sort -n | tail -n 1
```


解释：`%T@`输出修改时间戳，排序，取最后一条就是最新修改文件。


输出结果：
```bash
1788327166.8119620390 ./shell_hw.md
```

## 练习 9：`alias` 容错 `cd`，打错 `dc` 也能 `cd`
代码：
```bash
alias dc='cd'
```

解释：放到`.bashrc`永久生效。


## 练习 10：统计历史最常用 10 条命令
代码：
```bash
history | awk '{$1="";print substr($0,2)}' | sort | uniq -c | sort -n | tail -n 10
```
输出结果：
```bash
      4 cd ~
      4 pwd
      5 bash
      5 ls win_share
      5 nano shell_hw.md
      5 sudo apt update
      6 git status
      8 git push
      9 ls
     28 
```

## 练习 11：端口转发 ssh -N 后台转发
问题：查找`ssh`里的`-N`和`-f`参数分别是什么意思，写出一条能够实现后台端口转发的命令。


代码：
```bash
ssh -N -L 9999:localhost:8888 vm
```

解释：


`-N`：不执行远程`shell`，只做端口转发;


`-L`：本地端口转发。
