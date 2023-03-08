from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records") # data에서 뽑아온 정보를 dictionary로 변환 , 표 형식을 사용하기 위해 orient="records"를 이용 [{열:값, 열:값}, {열:값, 열:값}]
current_card = {}

# -------- card 넘기기 --------
def next_card():   
    '''
    click the check button, next card function
    '''
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, iamge=card_front_img)
    window.after(3000, func=flip_card)
# ---------------------------
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
# ---------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263,image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png") 
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()