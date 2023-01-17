from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
#import pyperclib # ! pyperclib import 오류있음 다시시도 해볼것
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def randomPwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    
    shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #     print(char)
    #     password += char
    password_entry.insert(0, f"{password}") # 패스워드 생성후 password칸에 출력
    print(f"Your password is: {password}")
    #pyperclip.
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='error', message="id 혹은 password에 빈공간이 있습니다.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                    f"\nPassword: {password} \nIs it OK to save?(y/n)")
        if is_ok:
            with open("data.txt", "a") as data_file:            #with -> file.close() 안해도 자동으로 열고 닫는다
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sososo@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button
generate_password_button = Button(text="Generate Password", width=10, command=randomPwd)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()