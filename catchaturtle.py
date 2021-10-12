# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random

#-----game configuration----
trtl_color = ["blue", "red", "green", "purple", "yellow"]
trtl_size = 3
trtl_shape = ["circle","turtle","arrow","classic","square"]
score = 0
font_setup=("arial", 20, "normal")
timer = 10
timer_up = False
counter_interval = 1000   #1000 represents 1 second

#-----initialize turtle-----
trtl=turtle.Turtle()
trtl.fillcolor(random.choice(trtl_color))
trtl.shape(random.choice(trtl_shape))
trtl.shapesize(trtl_size)
trtl.penup()

score_writer = turtle.Turtle()
score_writer.penup()
score_writer.goto(-150,195)
score_writer.hideturtle()

counter =  turtle.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(150,195)

#-----game functions--------
def turtle_clicked(x,y):
  global timer
  trtl.fillcolor(random.choice(trtl_color))
  trtl.shape(random.choice(trtl_shape))
  if timer_up == False:
    update_score()
    trtl.hideturtle()
    change_position()
    trtl.showturtle()
  else:
    trtl.hideturtle()
    

def change_position():
    new_xpos = random.randint(-190,190)
    new_ypos = random.randint(-140,140)
    trtl.goto(new_xpos,new_ypos)

def update_score():
    global score 
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    print(score)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
 

#-----events----------------

trtl.onclick(turtle_clicked)



wn = turtle.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()