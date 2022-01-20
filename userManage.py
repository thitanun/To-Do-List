from select import select
from tkinter import *
import tkinter.messagebox
# from tkinter import colorchooser
# from tkinter import filedialog
from tkcalendar import *
from tkcalendar import DateEntry
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



    # @classmethod 
    # def add_user(self):
    #     f = open('user.json')
    #     data = json.load(f)
    #     print(data)
    #     f.close() 
    #     todoMain.MainPage.name_user = []
    #     for v_data in data.values():
    #         for v_vdata in v_data:
    #             print(v_vdata)
    #             user = v_vdata['Username']
    #             todoMain.MainPage.name_user.append(user)
    #     print(todoMain.MainPage.name_user)     
    #     self.click_user = StringVar()
    #     self.click_user.set(todoMain.MainPage.name_user[0])
    #     return self.click_user ,todoMain.MainPage.name_user


    #command back to login page
    @classmethod
    def backtoLogin(self):
        if todoMain.main_page is not None:
            todoMain.main_page.withdraw()
            todoMain.MainPage.menu_user.destroy()
        todoMain.MainPage(todoMain.MainPage(todoMain.main_page))

