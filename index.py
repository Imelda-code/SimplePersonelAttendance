# import all  necessary libraries
from tkinter import *
import threading
import queue as Queue
import time
import cv2
import datetime
import sqlite3

now = datetime.datetime.now()
screen = Tk()
screen.geometry("500x500")
screen.title("Form")

firstname = StringVar()
lastname = StringVar()
var = IntVar()
c = StringVar()

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
img_counter = 0
frame_set = []
start_time = time.time()

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if time.time() - start_time >= 5: # Verifying the time interval
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_counter))
        start_time = time.time()
    img_counter += 1
# cap.release
# cv2.destroyAllWindows


def database():
    firstname1 = firstname.get()
    lastname1 = lastname.get()
    gender1 = var.get()
    status1 = c.get()
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Attendance (firstname TEXT,lastname TEXT,gender TEXT,status TEXT)')
    cursor.execute('INSERT INTO Attendance (firstname, lastname, gender, status) VALUES(?, ?, ?, ?)',
                   (firstname1, lastname1, gender1, status1))
    conn.commit()


heading = Label(screen, text="Attendance for " + now.strftime("%Y-%m-%d"),
                width="20", font=('Vendeta', 20))
heading.place(x=90, y=53)

first_name = Label(screen, text="firstname*: ", width=20, font=('bold', 13))
first_name.place(x=80, y=130)
firstname_entry = Entry(textvariable=firstname)
firstname_entry.place(x=240, y=130)

last_name = Label(text="lastname*: ", width=20, font=('bold', 13))
last_name.place(x=80, y=180)
lastname_entry = Entry(textvariable=lastname)
lastname_entry.place(x=240, y=180)

# checkbox
gen_der = Label(screen, text="Gender: ", width=20, font=('bold', 13))
gen_der.place(x=70, y=230)
Radiobutton(screen, text='Male', padx=5, variable=var, value=1).place(x=235, y=230)
Radiobutton(screen, text='Female', padx=20, variable=var, value=2).place(x=290, y=230)

# dropdown menu
status = Label(text="status : ", width=20, font=('bold', 13))
status.place(x=70, y=280)
list1 = ['Intern', 'Staff']
droplist = OptionMenu(screen, c, *list1)
droplist.config(width=15)
c.set('select your status')
droplist.place(x=240, y=274)

start_time = Label(text="start time: " + now.strftime("%H:%M:%S"), font=('bold', 13))
start_time.place(x=200, y=340)
# start_time =
ok_button = Button(text='OK', font=('Vendeta', 16, 'bold'),
                   command=lambda :[database, screen.destroy()], bg='lightblue', fg='black')
ok_button.place(x=240, y=400)
screen.mainloop()
