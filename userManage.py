from select import select
from tkinter import *
import tkinter.messagebox
from numpy import single
# from tkinter import colorchooser
# from tkinter import filedialog
from tkcalendar import *
from tkcalendar import DateEntry
from PIL import Image,ImageTk
from datetime import *
from datetime import date
import json
import todoMain
import sys
# import os
# from dataManage import showData

class userEdit:
        
    @classmethod 
    def __init__(self):
        pass

    #command for submit button
    @classmethod
    def submitReg(self):
        userregInput = todoMain.MainPage.txt_reguser.get()
        passregInput = todoMain.MainPage.txt_regpass.get()
        passregInputagain = todoMain.MainPage.txt_regpassagain.get()
        if userregInput == "" :
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter Username or")
        elif passregInput == "":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter Password")
        elif passregInputagain == "":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter Confirm Password")
        elif passregInput != passregInputagain:
            tkinter.messagebox.showwarning(title="Warning!",message="Password doesn't match")
        else:
            self.uDict = {'Username': userregInput, 'Password' : passregInput}
            print(self.uDict)        
            with open("user.json") as data:
                data = json.load(data)
                temp = data['User']
                print("temp",temp)
                temp.append(self.uDict)
            with open ("user.json","w") as f:
                json.dump(data,f,indent=4)  
            # self.add_user()
            tkinter.messagebox.showinfo(title="Success",message="Register success") 


    @classmethod
    def cancleLogin(self):
        todoMain.MainPage.log_frame.destroy()
        sys.exit()

    @classmethod
    def cancleReg(self):
        todoMain.MainPage.reg_page.destroy()

    #command for login buton
    @classmethod
    def loginProcess(self):
        self.op = open('user.json')
        self.da = json.load(self.op)
        self.op.close()
        userInt = todoMain.MainPage.txt_loguser.get()
        passInt = todoMain.MainPage.txt_logpass.get()
        yes = 0
        for x in self.da.values():
            for k in x:
                user_inp = k['Username']
                pass_inp = k['Password']
                if userInt == user_inp and passInt == pass_inp:
                    yes =+ 1
        if yes < 1:
            tkinter.messagebox.showwarning(title="Warning!",message="Username or Password is not correct")
        else:
            todoMain.main_page.deiconify()
            todoMain.MainPage.log_frame.withdraw()


    #command back to login page
    @classmethod
    def backtoLogin(self):
        if todoMain.main_page is not None:
            todoMain.main_page.withdraw()
            todoMain.MainPage.menu_user.destroy()
        todoMain.MainPage(todoMain.MainPage(todoMain.main_page))

    @classmethod
    def userWin(self):
        self.userwindow = Toplevel()
        self.userwindow.title("User")
        self.userwindow.geometry("350x385")
        self.userwindow.config(bg='#6fa0c6')

        self.frame_user = Frame(self.userwindow)
        self.frame_user.pack()
        self.frame_user.place(relx=0.03, rely=0.1)
        self.frame_user.config(bg='#6fa0c6')

        #Create scrollbar and listbox of user page
        self.scrollbar_user = Scrollbar(self.frame_user, orient=VERTICAL)
        self.scrollbar_user.pack(side=RIGHT, fill=Y)
        self.listbox_user = Listbox(self.frame_user,bg="#F0FFFF",fg="black",height=11,width=31,font='Calibri',yscrollcommand= self.scrollbar_user.set, selectmode=SINGLE)
        
        self.scrollbar_user.config(command=self.listbox_user.yview)      
        self.listbox_user.pack(pady=15)

        self.lb_myl = Label(self.userwindow, text='USER', bg='#6fa0c6', fg='black', font=('Calibri', 15))
        self.lb_myl.place(relx=0.025, rely=0.03)

        self.bt_deluser = Image.open('todoPic/deleteuser.png')
        self.resize_deluser = self.bt_deluser.resize((115,31),Image.ANTIALIAS)
        self.bt_newdeluser = ImageTk.PhotoImage(self.resize_deluser)
        self.bttn_deluser = Button(self.userwindow, image = self.bt_newdeluser,cursor="heart", bg='#6fa0c6', command = self.confirmDel , borderwidth=0)
        self.bttn_deluser.place(relx=0.65, rely=0.89, width=115, height=30)
        self.showUser()

    @classmethod
    def showUser(self):
        # self.todo = dataManage.dataEdit.User()
        self.f = open('user.json')
        self.data = json.load(self.f)
        for value in self.data.values():
            for i in range(len(value)):
                dictUser = value[i]
                username = dictUser['Username']
                self.listbox_user.insert(i, username)

    @classmethod
    def confirmDel(self):
        if self.listbox_user.curselection():
            self.condel = Toplevel()
            self.condel.title("Confirm Delete?")
            self.condel.geometry("350x150")
            self.condel.config(bg="#6fa0c6")

            self.txt = StringVar(self.condel)

            self.old_List = Entry(self.condel, show="*", textvariable=self.txt)
            self.old_List.place(relx=0.1, rely=0.35, height=30, width=283)
        
            self.lb_condel = Label(self.condel, text='ENTER PASSWORD', font=('Calibri', 14))
            self.lb_condel.place(relx=0.295, rely=0.1)
            self.lb_condel.config(bg="#6fa0c6")

            self.bt_confirm = Image.open('todoPic/confirm.png')
            self.resize_confirm = self.bt_confirm.resize((95,31),Image.ANTIALIAS)
            self.bt_newconfirm = ImageTk.PhotoImage(self.resize_confirm)
            self.bttn_confirm = Button(self.condel, image = self.bt_newconfirm,cursor="heart", bg='#6fa0c6', command = self.deleteUser , borderwidth=0)
            self.bttn_confirm.place(relx=0.23, rely=0.67, width=95, height=30)

            self.bt_cancle = Image.open('todoPic/cancle_2.png')
            self.resize_cancle = self.bt_cancle.resize((95,31),Image.ANTIALIAS)
            self.bt_newcancle = ImageTk.PhotoImage(self.resize_cancle)
            self.bttn_cancle = Button(self.condel, image = self.bt_newcancle,cursor="heart", bg='#6fa0c6', command = self.notDel_user , borderwidth=0)
            self.bttn_cancle.place(relx=0.52, rely=0.67, width=95, height=30)
        else:
            tkinter.messagebox.showwarning(title="Warning!",message="Please Select User")

    @classmethod
    def notDel_user(self):
        self.condel.destroy()

    @classmethod
    def deleteUser(self):
        password = self.txt.get()
        list_user = []
        c = -1
        list_index = []
        yes = 0

        self.f = open('user.json')
        self.data = json.load(self.f)

        for x in self.data.values():
            for k in x:
                user_inp = k['Username']
                pass_inp = k['Password']
                for p in reversed(self.listbox_user.curselection()):
                    userInt = self.listbox_user.get(p)
                    if userInt == user_inp and password == pass_inp:
                        yes =+ 1
                        for index in reversed(self.listbox_user.curselection()):
                            userName = self.listbox_user.get(index)
                            list_user.append(userName)
                            self.listbox_user.delete(index)

                        for key,value in self.data.items():
                            for j in list_user:
                                for i in range(len(value)):
                                    c = c + 1
                                    dict_user = value[i]
                                    if dict_user['Username'] == j:
                                        list_index.append(c)
                            for k in list_index:
                                del value[k]
                        self.data["User"] = value
        
                        jsonString = json.dumps(self.data)    
                        jsonFile = open("user.json", "w")
                        jsonFile.write(jsonString)
                        jsonFile.close()

                        self.f = open('bin.json')
                        self.databin = json.load(self.f)

                        self.f = open('complete.json')
                        self.datacom = json.load(self.f)

                        self.f = open('data.json')
                        self.data_data = json.load(self.f)

                        for m in list_user:
                            if m in self.databin.keys():
                                del self.databin[m]

                            if m in self.datacom.keys():
                                del self.datacom[m]

                            if m in self.data_data.keys():
                                del self.data_data[m]

                        jsonString = json.dumps(self.databin)    
                        jsonFile = open("bin.json", "w")
                        jsonFile.write(jsonString)
                        jsonFile.close()

                        jsonString = json.dumps(self.datacom)    
                        jsonFile = open("complete.json", "w")
                        jsonFile.write(jsonString)
                        jsonFile.close()

                        jsonString = json.dumps(self.data_data)    
                        jsonFile = open("data.json", "w")
                        jsonFile.write(jsonString)
                        jsonFile.close()
                        self.condel.destroy()
        if yes < 1:
            tkinter.messagebox.showwarning(title="Warning!",message="Password is not correct")
            self.condel.destroy()

