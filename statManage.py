from select import select
from tkinter import *
from tkcalendar import *
from tkcalendar import DateEntry
from datetime import *
from datetime import date
import json
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image,ImageTk
import dataManage


class statEdit:
    @classmethod
    def __init__(self):
        #Create frame for show graph
        self.stat_page = Toplevel()
        self.stat_page.title("Statistic Visualization")
        self.stat_page.geometry("540x620")
        self.stat_page.config(bg="#6fa0c6")

        self.bt_show= Image.open('todoPic/showgraph.png')
        self.resize_show = self.bt_show.resize((120,40),Image.ANTIALIAS)
        self.bt_newshow = ImageTk.PhotoImage(self.resize_show)
        self.bttn_show = Button(self.stat_page,image = self.bt_newshow,cursor="heart", bg='#6fa0c6', command = self.dataGraph , borderwidth=0)
        self.bttn_show.place(relx=0.03, rely=0.02, width=120, height=40)

        # self.bttn_show = Button(self.stat_page,text='Show Graph',font=('Calibri', 10),relief=RAISED,cursor="heart", command = self.dataGraph)
        # self.bttn_show.place(relx=0.05, rely=0.005, width=100, height=32)

        self.alreadyPlot = False

        self.stat_page.mainloop()


    @classmethod
    def dataGraph(self):
        if self.alreadyPlot == False:
            self.alreadyPlot = True
            self.todo = dataManage.dataEdit.User()
            self.list_today = 0
            self.list_complete_today = 0
            self.list_complete_week = 0
            self.list_late_today = 0
            self.list_late_week = 0
            self.list_complete_all = 0
            self.op_data = open('data.json')
            self.data = json.load(self.op_data)
            self.op_data.close()
            self.op_complete = open('complete.json')
            self.data_complete = json.load(self.op_complete)
            self.op_complete.close()

            self.today_date = datetime.today().date()
            self.new_today_date = self.today_date.strftime("%d/%m/%Y")
            self.date_today = datetime.strptime(self.new_today_date,"%d/%m/%Y") 

            self.today_datetime = datetime.now()
            self.new_today_datetime = self.today_datetime.strftime("%d/%m/%Y%H:%M:%S")
            self.datetime_today = datetime.strptime(self.new_today_datetime,"%d/%m/%Y%H:%M:%S")

            for user,value in self.data.items():
                if user == self.todo and len(value) > 0:
                    for list in value:
                        day_value =  list['Date']
                        daynew_value = datetime.strptime(day_value,"%d/%m/%Y")
                        day_time_value = list['Date']+list['hour']+":"+list['minutes']+":"+list['seconds']                
                        daytime_new_value = datetime.strptime(day_time_value,"%d/%m/%Y%H:%M:%S") 
                        if daynew_value == self.date_today:
                            self.list_today += 1                 
                            if  daytime_new_value < self.datetime_today :
                                self.list_late_today += 1                                    
                        for x in range(6,0,-1):
                            d = self.today_datetime - timedelta(days=x)
                            d_strftime = d.strftime("%d/%m/%Y")
                            d_strptime = datetime.strptime(d_strftime,"%d/%m/%Y")
                            if d_strptime == daytime_new_value:
                                self.list_late_week += 1                           
                    self.list_all_data = value
            if user == self.todo and len(value) == 0:
                    self.list_all_data = []


            for user,value in self.data_complete.items():
                if user == self.todo and len(value) > 0:
                    for v in value:
                        x = str(v).split(", ")
                        y = x[1].split(" ")
                        Date = y[0]
                        Date_complete = datetime.strptime(Date,"%d/%m/%Y") 
                        if Date_complete == self.date_today:
                            self.list_complete_today += 1 
                        for x in range(6,0,-1):
                            d_complete = self.today_datetime - timedelta(days=x)
                            d_complete_strftime = d_complete.strftime("%d/%m/%Y")
                            d_complete_strptime = datetime.strptime(d_complete_strftime,"%d/%m/%Y")
                            if d_complete_strptime == Date_complete:
                                self.list_complete_week += 1
                    self.list_complete_all = value
                if user == self.todo and len(value) == 0:
                    self.list_complete_all = []
        
                        
            self.list_all_data_count = len(self.list_all_data)
            self.list_complete_all_count = len(self.list_complete_all)
            # print('list_all_data_count',self.list_all_data_count)
            # print('list_today_count',self.list_today)
            # print('list_late_today_count',self.list_late_today)
            # print('list_complete_today_count',self.list_complete_today)
            # print('list_complete_all',self.list_complete_all)
            # print('list_late_week_count',self.list_late_week)
            # print('list_complete_week_count',self.list_complete_week)



            #ALL
            #show all data graph
            showFig = Figure(figsize=(4,2), dpi=90) 
            subplot = showFig.add_subplot(111) 
            label = 'Complete', 'Incomplete'
            if len(self.data[self.todo]) == 0: 
                pieSize = [1, 0]
            elif len(self.data[self.todo]) == 0 and len(self.data_complete[self.todo]) == 0:
                pieSize = [1, 0]
            elif len(self.data_complete[self.todo]) == 0: 
                pieSize = [0, 1]
            else:
                pieSize = [self.list_complete_all_count, self.list_all_data_count]
            my_color = 'Blue', 'Red'
            explodes = (0, 0.1)  
            subplot.pie(pieSize, colors=my_color, explode=explodes, labels=label, autopct='%1.1f%%', shadow=True, startangle=90)
            subplot.legend(title = "All:",bbox_to_anchor=(1.4, 1))
            pie1 = FigureCanvasTkAgg(showFig, self.stat_page)
            pie1.get_tk_widget().pack(side=BOTTOM, fill=X, expand=0)


            #WEEK
            #show week data graph
            showFig3 = Figure(figsize=(4,2), dpi=90) 
            subplot3 = showFig3.add_subplot(111) 
            label3 = 'Complete', 'Incomplete'
            if len(self.data[self.todo]) == 0:
                pieSize3 = [1, 0] 
            elif len(self.data[self.todo]) == 0 and len(self.data_complete[self.todo]) == 0:
                pieSize3 = [1, 0]
            else:
                pieSize3 = [(self.list_complete_week +  self.list_complete_today), (self.list_late_week + self.list_late_today)]
            my_color3 = 'Green', 'Silver'
            explodes3 = (0, 0.1)  
            subplot3.pie(pieSize3, colors=my_color3, explode=explodes3, labels=label3, autopct='%1.1f%%', shadow=True, startangle=90)
            subplot3.legend(title = "Week:",bbox_to_anchor=(1.4, 1))
            pie3 = FigureCanvasTkAgg(showFig3, self.stat_page)
            pie3.get_tk_widget().pack(side=BOTTOM, fill=X, expand=0)


            #TODAY
            #show today data graph
            showFig2 = Figure(figsize=(4,2), dpi=90) 
            subplot2 = showFig2.add_subplot(111) 
            label2 = 'Complete', 'Overdue' ,'Incomplete'
            if len(self.data[self.todo]) == 0:
                pieSize2 = [1, 0, 0]
            elif self.list_complete_today == 0 and self.list_late_today == 0 and self.list_today == 0:
                pieSize2 = [1, 0, 0]
            else:
                pieSize2 = [self.list_complete_today, self.list_late_today, (self.list_today - self.list_late_today)]
            my_color2 = 'Green', 'Red' , 'Silver'
            explodes2 = (0, 0.1 , 0)  
            subplot2.pie(pieSize2, colors=my_color2, explode=explodes2, labels=label2, autopct='%1.1f%%', shadow=True, startangle=90)
            subplot2.legend(title = "Today:",bbox_to_anchor=(1.4, 1))
            pie2 = FigureCanvasTkAgg(showFig2, self.stat_page)
            pie2.get_tk_widget().pack(side=BOTTOM, fill=X, expand=0)

