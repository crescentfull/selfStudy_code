from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 ==0:
        count_down(long_break_sec)
        title_label.conig(text="break", fg=RED)
    elif count_down(short_break_sec) % 2 == 0:
        count_down(short_break_sec)
    else:
        count_down(work_sec)

    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:                          # 시작할때 5:00 으로 표시
        count_sec = "00"
    elif count_sec < 10:                        # 9초부터 09 08 07 이렇게 표시해주기
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0: 
        window.after(1000, count_down, count -1)
    
# ---------------------------- UI SETUP ------------------------------- #

# GUI 생성
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW) # 위치조정, 배경색

# title
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# img
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # 위치조정, 배경색
tomato_img = PhotoImage(file="tomato.png") # 이미지 변수
canvas.create_image(100,112, image=tomato_img) # 이미지 생성
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) # 카운트 다운 숫자 생성
canvas.grid(column=1, row=1)

# button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightthickness=0)
reset_button.grid(column=2, row=2)
# ! pack() grid() 같이 못쓴다.

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)



window.mainloop()