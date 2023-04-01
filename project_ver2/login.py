import tkinter as tk 
from tkinter import *
from tkinter import ttk 
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
from dashboard import IMS
from billing import BillClass

root = Tk()
connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='prj_ver2')
c = connection.cursor()

# width and height
w = 450
h = 600
# background color
bgcolor = "#242323"

# ----------- CENTER FORM ------------- #
root.overrideredirect(1) # remove border
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws-w)/2
y = (hs-h)/2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# ----------- HEADER ------------- #
def close_win(self):
    root.destroy()

headerframe = tk.Frame(root, highlightbackgroun='#242323', highlightcolor='#242323', 
                       highlightthickness=2, bg='#242323', width=w, height=70)
titleframe = tk.Frame(headerframe, bg='#242323', padx=1, pady=1)
title_label = tk.Label(titleframe, text='Login', padx=20, pady=5, bg='#242323', 
                       fg='#de108b', font=('Tahoma',24), width=8)
close_label = tk.Label(headerframe, text='x', bg="#242323", fg="#eb1d0e", cursor="hand2",
                         font=('Verdana',15))
close_label.bind("<ButtonRelease-1>",close_win)

headerframe.pack()
titleframe.pack()
title_label.pack()
close_label.pack()

titleframe.place(y=26, relx=0.5, anchor=CENTER)
close_label.place(x=410, y=5)

def on_enter(self):
    username_entry.delete(0, "end")

def on_leave(self):
    name = username_entry.get()
    if name =="":
        username_entry.insert(0,"Username")

def on_enter2(self):
    password_entry.delete(0, "end")

def on_leave2(self):
    password_ = password_entry.get()
    if password_ =="":
        password_entry.insert(0,"Password")

def on_enter3(self):
    fullname_entry_rg.delete(0, "end")

def on_leave3(self):
    fullname = fullname_entry_rg.get()
    if fullname =="":
        fullname_entry_rg.insert(0,"Fullname")

def on_enter4(self):
    username_entry_rg.delete(0, "end")

def on_leave4(self):
    username = username_entry_rg.get()
    if username =="":
        username_entry_rg.insert(0,"Username")

def on_enter5(self):
    password_entry_rg.delete(0, "end")

def on_leave5(self):
    password_2 = password_entry_rg.get()
    if password_2 =="":
        password_entry_rg.insert(0,"Password")

def on_enter6(self):
    confirmpass_entry_rg.delete(0, "end")

def on_leave6(self):
    password_3 = confirmpass_entry_rg.get()
    if password_3 =="":
        confirmpass_entry_rg.insert(0,"Re-password")

def on_enter7(self):
    phone_entry_rg.delete(0, "end")

def on_leave7(self):
    phone= phone_entry_rg.get()
    if phone =="":
        phone_entry_rg.insert(0,"Phone")

def on_enter8(self):
    address_entry_rg.delete(0, "end")

def on_leave8(self):
    address = address_entry_rg.get()
    if address =="":
        address_entry_rg.insert(0,"Address")

def hide():
    open_eye.config(file='C:/Git/python_prj/project_ver2/picture/eye1.png')
    password_entry.config(show="*")
    eye_button.config(command=show)

def show():
    open_eye.config(file='C:/Git/python_prj/project_ver2/picture/view1.png')
    password_entry.config(show="")
    eye_button.config(command=hide)


def hide2():
    open_eye2.config(file='C:/Git/python_prj/project_ver2/picture/eye1.png')
    password_entry_rg.config(show="*")
    eye_button2.config(command=show2)

def show2():
    open_eye2.config(file='C:/Git/python_prj/project_ver2/picture/view1.png')
    password_entry_rg.config(show="")
    eye_button2.config(command=hide2)

def hide3():
    open_eye3.config(file='C:/Git/python_prj/project_ver2/picture/eye1.png')
    confirmpass_entry_rg.config(show="*")
    eye_button3.config(command=show3)

