import tkinter as tk
import tkinter.ttk
from tkinter import messagebox
import turtle as t

win = tk.Tk()
win.geometry('1024x300')
win.title('BUV Sunshine Hotel Management')


firstfl = (101,102,103,104)
secondfl = (201,202,203,204)
thirdfl = (301,302,303,304)

firstst = []
secondst = []
thirdst = []
def loadstatus():
    f = open('first_status.txt', 'r')
    data = f.read().split()
    for i in data:
        firstst.append(i)
    f.close()

    f = open('second_status.txt', 'r')
    data = f.read().split()
    for i in data:
        secondst.append(i)
    f.close()

    f = open('third_status.txt', 'r')
    data = f.read().split()
    for i in data:
        thirdst.append(i)
    f.close()
loadstatus()

print("Welcome to hotel management system.")
#Button and combo box for room check
rmlbl = tk.Label(text='Room number:')
rmlbl.grid(column=0,row=0)
rmcbbox = tkinter.ttk.Combobox()
rmcbbox.grid(column=1,row=0)
rmcbbox['value']=[101,102,103,104,201,202,203,204,301,302,303,304]
lblchoose = tk.Label(text='Please choose room')
lblchoose.grid(column=5,row=0,sticky='E')

#check room status function
def chksts():
    n = 0
    r = int(rmcbbox.get())
    for i in firstfl:
        if i == r:
            lblchoose.config(text='Room chosen :'+str(r)+' '+firstst[n])
        else:
            n +=1
    n = 0
    for i in secondfl:
        if i == r:
            lblchoose.config(text='Room chosen :'+str(r)+' '+secondst[n])
        else:
            n +=1
    n = 0
    for i in thirdfl:
        if i == r:
            lblchoose.config(text='Room chosen :'+str(r)+' '+thirdst[n])
        else:
            n +=1

btn_cf = tk.Button(text='Confirm',command=chksts)
btn_cf.grid(column=2,row=0)

#Label action
lblaction = tk.Label(text='Make change to chosen room:')
lblaction.grid(column=0,row=1)

#Combobox action
ltsaction = tkinter.ttk.Combobox()
ltsaction.grid(column=1,row=1)
ltsaction['value']=['Make occupied','Make reserved','Make available']


def btnclick():
    slt = str(ltsaction.get())
    if slt == str('Make occupied'):
        occupy()
    elif slt == str('Make reserved'):
        reserve()
    elif slt == str('Make available'):
        available()

#Button action
btn_action = tk.Button(text='OK',command=btnclick)
btn_action.grid(column=2,row=1)


def available():
    n = 0
    r = int(rmcbbox.get())
    for i in firstfl:
        if i == r:
            firstst[n] = 'Available'
            lblchoose.config(text='Room chosen :' + str(r) + ' ' + firstst[n])
            print(firstst)
            tk.messagebox.showinfo('Alert', 'Room ' + str(r) + ' has been updated successfully.')
            f = open('first_status.txt','w').close()
            f = open('first_status.txt', 'w')
            for i in firstst:
                print(i)
                f.write(str(i))
                f.write('\n')
            f.close()
        else: n+=1
    n = 0
    for i in secondfl:
        if i == r:
            secondst[n] = 'Available'
            lblchoose.config(text='Room chosen :' + str(r) + ' ' + secondst[n])
            tk.messagebox.showinfo('Alert', 'Room ' + str(r) + ' has been updated successfully.')
            f = open('second_status.txt', 'w').close()
            f = open('second_status.txt', 'w')
            for i in secondst:
                print(i)
                f.write(str(i))
                f.write('\n')
            f.close()
        else: n+=1
    n = 0
    for i in thirdfl:
        if i == r:
            thirdst[n] = 'Available'
            lblchoose.config(text='Room chosen :' + str(r) + ' ' + thirdst[n])
            tk.messagebox.showinfo('Alert', 'Room ' + str(r) + ' has been updated successfully.')
            f = open('third_status.txt', 'w').close()
            f = open('third_status.txt', 'w')
            for i in thirdst:
                print(i)
                f.write(str(i))
                f.write('\n')
            f.close()
        else: n+=1

