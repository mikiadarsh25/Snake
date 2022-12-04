import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_number + password_symbol
    random.shuffle(password_list)
    password_hai = "".join(password_list)
    password_box.insert(0, password_hai)
    pyperclip.copy(password_hai)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entry = website_box.get()
    email_entry = email_box.get()
    password_entry = password_box.get()
    new_data = {
        website_entry: {
            "email": email_entry,
            "Password": password_entry,
        }
    }

    if len(website_entry) == 0 or len(password_entry) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any box empty")
    else:
        is_ok = messagebox.askokcancel(title=website_entry,
                                       message=f"These are the details you entered: \nEmail: {email_entry}"
                                               f" \nPassword: {password_entry} \n Is it ok to save")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_box.delete(0, END)
                password_box.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_entry = website_box.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message= "No Data file Found!")
    else:
        if website_entry in data:
            email = data[website_entry]["email"]
            password = data[website_entry]["Password"]
            messagebox.showinfo(title=website_entry, message=f"Email:{email} \nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message= f"No details for {website_entry} exists. ")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

website_box = Entry(width=17)
website_box.grid(row=1, column=1)
website_box.focus()

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

email_box = Entry(width=35)
email_box.grid(row=2, column=1, columnspan=2 )
email_box.insert(0, "@gmail.com")

search = Button(text="Search", width=14, command=find_password)
search.grid(row=1, column=2)

password = Label(text="Password:")
password.grid(row=3, column=0)

password_box = Entry(width=17)
password_box.grid(row=3, column=1)

gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
