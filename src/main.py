from tkinter import *
import calendar
import datetime

root = Tk() # Окно приложения
root.title('Task manager')

current_time = datetime.datetime.now()
year = current_time.year
month = current_time.month

back_button = Button(root, text='<')
back_button.grid(row=0, column=0, sticky=NSEW)
next_button = Button(root, text='>')
next_button.grid(row=0, column=6, sticky=NSEW)

lbl = Label(root, text='0', width=1, height=1, font='Arial 16 bold', fg='blue')
lbl.grid(row=0, column=1, sticky=NSEW)

for day in range(7):
    lbl = Label(root, text=calendar.day_abbr[day], width=1, height=1, font='Arial 10 bold', fg='darkblue')
    lbl.grid(row=1, column=day, sticky=NSEW)

days = [] # ??
for row in range(2, 8):
    for column in range(7):
        lbl = Label(root, text='0', width=4, height=2, font='Arial 16 bold', fg='blue')
        lbl.grid(row=row, column=column, sticky=NSEW)

days.append(lbl)
print(*calendar.day_abbr)

root.mainloop() # Запускаем постоянный цикл, чтобы программа работала