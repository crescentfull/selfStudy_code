# 터틀 그래픽을 활용하여 별모양을 그려보는 프로그램을 for 문을 이용하여 작성하시오.

import turtle

t = turtle.Pen()

for i in range(5):
    t.forward(50)
    t.right(145)
    
turtle.exitonclick() #그래픽 창을 클릭해야 화면에서 사라지게하는 코드