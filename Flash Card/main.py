from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    learn = original_data.to_dict(orient="records")
else:
    learn = data.to_dict(orient="records")


# Next Card

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(background_img, image=card_front)
    window.after(3000, func=flip_card)


def is_known():
    learn.remove(current_card)
    data = pandas.DataFrame(learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# Flip Card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(background_img, image=card_back)


# UI Setup
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR, highlightthickness=0)
flip_timer = window.after(3000, func=flip_card)
# front card
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
background_img = canvas.create_image(400, 263, image=card_front)

# back card
card_back = PhotoImage(file="images/card_back.png")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# cross button
cross_img = PhotoImage(file="images/wrong.png")
no = Button(image=cross_img, highlightthickness=0, command=next_card)
no.grid(row=1, column=0)

# right button
right_img = PhotoImage(file="images/right.png")
yes = Button(image=right_img, highlightthickness=0, command=is_known)
yes.grid(row=1, column=1)

next_card()
window.mainloop()
