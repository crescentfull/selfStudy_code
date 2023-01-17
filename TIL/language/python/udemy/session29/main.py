from tkinter import *

window = Tk()

window.title("First GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=20)


# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack() # side=left right bottom top , expend=

my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.place(x=100, y=20) # 좌표설정 위치 마음대로 가능 ㅎ
# my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Entry
input = Entry(width=10)
input.pack()

# button
def button_clicked():                       # 버튼 클릭 이벤트 발생 함수
    my_label.config(text=input.get()) 

button = Button(text="Click", command=button_clicked)
button.pack()

window.mainloop()