#from select import select
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from tkcalendar import *
from tkcalendar import DateEntry
from datetime import *
import json
import todoMain
# from todoMain import m 

class dataEdit:
    @classmethod 
    def __init__(self):
        pass

    @classmethod
    def User(self):
        self.user = todoMain.MainPage.click.get()
        # self.user = 'yok'
        return self.user

    @classmethod 
    def changeWindow(self):

        for i in reversed(todoMain.MainPage.listbox_list.curselection()):
            aList = todoMain.MainPage.listbox_list.get(i)
            x = str(aList).split(",")
            self.oldList = x[0]

        self.editWin = Tk()
        self.editWin.title("Edit")
        self.editWin.geometry("500x350")
        
        self.lb_editWin = Label(self.editWin, text='Reminder', font=('Calibri', 14))
        self.lb_editWin.place(relx=0.02, rely=0.03)

        self.newtxt = StringVar(self.editWin)

        self.old_List = Entry(self.editWin, textvariable=self.newtxt)
        self.old_List.place(relx=0.18, rely=0.03, height=30, width=330)
        self.newtxt.set(self.oldList)
      
        self.newcal = Calendar(self.editWin, date_pattern = "dd/mm/y")
        self.newcal.place(relx=0.25, rely=0.18)

        self.newspinhour = Spinbox(self.editWin, from_= 0, to = 24)
        self.newspinhour.place(relx=0.38, rely=0.8, height=20, width=30)
        
        self.newspinminutes = Spinbox(self.editWin, from_= 0, to = 59)
        self.newspinminutes.place(relx=0.45, rely=0.8, height=20, width=30)

        self.newspinseconds = Spinbox(self.editWin, from_= 0, to = 59)
        self.newspinseconds.place(relx=0.52, rely=0.8, height=20, width=30)

        self.bt_addEdit = Button(self.editWin,text='Edit',font=('Calibri', 15),relief=RAISED,cursor="heart", command=self.editList)
        self.bt_addEdit.place(relx=0.85, rely=0.03, width=60, height=28)

        self.editWin.mainloop()


    @classmethod 
    def clearAll(self):
        #self.sureallWin.destroy()
        self.todo = self.User()
        self.fp = open('complete.json')
        self.datacom = json.load(self.fp)

        r = []
        vBin = []
        self.bin = open('bin.json')
        self.databin = json.load(self.bin)

        if self.todo in self.datacom.keys():
            for p,q in self.datacom.items():
                if self.todo == p:
                    for d in q:
                        r.append(d)
                    for e in r:
                        q.remove(e)
                    self.datacom[self.todo] = q
                    #print('datacom',self.datacom)

        for v in r:
            print('v',v)
            x = str(v).split(", ")
            listName = x[0]
            y = x[1].split(" ")
            z = y[1].split(":")
            Date = y[0]
            hour = z[0]
            minutes = z[1]
            seconds = z[2]
            vBin.append({'List Name': listName, 'Date' : Date, 'hour' : hour, 'minutes' : minutes, 'seconds' : seconds, 'complete' : " DONE \u2714"})
            #print('vbin',vBin)

        if self.databin:
            for a,b in self.databin.items():
                if self.todo == a:
                    for c in vBin:
                        b.append(c)
            self.databin[self.todo] = b
        else:
            self.databin[self.todo] = vBin 

        binString = json.dumps(self.databin)
        binFile = open("bin.json", "w")
        binFile.write(binString)
        binFile.close()
        self.bin.close()

        todoMain.MainPage.listbox_complete.delete(0, END)
        jsonString = json.dumps(self.datacom)
        jsonFile = open("complete.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()


    @classmethod
    def editList(self):
        self.todo = self.User()
        newList = self.newtxt.get()
        newDate = self.newcal.get_date()           
        newHour = self.newspinhour.get()  
        newMinute = self.newspinminutes.get()
        newSecond = self.newspinseconds.get()
        if newList == "" :
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter Reminder")
        elif int(newMinute) > 59 or int(newMinute) < 0 or int(newSecond) > 59 or int(newSecond) < 0 or int(newHour) < 0 or int(newHour) > 23:
            tkinter.messagebox.showwarning(title="Warning!",message="Please enter the correct time")
        else:
            if int(newHour) < 10:
                newHour = '0' + newHour
        
            if int(newMinute) < 10:
                newMinute = '0' + newMinute
            
            if int(newSecond) < 10:
                newSecond = '0' + newSecond

            #r = []
            self.f = open('data.json')
            self.data = json.load(self.f)
            # print(self.data)
            for v,a in self.data.items():
                #r.append(v)
                if self.todo == v:
                    dList = a
                    #print('dlist=',dList)
            #print('r=',r)
            for item in reversed(todoMain.MainPage.listbox_list.curselection()):
                #print('item',item)
                #print('dList[item]=',dList[item])
                '''dList.remove(dList[item])
                print('remove dList=',dList)'''
                #dList.append({'List Name': newList, 'Date' : newDate, 'hour' : newHour, 'minutes' : newMinute, 'seconds' : newSecond})
                dList[item] = {'List Name': newList, 'Date' : newDate, 'hour' : newHour, 'minutes' : newMinute, 'seconds' : newSecond}
                print('add dList=',dList)
                self.data[self.todo] = dList
                print('self.data=',self.data)

                todoMain.MainPage.listbox_list.delete(item)
                todoMain.MainPage.listbox_list.insert(item, newList +", "+ newDate + " "+ newHour+":"+ newMinute +":"+ newSecond)

                jsonString = json.dumps(self.data)
                jsonFile = open("data.json", "w")
                jsonFile.write(jsonString)
                jsonFile.close()
            self.editWin.destroy()


    @classmethod
    # #delete list in my list box
    def deleteList(self):
        self.sureWin.destroy()
        # if tkinter.messagebox.askquestion(title="Warning!",message="Please Enter Reminder") == True:
        self.selected = todoMain.MainPage.listbox_list.curselection()
        r = []
        dictBin = {}
        self.todo = self.User()
        self.f = open('data.json')
        self.data = json.load(self.f)

        self.fp = open('bin.json')
        self.databin = json.load(self.fp)
        print(self.databin)

        for v,a in self.data.items():
            if self.todo == v:
                dList = a
                #print('dList=',dList)
        for item in reversed(todoMain.MainPage.listbox_list.curselection()):
            r.append(dList[item])
            todoMain.MainPage.listbox_list.delete(item)

        for i in r:
            dList.remove(i)
        self.data[self.todo] = dList

        if self.todo in self.databin.keys():
            for b,c in self.databin.items():
                #print('b',b)
                #print('c',c)
                if self.todo == b:
                    for j in r:
                        #print('j',j)
                        c.append(j)
                self.databin[self.todo] = c
        else:
            self.databin[self.todo] = r
            
        binString = json.dumps(self.databin)
        binFile = open("bin.json", "w")
        binFile.write(binString)
        binFile.close()

        #print(self.data)
        jsonString = json.dumps(self.data)
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()


    @classmethod      
    def deleteAll(self):
        self.sureallWin.destroy()
        self.todo = self.User()
        self.fp = open('data.json')
        self.data = json.load(self.fp)

        r = []
        dictBin = {}
        self.bin = open('bin.json')
        self.databin = json.load(self.bin)

        for v,a in self.data.items():
            if self.todo == v:
                for b in a:
                    r.append(b)
                for e in r:
                    a.remove(e)
                self.data[self.todo] = a

        if self.todo in self.databin.keys():
            for p,c in self.databin.items():
                if self.todo == p:
                    for d in r:    
                        c.append(d)
                    self.databin[self.todo] = c
        else:
            self.databin[self.todo] = r
 
        binString = json.dumps(self.databin)
        binFile = open("bin.json", "w")
        binFile.write(binString)
        binFile.close()
        self.bin.close()

        todoMain.MainPage.listbox_list.delete(0, END)
        jsonString = json.dumps(self.data)
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    

    @classmethod
    # #not delete
    def notDel(self):
        self.sureWin.destroy()

    @classmethod
    def notallDel(self):
        self.sureallWin.destroy()

    @classmethod    
    # #make sure to delete
    def makeSure(self):
        if todoMain.MainPage.listbox_list.curselection():
            self.sureWin = Tk()
            self.sureWin.title("Are you sure?")
            self.sureWin.geometry("350x70")
        
            self.lb_editWin = Label(self.sureWin, text='Do you want to delete this REMINDER?', font=('Calibri', 14))
            self.lb_editWin.place(relx=0.06, rely=0.03)

        # tkinter.messagebox.askquestion(title="Warning!",message="Please Enter Reminder",command = self.deleteList)

            self.bt_sureEdit = Button(self.sureWin,text='Yes',font=('Calibri', 15),relief=RAISED,cursor="heart", command=self.deleteList)
            self.bt_sureEdit.place(relx=0.3, rely=0.5, width=60, height=28)

            self.bt_notEdit = Button(self.sureWin,text='No',font=('Calibri', 15),relief=RAISED,cursor="heart", command = self.notDel)
            self.bt_notEdit.place(relx=0.5, rely=0.5, width=60, height=28)

            self.sureWin.mainloop()

        else:
            tkinter.messagebox.showwarning(title="Warning!",message="Please Select Reminder")


    @classmethod    
    # #make sure to delete all
    def makeallSure(self):
        self.sureallWin = Tk()
        self.sureallWin.title("Are you sure?")
        self.sureallWin.geometry("350x100")
        
        self.lb_editallWin = Label(self.sureallWin, text='Do you want to delete all REMINDER?', font=('Calibri', 14))
        self.lb_editallWin.place(relx=0.06, rely=0.03)

        self.bt_sureallEdit = Button(self.sureallWin,text='Yes',font=('Calibri', 15),relief=RAISED,cursor="heart", command=self.deleteAll)
        self.bt_sureallEdit.place(relx=0.3, rely=0.5, width=60, height=28)

        self.bt_notallEdit = Button(self.sureallWin,text='No',font=('Calibri', 15),relief=RAISED,cursor="heart", command = self.notallDel)
        self.bt_notallEdit.place(relx=0.5, rely=0.5, width=60, height=28)

        self.sureallWin.mainloop()


    @classmethod
    #def restoreData(self):
    def showBin(self):
        self.listbox_winBin.delete(0,END)
        c = -1
        self.todo = self.User()
        self.f = open('bin.json')
        self.databin = json.load(self.f)
        if self.todo in self.databin.keys():
            for v,a in self.databin.items():
                if self.todo == v:
                    for b in range(len(a)):
                        status = ''
                        j = -1
                        c = c + 1
                        ID = a[b]
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
                        self.listbox_winBin.insert(c, Data)
                        status = ''


    @classmethod
    def Home(self):
        #Label in window 
        self.lb_myl = Label(todoMain.MainPage.my_frame, text='My Lists  ', font=('Calibri', 35))
        self.lb_myl.place(relx=0.025, rely=0.01)

        todoMain.MainPage.listbox_list.delete(0,END)

        todoMain.MainPage.showData()

    
    @classmethod
    def Addlist(self):
        #todoMain.MainPage.listbox_list = listbox
        self.addlist = Tk()
        self.addlist.title("New List")
        self.addlist.geometry("500x350")

        self.lb_listname = Label(self.addlist, text='Reminder', font=('Calibri', 14))
        self.lb_listname.place(relx=0.02, rely=0.03)

        self.txt = StringVar(self.addlist)

        self.myText = Entry(self.addlist, textvariable=self.txt)
        self.myText.place(relx=0.18, rely=0.03, height=30, width=330)

        self.bt_addDone = Button(self.addlist,text='Done',font=('Calibri', 15),relief=RAISED,cursor="heart",command= self.showmessage)
        self.bt_addDone.place(relx=0.85, rely=0.03, width=60, height=28)

        self.cal = Calendar(self.addlist, date_pattern = "dd/mm/y")
        self.cal.place(relx=0.25, rely=0.18)

        self.spinhour = Spinbox(self.addlist, from_= 0, to = 24)
        self.spinhour.place(relx=0.38, rely=0.8, height=20, width=30)

        self.spinminutes = Spinbox(self.addlist, from_= 0, to = 59)
        self.spinminutes.place(relx=0.45, rely=0.8, height=20, width=30)
        
        self.spinseconds = Spinbox(self.addlist, from_= 0, to = 59)
        self.spinseconds.place(relx=0.52, rely=0.8, height=20, width=30)


    @classmethod    
    def showmessage(self):
        self.todo = self.User()
        message = self.txt.get()
        cal_list = self.cal.get_date()           
        hour = self.spinhour.get()  
        minutes = self.spinminutes.get()
        seconds = self.spinseconds.get()
        if message == "" :
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter Reminder")
        elif int(minutes) > 59 or int(minutes) < 0 or int(seconds) > 59 or int(seconds) < 0 or int(hour) < 0:
            tkinter.messagebox.showwarning(title="Warning!",message="Please enter the correct time")
        else:
            if int(hour) < 10:
                hour = '0' + hour
        
            if int(minutes) < 10:
                minutes = '0' + minutes
            
            if int(seconds) < 10:
                seconds = '0' + seconds
            todoMain.MainPage.listbox_list.insert(END, message +", "+ cal_list + " "+ hour +":"+ minutes +":"+ seconds)
            self.addlist.destroy()
            
            self.f = open('data.json')
            self.data = json.load(self.f)
            if self.todo in self.data.keys():
                a = self.data[self.todo]
                a.append({'List Name': message, 'Date' : cal_list, 'hour' : hour, 'minutes' : minutes, 'seconds' : seconds})
                self.data[self.todo] = a
            else:
                self.data[self.todo] = [{'List Name': message, 'Date' : cal_list, 'hour' : hour, 'minutes' : minutes, 'seconds' : seconds}]
            
            jsonString = json.dumps(self.data)
            jsonFile = open("data.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            self.f.close()
            todoMain.MainPage.listbox_list.delete(0,END)
            todoMain.MainPage.showData()


    @classmethod
    #not restore
    def notRestore(self):
        self.sureRe.destroy()
        self.winBin.destroy()

    @classmethod
    def notallRestore(self):
        self.sureallRe.destroy()
        self.winBin.destroy()

    @classmethod
    def sureRestore(self):
        if self.listbox_winBin.curselection():
            self.sureRe = Tk()
            self.sureRe.title("Are you sure?")
            self.sureRe.geometry("350x70")
        
            self.lb_restore = Label(self.sureRe, text='Do you want to restore this REMINDER?', font=('Calibri', 14))
            self.lb_restore.place(relx=0.06, rely=0.03)

            # tkinter.messagebox.askquestion(title="Warning!",message="Please Enter Reminder",command = self.deleteList)
            self.bt_surerestore = Button(self.sureRe,text='Yes',font=('Calibri', 15),relief=RAISED,cursor="heart", command=self.restoreList)
            self.bt_surerestore.place(relx=0.3, rely=0.5, width=60, height=28)

            self.bt_notrestore = Button(self.sureRe,text='No',font=('Calibri', 15),relief=RAISED,cursor="heart", command = self.notRestore)
            self.bt_notrestore.place(relx=0.5, rely=0.5, width=60, height=28)
            self.sureRe.mainloop()

        else:
            tkinter.messagebox.showwarning(title="Warning!",message="Please Select Reminder")

    @classmethod
    def sureallRestore(self):
        self.sureallRe = Tk()
        self.sureallRe.title("Are you sure?")
        self.sureallRe.geometry("350x70")
    
        self.lb_restore = Label(self.sureallRe, text='Do you want to restore all REMINDER?', font=('Calibri', 14))
        self.lb_restore.place(relx=0.06, rely=0.03)

        # tkinter.messagebox.askquestion(title="Warning!",message="Please Enter Reminder",command = self.deleteList)
        self.bt_sureallRe = Button(self.sureallRe,text='Yes',font=('Calibri', 15),relief=RAISED,cursor="heart", command = self.restoreallList)
        self.bt_sureallRe.place(relx=0.3, rely=0.5, width=60, height=28)

        self.bt_notallRe = Button(self.sureallRe,text='No',font=('Calibri', 15),relief=RAISED,cursor="heart", command = self.notallRestore)
        self.bt_notallRe.place(relx=0.5, rely=0.5, width=60, height=28)
        self.sureallRe.mainloop()


    @classmethod
    def restoreList(self):
        self.bin = open('bin.json')
        self.databin = json.load(self.bin)
        r = []
        for relist in reversed(self.listbox_winBin.curselection()):
            restorelist = self.listbox_winBin.get(relist)
            x = str(restorelist).split(", ")
            listName = x[0]
            y = x[1].split(" ")
            z = y[1].split(":")
            Date = y[0]
            hour = z[0]
            minutes = z[1]
            seconds = z[2]

            if " DONE \u2714" in restorelist:
                self.c = open('complete.json')
                self.datacom = json.load(self.c)
                for a,j in self.datacom.items():
                    if self.todo == a:
                        j.append(restorelist)
                        self.datacom[self.todo] = j

                jsonString = json.dumps(self.datacom)    
                jsonFile = open("complete.json", "w")
                jsonFile.write(jsonString)
                jsonFile.close()
                todoMain.MainPage.listbox_complete.delete(0,END)
                todoMain.MainPage.showComplete()
            
            else:
                listCom = []
                self.f = open('data.json')
                self.data = json.load(self.f)
                for a,j in self.data.items():
                    if self.todo == a:
                        for b in j:
                            listCom.append(b)
                listCom.append({'List Name': listName, 'Date' : Date, 'hour' : hour, 'minutes' : minutes, 'seconds' : seconds})
                self.data[self.todo] = listCom
                #print(self.data)
                jsonString = json.dumps(self.data)    
                jsonFile = open("data.json", "w")
                jsonFile.write(jsonString)
                jsonFile.close()

            for d,e in self.databin.items():
                if self.todo == d:
                    r.append(e[relist])

        for f,g in self.databin.items():
            if self.todo == f:
                for h in r:
                    g.remove(h)
                self.databin[self.todo] = g
        self.listbox_winBin.delete(relist)
        
        jsonString = json.dumps(self.databin)    
        jsonFile = open("bin.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

        todoMain.MainPage.listbox_list.delete(0,END)
        todoMain.MainPage.showData()
        self.sureRe.destroy()
        self.winBin.destroy()


    @classmethod
    def restoreallList(self):
        self.todo = self.User()

        self.b = open('bin.json')
        self.databin = json.load(self.b)
        s = []
        for w,y in self.databin.items():
            if self.todo == w:
                for z in y:
                    s.append(z)
                #print(s)

        for k in range(len(s)):
            restorelist = self.listbox_winBin.get(k)
            x = str(restorelist).split(", ")
            listName = x[0]
            y = x[1].split(" ")
            z = y[1].split(":")
            Date = y[0]
            hour = z[0]
            minutes = z[1]
            seconds = z[2]
            if " DONE \u2714" in restorelist:
                self.c = open('complete.json')
                self.datacom = json.load(self.c)
                for a,j in self.datacom.items():
                    if self.todo == a:
                        j.append(restorelist)
                        self.datacom[self.todo] = j

                jsonString = json.dumps(self.datacom)    
                jsonFile = open("complete.json", "w")
                jsonFile.write(jsonString)
                jsonFile.close()
                todoMain.MainPage.listbox_complete.delete(0,END)
                todoMain.MainPage.showComplete()

            else:
                listCom = []
                self.f = open('data.json')
                self.data = json.load(self.f)
                for a,j in self.data.items():
                    if self.todo == a:
                        for b in j:
                            listCom.append(b)
                listCom.append({'List Name': listName, 'Date' : Date, 'hour' : hour, 'minutes' : minutes, 'seconds' : seconds})
                self.data[self.todo] = listCom

                jsonString = json.dumps(self.data)    
                jsonFile = open("data.json", "w")
                jsonFile.write(jsonString)
                jsonFile.close()

        for k in range(len(s)):
            self.listbox_winBin.delete(k)

        for m,n in self.databin.items():
            if self.todo == m:
                for p in s:
                    print('p',p)
                    n.remove(p)
                self.databin[self.todo] = n
                jsonString = json.dumps(self.databin)
                jsonFile = open("bin.json", "w")
                jsonFile.write(jsonString)
                jsonFile.close()
        
        self.listbox_winBin.delete(0, END)
        todoMain.MainPage.listbox_list.delete(0,END)
        todoMain.MainPage.showData()
        self.sureallRe.destroy()
        self.winBin.destroy()



    @classmethod
    #Create file data.json
    def create_datajson(self):
        jsonString = json.dumps({})
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()



    @classmethod
    def create_binjson(self):
        jsonString = json.dumps({})
        jsonFile = open("bin.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()



    @classmethod
    def create_completejson(self):
        jsonString = json.dumps({})
        jsonFile = open("complete.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()


    @classmethod
    def sort_list(self):
        index = []
        listd = []
        self.f = open('data.json')
        self.data = json.load(self.f)
        self.todo = self.User()
        for a,b in self.data.items():
            if self.todo == a:
                for ID in b:
                    index.append(ID['Date']+ID['hour']+":"+ID['minutes'] +":"+ ID['seconds'])
                    #print('index',index)
        dict_new = {} 
        index.sort(key = lambda date: datetime.strptime(date, '%d/%m/%Y%H:%M:%S'))
        print(index)
        for i in range(len(index)):          
            for c,d in self.data.items():
                if self.todo == c:
                    for v in d:
                        print('i',i)
                        print(v['Date'])
                        if v['Date']+v['hour']+":"+v['minutes'] +":"+ v['seconds'] == index[i]:
                            listd.append(v)
                    dict_new[c] = listd
                    print('dict_new v',dict_new)  
                # dict_new[c] = self.data[c]
                # print('dict_new c',dict_new)  
        jsonString = json.dumps(dict_new)
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        todoMain.MainPage.listbox_list.delete(0,END)
        todoMain.MainPage.showData()


    @classmethod
    def today_list(self):
        maintoday = Tk()
        maintoday.title("Today")
        maintoday.geometry("435x480")

        self.todaylist= Frame(maintoday)
        self.todaylist.pack()        
        self.todaylist.place(relx=0.03, rely=0.01)
        
        self.name_today = Label(self.todaylist, text='to-do list', font=('Calibri', 14))
        self.name_today .place(relx=0.02, rely=0.01)

        '''self.bt_addOk = Button(maintoday,text='Ok',font=('Calibri', 15),relief=RAISED,cursor="heart")
        self.bt_addOk.place(relx=0.82, rely=0.9, width=60, height=28)'''

        self.today_scrollbar = Scrollbar(self.todaylist, orient=VERTICAL)
        self.today_scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox_today = Listbox(self.todaylist,bg="white",fg="black",height=16,width=40,font='Calibri',yscrollcommand= self.today_scrollbar.set, selectmode=MULTIPLE)

        self.today_scrollbar.config(command=self.listbox_today.yview)
        #self.listbox_today.place(relx=0.03, rely=0.1) 
        self.listbox_today.pack(pady=46)     

        self.listbox_today.pack()
        self.todo = self.User()
        c = -1
        self.f = open('data.json')
        self.data = json.load(self.f)
        for a,b in self.data.items():
            if self.todo == a:
                today_date = datetime.today().date()
                print('today date',today_date)
                new_today_date = today_date.strftime("%d/%m/%Y")
                print('new today date',new_today_date)
                for v in b:        
                    if v['Date'] == str(new_today_date):
                        c = c+1
                        #print(str(new_today_date))
                        #print(v['Date'])
                        ListName = v['List Name']
                        Date = v['Date']
                        hour = v['hour']
                        minutes = v['minutes']
                        seconds = v['seconds']
                        Data = ListName + ', ' + Date + " "+ hour +":"+ minutes +":"+ seconds
                        self.listbox_today.insert(c, Data)


    @classmethod
    def windowBin(self):
        self.winBin = Tk()
        self.winBin.title("Trash")
        self.winBin.geometry("435x480")

        self.winBinlist= Frame(self.winBin)
        self.winBinlist.pack()        
        self.winBinlist.place(relx=0.03, rely=0.01)
        
        self.name_winBin = Label(self.winBinlist, text='Trash', font=('Calibri', 16))
        self.name_winBin .place(relx=0.02, rely=0.01)

        '''self.bt_addOk = Button(winBin,text='Ok',font=('Calibri', 15),relief=RAISED,cursor="heart")
        self.bt_addOk.place(relx=0.82, rely=0.9, width=60, height=28)'''
        self.bt_addrelist = Button(self.winBinlist,text='Restore List',font=('Calibri', 10),relief=RAISED,cursor="heart",command= self.sureRestore)
        self.bt_addrelist.place(relx=0.58, rely=0.01, width=72, height=28)

        self.bt_addreall = Button(self.winBinlist,text='Restore All',font=('Calibri', 10),relief=RAISED,cursor="heart",command= self.sureallRestore)
        self.bt_addreall.place(relx=0.78, rely=0.01, width=72, height=28)

        self.bt_addreall = Button(self.winBinlist,text='Permanent Delete',font=('Calibri', 10),relief=RAISED,cursor="heart", command=self.sureperDel)
        self.bt_addreall.place(relx=0.31, rely=0.01, width=100, height=28)

        self.winBin_scrollbar = Scrollbar(self.winBinlist, orient=VERTICAL)
        self.winBin_scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox_winBin = Listbox(self.winBinlist,bg="white",fg="black",height=16,width=40,font='Calibri',yscrollcommand= self.winBin_scrollbar.set, selectmode=MULTIPLE)

        self.winBin_scrollbar.config(command=self.listbox_winBin.yview)
        #self.listbox_winBin.place(relx=0.03, rely=0.1) 
        self.listbox_winBin.pack(pady=46)     
        self.listbox_winBin.pack()

        self.listbox_winBin.bind('<Double-1>', lambda event :self.sureRestore())
        self.listbox_winBin.pack()
        self.showBin()


#     @classmethod
#     def save_list(self):
#         file = filedialog.asksaveasfile(defaultextension='.txt',filetypes=[("Text file",".txt"),("All file",".*")])
#         self.f = open('data.json')
#         self.data = json.load(self.f)
#         self.f.close()       
#         for v in self.data.keys():
#             ID = self.data[str(v)]
#             ListName = ID['List Name']
#             Date = ID['Date']
#             hour = ID['hour']
#             minutes = ID['minutes']
#             seconds = ID['seconds']
#             time = hour +":"+ minutes +":"+ seconds
#             file.write('List Name :%s\n' % (ListName))
#             file.write('Date :%s\n' % (Date))
#             file.write('Time :%s\n\n' % (time))
#         file.close()


    @classmethod
    def perDel(self):
        #self.selected = self.listbox_winBin.curselection()
        self.todo = self.User()
        self.fp = open('bin.json')
        self.databin = json.load(self.fp)
        r = []

        for i,j in self.databin.items():
            if self.todo == i:
                for k in j:
                    r.append(k)

                for item in reversed(self.listbox_winBin.curselection()):
                    index = r[item]
                    j.remove(index)
                    self.listbox_winBin.delete(item)

        binString = json.dumps(self.databin)
        binFile = open("bin.json", "w")
        binFile.write(binString)
        binFile.close()

        self.sure_perDel.destroy()
        self.winBin.destroy()
        

    @classmethod
    #not Permanent Delete
    def notperDel(self):
        self.sure_perDel.destroy()
        self.winBin.destroy()


    @classmethod
    def sureperDel(self):
        if self.listbox_winBin.curselection():
            self.sure_perDel = Tk()
            self.sure_perDel.title("Are you sure?")
            self.sure_perDel.geometry("460x90")
        
            self.lb_perDel = Label(self.sure_perDel, text='Do you want to permanently delete this REMINDER?', font=('Calibri', 14))
            self.lb_perDel.place(relx=0.06, rely=0.03)
        
            self.bt_sureperDel = Button(self.sure_perDel,text='Yes',font=('Calibri', 15),relief=RAISED,cursor="heart", command = self.perDel)
            self.bt_sureperDel.place(relx=0.3, rely=0.5, width=60, height=28)

            self.bt_notperDel = Button(self.sure_perDel,text='No',font=('Calibri', 15),relief=RAISED,cursor="heart", command = self.notperDel)
            self.bt_notperDel.place(relx=0.5, rely=0.5, width=60, height=28)
            self.sure_perDel.mainloop()

        else:
            tkinter.messagebox.showwarning(title="Warning!",message="Please Select Reminder")
    
    