def show3():
    open_eye3.config(file='C:/Git/python_prj/project_ver2/picture/view1.png')
    confirmpass_entry_rg.config(show="")
    eye_button3.config(command=hide3)

# ----------- END HEADER ------------- #

mainframe = tk.Frame(root, width=w, height=h)

# ----------- Login Page ------------- #
loginframe = tk.Frame(mainframe, width=w, height=h)
login_contentframe = tk.Frame(loginframe, padx=30, pady=100, 
                     highlightbackgroun='#242323', highlightcolor='#242323', 
                     highlightthickness=2, bg=bgcolor)

#username_label = tk.Label(login_contentframe, text='Username:', fg="#de108b",font=('Verdana',16), bg=bgcolor)
#password_label = tk.Label(login_contentframe, text='Password:', font=('Verdana',16), bg=bgcolor, fg="#de108b")
user_type_label_rg = tk.Label(login_contentframe, text='Login as:', 
                           font=('Verdana',14), bg=bgcolor, fg="#de108b")

username_entry = tk.Entry(login_contentframe, font=('Verdana',16), width=28, bg=bgcolor, fg="#de108b", border=0)
username_entry.insert(0,"Username")
frame1 = tk.Frame(login_contentframe, height=2, width=370, bg="#de108b")

username_entry.bind("<FocusIn>", on_enter)
username_entry.bind("<FocusOut>", on_leave)

password_entry = tk.Entry(login_contentframe, font=('Verdana',16), width=28, bg=bgcolor, fg="#de108b", border=0)
password_entry.insert(0,"Password")
frame2 = tk.Frame(login_contentframe, height=2, width=370, bg="#de108b")

password_entry.bind("<FocusIn>", on_enter2)
password_entry.bind("<FocusOut>", on_leave2)

open_eye = tk.PhotoImage(file='C:/Git/python_prj/project_ver2/picture/view1.png')

eye_button = tk.Button(login_contentframe, image=open_eye, bd=0, bg=bgcolor, activebackground=bgcolor, cursor="hand2", command=hide)
eye_button.place(x=345, y=69)

radiosframe3 = tk.Frame(login_contentframe)
user_type = StringVar()
user_type.set('Customer')
customer_radiobutton = tk.Radiobutton(radiosframe3, text='Customer', font=('Verdana',14), 
                                  bg=bgcolor,fg="#de108b", variable=user_type, value='Customer')
seller_radiobutton = tk.Radiobutton(radiosframe3, text='Seller', font=('Verdana',14), 
                                    bg=bgcolor,fg="#de108b", variable=user_type, value='Seller')

login_button = tk.Button(login_contentframe,text="Login", font=('Verdana',16), 
                         bg='#de108b',fg='white', padx=25, pady=10, width=25)

go_register_label = tk.Label(login_contentframe, 
                    text=">> Don't have an account? Create one" , cursor="hand2",
                    font=('Verdana',10), bg=bgcolor, fg='white')

mainframe.pack(fill='both', expand=1)
loginframe.pack(fill='both', expand=1)
login_contentframe.pack(fill='both', expand=1)

#username_label.grid(row=0, column=0, pady=10)
username_entry.grid(row=0, column=0, columnspan=3, pady=10)
frame1.grid(row=1, column=0, columnspan=3)
#password_label.grid(row=1, column=0, pady=10)
password_entry.grid(row=2, column=0, columnspan=3, pady=10)
frame2.grid(row=3, column=0, columnspan=3)
user_type_label_rg.grid(row=4, column=0, pady=10)
radiosframe3.grid(row=4,column=1)
customer_radiobutton.grid(row=0, column=0)
seller_radiobutton.grid(row=0, column=1)

login_button.grid(row=5, column=0, columnspan=2, pady=40)

go_register_label.grid(row=6, column=0, columnspan=2, pady=20)

# create a function to display the register frame
def go_to_register():
    loginframe.forget()
    registerframe.pack(fill="both", expand=1)
    title_label['text'] = 'Register'
    title_label['bg'] = '#242323'


