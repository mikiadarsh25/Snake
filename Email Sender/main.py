import smtplib
from tkinter import *
from tkinter import messagebox



def send():
    my_email = email_box.get()
    my_password = password_box.get()
    subject = subject_box.get()
    message = message_box.get()
    sender = to_box.get()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=sender,
                            msg=f"Subject:{subject}\n\n{message}"
                            )
        messagebox.showinfo(title="Sent", message=f"Email Sent to {sender}")
        to_box.delete(0, END)
        subject_box.delete(0, END)
        message_box.delete(0, END)
        email_box.delete(0, END)
        password_box.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

email = Label(text="Email:")
email.grid(row=1, column=0)

email_box = Entry(width=35)
email_box.grid(row=1, column=1)
email_box.insert(0, "@gmail.com")
email_box.focus()

password = Label(text=" App Password:")
password.grid(row=2, column=0)

password_box = Entry(width=35)
password_box.grid(row=2, column=1)

to = Label(text="To")
to.grid(row=3, column=0)

to_box = Entry(width=35)
to_box.grid(row=3, column=1)

subject = Label(text="Subject:")
subject.grid(row=4, column=0)

subject_box = Entry(width=35)
subject_box.grid(row=4, column=1)

message = Label(text="Message:")
message.grid(row=5, column=0)

message_box = Entry(width=35)
message_box.grid(row=5, column=1)

send = Button(text="Send", width=36, command=send)
send.grid(row=6, column=1, columnspan=2)
window.mainloop()
