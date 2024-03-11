import tkinter as tk
from tkinter import ttk, messagebox

class LoginPage(tk.Frame):
    def __init__(self, parent, authenticate):
        super().__init__(parent)
        self.parent = parent
        self.authenticate = authenticate
        self.setup_ui()

    def setup_ui(self):
        self.parent.title("Login")

        self.label_username = ttk.Label(self, text="Username:")
        self.label_username.grid(row=0, column=0, sticky="e")

        self.entry_username = ttk.Entry(self)
        self.entry_username.grid(row=0, column=1)

        self.label_password = ttk.Label(self, text="Password:")
        self.label_password.grid(row=1, column=0, sticky="e")

        self.entry_password = ttk.Entry(self, show="*")
        self.entry_password.grid(row=1, column=1)

        self.button_login = ttk.Button(self, text="Login", command=self.login)
        self.button_login.grid(row=2, column=0, columnspan=2)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.authenticate(username, password):
            self.parent.destroy()  # Close the login window
            self.open_main_app()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_main_app(self):
        import main  # Import main.py after successful login
        main.start_application()

def start_login():
    root = tk.Tk()
    login_page = LoginPage(root, authenticate)
    login_page.pack()
    root.mainloop()

def authenticate(username, password):
    # Replace this with your authentication logic
    if username == "admin" and password == "password":
        return True
    else:
        return False

if __name__ == "__main__":
    start_login()
