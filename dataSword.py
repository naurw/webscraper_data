#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 21:04:29 2021

@author: William
"""
#This is to pull up prompt GUI, and to define variable inputs from User.
#Need to "pip install tk" in Terminal[MAC]/Cmd prompt[Windows]
import tkinter as Tk
from tkinter import *

class takeInput(object):

    def __init__(self,requestMessage):
        self.root = Tk()
        self.string = ''
        self.frame = Frame(self.root)
        self.frame.pack()        
        self.acceptInput(requestMessage)

    def acceptInput(self,requestMessage):
        r = self.frame

        k = Label(r,text=requestMessage)
        k.pack(side='left')
        self.e = Entry(r,text='Name')
        self.e.pack(side='left')
        self.e.focus_set()
        b = Button(r,text='Enter',command=self.gettext)
        b.pack(side='right')

    def gettext(self):
        self.string = self.e.get()
        self.root.destroy()

    def getString(self):
        return self.string

    def waitForInput(self):
        self.root.mainloop()

def getText(requestMessage):
    msgBox = takeInput(requestMessage)
    #loop until the user makes a decision and the window is destroyed
    msgBox.waitForInput()
    return msgBox.getString()
 # Asks from user what the user would wanted to add in
mySearch = getText('What do you want from Diana?')
print ("Selected Vessel Type: ", mySearch)


 # Asks from user what the user would wanted to add in
mySearch = getText('What do you want from Diana?')
print ("Top 5 Countries or something.: ", mySearch)






###Run lines from given inputs.(replace inputs with user variables)

import pandas as pd 
import os 

path = os.getcwd()

df = pd.read_csv('/Users/William/Desktop/ecommerceDAta.csv', encoding = 'unicode_escape')
len(df)


df_sample = df.sample(20)
df.info()
''' 0   InvoiceNo    541909 non-null  object 
 1   StockCode    541909 non-null  object 
 2   Description  540455 non-null  object 
 3   Quantity     541909 non-null  int64  
 4   InvoiceDate  541909 non-null  object 
 5   UnitPrice    541909 non-null  float64
 6   CustomerID   406829 non-null  float64
 7   Country      541909 non-null  object '''
 
#Top five countries within the df 
df.Country.value_counts().head(5) 
'''United Kingdom    495478
Germany             9495
France              8557
EIRE                8196
Spain               2533'''
df.groupby('Country')['Quantity'].sum().sort_values(ascending = False).head(5)
# =============================================================================
# eire = df[df['Country']=='EIRE']
# =============================================================================

unknown = ['?']

def clean (i):
    output1 = ~i.isin()
    return ({'huh': output1})

customerCountry = df[['CustomerID', 'Description', 'Quantity', 'Country']].sort_values(by= 'Quantity', ascending=False)
clean(customerCountry)['huh']
customerCountry = customerCountry[customerCountry['Description'].notna()]
customerCountry = customerCountry[customerCountry['CustomerID'].notna()]
test = customerCountry.head(5)
tes = customerCountry.tail(5).sort_values(by= 'Quantity', ascending= True)

customer= df.CustomerID.value_counts().head(5).to_frame().reset_index()
df.index.value_counts().head(5)

df['Costs'] = df['UnitPrice'] * df['Quantity']
costs = df[['Costs']].sort_values(by= 'Costs', ascending = False).round(0).head(5)

df['CustomerID'].nunique()

import datetime as dt
df['Date'] = df['InvoiceDate'].dt.InvoiceDate
df['InvoiceDate'].dtype
df['Date'] = pd.to_datetime(df['InvoiceDate']).dt.InvoiceDate


BinMonthdf = pd.date_range(start=df["InvoiceDate"].min(),end=df["InvoiceDate"].max(), freq = 'MS').to_pydatetime().tolist()
