import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import json
import variable as var
from client import *
from PIL import Image, ImageTk



class App:
    # menu 
    def __init__(self, root=None):
        self.root = root
        # menu frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

        ttk.Label(self.frame, text='-----------------------------------').pack(fill='x', expand=True)
        ttk.Label(self.frame, text='Username \t'+var.username).pack(fill='x', expand=True)
        ttk.Label(self.frame, text='Name \t\t'+var.name).pack(fill='x', expand=True)
        ttk.Label(self.frame, text='Money \t\t'+str(var.amount_credit)).pack(fill='x', expand=True)
        ttk.Label(self.frame, text='-----------------------------------').pack(fill='x', expand=True)

        # menu
        ttk.Label(self.frame, text='Menu').pack(fill='x', expand=True)
        # Pay Bill button
        ttk.Button(self.frame, text='Pay Bill',
                  command=self.make_page_1).pack(fill='x', expand=True, pady=10)
        self.page_1 = Page_1(master=self.root, app=self)
        # Create Bill button
        ttk.Button(self.frame, text='Create Bill',
                  command=self.make_page_2).pack(fill='x', expand=True, pady=10)
        self.page_2 = Page_2(master=self.root, app=self)
        # Transfer button
        ttk.Button(self.frame, text='Transfer',
                  command=self.make_page_3).pack(fill='x', expand=True, pady=10)
        self.page_3 = Page_3(master=self.root, app=self)

        # Logout button
        ttk.Button(self.frame, text='Logout',
                  command=self.logout).pack(fill='x', expand=True, pady=30)

        # otp
        self.otp1 = otp_pay_bill()(master=self.root, app=self)
        self.otp2 = otp_create_bill(master=self.root, app=self)
        self.otp3 = otp_transfer(master=self.root, app=self)


    def main_page(self):
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

    def make_page_1(self):
        self.frame.pack_forget()
        self.page_1.start_page()

        GetBill(var.username,'')

        for i in range(0, len(var.bill_form)):
            var.bill_name = var.bill_form[i]['bill_name']
            var.bill_id = var.bill_form[i]['bill_id']
            var.bill_sender = var.bill_form[i]['bill_sender']
            var.bill_amount = var.bill_form[i]['amount']
            var.bill_description = var.bill_form[i]['description']
            print(var.bill_name)
            print(var.bill_id)
            print(var.bill_sender)
            print(var.bill_amount)
            print(var.bill_description)

            ttk.Label(self.page_1.frame, text='Bill: ' + var.bill_name + ', ID: '+var.bill_id + ', Sender: ' + var.bill_sender).pack(fill='x', expand=True)
            ttk.Label(self.page_1.frame, text=' Amount: '+ str(var.bill_amount) + ', Description: ' + var.bill_description).pack(fill='x', expand=True)
            ttk.Label(self.page_1.frame, text='---------------------------------------------------').pack(fill='x', expand=True)
    

    def make_page_2(self):
        self.frame.pack_forget()
        self.page_2.start_page()

    def make_page_3(self):
        self.frame.pack_forget()
        self.page_3.start_page()

    def make_otp1(self):
        self.frame.pack_forget()
        self.otp1.start_page()
    
    def make_otp2(self):
        self.frame.pack_forget()
        self.otp2.start_page()
    
    def make_otp3(self):
        self.frame.pack_forget()
        self.otp3.start_page()

    def logout(self):
        self.frame.pack_forget()
        login=Login(root)


