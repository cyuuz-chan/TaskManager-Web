import psutil
import keyboard
import os
from flask import Flask, render_template, request, jsonify
import socket
import tkinter.messagebox


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

tkinter.messagebox.showinfo(ip_address,ip_address)

app = Flask(__name__)


@app.route("/")
def index():
    exclude_list = ["System Idle Process", "smss.exe", "Registry", "System","svchost.exe","csrss.exe","services.exe","wininit.exe","lsass.exe"]
    process_list = []
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            pinfo = proc.as_dict(attrs=["pid", "name"])
            if pinfo["name"] not in exclude_list:
                process_list.append(pinfo)
        except psutil.NoSuchProcess:
            pass
    return render_template("index.html", process_list=process_list)



@app.route("/kill")
def kill():
    # 获取要杀死进程的 PID
    pid = int(request.args.get("pid"))

    # 终止指定 PID 的进程
    try:
        p = psutil.Process(pid)
        p.terminate()
        return "Process {} has been terminated.".format(pid)
    except psutil.NoSuchProcess:
        return "Process {} does not exist.".format(pid)


@app.route("/keyboard")
def keyboard_page():
    # 渲染模拟按键的页面模板
    return render_template("keyboard.html")


@app.route("/keypress", methods=["POST"])
def keypress():
    # 获取网页表单中填写的键值
    key = request.form["key"]
    key = key.replace(" ", "+")
    # 模拟按键事件
    keyboard.press_and_release(key)

    # 返回处理结果
    return jsonify({"result": "success"})


@app.route("/command")
def command_page():
    # 渲染执行命令的页面模板
    return render_template("command.html")


@app.route("/exec_command", methods=["POST"])
def exec_command():
    # 获取要执行的命令
    cmd = request.form["cmd"]

    # 执行命令并获取输出结果
    os.system(cmd)

    # 返回处理结果
    return jsonify({"result": "success"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
