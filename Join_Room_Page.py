from tkinter import *
import tkinter.messagebox as messagebox
import Online_sort_part as OL
import On_Line_Game_page as OLG
import LianJi_main_page

class Join_page():
    def __init__(self,header,name):
        self.root = Tk()
        self.root.title("猪尾巴加入房间")
        self.root.minsize(500, 242)  # 最小尺寸
        self.root.maxsize(500, 242)  # 最大尺寸
        a = self.root.winfo_screenwidth() / 2 - 250
        b = self.root.winfo_screenheight() / 2 - 121
        self.root.geometry('500x242+%d+%d' % (a, b))  # 放置中间
        self.uuid = StringVar()
        self.name = name
        self.photo = PhotoImage(file="source/background/登陆界面.gif")
        self.header = header
        self.Join_Room()

    def Join_Room(self):
        Label(self.root, image=self.photo, compound=CENTER).place(x=-2, y=0)
        Label(self.root, text='房间号：').place(x=130, y=50)
        Entry(self.root, textvariable=self.uuid).place(x=200, y=50)
        Button(self.root, text='加入', command=self.insert).place(x=200, y=140)
        Button(self.root, text='返回',command=self.back).place(x=280, y=140)
        self.root.mainloop()
    def insert(self):
        uuid = self.uuid.get()
        temp = OL.Join_Game(uuid,self.header)
        if temp:
            messagebox.showinfo('加入成功', f"尊敬的{self.name}用户！\n Welcme to {uuid}")
            self.root.destroy()
            OLG.Game_page_C('联机PVP',uuid,self.name,self.header,1)
        else:
            messagebox.showerror('加入失败', '对局不存在')
            print(2)
    def back(self):
        self.root.destroy()
        LianJi_main_page.Main_page_C("联机", self.header, self.name)

