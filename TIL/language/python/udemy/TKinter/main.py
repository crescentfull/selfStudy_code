from tkinter import *

window = Tk()

window.title("First GUI program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack() # side=left right bottom top , expend=

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Entry
input = Entry(width=10)
input.pack()

# button
def button_clicked():                       # 버튼 클릭 이벤트 발생 함수
    my_label.config(text=input.get()) 

button = Button(text="Click", command=button_clicked)
button.pack()

window.mainloop()