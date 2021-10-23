from tkinter import *
import tkinter.messagebox as messagebox
import Online_sort_part as OL
import LianJi_main_page
import main_page
class loginpage():
    def __init__(self):
        self.root = Tk()
        self.root.title("猪尾巴登录界面")
        self.root.minsize(500, 242)  # 最小尺寸
        self.root.maxsize(500, 242)  # 最大尺寸
        a = self.root.winfo_screenwidth() / 2 - 250
        b = self.root.winfo_screenheight() / 2 - 121
        self.root.geometry('500x242+%d+%d' % (a, b))  # 放置中间
        self.usr_name = StringVar()
        self.usr_pwd = StringVar()
        self.photo = PhotoImage(file="source/background/登陆界面.gif")
        self.on_line()

    def on_line(self):
        Label(self.root, image=self.photo, compound=CENTER).place(x=-2, y=0)
        Label(self.root, text='学号').place(x=150, y=50)
        Entry(self.root, textvariable=self.usr_name).place(x=200, y=50)
        Label(self.root, text='密码').place(x=150, y=100)
        Entry(self.root, textvariable=self.usr_pwd, show='*').place(x=200, y=100)
        Button(self.root, text='登录', command=self.loginCheck).place(x=200, y=140)
        Button(self.root, text='返回',command=self.back).place(x=280, y=140)
        self.root.mainloop()
    def loginCheck(self):
        name = self.usr_name.get()
        pwd = self.usr_pwd.get()
        temp = OL.Login(name,pwd)
        if temp[0]:
            print(1)
            messagebox.showinfo('登陆成功', f"尊敬的{name}用户！\n Welcme to 猪尾巴's world!")
            self.root.destroy()
            LianJi_main_page.Main_page_C("联机",temp[1],name)
            # OLG.Game_page_C('联机PVP')
        else:
            messagebox.showerror('登录失败', '账户或密码错误')
            print(2)

    def back(self):
        self.root.destroy()
        main_page.main_page()

#loginpage()