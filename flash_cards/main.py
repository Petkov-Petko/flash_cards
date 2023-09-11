BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
from pandas import DataFrame
import  random

current_card = {}
to_learn = {}

try:
    text = pandas.read_csv("data/words_to_learn,csv")
except  FileNotFoundError:
    original_text = pandas.read_csv("data/french_words.csv")
    to_learn = original_text.to_dict(orient="records")
else:
    to_learn = text.to_dict(orient="records")


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="Black")
    canvas.itemconfig(front, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=current_card["English"], fill="White")
    canvas.itemconfig(front, image=black_card)

def is_known():
    to_learn.remove(current_card)
    next_card()
    data = DataFrame(to_learn)
    data.to_csv("data/words_to_learn,csv", index=False)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
black_card = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
front = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Title", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

check_button = Button(image=right, highlightthickness=0, command=is_known)
check_button.grid(column=1 , row=1)

next_card()

window.mainloop()