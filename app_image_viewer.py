from cgitb import text
import imghdr
import tkinter as tk
import glob
from PIL import ImageTk, Image

window = tk.Tk()
window.iconbitmap('icon.ico')
window.title("App Image Viewer")
window.resizable(width=True, height=True)

image_list = []
nm_of_images = 0
img_index = 0

def navigate_images(event):
    if event.keysym == "Left":
        show_prev_img()

    if event.keysym == "Right":
        show_next_img()

def show_prev_img():
    global img_index
    global image_list

    if img_index > 0: 
        img_index = img_index - 1
        panel["image"] = image_list[img_index]
        lbl_index["text"] = f"{img_index+1}/{nm_of_images}"

def show_next_img():
    global img_index
    global image_list

    if img_index < (nm_of_images - 1): 
        img_index = img_index + 1
        panel["image"] = image_list[img_index]
        lbl_index["text"] = f"{img_index+1}/{nm_of_images}"


#indexes all the images in the folder
for filename in glob.glob('images/*.*'):
    if imghdr.what(filename) !=None:
        im = Image.open(filename)
        im_resize = im.resize((256,256))
        im=ImageTk.PhotoImage(im_resize)
        image_list.append(im)
    else:
        continue

nm_of_images = len(image_list)

panel=tk.Label(image=image_list[img_index])
panel.grid(row=0, column=0, columnspan= 3) 

btn_prev = tk.Button( text="<", padx=20, command=show_prev_img)
btn_prev.grid(row=1,column=0,sticky="sw")

lbl_index = tk.Label( text=f"{img_index+1}/{nm_of_images}", padx=20)
lbl_index.grid(row=1,column=1)

btn_next = tk.Button( text=">",  padx=20, command=show_next_img)
btn_next.grid(row=1,column=2, sticky="se")

#Attaches keyboard keys
window.bind("<Right>", navigate_images)
window.bind("<Left>", navigate_images)

# Run the application
window.mainloop()