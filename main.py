import pandas as pd
import random
import tkinter as tk

TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"
WORD_DATABASE = "data/english_words.csv"
TIME = 3000

df = pd.read_csv(WORD_DATABASE)
lang_in = df.columns[0]
lang_out = df.columns[1]
df = df[df[lang_in].str.len() > 1]
translation = ""


# ---------------------------- PICK WORD ------------------------------- #
def pick_word():
    global translation, flip_timer
    window.after_cancel(flip_timer)
    rnd_index = random.choice(df.index)
    word = df.loc[rnd_index][lang_in]
    translation = df.loc[rnd_index][lang_out]
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(card_title, text=lang_in, fill="black")
    canvas.itemconfig(card_word, text=word, fill="black")
    flip_timer = window.after(TIME, func=flip_card)


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(card_title, text=lang_out, fill="white")
    canvas.itemconfig(card_word, text=translation, fill="white")
    # pick_word()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(TIME, func=flip_card)

canvas = tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
title = tk.Label()
card = canvas.create_image(410, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=TITLE_FONT, tags="title")
card_word = canvas.create_text(400, 263, text="", font=WORD_FONT, tags="word")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

x_button_img = tk.PhotoImage(file="images/wrong.png")
x_button = tk.Button(image=x_button_img, highlightthickness=0, border=0, command=pick_word)
x_button.grid(row=1, column=0)

v_button_img = tk.PhotoImage(file="images/right.png")
v_button = tk.Button(image=v_button_img, highlightthickness=0, border=0, command=pick_word)
v_button.grid(row=1, column=1)

pick_word()

window.mainloop()
