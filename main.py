from tkinter import *
import pandas as pd
import random

# Functionality
words_data = pd.read_csv("data/french_words.csv")
words_dict = {}
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(card_background, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def known_word():
    words_dict.remove(current_card)
    saved_data = pd.DataFrame(words_dict)
    saved_data.to_csv("Remaining_words_to_memorize.csv")
    next_card()

def known_word():
    words_dict.remove(current_card)
    remaining_word = pd.DataFrame(words_dict)
    remaining_word.to_csv("data/remaining_words_to_memorize.csv", index=False)
    next_card()

try:
    saved_data = pd.read_csv("Remaining_words_to_memorize.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    words_dict = original_data.to_dict(orient="records")
else:
    words_dict = words_data.to_dict(orient="records")

# UI Setup
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg="#B1DDC6")

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 30, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 50, "bold"))
canvas.config(bg="#B1DDC6", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

checked_image = PhotoImage(file="images/right.png")
checked_button = Button(image=checked_image, highlightthickness=0, command=known_word)
checked_button.grid(row=1, column=1)
flip_timer = window.after(3000, func=flip_card)

next_card()

window.mainloop()