go_register_label.bind("<Button-1>", lambda page: go_to_register())


# create a function to make the user login
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    user_type_value = user_type.get()
    vals = (username, password, user_type_value)
    select_query = "SELECT * FROM `users` WHERE `user_name` = %s and `password` = %s and `type` = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        if user_type_value == "Seller":
            #messagebox.showinfo('Test','Test')
            mainformwindow = tk.Toplevel()
            app = IMS(mainformwindow)
            root.withdraw() # hide the root
            mainformwindow.protocol("WM_DELETE_WINDOW", close_win) # close the app
        else:
            mainformwindow = tk.Toplevel()
            app = BillClass(mainformwindow)
            root.withdraw() # hide the root
            mainformwindow.protocol("WM_DELETE_WINDOW", close_win)
    else:
        messagebox.showwarning('Error','wrong username, password or login perspective')



login_button['command'] = login


# ----------- Register Page ------------- #

registerframe = tk.Frame(mainframe, width=w, height=h)
register_contentframe = tk.Frame(registerframe, padx=15, pady=15, 
                        highlightbackgroun='#242323', highlightcolor='#242323', 
                        highlightthickness=2, bg=bgcolor)

fullname_label_rg = tk.Label(register_contentframe, text='Fullname:', 
                             font=('Verdana',14),fg="#de108b", bg=bgcolor)
username_label_rg = tk.Label(register_contentframe, text='Username:', 
                             font=('Verdana',14), fg="#de108b",bg=bgcolor)
password_label_rg = tk.Label(register_contentframe, text='Password:', 
                             font=('Verdana',14), fg="#de108b",bg=bgcolor)
confirmpass_label_rg = tk.Label(register_contentframe, text='Re-Password:', 
                                font=('Verdana',14),fg="#de108b", bg=bgcolor)
phone_label_rg = tk.Label(register_contentframe, text='Phone:', 
                          font=('Verdana',14), fg="#de108b",bg=bgcolor)
gender_label_rg = tk.Label(register_contentframe, text='Gender:', 
                           font=('Verdana',14), fg="#de108b",bg=bgcolor)
address_label_rg = tk.Label(register_contentframe, text='Address:', 
                           font=('Verdana',14), fg="#de108b",bg=bgcolor)
type_person_label_rg = tk.Label(register_contentframe, text='Type:', 
                           font=('Verdana',14), fg="#de108b",bg=bgcolor)



fullname_entry_rg = tk.Entry(register_contentframe, font=('Verdana',16), width=28, bg=bgcolor, fg="#de108b", border=0)
fullname_entry_rg.insert(0,"Fullname")
frame3 = tk.Frame(register_contentframe, height=2, width=370, bg="#de108b")

fullname_entry_rg.bind("<FocusIn>", on_enter3)
fullname_entry_rg.bind("<FocusOut>", on_leave3)

username_entry_rg = tk.Entry(register_contentframe, font=('Verdana',16), width=28, bg=bgcolor, fg="#de108b", border=0)
username_entry_rg.insert(0,"Username")
frame4 = tk.Frame(register_contentframe, height=2, width=370, bg="#de108b")

username_entry_rg.bind("<FocusIn>", on_enter4)
username_entry_rg.bind("<FocusOut>", on_leave4)


password_entry_rg = tk.Entry(register_contentframe, font=('Verdana',16), width=28, bg=bgcolor, fg="#de108b", border=0)
password_entry_rg.insert(0,"Password")
frame5 = tk.Frame(register_contentframe, height=2, width=370, bg="#de108b")

password_entry_rg.bind("<FocusIn>", on_enter5)
password_entry_rg.bind("<FocusOut>", on_leave5)

open_eye2 = tk.PhotoImage(file='C:/Git/python_prj/project_ver2/picture/view1.png')

eye_button2 = tk.Button(register_contentframe, image=open_eye2, bd=0, bg=bgcolor, activebackground=bgcolor, cursor="hand2", command=hide2)
eye_button2.place(x=345, y=120)


