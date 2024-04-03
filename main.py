from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title= "Oops", message="Please don't leave any fields empty!")
    elif len(password) < 8:
        messagebox.showinfo(title= "Oops", message="Password should have more than 8 characters!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- Search ------------------------------- #
def search_data():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the {website} exists.")

        # When if-else statements can address the problem don't use the try-except-else method
        # try:
        #     messagebox.showinfo(title=website, message=f"Email: {data[website]["email"]}\n"
        #                                                f"Password: {data[website]["password"]}")
        # except KeyError:
        #     messagebox.showinfo(title="Error", message=f"No details for the {website} exists.")



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

search_button = Button(text="Search", width=8, command=search_data)
search_button.grid(row=1, column=1, sticky="E")

# Entries

web_entry = Entry(width=30)
web_entry.grid(column=1, row=1, sticky="w")
web_entry.focus()
email_entry = Entry(width=42)
email_entry.grid(column=1, row=2, sticky="w")
email_entry.insert(0, "username@gmail.com")
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
