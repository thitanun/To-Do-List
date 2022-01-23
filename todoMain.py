from select import select
from tkinter import *
import tkinter.messagebox
from tkinter import colorchooser
from tkinter import filedialog
from tkcalendar import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import *
from datetime import date
from PIL import Image,ImageTk
import json
import dataManage
import userManage
import statManage
# import sys
# from dataManage import showData
from itertools import repeat, chain
import os


class MainPage:

    @classmethod
    # def __init__(self,main_page,dataManage):
    def __init__(self,main_page):

        # self.log_frame = Toplevel()
        #Create frame 
        self.my_frame = Frame(main_page)
        self.my_frame.pack()        
        self.my_frame.place(relx=0.03, rely=0.1)
        self.my_frame.config(bg='#6fa0c6')

        self.log_frame = Toplevel()
        self.log_frame.geometry("350x380")
        self.log_frame.title("Login")
        self.log_frame.config(bg='#6fa0c6')

        #Label in login window
        self.lb_user = Label(self.log_frame, text='Username', bg='#6fa0c6', fg='#FBE7A1', font=('Calibri', 15, 'bold'))
        self.lb_user.place(relx=0.13, rely=0.08)

        self.lb_pass = Label(self.log_frame, text='Password', bg='#6fa0c6', fg='#FBE7A1', font=('Calibri', 15, 'bold'))
        self.lb_pass.place(relx=0.13, rely=0.28)

        #Button in login window
        self.button_logPic = Image.open('todoPic/login.png')
        self.resize_logBut = self.button_logPic.resize((110,50),Image.ANTIALIAS)
        self.button_newlog = ImageTk.PhotoImage(self.resize_logBut)
        self.bttn_log = Button(self.log_frame,image = self.button_newlog,cursor="heart", bg='#6fa0c6', command = userManage.userEdit.loginProcess , borderwidth=0)
        self.bttn_log.place(relx=0.35, rely=0.49, width=110, height=50)

        self.button_cloPic = Image.open('todoPic/cancle.png')
        self.resize_cloBut = self.button_cloPic.resize((110,50),Image.ANTIALIAS)
        self.button_newclo = ImageTk.PhotoImage(self.resize_cloBut)
        self.bttn_clo = Button(self.log_frame,image = self.button_newclo,cursor="heart", bg='#6fa0c6', command = userManage.userEdit.cancleLogin , borderwidth=0)
        self.bttn_clo.place(relx=0.35, rely=0.66, width=110, height=50)

        self.button_regPic = Image.open('todoPic/register.png')
        self.resize_regBut = self.button_regPic.resize((110,50),Image.ANTIALIAS)
        self.button_newreg = ImageTk.PhotoImage(self.resize_regBut)
        self.bttn_reg = Button(self.log_frame,image = self.button_newreg,cursor="heart", bg='#6fa0c6', command = self.registerUser , borderwidth=0)
        self.bttn_reg.place(relx=0.35, rely=0.83, width=110, height=50)


        #Entry in login window
        self.txt_loguser = StringVar(self.log_frame)
        self.ent_user = Entry(self.log_frame, textvariable=self.txt_loguser)
        self.ent_user.place(relx=0.12, rely=0.16, width=265, height=32)

        self.txt_logpass = StringVar(self.log_frame)
        self.ent_pass = Entry(self.log_frame, show="*", textvariable=self.txt_logpass)
        self.ent_pass.place(relx=0.12, rely=0.36, width=265, height=32)

        #Create scrollbar and listbox
        self.my_scrollbar = Scrollbar(self.my_frame, orient = VERTICAL)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)
        # self.xscrollbar = Scrollbar(self.my_frame, orient = HORIZONTAL)
        # self.xscrollbar.pack(side = BOTTOM, fill = X)
        #, xscrollcommand = self.xscrollbar.set
        self.listbox_list = Listbox(self.my_frame,bg="#F0FFFF",fg="black",height=9,width=50,font='Calibri',yscrollcommand= self.my_scrollbar.set, selectmode=MULTIPLE)
        
        self.my_scrollbar.config(command=self.listbox_list.yview)
        # self.xscrollbar.config(command=self.listbox_list.xview)
        #self.listbox_list.place(relx=0.03, rely=0.233)        
        self.listbox_list.pack(pady=15)
        
        #Button in window, bg='#6fa0c6'
        self.bt_today = Image.open('todoPic/today.png')
        self.resize_regtoday = self.bt_today.resize((150,100),Image.ANTIALIAS)
        self.bt_newtoday = ImageTk.PhotoImage(self.resize_regtoday)
        self.bttn_today = Button(main_page,image = self.bt_newtoday,cursor="heart", bg='#6fa0c6', command = dataManage.dataEdit.today_list , borderwidth=0)
        self.bttn_today.place(relx=0.35, rely=0.05, width=100, height=40)

        self.bt_markdone = Image.open('todoPic/markasdone.png')
        self.resize_markdone = self.bt_markdone.resize((43,34),Image.ANTIALIAS)
        self.bt_newmarkdone = ImageTk.PhotoImage(self.resize_markdone)
        self.bttn_markdone = Button(main_page,image = self.bt_newmarkdone,cursor="heart", bg='#6fa0c6', command = self.markdone , borderwidth=0)
        self.bttn_markdone.place(relx=0.88, rely=0.05, width=43, height=34)

        self.bt_unmark = Image.open('todoPic/unmark.png')
        self.resize_unmark = self.bt_unmark.resize((43,34),Image.ANTIALIAS)
        self.bt_newunmark = ImageTk.PhotoImage(self.resize_unmark)
        self.bttn_unmark = Button(main_page,image = self.bt_newunmark,cursor="heart", bg='#6fa0c6', command = self.unmark , borderwidth=0)
        self.bttn_unmark.place(relx=0.77, rely=0.05, width=43, height=34)

        self.bt_delete = Image.open('todoPic/deletelist.png')
        self.resize_delete = self.bt_delete.resize((85,31),Image.ANTIALIAS)
        self.bt_newdelete = ImageTk.PhotoImage(self.resize_delete)
        self.bttn_delete = Button(main_page,image = self.bt_newdelete,cursor="heart", bg='#6fa0c6', command = dataManage.dataEdit.makeSure , borderwidth=0)
        self.bttn_delete.place(relx=0.025, rely=0.51, width=85, height=30)

        self.bt_deleteAll = Image.open('todoPic/deleteall.png')
        self.resize_deleteAll = self.bt_deleteAll.resize((85,31),Image.ANTIALIAS)
        self.bt_newdeleteAll = ImageTk.PhotoImage(self.resize_deleteAll)
        self.bttn_deleteAll = Button(main_page,image = self.bt_newdeleteAll,cursor="heart", bg='#6fa0c6', command = dataManage.dataEdit.makeallSure , borderwidth=0)
        self.bttn_deleteAll.place(relx=0.22, rely=0.51, width=85, height=30)

        self.bt_edit = Image.open('todoPic/edit.png')
        self.resize_edit = self.bt_edit.resize((90,31),Image.ANTIALIAS)
        self.bt_newedit = ImageTk.PhotoImage(self.resize_edit)
        self.bttn_edit = Button(main_page,image = self.bt_newedit,cursor="heart", bg='#6fa0c6', command = dataManage.dataEdit.changeWindow , borderwidth=0)
        self.bttn_edit.place(relx=0.595, rely=0.51, width=90, height=30)

        self.bt_newlist = Image.open('todoPic/newlist.png')
        self.resize_newlist = self.bt_newlist.resize((90,31),Image.ANTIALIAS)
        self.bt_newnlist = ImageTk.PhotoImage(self.resize_newlist)
        self.bttn_newlist = Button(main_page,image = self.bt_newnlist,cursor="heart", bg='#6fa0c6', command = dataManage.dataEdit.Addlist , borderwidth=0)
        self.bttn_newlist.place(relx=0.79, rely=0.51, width=90, height=30)

        self.bt_sort= Image.open('todoPic/sort.png')
        self.resize_sort = self.bt_sort.resize((80,31),Image.ANTIALIAS)
        self.bt_newsort = ImageTk.PhotoImage(self.resize_sort)
        self.bttn_sort = Button(main_page,image = self.bt_newsort,cursor="heart", bg='#6fa0c6', command = dataManage.dataEdit.sort_list , borderwidth=0)
        self.bttn_sort.place(relx=0.415, rely=0.51, width=80, height=30)

        self.bt_bin= Image.open('todoPic/bin.png')
        self.resize_bin = self.bt_bin.resize((40,31),Image.ANTIALIAS)
        self.bt_newbin = ImageTk.PhotoImage(self.resize_bin)
        self.bttn_bin = Button(main_page,image = self.bt_newbin,cursor="heart", bg='#6fa0c6', command = dataManage.dataEdit.windowBin , borderwidth=0)
        self.bttn_bin.place(relx=0.89, rely=0.93, width=40, height=30)

        self.bt_clear= Image.open('todoPic/clear.png')
        self.resize_clear = self.bt_clear.resize((80,31),Image.ANTIALIAS)
        self.bt_newclear = ImageTk.PhotoImage(self.resize_clear)
        self.bttn_clear = Button(main_page,image = self.bt_newclear,cursor="heart", bg='#6fa0c6', command = dataManage.dataEdit.clearAll , borderwidth=0)
        self.bttn_clear.place(relx=0.72, rely=0.93, width=80, height=30)

        self.bt_graph= Image.open('todoPic/graph.png')
        self.resize_graph = self.bt_graph.resize((43,34),Image.ANTIALIAS)
        self.bt_newgraph = ImageTk.PhotoImage(self.resize_graph)
        self.bttn_graph = Button(main_page,image = self.bt_newgraph,cursor="heart", bg='#6fa0c6', command = statManage.statEdit , borderwidth=0)
        self.bttn_graph.place(relx=0.55, rely=0.05, width=43, height=34)

        '''self.bt_markdone = Button(main_page,text='Complete',font=('Calibri', 10),relief=RAISED,cursor="heart", command = self.showComplete)  
        self.bt_markdone.place(relx=0.78, rely=0.09, width=85, height=32)'''


        #Label in window
        self.lb_myl = Label(main_page, text='My Lists', bg='#6fa0c6', fg='black', font=('Calibri', 35))
        self.lb_myl.place(relx=0.025, rely=0.02)

        self.listbox_list.bind('<Double-1>', lambda event :dataManage.dataEdit.changeWindow())
        self.listbox_list.pack()
        
        #Create frame complete
        self.frame_comp = Frame(main_page)
        self.frame_comp.pack()
        self.frame_comp.place(relx=0.03, rely=0.59)
        self.frame_comp.config(bg='#6fa0c6')
        # self.frame_comp.place(relx=0.03, rely=0.55)

        #Create scrollbar and listbox of complete page
        self.scrollbar_comp = Scrollbar(self.frame_comp, orient=VERTICAL)
        self.scrollbar_comp.pack(side=RIGHT, fill=Y)
        self.listbox_complete = Listbox(self.frame_comp,bg="#F0FFFF",fg="black",height=7,width=50,font='Calibri',yscrollcommand= self.scrollbar_comp.set, selectmode=MULTIPLE)
        
        self.scrollbar_comp.config(command=self.listbox_complete.yview)      
        self.listbox_complete.pack(pady=15)

        self.lb_myl = Label(main_page, text='COMPLETE', bg='#6fa0c6', fg='black', font=('Calibri', 15))
        self.lb_myl.place(relx=0.025, rely=0.56)

        # sd = dataManage.dataEdit.showdata()

        menubar = Menu(main_page)
        filemenu = Menu(menubar, tearoff=0)
        # logoutmenu = Menu(menubar, tearoff=0)
        # filemenu.add_command(label="New",command=self.Addlist)
        # filemenu.add_command(label="Save",command=dataManage.dataEdit.save_list)
        filemenu.add_command(label="Save", command= self.save_list)
        filemenu.add_command(label="Open", command= self.open_file)
        filemenu.add_command(label="User", command = userManage.userEdit.userWin)
        filemenu.add_command(label="Logout", command = userManage.userEdit.backtoLogin)
        menubar.add_cascade(label="File",menu=filemenu)
        # menubar.add_cascade(label="Logout",menu=logoutmenu, command = dataManage.dataEdit.save_list)
        main_page.config(menu = menubar)

        #Dropdown menu
        # self.click,self.name_user = userManage.userEdit.add_user()
        # self.menu_user = OptionMenu(main_page, self.click, *self.name_user)
        # self.menu_user.pack()

        self.name_user = ['user']
        self.click = StringVar(main_page)
        self.click.set(self.name_user[0])
        # self.click.trace('w', self.name_user)
        # self.click, self.name_user = self.add_user
        self.menu_user = OptionMenu(main_page,self.click, self.name_user)
        self.menu_user.place(relx=0.81, rely=0.000005,height=25, width=80)
        self.menu_user.config(bg="#b95c5c", fg="#eeddd4", font=('Calibri', 13))


        self.bt_re= Image.open('todoPic/refresh.png')
        self.resize_re = self.bt_re.resize((43,34),Image.ANTIALIAS)
        self.bt_newre = ImageTk.PhotoImage(self.resize_re)
        self.bttn_re = Button(main_page,image = self.bt_newre,cursor="heart", bg='#6fa0c6', command = self.refresh , borderwidth=0)
        self.bttn_re.place(relx=0.66, rely=0.05, width=43, height=34)

    # def add_user(self):
        # self.name_user = ['user']
        # self.click = StringVar(main_page)
        # self.click.set(self.name_user[0])
        # self.click.trace('w', self.name_user)
        
        # return self.click , self.name_user

    @classmethod    
    def refresh(self):
        menu = self.menu_user["menu"]
        menu.delete(0, "end")
        f = open('user.json')
        data = json.load(f)
        f.close()
        self.name_user = []
        for v_data in data.values():
            for v_vdata in v_data:
                user = v_vdata['Username']
                self.name_user.append(user)       
        for string in self.name_user:
            menu.add_command(label=string,command=lambda value=string: self.click.set(value))
        self.listbox_list.delete(0,END)
        self.showData()
        self.listbox_complete.delete(0,END)
        self.showComplete()

            
    @classmethod
    def markdone(self):
        #dataManage.dataEdit.create_completejson()
        self.todo = dataManage.dataEdit.User()
        aDict = {}
        self.com = open('complete.json')
        self.datacomp = json.load(self.com)

        self.f = open('data.json')
        self.data = json.load(self.f)

        if self.todo in self.datacomp.keys():
            for a,b in self.datacomp.items():
                if self.todo == a:
                    index = []
                    value = []
                    for marked in reversed(self.listbox_list.curselection()):
                        temp_marked = self.listbox_list.get(marked)
                        temp_marked = temp_marked + " DONE ✔"
                        b.append(temp_marked)
                        self.datacomp[self.todo] = b
                        self.listbox_list.delete(marked)
                        self.listbox_complete.insert(marked, temp_marked)
                        index.append(marked)

                    for c,d in self.data.items():
                        if self.todo == c:
                            for i in index:
                                value.append(d[i])
                            for j in value:
                                d.remove(j)
                            self.data[self.todo] = d

                            jsonString = json.dumps(self.data)    
                            jsonFile = open("data.json", "w")
                            jsonFile.write(jsonString)
                            jsonFile.close()    

                    jsonString = json.dumps(self.datacomp)    
                    jsonFile = open("complete.json", "w")
                    jsonFile.write(jsonString)
                    jsonFile.close()
        else:
            clist = []
            index = []
            value = []
            for marked in reversed(self.listbox_list.curselection()):
                temp_marked = self.listbox_list.get(marked)
                temp_marked = temp_marked + " DONE ✔"
                clist.append(temp_marked)
                self.listbox_list.delete(marked)
                self.listbox_complete.insert(marked, temp_marked)
                index.append(marked)

            for c,d in self.data.items():
                if self.todo == c:
                    for i in index:
                        value.append(d[i])
                    for j in value:
                        d.remove(j)
                    self.data[self.todo] = d

                    jsonString = json.dumps(self.data)    
                    jsonFile = open("data.json", "w")
                    jsonFile.write(jsonString)
                    jsonFile.close()    

            self.datacomp[self.todo] = clist
            jsonString = json.dumps(self.datacomp)    
            jsonFile = open("complete.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()

        self.listbox_complete.delete(0,END)
        m.showComplete()


    @classmethod
    def unmark(self):
        r = []
        self.todo = dataManage.dataEdit.User()
        self.f = open('data.json')
        self.data = json.load(self.f)

        self.comp = open('complete.json')
        self.datacomp = json.load(self.comp)

        for a,b in self.data.items():
            if self.todo == a:
                for marked in reversed(self.listbox_complete.curselection()):
                    temp_marked = self.listbox_complete.get(marked)
                    temp_marked = temp_marked.strip(" DONE ✔")
                    r.append(marked)

                    x = str(temp_marked).split(", ")
                    listName = x[0]
                    y = x[1].split(" ")
                    z = y[1].split(":")
                    Date = y[0]
                    hour = z[0]
                    minutes = z[1]
                    seconds = z[2]
                    unmarkDict = {'List Name': listName, 'Date' : Date, 'hour' : hour, 'minutes' : minutes, 'seconds' : seconds}
                    print(unmarkDict)
                    b.append(unmarkDict)
                    self.listbox_complete.delete(marked)
                    self.listbox_list.insert(END, temp_marked)
                
                for c,k in self.datacomp.items():
                    if self.todo == c:
                        for j in r:
                            k.remove(k[j])
                        self.datacomp[self.todo] = k

                self.data[self.todo] = b
                jsonString = json.dumps(self.data)    
                jsonFile = open("data.json", "w")
                jsonFile.write(jsonString)
                jsonFile.close()
                
                jsonString = json.dumps(self.datacomp)    
                jsonFile = open("complete.json", "w")
                jsonFile.write(jsonString)
                jsonFile.close()

        self.listbox_complete.delete(0,END)
        m.showComplete()



    @classmethod
    def showComplete(self):
        c = -1
        #self.listbox_list.delete(0,END)
        self.todo = dataManage.dataEdit.User()
        self.f = open('complete.json')
        self.datacom = json.load(self.f)
        if self.datacom:
            for a,b in self.datacom.items():
                if self.todo == a:
                    for v in b:
                        c = c + 1
                        self.listbox_complete.insert(c, v)
        # c = -1
        # if datacom:
        #     for a in datacom:
        #         # print('a',a)
        #         if todo == a:
        #                 c = c + 1

    @classmethod
    # เเสดงข้อมูลจากไฟล์ data.json ขึ้น GUI
    def showData(self):
        self.todo = dataManage.dataEdit.User()
        self.f = open('data.json')
        self.data = json.load(self.f)
        for a,b in self.data.items():
            if self.todo == a:
                for c in range(len(b)):
                    status = ''
                    j = -1
                    ID = b[c]
                    ListName = ID['List Name']
                    Date = ID['Date']
                    hour = ID['hour']
                    minutes = ID['minutes']
                    seconds = ID['seconds']
                    
                    for i in ID.keys():
                        j = j + 1
                        if j > 4:
                            status = status + str(ID[i])
                            print('status')

                    Data = ListName + ', ' + Date + " "+ hour +":"+ minutes +":"+ seconds + status
                    self.listbox_list.insert(c, Data)
                    status = ''
        


    @classmethod
    #Create register
    def registerUser(self):

        # login_page.destroy()
        self.reg_page = Toplevel()
        self.reg_page.title("Register User")
        self.reg_page.geometry("350x380")
        self.reg_page.config(bg='#6fa0c6')

        #Label in window
        self.lb_regu = Label(self.reg_page, text='Username', bg='#6fa0c6', fg='#FBE7A1', font=('Calibri', 15, 'bold'))
        self.lb_regu.place(relx=0.13, rely=0.08)

        self.lb_regp = Label(self.reg_page, text='Password', bg='#6fa0c6', fg='#FBE7A1', font=('Calibri', 15, 'bold'))
        self.lb_regp.place(relx=0.13, rely=0.28)

        self.lb_regpagain = Label(self.reg_page, text='Confirm Password', bg='#6fa0c6', fg='#FBE7A1', font=('Calibri', 15, 'bold'))
        self.lb_regpagain.place(relx=0.13, rely=0.48)

        #Button in window
        self.button_submit = Image.open('todoPic/register.png')
        self.resize_submit = self.button_submit.resize((110,50),Image.ANTIALIAS)
        self.button_newsubmit = ImageTk.PhotoImage(self.resize_submit)
        self.bttn_submit = Button(self.reg_page, image = self.button_newsubmit, cursor="heart", bg='#6fa0c6', command = userManage.userEdit.submitReg ,borderwidth=0)
        self.bttn_submit.place(relx=0.35, rely=0.68, width=110, height=50)

        self.button_cancle = Image.open('todoPic/cancle.png')
        self.resize_cancle = self.button_cancle.resize((110,50),Image.ANTIALIAS)
        self.button_newcancle = ImageTk.PhotoImage(self.resize_cancle)
        self.bttn_cancle = Button(self.reg_page,image = self.button_newcancle,cursor="heart", bg='#6fa0c6', command = userManage.userEdit.cancleReg , borderwidth=0)
        self.bttn_cancle.place(relx=0.35, rely=0.84, width=110, height=50)

        # self.bttn_submit = Button(self.reg_page,text='Register',font=('Calibri', 10),relief=RAISED,cursor="heart", command = userManage.userEdit.submitReg)
        # self.bttn_submit.place(relx=0.42, rely=0.70, width=60, height=32)
        # self.bttn_cancle = Button(self.reg_page,text='Cancel',font=('Calibri', 10),relief=RAISED,cursor="heart", command = userManage.userEdit.cancleReg)
        # self.bttn_cancle.place(relx=0.42, rely=0.86, width=60, height=32)

        #Entry in window
        self.txt_reguser = StringVar(self.reg_page)
        self.ent_reguser = Entry(self.reg_page, textvariable=self.txt_reguser)
        self.ent_reguser.place(relx=0.12, rely=0.16, width=265, height=32)

        self.txt_regpass = StringVar(self.reg_page)
        self.ent_regpass = Entry(self.reg_page, show="*", textvariable=self.txt_regpass)
        self.ent_regpass.place(relx=0.12, rely=0.36, width=265, height=32)

        self.txt_regpassagain = StringVar(self.reg_page)
        self.ent_regpassagain = Entry(self.reg_page, show="*", textvariable=self.txt_regpassagain)
        self.ent_regpassagain.place(relx=0.12, rely=0.56, width=265, height=32)

        self.reg_page.mainloop()


    @classmethod
    def save_list(self):
        self.todo = dataManage.dataEdit.User()
        file = filedialog.asksaveasfile(defaultextension='.txt',filetypes=[("Json file",".json"),("Text file",".txt"),("All file",".*")])
        self.f = open('data.json')
        self.data = json.load(self.f)
        print(self.data)
        for v in self.data.keys():
            if v == self.todo:
                jsonString = json.dumps(self.data[v])
                self.f.close()       
                file.write(jsonString)
        file.close()
    
    @classmethod
    def open_file(self):
        self.todo = dataManage.dataEdit.User()
        filename = filedialog.askopenfilename(defaultextension='.json',filetypes=[("Json file",".json"),("Text file",".txt"),("All file",".*")])
        print(filename)
        name = os.path.split(filename)[1]
        print(type(name))
        file = open(filename)            
        self.data = file.read()
        file.close()
        jsonfile = json.loads(self.data)
        with open ("data.json") as data:
            data = json.load(data)
            for key in data.keys():
                temp = data[key]
                # print('temp',temp)
                if key == self.todo:
                    for value in jsonfile:
                        print(value)
                        temp.append(value)
        with open ("data.json","w") as f:
            json.dump(data,f,indent=4)               
        self.showData()
            

#size of window
main_page = Tk()
main_page.title("To-Do List")
main_page.geometry("540x620")
main_page.config(bg='#6fa0c6')
m = MainPage(main_page)
# l = MainPage(login_page)
m.showData()
m.showComplete()
main_page.withdraw()
main_page.mainloop()