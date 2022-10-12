#imports
import turtle, time, random

delay = 0.1

#score
score = 0
high_score = 0

#set up screen
window=turtle.Screen()
window.title("Snake Game")
window.bgcolor("white")
window.setup(width=600, height=600)
window.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.shapesize(stretch_wid=1, stretch_len=1)
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.shapesize(stretch_wid=0.8, stretch_len=0.8)
food.penup()
food.goto(0, 100)

segments = []

#scoreboards
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("score: 0 High score: 0", align = "center", font=("ds-digital", 24, "normal"))

 #function
 #setting the rule for the movement
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#keyboard bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
#i will try to use this same setting to d the second control
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

#main loop
while True:
    window.update()

    #check collision with border area
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide the segments
        for segment in segments:
            segment.goto(1000,1000) #out of range
        segments.clear()

        #reset secre
        score = 0

        #reset delay
        delay = 0.1

        sc.clear()
        sc.write("score: {} High score: {}".format(score, high_score), align="center", font=("ds-digital",24,"normal"))

    #check collision with food
    if head.distance(food) <20:
        #move the food to random place
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

            #add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -= 0.001
        #increase the score
        score += 10

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("score: {} High score: {}".format(score, high_score), align="center", font=("ds-digital",24,"normal"))

    #move the segment in reverse order
    for index in range(len(segments)-1,0,-1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x,y)
        #move segment 0 to head
    if len(segments)>0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

    move()

    #check for collision with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide segment
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1

            #update thr score
            sc.clear()
            sc.write("score: {} High score: {}".format(score,high_score), align="center", font=("ds-digital",24,"normal"))
    time.sleep(delay)
window.mainloop()