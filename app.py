import customtkinter as ctk
from PIL import Image, ImageTk
import sys
import os
import subprocess

# os.chdir("python")
# os.system('source machine_learning/bin/activate')

def button_callback():
    sys.exit()

def shutdown_system():
    os.system("shutdown now")

def reboot_system():
    os.system('reboot')

def clean_trash():
    os.system('rm -rf ~/.local/share/Trash/*')
    sys.exit()

def update_arch_based_system():
    command = 'sudo pacman -Syu'
    subprocess.run(["kitty", "-e", "sh", "-c", command])
    sys.exit()

def update_yay():
    command = 'yay -Syu'
    subprocess.run(["kitty", "-e", "sh", "-c", command])
    sys.exit()

def lock_system():
    os.system('hyprlock & pkill python')
    # sys.exit()

app = ctk.CTk()
app.geometry('1000x600')
app.title('Linux')
app.wm_iconname('/home/naturalcapsule/python/app/rocket.ico')
app._set_appearance_mode('dark')
app.overrideredirect(True)

def start_move(event):
    app.x = event.x
    app.y = event.y

def stop_move(event):
    app.x = None
    app.y = None

def on_motion(event):
    x = event.x_root - app.x
    y = event.y_root - app.y
    app.geometry(f"+{x}+{y}")

app.bind('<Button-1>', start_move)
app.bind('<ButtonRelease-1>', stop_move)
app.bind('<B1-Motion>', on_motion)

# Create the images
shutdown_image = Image.open("/home/naturalcapsule/python/app/power.png").convert("RGBA")
background_image_shutdown = ImageTk.PhotoImage(shutdown_image.resize((120, 120)))

lock_image = Image.open("/home/naturalcapsule/python/app/lock.png").convert("RGBA")
background_image_lock = ImageTk.PhotoImage(lock_image.resize((120, 120)))


reboot_image = Image.open("/home/naturalcapsule/python/app/reboot.png").convert("RGBA")
background_image_reboot = ImageTk.PhotoImage(reboot_image.resize((120, 120)))

clean_trash_image = Image.open("/home/naturalcapsule/python/app/trash.png").convert("RGBA")
background_image_clean_trash = ImageTk.PhotoImage(clean_trash_image.resize((120, 120)))

clean_system_image = Image.open("/home/naturalcapsule/python/app/update_pacman.png").convert("RGBA")
background_image_clean_system = ImageTk.PhotoImage(clean_system_image.resize((120, 120)))

clean_yay_image = Image.open("/home/naturalcapsule/python/app/update_yay.png").convert("RGBA")
background_image_clean_yay = ImageTk.PhotoImage(clean_yay_image.resize((120, 120)))

app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)
app.columnconfigure(3, weight=1)

label1 = ctk.CTkLabel(app, text='', image=background_image_shutdown, fg_color='#2E2E2E')
label1.grid(row=1, column=0, padx=20, pady=20)

button1 = ctk.CTkButton(app, text='ShutDown', command=shutdown_system, bg_color='#2E2E2E')
button1.grid(row=2, column=0, padx=20, pady=20)

label2 = ctk.CTkLabel(app, text='', image=background_image_clean_trash, bg_color='#2E2E2E')
label2.grid(row=3, column=0, padx=20, pady=20)

button2 = ctk.CTkButton(app, text='Clean Trash', command=clean_trash, bg_color='#2E2E2E') #########
button2.grid(row=4, column=0, padx=20, pady=20)

label3 = ctk.CTkLabel(app, text='', image=background_image_reboot, fg_color='#2E2E2E')
label3.grid(row=1, column=1, padx=20, pady=20)

button3 = ctk.CTkButton(app, text='Reboot', command=reboot_system, bg_color='#2E2E2E')
button3.grid(row=2, column=1, padx=20, pady=20)

label4 = ctk.CTkLabel(app, text='', image=background_image_clean_system, fg_color='#2E2E2E')
label4.grid(row=3, column=1, padx=20, pady=20)

button4 = ctk.CTkButton(app, text='Update System', command=update_arch_based_system, bg_color='#2E2E2E')
button4.grid(row=4, column=1, padx=20, pady=20)

label5 = ctk.CTkLabel(app, text='', image=background_image_lock, fg_color='#2E2E2E')
label5.grid(row=1, column=2, padx=20, pady=20)

button5 = ctk.CTkButton(app, text='Lock', command=lock_system, bg_color='#2E2E2E')
button5.grid(row=2, column=2, padx=20, pady=20)

label6 = ctk.CTkLabel(app, text='', image=background_image_clean_yay, fg_color='#2E2E2E')
label6.grid(row=3, column=2, padx=20, pady=20)

button6 = ctk.CTkButton(app, text='Update yay', command=update_yay, bg_color='#2E2E2E')
button6.grid(row=4, column=2, padx=20, pady=20)

exit_button = ctk.CTkButton(app, text='Exit Program', command=button_callback, bg_color='#2E2E2E')
exit_button.grid(row=0, column=0, columnspan=3, pady=20)

app.mainloop()