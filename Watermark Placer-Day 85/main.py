import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

root_image_path = "bg.jpg"
bg = '#16425D'

logo_path = None
img_label = None
pil_img_base = None  # Keeps a clean copy of the original image
pil_logo = None      # Keeps the loaded logo image in memory
x = 0
y = 0

def display_img(img_path):
    global img_label,x,y, pil_img_base
    if not img_path:
        return
    pil_img_base = Image.open(img_path)
    pil_img_base = pil_img_base.convert('RGBA')
    pil_img_base.thumbnail((1100, 550))  # reduced from (1200, 700)
    tk_img = ImageTk.PhotoImage(pil_img_base)

    y = tk_img.height()//2
    x = tk_img.width()//2
    if img_label is None:
        img_label = tk.Label(window, image=tk_img)
        img_label.grid(row=0, column=0, columnspan=4, pady=10)
    else:
        img_label.configure(image=tk_img)
def import_img(logo):
        global logo_path, pil_logo
        if logo:
            selected_path = filedialog.askopenfilename(title="Select a logo",filetypes=[("Image files", "*.png *.jpg *.jpeg")])
            if selected_path:
                logo_path = selected_path
                pil_logo = Image.open(logo_path).convert('RGBA')
                pil_logo.thumbnail((150, 150))
                paste()

        else:
            img_path = filedialog.askopenfilename(title="Select an image",filetypes=[("Image files", "*.png *.jpg *.jpeg")])
            display_img(img_path)

def download_img():
    if pil_img_base:
        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if save_path:
            final_img = pil_img_base.copy()
            if pil_logo:
                final_img.paste(pil_logo,(x,y),pil_logo)
            final_img.convert("RGB").save(save_path)

def paste():
    global img_label, x, y, pil_img_base, pil_logo
    if pil_img_base is None or pil_logo is None:
        return
    temp_img = pil_img_base.copy()
    temp_img.paste(pil_logo, (x, y), pil_logo)

    tk_img = ImageTk.PhotoImage(temp_img)
    img_label.configure(image=tk_img)
    img_label.image = tk_img


def move_up():
    global y
    y -= 5
    return paste()
def move_down():
    global y
    y+= 5
    return paste()
def move_left():
    global x
    x -= 5
    return paste()
def move_right():
    global x
    x += 5
    return paste()
window = tk.Tk()

window.title("Watermark Placer")
window.configure(background=bg, padx=30, pady=20)
display_img(root_image_path)

#LEFT COLUMN
tk.Label(window, text="Select Image", bg=bg, fg="white").grid(row=1, column=0, sticky="e", padx=5, pady=5)
tk.Button(window, text="Select Image", command=lambda: import_img(False)).grid(row=1, column=1, sticky="w", pady=5)

tk.Label(window, text="Select Logo", bg=bg, fg="white").grid(row=2, column=0, sticky="e", padx=5, pady=5)
tk.Button(window, text="Select Logo", command=lambda: import_img(True)).grid(row=2, column=1, sticky="w", pady=5)


tk.Label(window, text="Download", bg=bg, fg="white").grid(row=3, column=0, sticky="e", padx=5, pady=5)
tk.Button(window, text="Download Image", command=download_img).grid(row=3, column=1, sticky="w", pady=5)

#Right Column
tk.Button(window, text="⬆️", command=move_up).grid(row=1, column=2, sticky="n", pady=5)
tk.Button(window, text="⬅️", command=move_left).grid(row=2, column=2, sticky="w", pady=5)
tk.Button(window, text="➡️", command=move_right).grid(row=2, column=2, sticky="e", pady=5)
tk.Button(window, text="⬇️", command=move_down).grid(row=3, column=2, sticky="s", pady=5)

window.mainloop()