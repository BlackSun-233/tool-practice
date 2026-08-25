# Missing‑Semester Shell 课后练习（1‑10）


## 题目1：`ls` `-l` 参数
命令：
```bash
ls -l /
```
问题：`ls` 的 `-l` 选项作用是什么？每一行最前面 10 个字符分别代表什么？

回答：

`-l` 参数使用长格式，展示文件类型、权限、所有者、大小、修改时间。

开头10字符：第1位是文件类型；2‑4所有者权限；5‑7用户组权限；8‑10其他用户权限。d代表目录，l代表软链接。


输出结果：
```bash
total 100
drwxr-xr-x   2 root root  4096 Oct 31  2025 bin
drwxr-xr-x   3 root root  4096 Oct 31  2025 boot
drwxrwxr-x   2 root root  4096 Oct  4  2025 cdrom
drwxr-xr-x  18 root root  4000 Aug 24 00:07 dev
drwxr-xr-x 135 root root 12288 Aug 24 06:39 etc
drwxr-xr-x   3 root root  4096 Oct  4  2025 home
lrwxrwxrwx   1 root root    34 Oct 31  2025 initrd.img -> boot/initrd.img-4.15.0-142-generic
lrwxrwxrwx   1 root root    34 Oct  4  2025 initrd.img.old -> boot/initrd.img-4.15.0-112-generic
drwxr-xr-x  22 root root  4096 Oct  4  2025 lib
drwxr-xr-x   2 root root  4096 Oct 31  2025 lib64
drwx------   2 root root 16384 Oct  4  2025 lost+found
drwxr-xr-x   3 root root  4096 Aug  6  2020 media
drwxr-xr-x   3 root root  4096 Oct 27  2025 mnt
drwxr-xr-x   2 root root  4096 Oct  4  2025 opt
dr-xr-xr-x 245 root root     0 Aug 24 00:07 proc
drwx------   4 root root  4096 Oct 30  2025 root
drwxr-xr-x  25 root root   840 Aug 24 17:27 run
drwxr-xr-x   2 root root 12288 Oct 31  2025 sbin
drwxr-xr-x   2 root root  4096 Oct  4  2025 snap
drwxr-xr-x   2 root root  4096 Aug  6  2020 srv
dr-xr-xr-x  13 root root     0 Aug 24 00:07 sys
drwxrwxrwt  14 root root  4096 Aug 24 17:27 tmp
drwxr-xr-x  12 root root  4096 Aug  6  2020 usr
drwxr-xr-x  14 root root  4096 Aug  6  2020 var
lrwxrwxrwx   1 root root    31 Oct 31  2025 vmlinuz -> boot/vmlinuz-4.15.0-142-generic
lrwxrwxrwx   1 root root    31 Oct 31  2025 vmlinuz.old -> boot/vmlinuz-4.15.0-112-generic
```


## 题目 2：glob 通配符
命令：
```bash
mkdir test_glob
cd test_glob
touch a.txt b.txt file1.txt file2.txt
ls *.txt
ls file?.txt
ls {a,b,c}.txt
cd ..
```
问题：什么是 glob？

回答：
```bash
a.txt  b.txt  file1.txt  file2.txt
file1.txt  file2.txt
ls: cannot access 'c.txt': No such file or directory
a.txt  b.txt
```
glob是Shell在执行命令之前做的文件名模式展开，不是`ls`程序本身实现。

`*` 匹配任意长度任意字符；

`?` 严格匹配单个字符；

`{a,b,c}`批量展开多个文件名。

即使展开后的文件不存在，shell依旧会把名字传给命令，于是程序会报文件找不到。

## 题目 3：三种引号
命令：
```bash
echo $'符号测试 $ ! \n这里是换行'
```
问题：单引号`''`、双引号`""`、`'$'` 的区别？

回答：
```bash
符号测试 $ ! 
这里是换行
```

三种引号区别：

1. 单引号 `''`：原样输出所有字符，`$`、`!`、转义符全部不解析。

2. 双引号 `""`：可以解析变量`$`，但不处理`\n`换行转义。

3. `'$'`：支持`\n`这类转义换行，特殊符号直接打印。


## 题目 4：标准流重定向
命令：
```bash
ls /nonexistent /tmp > out_std.txt 2> out_err.txt
ls /nonexistent /tmp > all_out.txt 2>&1
```
问题：如何分别重定向、如何合并 stdout 与 stderr？

