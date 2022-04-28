import tkinter
import random
import pyperclip
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Your password is: {password}")
    my_password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = my_web_input.get()
    username = my_username_input.get()
    password = my_password_input.get()

    if len(website) != 0 and len(password) != 0:
        ## Popup box to perform validation before saving data to the text file.
        is_it_ok = messagebox.askokcancel(title=website, message=f" Please confirm the entered "
                                                  f"details are correct or not \n username: {username} \n password: {password}")
        if is_it_ok:
            with open("Save_data.txt", "a") as savedata:
                savedata.write(f"{website} | {username} | {password}\n")
                my_web_input.delete(0, 'end')
                my_password_input.delete(0, 'end')
    else:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty ")

# ---------------------------- UI SETUP ------------------------------- #

mywindow = tkinter.Tk()
mywindow.title("Password Manager")
mywindow.config(padx=40, pady=40)

lock_image = tkinter.PhotoImage(file="logo.png")
my_canvas = tkinter.Canvas(width=260, height=260, bg="white")
my_canvas.create_image(100, 100, image=lock_image)
#my_canvas.pack()
my_canvas.grid(row=0, column=1)
my_web_name_label = tkinter.Label(text="Website:")
my_web_name_label.grid(column=0, row=1)
my_username_label = tkinter.Label(text="Email/Username:")
my_username_label.grid(column=0, row=2)
my_password_label = tkinter.Label(text="Password:")
my_password_label.grid(column=0, row=3)


# for Data input
my_web_input = tkinter.Entry(width=35)
my_web_input.grid(row=1, column=1, columnspan=2)
my_web_input.focus()
my_username_input = tkinter.Entry(width=35)
my_username_input.grid(column=1, row=2, columnspan=2)
my_username_input.insert(0,"home.bejagam@gmail.com")
my_password_input = tkinter.Entry(width=18)
my_password_input.grid(column=1, row=3)
my_password_generator = tkinter.Button(text="Generate Password", command=password_generator)
my_password_generator.grid(column=2, row=3)


add_button = tkinter.Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

mywindow.mainloop()
