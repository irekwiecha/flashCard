import tkinter as tk

TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
title = tk.Label()
canvas.create_image(410, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
canvas.create_text(400, 263, text="word", font=WORD_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

x_button_img = tk.PhotoImage(file="images/wrong.png")
x_button = tk.Button(image=x_button_img, highlightthickness=0, border=0)
x_button.grid(row=1, column=0)

v_button_img = tk.PhotoImage(file="images/right.png")
v_button = tk.Button(image=v_button_img, highlightthickness=0, border=0)
v_button.grid(row=1, column=1)

window.mainloop()