回答：
```bash
# cat out_std.txt
/tmp:
config-err-vVjmwY
gnome-software-QPTEU3
systemd-private-eec8dc2894454e4481e39e08d7f52123-colord.service-KYgn1N
systemd-private-eec8dc2894454e4481e39e08d7f52123-fwupd.service-V7X0lm
systemd-private-eec8dc2894454e4481e39e08d7f52123-rtkit-daemon.service-4Xh22r
systemd-private-eec8dc2894454e4481e39e08d7f52123-systemd-timesyncd.service-xlHmmg
unity_support_test.0
VMwareDnD
vmware-root

# cat out_err.txt
ls: cannot access '/nonexistent': No such file or directory

# cat all_out.txt
ls: cannot access '/nonexistent': No such file or directory
/tmp:
config-err-vVjmwY
gnome-software-QPTEU3
systemd-private-eec8dc2894454e4481e39e08d7f52123-colord.service-KYgn1N
systemd-private-eec8dc2894454e4481e39e08d7f52123-fwupd.service-V7X0lm
systemd-private-eec8dc2894454e4481e39e08d7f52123-rtkit-daemon.service-4Xh22r
systemd-private-eec8dc2894454e4481e39e08d7f52123-systemd-timesyncd.service-xlHmmg
unity_support_test.0
VMwareDnD
vmware-root
```

解释：

`>`: 重定向标准输出stdout；

`2>`: 重定向标准错误stderr；

`2>&1`: 将stderr合并到stdout，正常输出和报错写入同一个文件。


## 题目 5：条件创建目录
命令：
```bash
[ ! -d "/tmp/mydir" ] && mkdir /tmp/mydir
```
问题：解释这条一行命令逻辑

回答：
```bash
# 终端输出：无任何打印
```
解释：

 `[ ! -d "/tmp/mydir" ]`  判断  `/tmp/mydir`  这个目录是否不存在。

 `!` 代表取反， `-d` 判断是否为目录。

 `&&`  逻辑与：只有前面判断条件为真，才执行后面的 `mkdir` 创建目录


## 题目 6：`cd` 为什么是 shell 内置命令
回答：

`cd` 的作用是改变当前Shell进程本身的工作目录。

如果`cd`是一个外部独立程序，运行时会开启子进程；子进程修改自己的目录，不会影响父Shell，命令结束后就失效。

因此`cd`必须作为Shell内置命令，直接在当前Shell进程内部修改工作目录。


## 题目 7：判断文件是否存在脚本 check.sh
```bash
./check.sh check.sh
./check.sh nofile.txt
```
输出结果：
```bash
./check.sh check.sh
File check.sh exists.

./check.sh nofile.txt
File nofile.txt does NOT exist.
```
解释：

 `$1` 代表脚本接收的第一个命令行参数。

 `-f`  判断是否为普通文件。脚本判断传入名字对应的文件是否存在，打印对应提示。


## 题目 8：`chmod +x` 执行权限
问题：为什么需要 `chmod +x`？

回答：

Linux新建的文本文件默认没有可执行权限。

 `chmod +x`  给文件加上执行权限，系统才能够把这个文件当做程序脚本运行。

不加的话，无法用  `./`文件名  的方式直接执行脚本。


## 题目 9：`set -x` 脚本调试
```bash
./debug.sh
```
观察输出：
```bash
+ ./debug.sh
a的值是 10
+ set +x
```
解释：

 `set -x` 开启shell调试模式，会打印实际执行的命令； `set +x` 关闭调试。

调试模式方便看变量替换、shell实际执行了什么语句。


## 题目 10：带日期备份文件
```bash
touch notes.txt
cp notes.txt notes_$(date +%Y-%m-%d).txt
ls
```
输出：
```bash
touch notes.txt
cp notes.txt notes_$(date +%Y-%m-%d).txt
ls

all_out.txt  notes_2026-08-24.txt  out_std.txt
check.sh     notes.txt             shell_hw.md
debug.sh     out_err.txt           test_glob
```
解释：

 `$`(命令)  是命令替换，会先执行括号内命令，把输出结果嵌入到当前命令行。

这里 date 输出当前日期，拼接成带时间戳的备份文件名。
