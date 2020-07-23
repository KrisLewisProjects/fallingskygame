# Beginner level game in Python
# Tutorial by @TokyoEdTech


import turtle
import random
#import os

# add sound
#os.PlaySound("flamesound.mp3", winsound.SND_FILENAME)

score = 0
lives = 3

wn = turtle.Screen()
wn.title("Falling Stars")
wn.bgcolor("black")
wn.bgpic("nightskyyy.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("rain.gif")
wn.register_shape("bolt.gif")
wn.register_shape("player.gif")
wn.register_shape("player_left.gif")
wn.register_shape("nightskyyy.gif")

#camera_dx = 0
#camera_x = 0

# Add player
player = turtle.Turtle()
player.speed(0)
player.shape("player.gif")
player.color("gold")
player.penup()
player.goto(0, -250)
# making player move
player.direction = "stop"

# create list of rain
drops = []

# Add falling rain
for _ in range(50):
    rain = turtle.Turtle()
    rain.speed(-2)
    rain.shape("rain.gif")
    rain.color("blue")
    rain.penup()
    rain.goto(-100, 250)
    rain.speed = random.randint(1, 4)
    drops.append(rain)

# create list of Bolts
bolts = []

# Add bolts
for _ in range(10):
    bolt = turtle.Turtle()
    bolt.speed(-1)
    bolt.shape("bolt.gif")
    bolt.color("blue")
    bolt.penup()
    bolt.goto(100, 250)
    bolt.speed = random.randint(1, 2)
    bolts.append(bolt)

# making player move

# Make the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(-4)
pen.shape("square")
pen.color("red")
pen.penup()
pen.goto(0, 260)
font = ("Courier", 24, "bold")
pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

# Functions
def go_left():
    #global camera_dx
    #camera_dx += 3
    player.direction = "left"
    player.shape("player_left.gif")

def go_right():
    #global camera_dx
    #camera_dx += -3
    player.direction = "right"
    player.shape("player.gif")


# Keyboard binding
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:

    #camera_x += camera_dx
    #pen.goto(camera_x, 300)

    # Update Screen
    wn.update()
    #pen.clear()

    # Create scrolling background
    # pen.shape("nightskyyy.gif")
    # pen.stamp()

    # Move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)

    # Move the drops
    for rain in drops:
        y = rain.ycor()
        y -= rain.speed
        rain.sety(y)

        # check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            rain.goto(x, y)

        # check for a collision with player
        if rain.distance(player) < 100:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            rain.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

    # Move the bolts
    for bolt in bolts:
        y = bolt.ycor()
        y -= bolt.speed
        bolt.sety(y)

        # check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bolt.goto(x, y)

        # check for a collision with player
        if bolt.distance(player) < 40:
            #os.system("afplay power_up.mp3&")
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bolt.goto(x, y)
            score += 10
            lives -= 1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

wn.mainloop()
