import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import rpyc
from tkcalendar import DateEntry

import numpy as np
# Implement the default Matplotlib key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt 

import tkTools as T

import csv



class UIbudget(tk.Tk):
    def __init__(self, user):
        #create window
        super().__init__() 
        self.title("Budget Overview")
        self.geometry('800x600')

        #get user information
        #download file into main directory

        #widgets
        overview = Overview(self, user)
        overview.place(x=0, y=0, relwidth = .4, relheight = 1)

        # pie = Pie(self, user)
        # pie.place(x = 300, y = 0, relwidth = .6, relheight = .7)

        input = Input(self, user)
        input.place(x = 300, y = 600 * .7, relwidth = .62, relheight = .3)

        #run 
        self.mainloop()

        
class Overview(ttk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)

        self.category_budget = {}
        self.get_info(user)
        self.create_bars(parent, user)


    def get_info(self,user):
        with open(f"user_db/{user}/catagories.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile) #read information as csvfile
            for row in reader:
                self.category_budget[row['catagory']] = int(row['budget'])

    def create_bars(self, parent, user):
        for idx, (catagory, budget) in enumerate(self.category_budget.items()):
            bar = Bar(parent, catagory, budget, user)
            bar.grid(row = idx)


class BarFigure(tk.Canvas):
    def __init__(self, parent, catagory, budget, user):
        super().__init__(parent, width = 150, height = 39) #initializes canvas width and height
        
        self.x0 = 12
        self.x1 = 13
        total_spent = self.get_total(catagory, user)
        self.calculate_position(total_spent, catagory, budget)
        

        self.box = self.create_rectangle(10, 20, 150, 40, outline = 'black', fill = 'white')
        self.green_box = self.create_rectangle(self.x0, 22, self.x1, 39, outline = '', fill = 'green')
        if self.x1 > 140:
            self.amount = self.create_text(140, 12, text = '$' + str(total_spent))
        else:
            self.amount = self.create_text(self.x1, 12, text = '$' + str(total_spent))

    def get_total(self, catagory, user):
        cost = 0
        with open(f"user_db/{user}/{catagory}.csv" , 'r') as csvFile:
            csv_reader = csv.DictReader(csvFile)
            
            for row in csv_reader:
                cost += int(row['cost'])

        return cost
    
    def calculate_position(self, total_spent, catagory, budget):
        # pixel range for green box is 13-149
        # 149-13=136
        value = budget - total_spent

        if value < 0:
            self.x1 = 149   #turn red

        else:
            percent = total_spent/budget
            self.x1 = (136 * percent) + 13



class Bar(ttk.Frame):
    def __init__(self, parent, catagory, budget, user):
        super().__init__(parent)
        
        label = ttk.Label(self, text = catagory, font=("default", 11))
        budget_L = ttk.Label(self, text = '$' + str(budget))

        barfig = BarFigure(self, catagory, budget, user)

        #self.grid(row = 0, column = 0)
        label.grid(row = 0, column = 0, sticky = 'SE', pady= 10)
        self.columnconfigure(0, minsize = 100) #to make colun 1 expand
        barfig.grid(row = 0, column = 1, pady = 5)

        budget_L.grid(row = 0, column = 2, sticky = 'S', pady = 5)


class Input(ttk.Frame):
    def __init__(self, parent, username):
        super().__init__(parent)
        self.user = username
        self.expense_input()
        self.income_input()

    def expense_input(self):
        expense_label = T.create_label(self, "Expense", 0, 0)
        clicked = self.expense_drop_down(1, 0)
        dollar_symbol = T.create_label(self, "$", 1, 1)
        expense_entry = T.create_entry(self, 10, 1, 2)
        description_entry = T.create_entry(self, 25, 1, 3)
        description_label = T.create_label(self, "Description", 0, 3)
        calendar = T.create_date_entry(self, 1, 4)
        input_button = T.create_button(self, "Confirm", lambda: self.expense_confirmation(clicked, expense_entry, description_entry, calendar), 1, 5)


    def expense_drop_down(self, row, column):
        options = [
            "bills",
            "entertainment",
            "food",
            "other",
            "shopping",
            "transportation"
        ]
        clicked = T.create_option_menu(self, options, row, column)
        return clicked
    

    def expense_confirmation(self, clicked, expense, description, calendar):
        catagory = clicked.get()
        ex = expense.get()
        des = description.get()
        year_month_day = str(calendar.get_date()) #YYYY-MM-DD
        year, month, day = year_month_day.split("-")

        new_data = {"cost": ex,
                    "description": des,
                    "day": day,
                    "month": month,
                    "year": year}

        #going to need user's name in order to put information into a file
        csv_columns = ["cost", "description", "day", "month", "year"]
        with open(f"user_db/{self.user}/{catagory}.csv", 'a', newline='') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=csv_columns)
            writer.writerow(new_data)
            
 

    def income_input(self):
        income_label = T.create_label(self, "Income", 2, 0)
        clicked = self.income_drop_down(3, 0)
        dollar_symbol = T.create_label(self, "$", 3, 1)
        income_entry = T.create_entry(self, 10, 3, 2)
        # description_label = T.create_label(self, "Description", 2, 3)
        description_entry = T.create_entry(self, 25, 3, 3)
        calendar = T.create_date_entry(self, 3, 4)
        input_button = T.create_button(self, "Confirm", lambda: self.income_confirmation(), 3, 5)

    def income_confirmation(self):
        pass

    def income_drop_down(self, row, column):
        options = [
            "Job",
            "Investment",
            "Other"
        ]
        
        clicked = T.create_option_menu(self, options, row, column)
        return clicked








class Pie(ttk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        # ttk.Label(self, background = 'green').pack(expand = True, fill = 'both')

        catagories = self.get_catagories(user)  #list
        # totals = self.get_totals(user, catagories)  #dictionary
        # percentage = self.get_percentage
        # self.get_totals()
        #percentage = self.get_percentage(user, catagories)
        percentage = [10, 10, 10, 10, 20, 40]
        fig = Figure() # create a figure object
        fig.set_facecolor('#f0f0f0')

        ax = fig.add_subplot(111) # add an Axes to the figure
        ax.pie(percentage, radius=1, labels=catagories, autopct='%0.0f%%')

        chart1 = FigureCanvasTkAgg(fig, self)
        chart1.get_tk_widget().pack()


    def get_catagories(self, user):
        catagories = []
        with open(f"user_db/{user}/catagories.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            headers = next(csv_reader)
            for row in csv_reader: #remove income from expense catagories and create an income catagores so job, freelance, sold items, investments
                    catagories.append(row[0])
        return catagories
    
    # def get_totals(self, user, catagories):
    #     totals = {}
    #     for catagory in catagories:
    #         with open(f"user_db/{user}/{catagory}.csv", 'r') as csvFile:
    #             csvReader = csv.DictReader(csvFile)
    #             for row in csvReader:
    #                 totals[catagory] += int(row['cost'])

        return totals

