fruits = ["apple", "pear", "orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except:
        print("fruit pie")
    else:
        print(fruit+"pie")

make_pie(2)
make_pie(1)
make_pie(0)
make_pie(5)

