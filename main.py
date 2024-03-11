import tkinter as tk
from tkinter import filedialog, Scale, messagebox
from PIL import Image, ImageTk, ImageEnhance
from collections import deque
from login import start_login

class PhotoEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Editor")

        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_image)
        self.file_menu.add_command(label="Save", command=self.save_image)

        self.edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Crop", command=self.crop_image)
        self.edit_menu.add_command(label="Rotate", command=self.rotate_image)

        self.brightness_scale = Scale(self.root, label="Brightness", from_=0, to=200, orient=tk.HORIZONTAL, command=self.adjust_brightness)
        self.brightness_scale.pack()

        self.contrast_scale = Scale(self.root, label="Contrast", from_=0, to=200, orient=tk.HORIZONTAL, command=self.adjust_contrast)
        self.contrast_scale.pack()

        self.image = None
        self.image_history = deque(maxlen=10)  # Store a history of up to 10 images
        self.current_index = -1  # Index for undo/redo

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.image_history.append(self.image.copy())  # Save a copy of the original image
            self.current_index = len(self.image_history) - 1
            self.display_image()

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
            if file_path:
                self.image.save(file_path)

    def display_image(self):
        if self.image:
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def crop_image(self):
        if self.image:
            messagebox.showinfo("Crop", "Crop functionality will be added in future updates.")

    def rotate_image(self):
        if self.image:
            messagebox.showinfo("Rotate", "Rotate functionality will be added in future updates.")

    def adjust_brightness(self, brightness):
        if self.image:
            brightness_factor = float(brightness) / 100.0
            enhanced_image = ImageEnhance.Brightness(self.image_history[self.current_index]).enhance(brightness_factor)
            self.image = enhanced_image
            self.display_image()

    def adjust_contrast(self, contrast):
        if self.image:
            contrast_factor = float(contrast) / 100.0
            enhanced_image = ImageEnhance.Contrast(self.image_history[self.current_index]).enhance(contrast_factor)
            self.image = enhanced_image
            self.display_image()

    def start_application(self):
        self.root.mainloop()

def start_application():
    root = tk.Tk()
    app = PhotoEditorApp(root)
    app.start_application()

if __name__ == "__main__":
    start_login()
