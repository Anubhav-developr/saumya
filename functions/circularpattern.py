import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
star_turtle = turtle.Turtle()
star_turtle.shape("turtle")
star_turtle.speed(10)

# Function to draw a circle of stars
def draw_star_circle(radius, num_stars):
    angle = 360 / num_stars  # Angle between each star

    for _ in range(num_stars):
        star_turtle.penup()
        star_turtle.forward(radius)
        star_turtle.pendown()
        star_turtle.write("*", align="center", font=("Arial", 12, "normal"))
        star_turtle.penup()
        star_turtle.backward(radius)
        star_turtle.left(angle)

# Call the function to draw the circle of stars
draw_star_circle(100, 12)  # 100 is the radius and 12 is the number of stars

# Hide the turtle and display the window
star_turtle.hideturtle()
turtle.done()