class Page_1:
    # Pay Bill
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        # Pay Bill frame
        self.frame = ttk.Frame(self.master)
        # Pay Bill
        ttk.Label(self.frame, text='Bill List', font=("Arial", 20)).pack(fill='x', expand=True)

        ttk.Label(self.frame, text='---------------------------------------------------').pack(fill='x', expand=True)

        self.bill_id = tk.StringVar()

        # Bill Id
        ttk.Label(self.frame, text="Bill ID:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.bill_id).pack(fill='x', expand=True)
        # Pay Button
        ttk.Button(self.frame, text='Pay', command=self.pay_bill).pack(fill='x', expand=True)

        ttk.Button(self.frame, text='Back to Main Menu', command=self.go_back).pack(fill='x', expand=True, pady=30)

        

    def start_page(self):
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

    def pay_bill(self):
        self.frame.pack_forget()
        self.app.make_otp1()
        
class Page_2:
    # Create Bill
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        # Create Bill Frame
        self.frame = ttk.Frame(self.master)
        # Create Bill
        ttk.Label(self.frame, text='Create Bill', font=("Arial", 20)).pack(fill='x', expand=True)

        # Variabel
        self.bill_name = tk.StringVar()
        self.bill_recipient= tk.StringVar()
        self.amount = tk.StringVar()
        self.description = tk.StringVar()

        ttk.Label(self.frame, text="Bill Name:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.bill_name).pack(fill='x', expand=True)

        ttk.Label(self.frame, text="Recipient:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.bill_recipient).pack(fill='x', expand=True)

        ttk.Label(self.frame, text="Amount:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.amount).pack(fill='x', expand=True)

        ttk.Label(self.frame, text="Description:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.description).pack(fill='x', expand=True)

        # Create Button
        ttk.Button(self.frame, text='Create', command=self.create_bill_clicked).pack(fill='x', expand=True, pady=10)

        # Back button
        ttk.Button(self.frame, text='Back to Main Menu', command=self.go_back).pack(fill='x', expand=True, pady=30)

    def start_page(self):
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()
    
    def otp_page(self):
        self.frame.pack_forget()
        self.app.make_otp2()

    def create_bill_clicked(self):
        flag = CheckRecipient(self.bill_recipient.get())
        if(flag==1):
            showinfo(
                title='Information',
                message="Transaction Failed, User not Found"
            )
        else:
            RequestOTP()
            self.frame.pack_forget()
            self.app.make_otp2()

        # flag = CreateBill(self.bill_name.get(), self.bill_recipient.get(), self.amount.get(), self.description.get())
        # if(flag==1):
        #     showinfo(
        #         title='Information',
        #         message="Transaction Failed, User not Found"
        #     )

        # ttk.Entry(self.frame, textvariable=self.bill_name).delete(0,'end')
        # ttk.Entry(self.frame, textvariable=self.bill_recipient).delete(0,'end')
        # ttk.Entry(self.frame, textvariable=self.amount).delete(0,'end')
        # ttk.Entry(self.frame, textvariable=self.description).delete(0,'end')
class Page_3:
    # Transfer
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        # Transfer Frame
        self.frame = ttk.Frame(self.master)
        # Transfer
        ttk.Label(self.frame, text='Transfer', font=("Arial", 20)).pack(fill='x', expand=True)

        # Variabel
        self.transfer_recipient= tk.StringVar()
        self.amount = tk.StringVar()
        self.description = tk.StringVar()


        ttk.Label(self.frame, text="Recipient:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.transfer_recipient).pack(fill='x', expand=True)

        ttk.Label(self.frame, text="Amount:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.amount).pack(fill='x', expand=True)

        ttk.Label(self.frame, text="Description:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.description).pack(fill='x', expand=True)

        # Transfer Button
        ttk.Button(self.frame, text='Transfer', command=self.transfer_clicked).pack(fill='x', expand=True, pady=10)

        # Back button
        ttk.Button(self.frame, text='Back to Main Menu', command=self.go_back).pack(fill='x', expand=True, pady=30)

    def start_page(self):
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

    def go_back(self):
        ttk.Entry(self.frame, textvariable=self.transfer_recipient).delete(0, 'end')
        ttk.Entry(self.frame, textvariable=self.amount).delete(0, 'end')
        ttk.Entry(self.frame, textvariable=self.description).delete(0, 'end')
        self.frame.pack_forget()
        self.app.main_page()
    
    def otp_page(self):
        self.frame.pack_forget()
        self.app.make_otp3()

    def transfer_clicked(self):
        flag = CheckRecipient(self.transfer_recipient.get())
        if(flag==1):
            showinfo(
                title='Information',
                message="Transaction Failed, User not Found"
            )
        else:
            RequestOTP()
            self.frame.pack_forget()
            self.app.make_otp3()

        # flag = TransferMoney(self.transfer_recipient.get(), self.amount.get(), self.description.get(), var.token)
        # if(flag==1):
        #     showinfo(
        #         title='Information',
        #         message="Transaction Failed, User not Found"
        #     )
        # Clear Entry
        # ttk.Entry(self.frame, textvariable=self.transfer_recipient).delete(0, 'end')
        # ttk.Entry(self.frame, textvariable=self.amount).delete(0, 'end')
        # ttk.Entry(self.frame, textvariable=self.description).delete(0, 'end')
class Login:
    def __init__(self, root=None):
        self.root = root
        # username & password
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        
        # Sign in frame
        self.signin = ttk.Frame(root)
        self.signin.pack(padx=10, pady=10, fill='x', expand=True)
        
        # image crab
        crab = Image.open("crab.png")
        crab_image = ImageTk.PhotoImage(crab)
        self.im = ttk.Label(self.signin, image=crab_image)
        self.im.image = crab_image
        self.im.pack(ipadx=10, ipady=10)

        # Title
        ttk.Label(self.signin, text="\"MATA DUITAN\" PAYMENT SYSTEM", font=("Arial", 20)).pack(fill='x', expand=True, pady=20)

        # username
        self.username_label = ttk.Label(self.signin, text="Username :")
        self.username_label.pack(fill='x', expand=True)

        self.username_entry = ttk.Entry(self.signin, textvariable=self.username)
        self.username_entry.pack(fill='x', expand=True)
        self.username_entry.focus()

        # password
        self.password_label = ttk.Label(self.signin, text="Password:")
        self.password_label.pack(fill='x', expand=True)

        self.password_entry = ttk.Entry(self.signin, textvariable=self.password, show="*")
        self.password_entry.pack(fill='x', expand=True)

        # login button
        self.login_button = ttk.Button(self.signin, text="Login", command=self.login_clicked)
        self.login_button.pack(fill='x', expand=True, pady=10)
        
        # signup button
        self.sign_up_button = ttk.Button(self.signin, text="Sign Up", command=self.sign_up_clicked)
        self.sign_up_button.pack(fill='x', expand=True, pady=10)

    def login_clicked(self):
        
        flag = Signin(self.username.get(), self.password.get())

        if(flag==0):
            self.signin.pack_forget()
            app = App(root)
        elif(flag==1):
            showinfo(
                title='Information',
                message="User not Found"
            )
        elif(flag==2):
            showinfo(
                title='Information',
                message="Wrong Password"
            )   
        # print(flag)

    def sign_up_clicked(self):
        self.signin.pack_forget()
        signup = Signup(root) 

class otp:
    # otp
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        # otp Frame
        self.frame = ttk.Frame(self.master)

        # Variabel
        self.otp= tk.StringVar()

        ttk.Label(self.frame, text="Masukkan OTP:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.otp).pack(fill='x', expand=True, pady=5)

        # Ok Button
        ttk.Button(self.frame, text='Ok').pack(fill='x', expand=True, pady=10)

        # Cancel
        ttk.Button(self.frame, text='Cancel', command=self.go_back).pack(fill='x', expand=True, pady=5)

    def start_page(self):
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page() 

class otp_create_bill:
    # otp
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        # otp Frame
        self.frame = ttk.Frame(self.master)

        # Variabel
        self.otp= tk.StringVar()

        ttk.Label(self.frame, text="Masukkan OTP:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.otp).pack(fill='x', expand=True, pady=5)

        # Ok Button
        ttk.Button(self.frame, text='Ok', command=self.ok_clicked).pack(fill='x', expand=True, pady=10)

        # Cancel
        ttk.Button(self.frame, text='Cancel', command=self.go_back).pack(fill='x', expand=True, pady=5)

    def start_page(self):
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page() 

    def ok_clicked(self):
        success = CreateBill(self.app.page_2.bill_name.get(), self.app.page_2.bill_recipient.get(), self.app.page_2.amount.get(), self.app.page_2.description.get(),  self.otp.get())
        print(success)

class otp_pay_bill:
    # otp
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        # otp Frame
        self.frame = ttk.Frame(self.master)

        # Variabel
        self.otp= tk.StringVar()

        ttk.Label(self.frame, text="Masukkan OTP:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.otp).pack(fill='x', expand=True, pady=5)

        # Ok Button
        ttk.Button(self.frame, text='Ok', command=self.ok_clicked).pack(fill='x', expand=True, pady=10)

        # Cancel
        ttk.Button(self.frame, text='Cancel', command=self.go_back).pack(fill='x', expand=True, pady=5)

    def start_page(self):
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page() 

    def ok_clicked(self):
        success = CreateBill(self.app.page_2.bill_name.get(), self.app.page_2.bill_recipient.get(), self.app.page_2.amount.get(), self.app.page_2.description.get(),  self.otp.get())
        print(success)

class otp_transfer:
    # otp
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        # otp Frame
        self.frame = ttk.Frame(self.master)

        # Variabel
        self.otp= tk.StringVar()

        ttk.Label(self.frame, text="Masukkan OTP:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.otp).pack(fill='x', expand=True, pady=5)

        # Ok Button
        ttk.Button(self.frame, text='Ok', command=self.ok_clicked).pack(fill='x', expand=True, pady=10)

        # Cancel
        ttk.Button(self.frame, text='Cancel', command=self.go_back).pack(fill='x', expand=True, pady=5)

    def start_page(self):
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page() 

    def ok_clicked(self):
        success = TransferMoney(self.app.page_3.transfer_recipient.get(), self.app.page_3.amount.get(), self.app.page_3.description.get(), self.otp.get(), var.token)
        print(success)

class Signup():
    # sign up
    def __init__(self, root=None):
        self.root = root
        # signup frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)
        
        # signup
        ttk.Label(self.frame, text='Sign Up', font=("Arial", 20)).pack(fill='x', expand=True)

        # Variabel
        self.username = tk.StringVar()
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.repeat_password = tk.StringVar()
        self.name = tk.StringVar()

        ttk.Label(self.frame, text="Name:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.name).pack(fill='x', expand=True)

        ttk.Label(self.frame, text="Email:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.email).pack(fill='x', expand=True)

        ttk.Label(self.frame, text="Username:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.username).pack(fill='x', expand=True)

        ttk.Label(self.frame, text="Password:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.password, show="*").pack(fill='x', expand=True)

        ttk.Label(self.frame, text="Repeat Password:").pack(fill='x', expand=True)
        ttk.Entry(self.frame, textvariable=self.repeat_password, show="*").pack(fill='x', expand=True)

        # Create Button
        ttk.Button(self.frame, text='Create', command = self.create_clicked).pack(fill='x', expand=True, pady=10)

        # Back to Login Menu
        ttk.Button(self.frame, text='Back to Login Menu', command = self.back_login_clicked).pack(fill='x', expand=True, pady=10)


    def create_clicked(self):
        if(self.password.get()==self.repeat_password.get()):
            form =  {"username" : self.username.get(),
                "email" : self.email.get(),
                "name" : self.name.get(),
                "password" : self.password.get(),
            }
            # Serializing form
            self.form_json = json.dumps(form)
            SignUp(form)
            ttk.Entry(self.frame, textvariable=self.name).delete(0, 'end')
            ttk.Entry(self.frame, textvariable=self.email).delete(0, 'end')
            tk.Entry(self.frame, textvariable=self.username).delete(0, 'end')
            ttk.Entry(self.frame, textvariable=self.password, show="*").delete(0, 'end')
            ttk.Entry(self.frame, textvariable=self.repeat_password, show="*").delete(0, 'end')
        else:
            showinfo(
                title='Information',
                message="Password are not matched"
            )   

    def back_login_clicked(self):
        self.frame.pack_forget()
        login=Login(root)
        
    

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Tubes PPLJ | Payment System")
    root.geometry("500x500")
    login=Login(root)
    root.mainloop()