def occupy():
    n = 0
    r = int(rmcbbox.get())
    for i in firstfl:
        if i == r:
            firstst[n] = 'Occupied'
            lblchoose.config(text='Room chosen :' + str(r) + ' ' + firstst[n])
            tk.messagebox.showinfo('Alert', 'Room ' + str(r) + ' has been updated successfully.')
        else: n+=1
    n = 0
    for i in secondfl:
        if i == r:
            secondst[n] = 'Occupied'
            lblchoose.config(text='Room chosen :' + str(r) + ' ' + secondst[n])
            tk.messagebox.showinfo('Alert', 'Room ' + str(r) + ' has been updated successfully.')
        else: n+=1
    n = 0
    for i in thirdfl:
        if i == r:
            thirdst[n] = 'Occupied'
            lblchoose.config(text='Room chosen :' + str(r) + ' ' + thirdst[n])
            tk.messagebox.showinfo('Alert', 'Room ' + str(r) + ' has been updated successfully.')
        else: n+=1

def reserve():
    n = 0
    r = int(rmcbbox.get())
    for i in firstfl:
        if i == r:
            if firstst[n] == str('Available'):
                firstst[n] = 'Reserved'
                lblchoose.config(text='Room chosen :' + str(r) + ' ' + firstst[n])
                tk.messagebox.showinfo('','Room ' + str(r) + ' has been updated successfully.')
            else:
                tk.messagebox.showinfo('','This room is occupied and cannot be reserved.')
        else: n+=1
    n = 0
    for i in secondfl:
        if i == r:
            if secondst[n] == str('Available'):
                secondst[n] = 'Reserved'
                lblchoose.config(text='Room chosen :' + str(r) + ' ' + secondst[n])
                tk.messagebox.showinfo('', 'Room ' + str(r) + ' has been updated successfully.')
            else:
                tk.messagebox.showinfo('', 'This room is occupied and cannot be reserved.')
        else:
            n += 1
    n = 0
    for i in thirdfl:
        if i == r:
            if thirdst[n] == str('Available'):
                thirdst[n] = 'Reserved'
                lblchoose.config(text='Room chosen :' + str(r) + ' ' + thirdst[n])
                tk.messagebox.showinfo('', 'Room ' + str(r) + ' has been updated successfully.')
            else:
                tk.messagebox.showinfo('', 'This room is occupied and cannot be reserved.')
        else:
            n += 1

def map():
    t.speed(10)
    for i in range(4):
        for i in range(4):
            t.forward(100)
            t.left(90)
        t.forward(100)

    t.penup()
    t.goto(0, 100)
    t.pendown()
    for i in range(4):
        for i in range(4):
            t.forward(100)
            t.left(90)
        t.forward(100)

    t.penup()
    t.goto(0, 200)
    t.pendown()
    for i in range(4):
        for i in range(4):
            t.forward(100)
            t.left(90)
        t.forward(100)


    t.penup()
    t.goto(50, 50)
    t.write(101)
    t.pendown()

    t.penup()
    t.goto(150, 50)
    t.write(102)
    t.pendown()

    t.penup()
    t.goto(250, 50)
    t.write(103)
    t.pendown()

    t.penup()
    t.goto(350, 50)
    t.write(104)
    t.pendown()

    t.penup()
    t.goto(50, 150)
    t.write(201)
    t.pendown()

    t.penup()
    t.goto(150, 150)
    t.write(202)
    t.pendown()

    t.penup()
    t.goto(250, 150)
    t.write(203)
    t.pendown()

    t.penup()
    t.goto(350, 150)
    t.write(204)
    t.pendown()

    t.penup()
    t.goto(50, 250)
    t.write(301)
    t.pendown()

    t.penup()
    t.goto(50, 250)
    t.write(301)
    t.pendown()

    t.penup()
    t.goto(150, 250)
    t.write(302)
    t.pendown()

    t.penup()
    t.goto(250, 250)
    t.write(303)
    t.pendown()

    t.penup()
    t.goto(350, 250)
    t.write(304)
    t.pendown()



btn_map = tk.Button(text='Show hotel rooms map',command=map)
btn_map.grid(column=2,row=3)



win.mainloop()
t.mainloop()
