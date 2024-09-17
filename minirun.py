import os
import tkinter as tk
import tkinter.messagebox
def b():
    with open('config.json', 'r') as file:
        content = file.read()
    root.destroy()
    os.system(content + "\MicroMiniNew.exe")
def old_b():
    with open('config.json', 'r') as file:
        content = file.read()
    root.destroy()
    os.system(content+"\MicroMiniNew_.exe")
def e():
    e=entry.get()
    if (e==""):
        tk.messagebox.showwarning(title='保存',message='请写入安装路径')
    else:
        with open('config.json', 'w') as f:
            f.write(e)
root=tk.Tk()
root.iconbitmap('logo.ico')
root.title("迷你启动器")
root.geometry('400x200')
root.resizable(0,0)
w = tk.Label(root, text="第一次启动请填入安装位置,并保存").place(x=3,y=3)
w1 = tk.Label(root, text="默认:C:\用户(Users)\名称\AppData\Roaming\miniworldgameguan110").place(x=0,y=35)
button=tk.Button(root,width=7, height=1,text="新版界面",bg="#FF6347",fg="#FFF5EE",command=b).place(x=335,y=130)
entry=tk.Entry(root,bd=5,width=30)
entry.place(x=3,y=65)
button1=tk.Button(root,width=7, height=1,text="保存",bg="#FF4500",fg="#FFF5EE",activebackground="#556B2F",activeforeground="#FFF5EE",command=e).place(x=235,y=63)
button2=tk.Button(root,width=7, height=1,text="老版界面",bg="#FF6347",fg="#FFF5EE",command=old_b).place(x=335,y=165)
root.mainloop()
