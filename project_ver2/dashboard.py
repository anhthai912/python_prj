from tkinter import *
from PIL import Image, ImageTk
from modify_product import modify_product_class
from sales import sale_class

# unified file path
import os
script_dir = os.path.dirname("D://bi12-year2/advpython/project/python_prj/")

class IMS:
    def __init__(self, root):
        self.root = root
        
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        self.root.geometry("%sx%s+%s+%s" % (ws - 10,hs - 35,0,0))
        self.root.title("Food Market Information Management System")
        self.root.config(bg="white")
#title
        title = Label(self.root, text="Food Market Information Management System", bd=2,font=("times new roman", 40, "bold"), bg="#242323", fg="#de108b").place(x=0, y=0, relwidth=1, height=70)
#left menu

        left_menu = Frame(self.root, bd=0, relief=RIDGE, bg="#242323")
        left_menu.place(x=0, y=70, width=200, height=1010)

        label_left_menu = Label(left_menu, text = "Menu", font = ("times new roman", 20), bg="#242323", fg="#de108b").pack(side = TOP, fill = X)
        button_modify_product = Button(left_menu, text = ">> Modify",command=self.modify_product, font = ("times new roman", 20, "bold"), bg="#242323", bd=0, cursor="hand2", fg="#de108b").pack(side = TOP, fill = X)
        self.photo1=Image.open(os.path.join(script_dir,"project_ver2/picture/checklist3.png"))
        self.photo1=ImageTk.PhotoImage(self.photo1)
        
        lbl_image2=Label(left_menu,image=self.photo1,bd=0, bg="#242323")
        lbl_image2.pack(side=TOP, fill=X)
        #button_cart = Button(left_menu, text = "Cart", font = ("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side = TOP, fill = X)
        button_bill = Button(left_menu, text = ">> Bill", command=self.sale, font = ("times new roman", 20, "bold"), bg="#242323", bd=0, cursor="hand2", fg="#de108b").pack(side = TOP, fill = X)
        
        self.photo2=Image.open(os.path.join(script_dir,"project_ver2/picture/menu1.png"))
        self.photo2=ImageTk.PhotoImage(self.photo2)
        
        lbl_image3=Label(left_menu,image=self.photo2,bd=0, bg="#242323")
        lbl_image3.pack(side=TOP, fill=X)

        button_exit = Button(left_menu, text = ">> Exit", command=exit, font = ("times new roman", 20, "bold"), bg="#242323", bd=0, cursor="hand2", fg="#de108b").pack(side = TOP, fill = X)

        self.photo3=Image.open(os.path.join(script_dir,"project_ver2/picture/logout1.png"))
        self.photo3=ImageTk.PhotoImage(self.photo3)
        
        lbl_image4=Label(left_menu,image=self.photo3,bd=0, bg="#242323")
        lbl_image4.pack(side=TOP, fill=X)

#main
        self.photo4=Image.open(os.path.join(script_dir,"project_ver2/picture/bg_login_image1.jpg"))
        self.photo4=ImageTk.PhotoImage(self.photo4)
        
        lbl_image5=Label(self.root,image=self.photo4,bd=0, bg="#242323")
        lbl_image5.place(x=200,y=70)

#footer
        label_footer = Label(self.root, text = "Food Market Information Management System | Developed by Group 31\nFor any technical issue please contact: 098xxxxxx36 ", font = ("times new roman", 15), bg="#242323", fg="#de108b").pack(side=BOTTOM, fill = X)


    def modify_product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = modify_product_class(self.new_win)

    def sale(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = sale_class(self.new_win)

    def exit_(self):
        root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()