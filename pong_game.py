# Basic Pong Game Using the Turtle Library
#
#
#################################################


### Imports and creating the window

from random import choice
import turtle
window = turtle.Screen()
window.setup(height = 600, width = 900)
window.bgcolor("black")
window.title("Pong")
window.tracer(0)


### Game instructions

gameInstructions = turtle.Turtle()
gameInstructions.speed(0)
gameInstructions.penup()
gameInstructions.goto(0, 0)
gameInstructions.color("white")
gameInstructions.write("Press spacebar to start the game\n", font = ("Roboto", 20), \
        align = "center")
gameInstructions.goto(0, -30)
gameInstructions.write("First to 3 goals wins", font = ("Roboto", 20), align = "center")
gameInstructions.goto(0, -90)
gameInstructions.write("Click to exit the program", font = ("Roboto", 20), align = "center")
gameInstructions.hideturtle()


### Paddle instructions 

instructions = turtle.Turtle()
instructions.speed(0)
instructions.penup()
instructions.goto(0, -210)
instructions.color("white")
instructions.write("Left paddle: W and S keys to move        \
    Right paddle: Up and Down arrow keys to move", font = ("Roboto", 15), align = "center")
instructions.hideturtle()


### Creating the scoreboard

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.penup()
scoreboard.goto(0, 210)
scoreboard.color("white")
scoreboard.write("0                   0", font = ("Roboto", 45), align = "center")
scoreboard.hideturtle()
left_score = 0
right_score = 0


### Creating the paddles and the ball

# Left paddle
paddleLeft = turtle.Turtle()
paddleLeft.speed(0)
paddleLeft.penup()
paddleLeft.goto(-400, 0)
paddleLeft.shape("square")
paddleLeft.color("white")
paddleLeft.shapesize(6, 1)

# Right paddle
paddleRight = turtle.Turtle()
paddleRight.speed(0)
paddleRight.penup()
paddleRight.goto(400, 0)
paddleRight.shape("square")
paddleRight.color("white")
paddleRight.shapesize(6, 1)

# The ball
ball = turtle.Turtle()
ball.penup()
ball.goto(0, 0)
ball.shape("circle")
ball.color("white")
ball.shapesize(1)
speeds = [-1, 1]
direction = choice(speeds)
ball_x_speed = 0.255 * direction
ball_y_speed = 0.255 * direction


### Functions

# Left paddle moving up
def paddleLeftUp():
    leftY = paddleLeft.ycor() + 20
    paddleLeft.sety(leftY)
    if leftY > 240:
        leftY -= 20
        paddleLeft.sety(leftY)

# Left paddle moving down
def paddleLeftDown():
    leftY = paddleLeft.ycor() - 20
    paddleLeft.sety(leftY)
    if leftY < -240:
        leftY += 20
        paddleLeft.sety(leftY)

# Right paddle moving up
def paddleRightUp():
    rightY = paddleRight.ycor() + 20
    paddleRight.sety(rightY)
    if rightY > 240:
        rightY -= 20
        paddleRight.sety(rightY)

# Right paddle moving down
def paddleRightDown():
    rightY = paddleRight.ycor() - 20
    paddleRight.sety(rightY)
    if rightY < -240:
        rightY += 20
        paddleRight.sety(rightY)


# Function to start the game
def startGame():
    gameInstructions.clear()
    instructions.clear()

    global left_score
    global right_score
    global ball_x_speed
    global ball_y_speed

    # While loop to keep the game running until a player reaches 3 points
    while left_score < 3 and right_score < 3:
        window.update()

        ball.setx(ball.xcor() + ball_x_speed)
        ball.sety(ball.ycor() + ball_y_speed)

        ## Scoring a point and the boundaries for the ball

        # Left paddle scores
        if ball.xcor() > 460:
            left_score += 1
            scoreboard.clear()
            scoreboard.write(f"{left_score}                   {right_score}", \
                    font = ("Roboto", 45), align = "center")
            ball.goto(0, 0)
            direction = choice(speeds)
            ball_x_speed *= -1
            ball_y_speed *= direction

        # Right paddle scores
        if ball.xcor() < -460:
            right_score += 1
            scoreboard.clear()
            scoreboard.write(f"{left_score}                   {right_score}", \
                    font = ("Roboto", 45), align = "center")
            ball.goto(0, 0)
            direction = choice(speeds)
            ball_x_speed *= -1
            ball_y_speed *= direction

        # Ball hitting the top and bottom boundaries
        if ball.ycor() > 290:
            ball.sety(290)
            ball_y_speed *= -1
            
        if ball.ycor() < -290:
            ball.sety(-290)
            ball_y_speed *= -1
        
        ## Physics for the ball hitting the paddles

        # Hitting the left paddle    
        if (ball.xcor() < (paddleLeft.xcor() + 10) and ball.xcor() > (paddleLeft.xcor() - 10)) \
        and (ball.ycor() >= (paddleLeft.ycor() - 60) and ball.ycor() <= (paddleLeft.ycor() + 60)):
            ball_x_speed *= -1
            ball_y_speed *= -1
        
        # Hitting the right paddle
        if (ball.xcor() > (paddleRight.xcor() - 10) and ball.xcor() < (paddleRight.xcor() + 10)) \
        and (ball.ycor() >= (paddleRight.ycor() - 60) and ball.ycor() \
        <= (paddleRight.ycor() + 60)):
            ball_x_speed *= -1
            ball_y_speed *= -1

    ## Ending the game and declaring a winner
            
    if left_score > right_score:
        scoreboard.goto(0, 0)
        scoreboard.write("Left Player Wins!", font = ("Roboto", 30), align = "center")

    elif right_score > left_score:
        scoreboard.goto(0, 0)
        scoreboard.write("Right Player Wins!", font = ("Roboto", 30), align = "center")


### Keystrokes

window.onkeypress(startGame, "space")
window.onkeypress(paddleRightUp, "Up")
window.onkeypress(paddleRightDown, "Down")
window.onkeypress(paddleLeftUp, "w")
window.onkeypress(paddleLeftDown, "s")
window.listen()

# Exiting the game
window.exitonclick()



### End of program
