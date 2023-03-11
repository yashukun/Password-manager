from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import pandas
import json

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# my file
pass_dict = {"website": [],
             "email": [],
             "password": []}

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_letters+ password_symbols

    random.shuffle(password_list)

    password1 = '' . join(password_list)
    pass_box.delete(0, END)
    pyperclip.copy(password1)
    pass_box.insert(0, password1)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def search():
    website_name = web_box.get()
    website_name.title()
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
            email = data[website_name]["Email"]
            password = data[website_name]["Password"]

    except KeyError:
        messagebox.showwarning(title="Error", message="Data Does not Exist")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="Data Does not Exist")
    else:
        messagebox.showinfo(title=website_name, message=f"Email:{email}\nPassword:{password}")


def save():
    website_name = web_box.get()
    website_name.title()
    email = email_box.get()
    password = pass_box.get()

    new_data = {
        website_name:
            {"Email": email,
             "Password": password
             }
    }

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showwarning(title="opps", message="Hey do not leave any fields empty")
    else:

        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details you have entered"
                                                                   f"\nEmail:{email}\nPassword:{password}"
                                                                   f"\n Is it ok to save?")
        if is_ok:
            # with open("data.txt", mode='a') as data:
            #     new_data = f"{website_name} | {email} | {password}"
            #     data.write(new_data + '\n')
            # web_box.delete(0, END)
            # pass_box.delete(0, END)
            # web_box.focus()
            #
            # # save to csv file
            # pass_dict["website"].append(website_name)
            # pass_dict["email"].append(email)
            # pass_dict["password"].append(password)
            #
            # df = pandas.DataFrame(pass_dict)
            # df.to_csv("password.csv", mode='a')

            # data to json
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                web_box.delete(0, END)
                pass_box.delete(0, END)
                web_box.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

# lock image
lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
canvas.create_image(90, 100, image=lock_image)
canvas.grid(column=1, row=0)
# canvas.pack()

# website lable
web_lable = Label(text="Website:", font=(FONT_NAME, 12), bg=YELLOW, fg=RED)
web_lable.grid(column=0, row=1)

# web box
web_box = Entry(width=18)
web_box.grid(column=1, row=1)
web_box.focus()

# search button
search_button = Button(width=12, text="search", bg=YELLOW, fg=RED, command=search)
search_button.grid(column=2, row=1)

# email_lable
email_lable = Label(text="Email/Username:", font=(FONT_NAME, 12), bg=YELLOW, fg=RED)
email_lable.grid(column=0, row=2)

# email box
email_box = Entry(width=35)
email_box.insert(0, string='my@gmail.com')
email_box.grid(column=1, row=2, columnspan=2)


# password lable
pass_lable = Label(text="Password:", font=(FONT_NAME, 12), bg=YELLOW, fg=RED)
pass_lable.grid(column=0, row=3)

# pass box
pass_box = Entry(width=35)
pass_box.grid(column=1, row=3, columnspan=2)

# pass button
pass_button = Button(text="Generate Password", width=15, command=generate_password, bg=YELLOW, fg=RED)
pass_button.grid(column=1, row=4)

# Add button
add_button = Button(text="add", width=13, command=save, bg=YELLOW, fg=RED)
add_button.grid(column=2, row=4)


window.mainloop()
