from tkinter import *
import calendar
import datetime

class Calendar:
    def __init__(self, root):
        self.root = root
        self.current_time = datetime.datetime.now()
        self.year = self.current_time.year
        self.month = self.current_time.month
        self.day = self.current_time.day

        self.back_button = Button(self.root, text='<', command=self.move_back)
        self.back_button.grid(row=0, column=5, sticky=NSEW)
        self.forward_button = Button(self.root, text='>', command=self.move_forward)
        self.forward_button.grid(row=0, column=6, sticky=NSEW)

        for w_day in range(7):
            lbl = Label(self.root, text=calendar.day_abbr[w_day], width=1, height=1, font='Arial 10 bold', fg='gray30')
            lbl.grid(row=1, column=w_day, sticky=NSEW)

        self.fill_month()

    def move_back(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.fill_month()

    def move_forward(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.fill_month()

    def fill_month(self):
        top_lbl = Label(self.root, text=f'{calendar.month_name[self.month]} {self.year}', width=1, height=1,
                        font='Arial 16 bold',
                        fg='black')
        top_lbl.grid(row=0, column=0, columnspan=5, sticky=NSEW)  # Объединяем с 0-й по 4-ю ячейки в одну

        self.week_day, self.month_days = calendar.monthrange(self.year, self.month)  # День недели начала месяца и число дней в месяце

        if self.month == 1:
            self.back_month_days = calendar.monthrange(self.year - 1, 12)[1]
        else:
            self.back_month_days = calendar.monthrange(self.year, self.month - 1)[1]

        for row in range(2, 8):
            for column in range(7):
                num_day = (row - 2) * 7 + column  # Номер дня на календаре: 0, ..., 41
                if self.week_day <= num_day <= self.week_day + self.month_days - 1:  # Текущий месяц
                    self.fill_this_month(row, column, num_day)
                elif num_day < self.week_day:
                    self.fill_beginning(row, column, num_day)
                else:
                    self.fill_end(row, column, num_day)

    def fill_beginning(self, row, column, num_day):
        lbl = Label(self.root, text=self.back_month_days - self.week_day + 1 + num_day, width=4, height=2, font='Arial 16 bold', fg='gray30')
        lbl.grid(row=row, column=column, sticky=NSEW)
    def fill_end(self, row, column, num_day):
        lbl = Label(self.root, text=num_day - self.month_days - self.week_day + 1, width=4, height=2, font='Arial 16 bold', fg='gray30')
        lbl.grid(row=row, column=column, sticky=NSEW)
    def fill_this_month(self, row, column, num_day):
        lbl = Label(self.root, text=num_day - self.week_day + 1, width=4, height=2, font='Arial 16 bold', fg='black')
        lbl.grid(row=row, column=column, sticky=NSEW)

        if self.year == self.current_time.year and self.month == self.current_time.month and self.current_time.day == (num_day - self.week_day + 1):
            lbl['fg'] = 'white'
            lbl['bg'] = 'blue'
def main():
    root = Tk()  # Окно приложения
    root.title('Task manager')
    cal = Calendar(root)
    root.mainloop() # Запускаем постоянный цикл, чтобы программа работала

if __name__ == '__main__':
    main()
