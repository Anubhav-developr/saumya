import math

# Function to draw a circular pattern of stars
def draw_star_circle(radius):
    # Loop through a square grid that contains the circle
    for y in range(-radius, radius+1):
        for x in range(-radius, radius+1):
            # Calculate the distance from the center (0, 0)
            distance = math.sqrt(x**2 + y**2)
            
            # If the distance is close to the radius, print a star
            if radius - 0.5 < distance < radius + 0.5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Call the function to draw the circle
draw_star_circle(10)  # 10 is the radius of the circle
