# TaskManager-Web
网页端的任务管理器，支持Windows / Linux / MacOS

## 有什么用
顾名思义，可以通过网页控制电脑进程，此外还有**键盘控制**和**执行指令**的功能  
使用场景：
- 电脑被某个进程卡死，无法打开任务管理器关闭进程
- 躺在床上不想跑到电脑前按键盘
- 不打开终端的前提下快速执行命令

## 使用
先记得安装以下这些
```bash
pip install psutil keyboard flask
```
然后直接运行 `main.py`
### 管理页面
运行后会提示你的IP地址，可以通过`5000`端口访问  
默认打开TaskManager，若果想使用键盘控制或执行指令功能，请访问`/keyboard`或`/command`  
例如：
- http://127.0.0.1:5000
- http://192.168.1.114:5000/keyboard
