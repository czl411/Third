from tkinter import *
import tkinter.messagebox as messagebox
import Online_sort_part as OL
import On_Line_Game_page as OLG
import LianJi_main_page

class Creat_Room_page():
    def __init__(self,header,name):
        self.root = Tk()
        self.root.title("猪尾巴创建房间")
        self.root.minsize(500, 242)  # 最小尺寸
        self.root.maxsize(500, 242)  # 最大尺寸
        a = self.root.winfo_screenwidth() / 2 - 250
        b = self.root.winfo_screenheight() / 2 - 121
        self.root.geometry('500x242+%d+%d' % (a, b))  # 放置中间
        self.attribute = StringVar()
        self.photo = PhotoImage(file="source/background/登陆界面.gif")
        self.name = name
        self.header = header
        self.creat_page()

    def creat_page(self):
        Label(self.root, image=self.photo, compound=CENTER).place(x=-2, y=0)
        Label(self.root, text='房间属性：').place(x=100, y=50)
        Entry(self.root, textvariable=self.attribute).place(x=200, y=50)
        Button(self.root, text='创建', command=self.Creat_Room).place(x=200, y=140)
        Button(self.root, text='返回',command=self.back).place(x=280, y=140)
        self.root.mainloop()

    def Creat_Room(self):
        if self.attribute.get() == 'c':
            status = True
        else:
            status = False
        self.attribute = {
            "private": status
        }
        self.uuid = OL.C_Game(self.header,self.attribute)
        print(self.uuid)
        if status == True:
            messagebox.showinfo('创建私人房间成功', f"房间号：{self.uuid}")
            self.root.destroy()
            OLG.Game_page_C("联机PVP", self.uuid,self.name,self.header,0)
        else:
            messagebox.showinfo('创建公开房间成功', f"房间号：{self.uuid}")
            self.root.destroy()
            OLG.Game_page_C("联机PVP", self.uuid, self.name,self.header,0)

    def back(self):
        self.root.destroy()
        LianJi_main_page.Main_page_C("联机", self.header, self.name)