confirmpass_entry_rg = tk.Entry(register_contentframe, font=('Verdana',16), width=28, bg=bgcolor, fg="#de108b", border=0)
confirmpass_entry_rg.insert(0,"Re-password")
frame6 = tk.Frame(register_contentframe, height=2, width=370, bg="#de108b")

confirmpass_entry_rg.bind("<FocusIn>", on_enter6)
confirmpass_entry_rg.bind("<FocusOut>", on_leave6)

open_eye3 = tk.PhotoImage(file='C:/Git/python_prj/project_ver2/picture/view1.png')

eye_button3 = tk.Button(register_contentframe, image=open_eye3, bd=0, bg=bgcolor, activebackground=bgcolor, cursor="hand2", command=hide3)
eye_button3.place(x=345, y=169)


phone_entry_rg = tk.Entry(register_contentframe, font=('Verdana',16), width=28, bg=bgcolor, fg="#de108b", border=0)
phone_entry_rg.insert(0,"Phone")
frame7 = tk.Frame(register_contentframe, height=2, width=370, bg="#de108b")

phone_entry_rg.bind("<FocusIn>", on_enter7)
phone_entry_rg.bind("<FocusOut>", on_leave7)


address_entry_rg = tk.Entry(register_contentframe, font=('Verdana',16), width=28, bg=bgcolor, fg="#de108b", border=0)
address_entry_rg.insert(0,"Address")
frame8 = tk.Frame(register_contentframe, height=2, width=370, bg="#de108b")

address_entry_rg.bind("<FocusIn>", on_enter8)
address_entry_rg.bind("<FocusOut>", on_leave8)


#fullname_entry_rg = tk.Entry(register_contentframe, font=('Verdana',14), width=22)
#username_entry_rg = tk.Entry(register_contentframe, font=('Verdana',14), width=22)
#password_entry_rg = tk.Entry(register_contentframe, font=('Verdana',14), width=22,  show='*')
#confirmpass_entry_rg = tk.Entry(register_contentframe, font=('Verdana',14), width=22, show='*')
#phone_entry_rg = tk.Entry(register_contentframe, font=('Verdana',14), width=22)
#address_entry_rg = tk.Entry(register_contentframe, font=('Verdana',14), width=22)

radiosframe1 = tk.Frame(register_contentframe)
gender = StringVar()
gender.set('Male')
male_radiobutton = tk.Radiobutton(radiosframe1, text='Male', font=('Verdana',14), 
                                  bg=bgcolor,fg="#de108b", variable=gender, value='Male')
female_radiobutton = tk.Radiobutton(radiosframe1, text='Female', font=('Verdana',14), 
                                    bg=bgcolor,fg="#de108b", variable=gender, value='Female')

radiosframe2 = tk.Frame(register_contentframe)
person = StringVar()
person.set('Customer')
customer_radiobutton = tk.Radiobutton(radiosframe2, text='Customer', font=('Verdana',14), 
                                  bg=bgcolor,fg="#de108b", variable=person, value='Customer')
seller_radiobutton = tk.Radiobutton(radiosframe2, text='Seller', font=('Verdana',14), 
                                    bg=bgcolor,fg="#de108b", variable=person, value='Seller')

register_button = tk.Button(register_contentframe,text="Register", font=('Verdana',16)
                            , bg='#de108b',fg='white', padx=25, pady=10, width=25)

go_login_label = tk.Label(register_contentframe, 
                          text=">> Already have an account? Sign in" , cursor="hand2", 
                          font=('Verdana',10), bg=bgcolor, fg='white')

#mainframe.pack(fill='both', expand=1)
#registerframe.pack(fill='both', expand=1)
register_contentframe.pack(fill='both', expand=1)

