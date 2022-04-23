# -*- coding: utf-8 -*-
"""
@author: Zachary
"""

from tkinter import *
import time
import socket
import sys
import client


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title('Grid Manager')
       
        ''' Row and Column Configuration '''
        for r in range(1):
            self.master.rowconfigure(r, weight=1)
           
        for c in range(2):
            self.master.columnconfigure(c, weight=1)
        
        ''' Initial Frames '''
        #top left room
        self.Frame1 = Frame(master, bg='grey', height=240, width=300, borderwidth=1)
        self.Frame1.grid(row=0, column=0)
        
        #middle room
        self.Frame2 = Frame(master, bg='grey', height=240, width=300, borderwidth=1)
        self.Frame2.grid(row=0, column=1)
        
        #top right room
        self.Frame3 = Frame(master, bg='grey', height=240, width=300, borderwidth=1)
        self.Frame3.grid(row=0, column=2)
        
        #bottom left room
        self.Frame4 = Frame(master, bg='grey', height=240, width=300, borderwidth=1)
        self.Frame4.grid(row=1, column=0)
        
        #bottom middle room
        self.Frame5 = Frame(master, bg='grey', height=240, width=300, borderwidth=1)
        self.Frame5.grid(row=1, column=1)
        
        #bottom right room
        self.Frame6 = Frame(master, bg='grey', height=240, width=300, borderwidth=1)
        self.Frame6.grid(row=1, column=2)
        
        ''' Empty desks '''
        self.pic_empty1 = PhotoImage(file='EmptyDesk.png')
        self.empty_sized1 = self.pic_empty1.subsample(2)
        self.empty_label1 = Label(self.Frame1, image=self.empty_sized1)
        self.empty_label1.grid(row=0, column=0)
        
        self.pic_empty2 = PhotoImage(file='EmptyDesk.png')
        self.empty_sized2 = self.pic_empty2.subsample(2)
        self.empty_label2 = Label(self.Frame2, image=self.empty_sized2)
        self.empty_label2.grid(row=0, column=1)
        
        self.pic_empty3 = PhotoImage(file='EmptyDesk.png')
        self.empty_sized3 = self.pic_empty3.subsample(2)
        self.empty_label3 = Label(self.Frame3, image=self.empty_sized3)
        self.empty_label3.grid(row=0, column=2)
        
        self.pic_empty4 = PhotoImage(file='EmptyDesk.png')
        self.empty_sized4 = self.pic_empty4.subsample(2)
        self.empty_label4 = Label(self.Frame4, image=self.empty_sized4)
        self.empty_label4.grid(row=1, column=0)
        
        self.pic_empty5 = PhotoImage(file='EmptyDesk.png')
        self.empty_sized5 = self.pic_empty5.subsample(2)
        self.empty_label5 = Label(self.Frame5, image=self.empty_sized5)
        self.empty_label5.grid(row=1, column=1)
        
        self.nextbutton = Button(self.Frame6, text='REFRESH',\
                                 compound=LEFT, font=('Verdana', 20), command=self.refresh)
        self.nextbutton.grid(row=1, column=2, sticky=S+E+W+N)
        
        ''' Full desk image'''
        # while True:
        #     self.refresh()
        
        
    def refresh(self):
        # Socket program to reach out to database
        ''' Full desk image'''
        self.pic_full = PhotoImage(file='BusyDesk.png')
        self.pic_sized = self.pic_full.subsample(2)
        
        
        
        check = client.main()
        
        if check==1:
            #assign a room to busy
            self.pic_label = Label(self.Frame2, image=self.pic_sized)
            self.pic_label.grid(row=0, column=1)
        
        # goes back to empty
        else:
            self.empty_label2 = Label(self.Frame2, image=self.empty_sized2)
            self.empty_label2.grid(row=0, column=1)
        
        
        
        
if __name__=="__main__":
    root = Tk()
    root.geometry("900x480")
    root.title("Library Locator")
    a = App(master=root)
    a.mainloop()