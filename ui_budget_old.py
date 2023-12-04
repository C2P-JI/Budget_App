import tkinter as tk
from tkinter import messagebox
import rpyc

import numpy as np
# Implement the default Matplotlib key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt 

import csv

class UIbudget(tk.Tk):
    def __init__(self, user):

        super().__init__()
        self.username = user


    def close_budget_root_app(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()


        #need to show all inputs and be able to change the values if 
        #a mistake was entered

        #need to include a undo previous input


        #Input Expense
            #timestamp
    def input_expense(self):
        pass
        #need a button to click on opens a window input all information
        # myButton = tk.Button(self.budget_root, text="Enter a expense")
        # myButton.pack()

        #Input Income
            #timestamp
    def input_income(self):
        pass

    def get_catagories(self):
        file = f"user_db/{self.username}/catagories.csv"
        catagories = []
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            headers = next(csv_reader)
            for row in csv_reader:
                catagories.append(row[0])

        return catagories


    def get_totals(self):
        #return list in same way we made the get catagories
        #so for each row after header we can use a function to collect and append to a list

        #with open(file path to catagories, 'r') as csv_file
        #   csv_reader = csv.reader(csv_file)
        #   header = next(csv_reader)
        #   for row in csv_reader:
        #        with open(f"user_db/{self.username}/{row}.csv") as cat_file
        #           for cat_row in cat_file
        #                print(cat_row)
        with open(f"user_db/{self.username}/catagories.csv", 'r') as catagories_file:
            catagories_reader = csv.reader(catagories_file)
            header = next(catagories_file)
            for row in catagories_reader:
                catagory_name = row[0]
                with open(f"user_db/{self.username}/{catagory_name}.csv", 'r') as cat_file:
                    cat_header = next(cat_file)
                    # for cat_row in cat_file:
                    #     print(cat_row)

            #how to store these totals into a list or a dictionary
            #if I were to use a dictionary I could probably store each one properly

            #or if it's from 'bills.csv' it will store into key:bills, value:$$$$

            #where do I store total information. Do I store total for each day in a csv file
            #are all these csv files using up too much memory?
            #what other ways can we store mass amount of information and how can we retrieve it?

            #I need the total for the days to calculate the total for the overal month 
            #so if the time is included for each income 

            #let's make it easy
            #sum the total of all expenses for the pie chart!


        #Show Pie chart of the Month for month
    def pie_graph(self, budget_window):
        frame_chart = tk.Frame(budget_window)
        frame_chart.grid(row=0, column=1)
        #get the catagories into a list
        
        catagories = self.get_catagories()
        print(catagories)
        self.get_totals()
        percentage = [10,10,10,10,10,10,40]

        fig = Figure() # create a figure object
        ax = fig.add_subplot(111) # add an Axes to the figure

        ax.pie(percentage, radius=1, labels=catagories, autopct='%0.2f%%', shadow=True)

        chart1 = FigureCanvasTkAgg(fig, frame_chart)
        chart1.get_tk_widget().pack()

        #We want to draw the shoadow for each pie 
        

            #collect for one day

            #accumulate total over the current week
                #week tracking

            #accumulate total over the current month
                #month tracking


        #Show money left for month
            #Set budget limits 
            #compare budget limits to total within time frame

        #Show approaching limits

        #show details of every catagory in a seperate window

        #quit

        

    def open_budget_window(self):
        self.protocol("WM_DELETE_WINDOW", self.close_budget_root_app) #no parenthis or else runs function right away
        self.title('Budget Overview') 
        #Today's date function


        #income and expenses
        frame = tk.Frame(self)
        frame.grid(row=0, column=0)

        today_label = tk.Label(frame, text="12, November, 2023")
        today_label.grid(row=0,column=0)
        
        input_expense_button = tk.Button(frame, text="input expense", 
                                         command=self.input_expense)
        input_expense_button.grid(row=1, column=0)

        input_income_button = tk.Button(frame, text="input income",
                                        command=self.input_expense)
        input_income_button.grid(row=2, column=0)

        #pie graph
        self.pie_graph(budget_window)




'''
collect user information from either txt or csv files

what information do we need. basics
income
expenses like housing (rent, mortgage), utilities(water, power, gas), bills(phone, insurance, car, etc)
                      food (groceries, eating out, drinks, snacks), entertainment(subscriptions, clubs, gyms, etc)

            
    pass in user's name that logged in or registered

    create a pie graph to show where money has been spent

    a series of bars that are filled to a certain % or highlighted red if over budget

    left side of the screen input income or expense
        maybe like a box a frame where you select expense or income
        then depending on the choice the following would appear
        for expense the following selections
            dropdown box of what catagory the expense falls under (for now we will keep it to rent, bills, food, entertainment, savings?)
            
'''