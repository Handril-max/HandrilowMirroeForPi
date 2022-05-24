# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# HandrilFunctionServices
# Handril startapp
# -*- coding:utf-8 -*-
from posixpath import split
import subprocess
from . import fileprocess as fp
import tkinter as tk
import os
import shutil
from . import threadpool as thdpol
from . import for_web
from . import cpupack as cpk
from .openHandrilow import set_path
from . import threadpool as thdpol
import multiprocessing
import importlib
import sys
fath_path = set_path.pwd()
pids = "./HandrilowOSLauncherCode/H_fileprocess/m1.pid"
#####################################################
memory = []
#####################################################
#含昭系统核心
def sys_launch(mark):#系统调用
    global memory
    path = fath_path+'/HandrilowOSLauncherCode/openHandrilow'
    appath_py = path + '/' + mark +'/'+ mark + '.py'
    evirment = 'HandrilowOSLauncherCode.openHandrilow.' + mark + '.' + mark
    if evirment in memory:
        None
    else:
        memory.append(evirment)
        cpk.unpathfilewrite("thread_all.psw", "a", str(mark)+'\n')
    #memory = list(open('thread_all.psw','r'))
    import_app = importlib.import_module(evirment)
    thdpol.dissetp.thd2(import_app.main())

def app_launch(mark):#系统调用
    global memory
    path = fath_path+'/HandrilowOSLauncherCode/sys/programe'
    appath_py = path + '/' + mark +'/'+ mark + '.py'
    evirment = 'HandrilowOSLauncherCode.sys.programe.' + mark + '.' + mark
    if evirment in memory:
        None
    else:
        memory.append(evirment)
        cpk.unpathfilewrite("thread_all.psw", "a", str(mark)+'\n')
    #memory = list(open('thread_all.psw','r'))
    import_app = importlib.import_module(evirment)
    thdpol.dissetp.thd2(import_app.main())
    
def all_launch(mark):
    path = fath_path+'/HandrilowOSLauncherCode/openHandrilow'
    appath_py = path + '/' + mark +'/'+ mark + '.py'
    path1 = fath_path+'/HandrilowOSLauncherCode/sys/programe'
    appath_py1 = path1 + '/' + mark +'/'+ mark + '.py'
    if os.path.exists(appath_py):
        sys_launch(mark)
    elif os.path.exists(appath_py1):
        app_launch(mark)
    else:
        cpk.message('提示','此指令不存在于系统')

def launch(cmd, mark):#应用调用
    cpk.unpathfilewrite("apppath.psw", "w", mark)
    #cmd = 'E:/Handrilow/programe/game/game.py'
    example = fath_path+'/HandrilowOSLauncherCode/sys'
    path = fath_path+'/HandrilowOSLauncherCode/sys/programe'
    appath_html = path + '/' + mark +'/'+ mark + '.htmr'
    evirment = 'HandrilowOSLauncherCode.sys.programe.' + mark + '.' + mark
    appath_py = path + '/' + mark +'/'+ mark + '.py'
    appath_pyw = path + '/' + mark +'/'+ mark + '.pyw'
    if os.path.exists(appath_html) == True:
        with open(appath_html, "r") as fp:
            bg = fp.read()
        print(bg)
        for_web.main(bg)
    elif os.path.exists(appath_py) == True:
        import_app = importlib.import_module(evirment)
        thdpol.dissetp.thd2(import_app.main())
    elif os.path.exists(appath_pyw) == True:
        import_app = importlib.import_module(evirment)
        thdpol.dissetp.thd2(import_app.main())
    else:
        cpk.message('警告','非可执行文件')
#####################################################
#####################################################
       
def syslaunch(cmd):
    subprocess.Popen(cmd)


def killprocess(cmd):
    #cmd = 'E:/Handrilow/programe/game/game.py'
    os.system("taskkill /f /im " + cmd)
# launch()


def applist(master, filenames, path, A4, f1):
    def selectbg():
        with open("selectbg.psw", "r") as fp:
            bg = fp.read()
        theLB.config(selectbackground=bg)
        theLB.after(1000, selectbg)
    theLB = tk.Listbox(master, bd=0, bg=A4, exportselection=True, fg='black', highlightcolor=A4, width=25, height=20,
                       selectforeground=A4, font=('等线',11), highlightbackground=A4,
                       selectmod="browse")
    theLB.pack(side='top', pady=5, padx=10)
    selectbg()

    name2 = tk.Label(master, bg=A4, fg='#4D4D4D',
                     font=('华文细黑', 10, "bold"), bd=0)
    name2.pack(side='top', pady=5, padx=5)
    name2.config(text="应用列表 @ Programe")
    for item in filenames:
        theLB.insert("end", item)

    def deleat():
        a = theLB.get(theLB.curselection())
        b = theLB.delete("active")
        shutil.rmtree(path + '/' + a)
        for item in filenames:
            theLB.delete(0, END)
            theLB.insert("end", item)
    
    def to_desktop():
        appname = theLB.get(theLB.curselection())
        cpk.unpathfilewrite(fath_path + "/HandrilowOSLauncherCode/disk/allfile/"+appname, "w","") 
        #cpk.unpathfilewrite(fath_path + "/HandrilowOSLauncherCode/disk/allfile/"+appname+"/auto.info", "w", "icon/"+appname+".png")

    def printList():
        pids = fath_path+"/HandrilowOSLauncherCode/H_fileprocess/applaunched.pid"
        pids1 = fath_path + "/HandrilowOSLauncherCode/H_fileprocess/m1.pid"
        cpk.pathfilewrite(pids, "w")
        a = theLB.get(theLB.curselection())
        fp.exitesys(master,pids1)
        master.destroy()
        with open("tipname.psw", "w") as f:
            f.write(a)
        dirs = fath_path+"/HandrilowOSLauncherCode/job" + "/" + a
        fileexists = os.path.exists(dirs)
        if fileexists == True:
            pass
        else:
            b = os.mkdir(dirs)
        appath = path + '/' + a + '/' + a + '.py'
        #launch(appath, a)
        a = multiprocessing.Process(target=launch,args=(appath, a))
        a.start()
        #t=threading.Thread(target=launch,args=(appath, a))
        #t.start()
    menubar = tk.Menu(master)
    menu = tk.Menu(master, tearoff=0)
    #menu.add_command(label='消除此项',command=lambda x=theLB:x.delete("active") and deleat)
    menu.add_command(label='从Handrilow卸载此程序', command=deleat)
    menu.add_command(label='添加到查阅', command=to_desktop)
    menu.add_separator()

    def popumenua(event):
        menu.post(event.x_root, event.y_root)
    def to_launch(_):
        printList()
        print(sys.getsizeof(printList))
        #printList()
    theLB.bind('<Button-3>', popumenua)
    theLB.bind('<Double-Button-1>', to_launch)
    theLB.bind('<Return>', to_launch)
