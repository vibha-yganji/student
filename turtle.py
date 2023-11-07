import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Turtle Dodge Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.speed(0)
player.penup()
player.goto(0, -250)

# Set the player's speed
player_speed = 15

# Create a list of enemy turtles
enemies = []

# Function to create a new enemy
def create_enemy():
    enemy = turtle.Turtle()
    enemy.shape("square")
    enemy.color("red")
    enemy.speed(0)
    enemy.penup()
    enemy.goto(random.randint(-290, 290), 290)
    enemy.dy = random.randint(2, 7)
    enemies.append(enemy)

# Function to move the player left
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -290:
        x = -290
    player.setx(x)

# Function to move the player right
def move_right():
    x = player.xcor()
    x += player_speed
    if x > 290:
        x = 290
    player.setx(x)

# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Create initial enemies
for _ in range(5):
    create_enemy()

# Main game loop
while True:
    # Move the enemies
    for enemy in enemies:
        y = enemy.ycor()
        y -= enemy.dy
        enemy.sety(y)

        # Check for collision with player
        if player.distance(enemy) < 20:
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over!")
            wn.bye()
        
        # Check if the enemy is out of the screen
        if y < -300:
            enemy.hideturtle()
            enemies.remove(enemy)
            create_enemy()

    # Update the screen
    wn.update()

# Close the game window when done
wn.bye()
