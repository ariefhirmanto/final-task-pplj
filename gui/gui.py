import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

        
class App:
    # menu 
    def __init__(self, root=None):
        self.root = root
        # menu frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)
        
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
        # otp
        self.otp = otp(master=self.root, app=self)


    def main_page(self):
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

    def make_page_1(self):
        self.frame.pack_forget()
        self.page_1.start_page()

    def make_page_2(self):
        self.frame.pack_forget()
        self.page_2.start_page()

    def make_page_3(self):
        self.frame.pack_forget()
        self.page_3.start_page()

    def make_otp(self):
        self.frame.pack_forget()
        self.otp.start_page()

class Page_1:
    # Pay Bill
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        # Pay Bill frame
        self.frame = ttk.Frame(self.master)
        # Pay Bill
        ttk.Label(self.frame, text='Bill List').pack(fill='x', expand=True)

        # Bill 1
        ttk.Label(self.frame, text='Bill 1 -> From: Arif, Amount: 120000, Description: Hutang').pack(fill='x', expand=True)
        # Pay Button 1
        ttk.Button(self.frame, text='Pay', command=self.otp_page).pack(fill='x', expand=True)

        # Bill 2
        ttk.Label(self.frame, text='Bill 2 -> From: Ardi, Amount: 50000, Description: Iuaran Sampah').pack(fill='x', expand=True)
        # Pay Button 2
        ttk.Button(self.frame, text='Pay', command=self.otp_page).pack(fill='x', expand=True)

        ttk.Button(self.frame, text='Back to Main Menu', command=self.go_back).pack(fill='x', expand=True, pady=30)


    def start_page(self):
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

    def otp_page(self):
        self.frame.pack_forget()
        self.app.make_otp()

class Page_2:
    # Create Bill
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        # Create Bill Frame
        self.frame = ttk.Frame(self.master)
        # Create Bill
        ttk.Label(self.frame, text='Create Bill').pack(fill='x', expand=True)

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
        ttk.Button(self.frame, text='Create', command=self.otp_page).pack(fill='x', expand=True, pady=10)

        # Back button
        ttk.Button(self.frame, text='Back to Main Menu', command=self.go_back).pack(fill='x', expand=True, pady=30)

    def start_page(self):
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()
    
    def otp_page(self):
        self.frame.pack_forget()
        self.app.make_otp()

class Page_3:
    # Transfer
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        # Transfer Frame
        self.frame = ttk.Frame(self.master)
        # Transfer
        ttk.Label(self.frame, text='Transfer').pack(fill='x', expand=True)

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
        ttk.Button(self.frame, text='Transfer', command=self.otp_page).pack(fill='x', expand=True, pady=10)

        # Back button
        ttk.Button(self.frame, text='Back to Main Menu', command=self.go_back).pack(fill='x', expand=True, pady=30)

    def start_page(self):
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()
    
    def otp_page(self):
        self.frame.pack_forget()
        self.app.make_otp()

class Login:
    def __init__(self, root=None):
        self.root = root
        # username & password
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        
        # Sign in frame
        self.signin = ttk.Frame(root)
        self.signin.pack(padx=10, pady=10, fill='x', expand=True)

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

    def login_clicked(self):
        if(self.username.get()=="pplj" and self.password.get()=="123"):
            flag = 1
        else:
            flag = 0

        if(flag):
            self.signin.pack_forget()
            app = App(root)
        else:
            showinfo(
                title='Information',
                message="Wrong Password"
            )   

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

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Tubes PPLJ")
    root.geometry("500x500")
    login=Login(root)
    root.mainloop()