fullname_entry_rg.grid(row=0, column=0, columnspan=3, pady=10)
frame3.grid(row=1, column=0, columnspan=3)
username_entry_rg.grid(row=2,column=0,columnspan=3,pady=10)
frame4.grid(row=3, column=0, columnspan=3)
password_entry_rg.grid(row=4, column=0, columnspan=3, pady=10)
frame5.grid(row=5, column=0, columnspan=3)
confirmpass_entry_rg.grid(row=6, column=0,columnspan=3, pady=10)
frame6.grid(row=7, column=0, columnspan=3)
phone_entry_rg.grid(row=8,column=0,columnspan=3,pady=10)
frame7.grid(row=9, column=0, columnspan=3)
address_entry_rg.grid(row=10,column=0,columnspan=3,pady=10)
frame8.grid(row=11, column=0, columnspan=3)

"""fullname_label_rg.grid(row=0, column=0, pady=5, sticky='e')
fullname_entry_rg.grid(row=0, column=1)

username_label_rg.grid(row=1, column=0, pady=5, sticky='e')
username_entry_rg.grid(row=1, column=1)

password_label_rg.grid(row=2, column=0, pady=5, sticky='e')
password_entry_rg.grid(row=2, column=1)

confirmpass_label_rg.grid(row=3, column=0, pady=5, sticky='e')
confirmpass_entry_rg.grid(row=3, column=1)

phone_label_rg.grid(row=4, column=0, pady=5, sticky='e')
phone_entry_rg.grid(row=4, column=1)

address_label_rg.grid(row=5, column=0, pady=5, sticky='e')
address_entry_rg.grid(row=5, column=1)"""

gender_label_rg.grid(row=12, column=0, pady=5, sticky='e')
radiosframe1.grid(row=12, column=1)
male_radiobutton.grid(row=0, column=0)
female_radiobutton.grid(row=0, column=1)

type_person_label_rg.grid(row=13, column=0, pady=5, sticky='e')
radiosframe2.grid(row=13, column=1)
customer_radiobutton.grid(row=0, column=0)
seller_radiobutton.grid(row=0, column=1)


register_button.grid(row=14, column=0, columnspan=2, pady=10)

go_login_label.grid(row=15, column=0, columnspan=2, pady=10)


# create a function to display the login frame
def go_to_login():
    registerframe.forget()
    loginframe.pack(fill="both", expand=1)
    title_label['text'] = 'Login'
    title_label['bg'] = '#242323'


go_login_label.bind("<Button-1>", lambda page: go_to_login())
# --------------------------------------- #

# create a function to check if the username already exists
def check_username(username):
    username = username_entry_rg.get().strip()
    vals = (username,)
    select_query = "SELECT * FROM `users` WHERE `user_name` = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        return True
    else:
        return False

# --------------------------------------- #


# create a function to register a new user
def register():

    full_name = fullname_entry_rg.get().strip() # remove white space
    user_name = username_entry_rg.get().strip()
    password = password_entry_rg.get().strip()
    confirm_password = confirmpass_entry_rg.get().strip()
    phone_number = phone_entry_rg.get().strip()
    address = address_entry_rg.get().strip()
    gdr = gender.get()
    type_person = person.get()

    if len(full_name) > 0 and  len(user_name) > 0 and len(password) > 0 and len(phone_number) > 0 and len(address)> 0:
        if check_username(user_name) == False: 
            if password == confirm_password:
                vals = (full_name, user_name, password, phone_number, gdr, address, type_person)
                insert_query = "INSERT INTO `users`(`full_name`, `user_name`, `password`, `phone_number`, `gender`, `address`, `type`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                c.execute(insert_query, vals)
                connection.commit()
                messagebox.showinfo('Register','your account has been created successfully')
                go_to_login()
                
            else:
                messagebox.showwarning('Password','incorrect password confirmation')
        else:
            messagebox.showwarning('Duplicate Username','This Username Already Exists, try another one')
    else:
        messagebox.showwarning('Empty Fields','make sure to enter all the information')

register_button['command'] = register

# --------------------------------------- #

# ------------------------------------------------------------------------ #


root.mainloop()