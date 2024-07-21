from tkinter import *
import calendar
import datetime

root = Tk() # Окно приложения
root.title('Task manager')

back_button = Button(root, text='<')
back_button.grid(row=0, column=5, sticky=NSEW)
next_button = Button(root, text='>')
next_button.grid(row=0, column=6, sticky=NSEW)

current_time = datetime.datetime.now()
year = current_time.year
month = current_time.month
day = current_time.day

top_lbl = Label(root, text=f'{calendar.month_name[month]}, {year}', width=1, height=1, font='Arial 16 bold', fg='blue')
top_lbl.grid(row=0, column=0, columnspan=5, sticky=NSEW) # Объединяем с 1-й по 5-ю ячейки в одну


####
week_day, month_days = calendar.monthrange(year, month)  # День недели начала месяца и число дней в месяце

if month == 1:
    back_month_days = calendar.monthrange(year - 1, 12)[1]
else:
    back_month_days = calendar.monthrange(year, month - 1)[1]
def fill_beginning():
    lbl = Label(root, text=back_month_days - week_day + 1 + num_day, width=4, height=2, font='Arial 16 bold', fg='gray30')
    lbl.grid(row=row, column=column, sticky=NSEW)
def fill_end():
    lbl = Label(root, text=num_day - month_days - week_day + 1, width=4, height=2, font='Arial 16 bold', fg='gray30')
    lbl.grid(row=row, column=column, sticky=NSEW)
def fill_this_month(): #
    lbl = Label(root, text=num_day - week_day + 1, width=4, height=2, font='Arial 16 bold', fg='black')
    lbl.grid(row=row, column=column, sticky=NSEW)

    if day == (num_day - week_day + 1):
        lbl['fg'] = 'white'
        lbl['bg'] = 'blue'

for w_day in range(7):
    lbl = Label(root, text=calendar.day_abbr[w_day], width=1, height=1, font='Arial 10 bold', fg='gray30')
    lbl.grid(row=1, column=w_day, sticky=NSEW)


for row in range(2, 8):
    for column in range(7):
        num_day = (row - 2) * 7 + column # Номер дня на календаре: 0, ..., 41
        if week_day <= num_day <= week_day + month_days - 1: # Текущий месяц
            fill_this_month()
        elif num_day < week_day:
            fill_beginning()
        else:
            fill_end()

root.mainloop() # Запускаем постоянный цикл, чтобы программа работала