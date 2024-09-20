import tkinter,os
from tkinter import ttk
import tkinter.messagebox
root=tkinter.Tk()
def b():
    with open('config.json', 'r') as file:
        content = file.read()
    root.destroy()
    os.system(content + "\MicroMiniNew.exe")
def old_b():
    with open('config.json', 'r') as file:
        content = file.read()
    root.destroy()
    os.system(content + "\MicroMiniNew_.exe")

def e():
    e=entry.get()
    if (e==""):
        tkinter.messagebox.showwarning(title='保存',message='请写入安装路径')
    else:
        with open('config.json', 'w') as f:
            f.write(e)
def download():
    os.system("start https://mdownload.mini1.cn/latest/miniworldoffice.exe")
root.iconbitmap('logo.ico')
root.title("迷你启动器")
root.geometry('400x200')
root.resizable(0,0)
w = ttk.Label(root, text="第一次启动请填入安装位置,并保存")
w.place(x=3,y=3)
w1 = ttk.Label(root, text="默认:C:\用户(Users)\名称\AppData\Roaming\miniworldgameguan110")
w1.place(x=0,y=25)
button=ttk.Button(root, text="新版界面",command=b,width=7)
button.place(x=335,y=140)
entry=ttk.Entry(root,width=30)
entry.place(x=3,y=55)
button1=ttk.Button(root,text="保存",command=e,width=7)
button1.place(x=225,y=54)
button2=ttk.Button(root,text="老版界面",command=old_b,width=7)
button2.place(x=335,y=170)
button3=ttk.Button(root,text="下载",width=7,command=download)
button3.place(x=3,y=170)
root.mainloop()
