import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

def open_image():
    global image_label
    filename = filedialog.askopenfilename(initialdir="/", title="Select Image", 
                                          filetypes=(("Image Files", "*.jpg *.png *.jpeg"), ("All Files", "*.*")))
    if filename:
        image = Image.open(filename)
        image.thumbnail((500, 500))
        image_tk = ImageTk.PhotoImage(image)
        image_label.configure(image=image_tk)
        image_label.image = image_tk

root = tk.Tk()

button = tk.Button(root, text="Open Image", command=open_image)
button.pack()

image_label = tk.Label(root)
image_label.pack()

root.mainloop()