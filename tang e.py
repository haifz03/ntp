import turtle

# Khởi tạo Turtle

t = turtle.Turtle()

# Thay đổi màu nét vẽ thành đỏ

t.pencolor("red")

# Tô màu đỏ cho trái tim

t.begin_fill()

t.fillcolor("red")

t.left(45)

t.forward(100)

t.circle(50, 180)

t.right(90)

t.circle(50, 180)

t.forward(100)

t.end_fill()

# Vẽ chi tiết rêu trên trái tim

t.penup()

t.goto(40, 60)

t.pencolor("green")

t.pendown()

t.right(45)

t.forward(15)

t.circle(10, 180)

t.forward(15)

# Vẽ chi tiết hoa trên trái tim

t.penup()

t.goto(-50, 80)

t.pencolor("yellow")

t.pendown()

t.begin_fill()

t.fillcolor("yellow")

for i in range(5):

    t.forward(20)

    t.right(144)

t.end_fill()

# Viết chữ "I love you" vào trong trái tim

t.penup()

t.goto(0, 60)

t.pencolor("white")

t.write("I love you", align="center", font=("Arial", 20, "bold"))

# Dừng chương trình để xem kết quả

turtle.done()