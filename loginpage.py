import tkinter as tk
from tkinter import messagebox, ttk

class LoginPage:
    def __init__(self, root, authenticate_callback):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("400x300")
        self.authenticate_callback = authenticate_callback
        
        # Background Image
        self.background_image = tk.PhotoImage(file="background.png")
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.login_frame = tk.Frame(self.root, bg="white", bd=5)
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.username_label = tk.Label(self.login_frame, text="Username:", bg="white")
        self.username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = ttk.Entry(self.login_frame, width=20)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = tk.Label(self.login_frame, text="Password:", bg="white")
        self.password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = ttk.Entry(self.login_frame, width=20, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.login_button = ttk.Button(self.login_frame, text="Login", command=self.authenticate)
        self.login_button.grid(row=2, columnspan=2, pady=10)

    def authenticate(self):
        # Check username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Call the authentication callback function
        if self.authenticate_callback(username, password):
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            self.root.destroy()  # Close the login window
            # Here you can proceed to open your main application window
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
