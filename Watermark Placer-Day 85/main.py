import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

root_image_path = "bg.jpg"
bg = '#16425D'

img_label = None

def display_img(img_path):
    global img_label
    pil_img = Image.open(img_path)
    pil_img.thumbnail((1100, 550))  # reduced from (1200, 700)
    tk_img = ImageTk.PhotoImage(pil_img)

    if img_label is None:
        img_label = tk.Label(window, image=tk_img)
        img_label.grid(row=0, column=0, columnspan=4, pady=10)
    else:
        img_label.configure(image=tk_img)

    img_label.image = tk_img

def import_img():
    img_path = filedialog.askopenfilename(title="Select an image")
    if img_path:
        display_img(img_path)

def show_text():
    print(entry_box.get())

def download_img():
    pass

def choose_color():
    pass

def move_up():
    pass

def move_down():
    pass

def move_left():
    pass

def move_right():
    pass

window = tk.Tk()

window.title("Watermark Generator")
window.configure(background=bg, padx=30, pady=20)
display_img(root_image_path)

# ---- LEFT COLUMN: image + text controls ----
tk.Label(window, text="Select Image", bg=bg, fg="white").grid(row=1, column=0, sticky="e", padx=5, pady=5)
tk.Button(window, text="Select Image", command=import_img).grid(row=1, column=1, sticky="w", pady=5)

tk.Label(window, text="Add Text", bg=bg, fg="white").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_box = tk.Entry(window, width=30)
entry_box.grid(row=2, column=1, sticky="w", pady=5)

tk.Label(window, text="Show Text", bg=bg, fg="white").grid(row=3, column=0, sticky="e", padx=5, pady=5)
tk.Button(window, text="Show Text", command=show_text).grid(row=3, column=1, sticky="w", pady=5)

tk.Label(window, text="Download", bg=bg, fg="white").grid(row=4, column=0, sticky="e", padx=5, pady=5)
tk.Button(window, text="Download Image", command=download_img).grid(row=4, column=1, sticky="w", pady=5)


window.mainloop()