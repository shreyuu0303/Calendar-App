import calendar
from tkinter import *

def show_calendar():
    try:
        year=int(year_enter.get())
        month=int(month_enter.get())
        cal_output=calendar.month(year,month)
        Text_area.delete("1.0",END)
        Text_area.insert(END,cal_output)
    except ValueError:
        Text_area.delete("1.0",END)
        Text_area.insert(END,"please  enter your month and year")

root=Tk()
root.title("Calender app")
root.geometry("300x350")
root.resizable(False,False)

Label(root,text="Calender app",font=("Arial",16,"bold")).pack(pady=10)


#enter the year
Label(root,text="Enter year").pack()
year_enter=Entry(root,width=10)
year_enter.pack(pady=5)

Label(root,text="enter month (1-12)").pack()
month_enter=Entry(root,width=10)
month_enter.pack(pady=5)

Button(root,text="show calender",command=show_calendar).pack(pady=10)

Text_area=Text(root,width=28,height=10,font=("courier",10))
Text_area.pack(pady=5)

Scrollbar=Scrollbar(root,command=Text_area.yview)
Scrollbar.pack(side=RIGHT,fill=Y)
Text_area.config(yscrollcommand=Scrollbar.set)

root.mainloop()