#터틀 그래픽을 이용하여 사각형 3개를 그려보자. 단 조건은 사각형은 20도씩 기울어져 있다.
import turtle

t = turtle.Pen()

# for i in range(5):
#     t.right(20)
#     t.forward(50)
#     t.right(90)
#     t.forward(50)
#     t.right(90)
#     t.forward(50)
#     t.right(90)
for i in range(3):
    t.left(20) #
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
turtle.exitonclick()