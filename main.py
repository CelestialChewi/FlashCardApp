from tkinter import *


# UI Setup
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg="#B1DDC6")

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text="Title", font=("Arial", 30, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 50, "bold"))
canvas.config(bg="#B1DDC6", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0)
cross_button.grid(row=1, column=0)

checked_image = PhotoImage(file="images/right.png")
checked_button = Button(image=checked_image, highlightthickness=0)
checked_button.grid(row=1, column=1)

window.mainloop()