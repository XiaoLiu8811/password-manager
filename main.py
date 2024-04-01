from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title= "Oops", message="Please don't leave any fields empty!")
    elif len(password) < 8:
        messagebox.showinfo(title= "Oops", message="Password should have more than 8 characters!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            web_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager", )
window.config(padx=50, pady=50)

# Create the canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(80, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Create buttons

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, sticky="w")

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=1, sticky="E")

# Entries

web_entry = Entry(width=42)
web_entry.grid(column=1, row=1, sticky="w")
web_entry.focus()
email_entry = Entry(width=42)
email_entry.grid(column=1, row=2, sticky="w")
email_entry.insert(0, "your@gmail.com")
password_entry = Entry(width=23)
password_entry.grid(column=1, row=3, sticky="w")

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

window.mainloop()
