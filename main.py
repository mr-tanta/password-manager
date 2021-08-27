from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

BLUE = "#f4f9f9"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 13))]
    password_symbols = [choice(symbols) for _ in range(randint(3, 5))]
    password_numbers = [choice(numbers) for _ in range(randint(4, 6))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"url: {website}\nusername: {email}\npassword: {password}\n\n ----!o ---- o!----\n\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=BLUE)

canvas = Canvas(width=200, height=200, bg=BLUE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

canvas.grid(column=2, row=1)

website_label = Label(text="Website:", bg=BLUE)
website_label.grid(column=1, row=2)

website_input = Entry(width=35)
website_input.grid(row=2, column=2, columnspan=2)
website_input.get()
website_input.focus()

email_label = Label(text="Email/Username", bg=BLUE)
email_label.grid(column=1, row=3)

email_input = Entry(width=35)
email_input.grid(column=2, row=3, columnspan=2)
email_input.insert(0, "abraham@tantasecure.com")

password_label = Label(text="Password", bg=BLUE)
password_label.grid(column=1, row=4)

password_input = Entry(width=21)
password_input.grid(column=2, row=4)
password_input.get()

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=2, row=5, columnspan=2)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=3, row=4)

window.mainloop()
