'''
Implementation of creative coding problems from Brilliant.
'''

import turtle
import math

# ============= Basic Setup Functions =============
def setup_screen(width=400, height=400):
    """Set up the screen with specified dimensions"""
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.bgcolor("white")
    screen.setworldcoordinates(-width/2, -height/2, width/2, height/2)
    return screen

def setup_turtle():
    """Initialize the turtle with proper settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.hideturtle()
    return t

# ============= Basic Shape Functions =============
def draw_circle(t, radius, color):
    """Draw a circle with given radius and color"""
    t.penup()
    t.goto(0, -radius)
    t.setheading(0)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_regular_polygon(t, sides, radius, color, rotation=0):
    """Draw a regular polygon with given sides, radius, color, and rotation"""
    t.penup()
    t.goto(0, 0)
    t.setheading(rotation)
    
    # Calculate side length
    side_length = 2 * radius * math.sin(math.pi / sides)
    
    # Move to starting position
    t.forward(radius)
    t.right(90 + (180 / sides))
    
    # Draw the polygon
    t.fillcolor(color)
    t.begin_fill()
    t.pendown()
    for _ in range(sides):
        t.forward(side_length)
        t.right(360 / sides)
    t.end_fill()

# ============= Original Shape Creation Functions =============
def create_nested_shapes():
    """Create the original nested shapes figure"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Base radius for scaling
    base_radius = 150
    
    # Draw shapes from largest to smallest
    draw_circle(t, base_radius, "red")
    draw_regular_polygon(t, 6, base_radius * 1.0, "yellow", 90)
    draw_regular_polygon(t, 4, base_radius * 1.0, "green", 45)
    draw_regular_polygon(t, 3, base_radius * 1.0, "blue", 90)
    
    # Save and clean up
    canvas = screen.getcanvas()
    canvas.postscript(file="figure1.eps", colormode='color')
    screen.clear()

def create_nested_squares():
    """Create nested squares figure with black borders"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties for border
    t.width(1)
    t.pencolor("black")
    
    size = 150
    for _ in range(15):
        # Draw square
        t.penup()
        t.goto(-size/2, -size/2)  # Center the square
        t.setheading(0)
        
        # Set colors and start drawing
        t.fillcolor("red")
        t.pendown()  # Ensure pen is down for border
        t.begin_fill()
        
        # Draw the square
        for _ in range(4):
            t.forward(size)
            t.left(90)
        
        t.end_fill()
        size -= 10
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure2.eps", colormode='color')
    screen.clear()

def create_shrinking_hexagons():
    """Create nested hexagons with 90% reduction"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    size = 125
    for _ in range(15):
        draw_regular_polygon(t, 6, size, "yellow", 0)
        size *= 0.9
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure3.eps", colormode='color')
    screen.clear()

def create_shrinking_triangles():
    """Create nested triangles with 50% reduction"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    size = 120
    for _ in range(6):
        draw_regular_polygon(t, 3, size, "green", 90)
        size *= 0.5
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure4.eps", colormode='color')
    screen.clear()

def create_shrinking_circles():
    """Create nested circles with 5-pixel reduction"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    size = 125
    for _ in range(25):
        draw_circle(t, size, "blue")
        size -= 5
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure5.eps", colormode='color')
    screen.clear()

# ============= Rotating Square Pattern Functions =============
def draw_rotating_square_pattern(filename, initial_color, color_function):
    """
    Draw rotating squares with a specified color pattern
    
    Args:
        filename: Output EPS file name
        initial_color: Starting color for the squares
        color_function: Function that determines the next color based on current color
    """
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    size = 120
    angle = 30
    color = initial_color
    
    # Set pen properties for border
    t.width(1)  # Set border width
    t.pencolor("black")  # Set border color
    
    for i in range(10):
        t.penup()
        t.goto(0, 0)  # Move to center
        t.setheading(angle)  # Set rotation angle
        
        # Move back by half the size to center the square
        t.forward(-size/2)
        t.right(90)
        t.forward(size/2)
        t.left(90)
        
        # Draw square
        t.fillcolor(color)
        t.begin_fill()
        t.pendown()  # Ensure pen is down to draw border
        for _ in range(4):
            t.forward(size)
            t.left(90)
        t.end_fill()
        
        # Update variables
        size -= 10
        angle += 30
        color = color_function(color, angle)
    
    canvas = screen.getcanvas()
    canvas.postscript(file=filename, colormode='color')
    screen.clear()

# Color changing functions
def red_white_alternating(current_color, angle):
    return "white" if current_color == "red" else "red"

def blue_white_alternating(current_color, angle):
    return "white" if current_color == "blue" else "blue"

def white_blue_alternating(current_color, angle):
    return "blue" if current_color == "white" else "white"

def angle_based_color(current_color, angle):
    return "red" if angle > 90 else "white"

def create_red_white_squares():
    """Create rotating squares alternating red and white"""
    draw_rotating_square_pattern("figure6.eps", "red", red_white_alternating)

def create_blue_white_squares():
    """Create rotating squares alternating blue and white"""
    draw_rotating_square_pattern("figure7.eps", "blue", blue_white_alternating)

def create_white_blue_squares():
    """Create rotating squares starting with white"""
    draw_rotating_square_pattern("figure8.eps", "white", white_blue_alternating)

def create_angle_based_squares():
    """Create rotating squares with color based on angle"""
    draw_rotating_square_pattern("figure9.eps", "white", angle_based_color)

def create_alternating_color_squares(initial_color="white"):
    """Create rotating squares with specified initial color"""
    draw_rotating_square_pattern("figure10.eps", initial_color, white_blue_alternating)

def create_count_based_spiral():
    """Create spiral pattern with count-based size reduction and angle"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties for border
    t.width(1)
    t.pencolor("black")
    
    for count in range(1, 31):  # 30 squares
        # Calculate size and angle based on count
        size = 150 - (count * 5)
        angle = count * 5
        
        t.penup()
        t.goto(0, 0)  # Move to center
        t.setheading(angle)  # Set rotation angle
        
        # Move back by half the size to center the square
        t.forward(-size/2)
        t.right(90)
        t.forward(size/2)
        t.left(90)
        
        # Draw square
        t.fillcolor("blue")
        t.begin_fill()
        t.pendown()
        for _ in range(4):
            t.forward(size)
            t.left(90)
        t.end_fill()
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure11.eps", colormode='color')
    screen.clear()

def create_divided_squares():
    """Create pattern with size divided by count"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties for border
    t.width(1)
    t.pencolor("black")
    
    for count in range(1, 11):  # 10 squares
        # Calculate size and angle based on count
        size = 150 / count
        angle = count * 5
        
        t.penup()
        t.goto(0, 0)  # Move to center
        t.setheading(angle)  # Set rotation angle
        
        # Move back by half the size to center the square
        t.forward(-size/2)
        t.right(90)
        t.forward(size/2)
        t.left(90)
        
        # Draw square
        t.fillcolor("green")
        t.begin_fill()
        t.pendown()
        for _ in range(4):
            t.forward(size)
            t.left(90)
        t.end_fill()
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure12.eps", colormode='color')
    screen.clear()

def create_fifth_shape_pattern():
    """Create pattern where every fifth shape is green and rotated"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties for border
    t.width(1)
    t.pencolor("black")
    
    for count in range(1, 13):  # 12 shapes
        size = 125 - (count * 10)
        
        # Set color and angle based on count
        if count % 5 == 0:
            color = "green"
            angle = 45
        else:
            color = "white"
            angle = 0
            
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        
        # Center the square
        t.forward(-size/2)
        t.right(90)
        t.forward(size/2)
        t.left(90)
        
        # Draw square
        t.fillcolor(color)
        t.begin_fill()
        t.pendown()
        for _ in range(4):
            t.forward(size)
            t.left(90)
        t.end_fill()
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure13.eps", colormode='color')
    screen.clear()

def create_third_shape_rotation():
    """Create pattern where every third shape is green and rotated"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties for border
    t.width(1)
    t.pencolor("black")
    
    for count in range(1, 13):  # 12 shapes
        size = 125 - (count * 10)
        
        # Set color and angle based on count
        if count % 3 == 0:
            color = "green"
            angle = 45
        else:
            color = "white"
            angle = 0
            
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        
        # Center the square
        t.forward(-size/2)
        t.right(90)
        t.forward(size/2)
        t.left(90)
        
        # Draw square
        t.fillcolor(color)
        t.begin_fill()
        t.pendown()
        for _ in range(4):
            t.forward(size)
            t.left(90)
        t.end_fill()
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure14.eps", colormode='color')
    screen.clear()

def create_third_hexagon_pattern():
    """Create pattern where every third hexagon is green"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties for border
    t.width(1)
    t.pencolor("black")
    
    for count in range(1, 13):  # 12 shapes
        size = 125 - (count * 10)
        
        # Set color based on count
        color = "green" if count % 3 == 0 else "white"
        
        # Draw hexagon using regular polygon function
        draw_regular_polygon(t, 6, size, color, 0)
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure15.eps", colormode='color')
    screen.clear()

def create_even_odd_hexagon_pattern():
    """Create pattern where even count shapes are green"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties for border
    t.width(1)
    t.pencolor("black")
    
    for count in range(1, 13):  # 12 shapes
        size = 125 - (count * 10)
        
        # Set color based on even/odd count
        color = "green" if count % 2 == 0 else "white"
        
        # Draw hexagon using regular polygon function
        draw_regular_polygon(t, 6, size, color, 0)
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure16.eps", colormode='color')
    screen.clear()

def create_moving_hexagons():
    """Create pattern of hexagons that shift right progressively"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties for border
    t.width(1)
    t.pencolor("black")
    
    size = 50  # Fixed size for all hexagons
    y_offset = -5  # Fixed y position
    
    for count in range(10):  # 0 to 9
        # Calculate x position based on count
        x_offset = count * 5
        
        # Move to position before drawing
        t.penup()
        t.goto(x_offset, y_offset)
        
        # Draw hexagon
        t.fillcolor("red")
        t.begin_fill()
        t.pendown()
        
        # Draw hexagon manually to ensure proper positioning
        for _ in range(6):
            t.forward(size)
            t.left(60)
            
        t.end_fill()
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure17.eps", colormode='color')
    screen.clear()

def create_moving_triangles():
    """Create pattern of triangles that move right and down"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties for border
    t.width(1)
    t.pencolor("black")
    
    size = 50  # Fixed size for all triangles
    
    for count in range(11):  # 0 to 10
        # Calculate positions based on count
        x = -50 + (count * 10)  # Start at -50, move right by 10 each time
        y = 25 - (count * 5)    # Start at 25, move down by 5 each time
        
        # Move to position before drawing
        t.penup()
        t.goto(x, y)
        t.setheading(0)  # Point right
        
        # Draw triangle
        t.fillcolor("red")
        t.begin_fill()
        t.pendown()
        
        # Draw equilateral triangle
        for _ in range(3):
            t.forward(size)
            t.left(120)
            
        t.end_fill()
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure18.eps", colormode='color')
    screen.clear()

def create_conditional_vertical_triangles():
    """Create pattern with triangles moving down based on count parity and zigzagging"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties
    t.width(1)
    t.pencolor("black")
    
    # Draw the sun/circle centered
    t.penup()
    t.goto(0, 0)  # Center position
    t.fillcolor("yellow")
    t.begin_fill()
    t.pendown()
    t.circle(50)
    t.end_fill()
    
    # Move to initial position for triangles
    t.penup()
    t.goto(0, 10)  # Starting position
    
    # Draw triangles with conditional movement
    size = 50
    for count in range(11):  # 0 to 10
        # Calculate x position - zigzag pattern
        if count % 2 == 0:
            x = count * 5  # Move right
        else:
            x = count * -5  # Move left
            
        # Calculate y position based on even/odd
        if count % 2 == 0:
            y = count * -2  # Move down by twice count
        else:
            y = count * -3  # Move down by three times count
        
        # Move to position and draw triangle
        t.penup()
        t.goto(x, y)
        t.setheading(0)
        
        # Draw triangle
        t.fillcolor("green")
        t.begin_fill()
        t.pendown()
        for _ in range(3):
            t.forward(size)
            t.left(120)
        t.end_fill()
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure19.eps", colormode='color')
    screen.clear()

def create_conditional_horizontal_triangles():
    """Create pattern with triangles moving left/right based on count parity"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties
    t.width(1)
    t.pencolor("black")
    
    size = 50
    for count in range(10):  # 0 to 9
        # Calculate x position based on even/odd
        if count % 2 == 0:
            x = count * 5  # Move right
        else:
            x = count * -5  # Move left
            
        y = 0  # Fixed y position
        
        # Move to position and draw triangle
        t.penup()
        t.goto(x, y)
        t.setheading(0)
        
        # Draw triangle
        t.fillcolor("green")
        t.begin_fill()
        t.pendown()
        for _ in range(3):
            t.forward(size)
            t.left(120)
        t.end_fill()
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure20.eps", colormode='color')
    screen.clear()

def create_rgb_pattern_circles():
    """Create concentric circles with RGB color patterns"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties
    t.width(1)
    t.pencolor("black")
    
    # Draw circles from largest to smallest
    g = 50  # Fixed green value
    b = 50  # Fixed blue value
    
    for count in range(5):  # 0 to 4
        # Calculate size
        size = 120 - (count * 20)
        
        # Calculate color values
        r = count * 50  # Red increases: 0, 50, 100, 150, 200
        # g stays constant at 50
        # b stays constant at 50
        
        # Create RGB color string
        color = (r/255, g/255, b/255)  # Convert to 0-1 range for turtle
        
        # Draw circle
        t.penup()
        t.goto(0, -size)  # Position for circle
        t.pendown()
        
        t.fillcolor(color)
        t.begin_fill()
        t.circle(size)
        t.end_fill()
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure21.eps", colormode='color')
    screen.clear()

def create_rgb_pattern_circles_green():
    """Create concentric circles with increasing green values"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties
    t.width(1)
    t.pencolor("black")
    
    for count in range(5):  # 0 to 4
        # Calculate size
        size = 120 - (count * 20)
        
        # Calculate RGB values
        r = count * 50  # Red: 0, 50, 100, 150, 200
        g = 30 + (count * 30)  # Green: 30, 60, 90, 120, 150
        b = 160 - (count * 40)  # Blue: 160, 120, 80, 40, 0
        
        # Create RGB color string
        color = (r/255, g/255, b/255)
        
        # Draw circle
        t.penup()
        t.goto(0, -size)
        t.pendown()
        
        t.fillcolor(color)
        t.begin_fill()
        t.circle(size)
        t.end_fill()
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure22.eps", colormode='color')
    screen.clear()

import random

import random

def create_random_circles():
    """Create pattern of circles with random positions, sizes, and colors"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties
    t.width(1)
    t.pencolor("black")
    
    for count in range(30):  # 0 to 29
        # Random position
        x = random.randint(-75, 75)
        y = random.randint(-75, 75)
        
        # Random size
        size = random.randint(0, 100)
        
        # Random RGB colors (converting to 0-1 range)
        r = random.randint(0, 250) / 255
        g = random.randint(0, 250) / 255
        b = random.randint(0, 250) / 255
        
        # Move to position
        t.penup()
        t.goto(x, y)
        
        # Draw circle
        t.fillcolor((r, g, b))
        t.begin_fill()
        t.pendown()
        t.circle(size)
        t.end_fill()
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure23.eps", colormode='color')
    screen.clear()

def create_random_concentric_circles():
    """Create concentric circles with random RGB values"""
    turtle.reset()
    turtle.clearscreen()
    
    screen = setup_screen()
    t = setup_turtle()
    
    # Set pen properties
    t.width(1)
    t.pencolor("black")
    
    for count in range(5):  # 0 to 4
        # Calculate size
        size = 120 - (count * 20)
        
        # Random RGB values with constraints (converting to 0-1 range)
        r = random.randint(150, 250) / 255  # Higher range for red
        g = random.randint(0, 250) / 255    # Full range for green
        b = random.randint(0, 250) / 255    # Full range for blue
        
        # Move to position and draw
        t.penup()
        t.goto(0, -size)
        
        # Draw circle
        t.fillcolor((r, g, b))
        t.begin_fill()
        t.pendown()
        t.circle(size)
        t.end_fill()
    
    canvas = screen.getcanvas()
    canvas.postscript(file="figure24.eps", colormode='color')
    screen.clear()

# Update main() function to include new patterns
def main():
    """Create all figures sequentially"""
    try:
        #'''
        print("Creating original figures...")
        create_nested_shapes()          # figure1.eps - Original nested shapes
        create_nested_squares()         # figure2.eps - Nested red squares
        create_shrinking_hexagons()     # figure3.eps - Shrinking hexagons
        create_shrinking_triangles()    # figure4.eps - Shrinking triangles
        create_shrinking_circles()      # figure5.eps - Shrinking circles
        
        print("Creating rotating square patterns...")
        create_red_white_squares()      # figure6.eps - Red/white alternating
        create_blue_white_squares()     # figure7.eps - Blue/white alternating
        create_white_blue_squares()     # figure8.eps - White/blue alternating
        create_angle_based_squares()    # figure9.eps - Angle-based coloring
        create_alternating_color_squares() # figure10.eps - Alternating colors
        
        print("Creating count-based patterns...")
        create_count_based_spiral()     # figure11.eps - Blue spiral
        create_divided_squares()        # figure12.eps - Divided squares
        
        print("Creating modulo-based patterns...")
        create_fifth_shape_pattern()    # figure13.eps - Every fifth shape green
        create_third_shape_rotation()   # figure14.eps - Every third shape rotated
        create_third_hexagon_pattern()  # figure15.eps - Every third hexagon pattern
        create_even_odd_hexagon_pattern() # figure16.eps - Even/odd hexagons
        
        print("Creating moving patterns...")
        create_moving_hexagons()        # figure17.eps - Moving hexagons
        create_moving_triangles()       # figure18.eps - Moving triangles
        create_conditional_vertical_triangles() # figure19.eps - Conditional vertical
        create_conditional_horizontal_triangles() # figure20.eps - Conditional horizontal
        
        print("Creating color intensity patterns...")
        # First RGB pattern - with red progression
        create_rgb_pattern_circles()    # figure21.eps - Red progression (0,50,100,150,200)
        # Second RGB pattern - with green progression
        create_rgb_pattern_circles_green() # figure22.eps - Multiple color progressions
        #'''        
        print("Creating random patterns...")
        create_random_circles()        # figure23.eps - Random position circles
        create_random_concentric_circles() # figure24.eps - Random color concentric circles
        
        print("All figures have been created successfully!")
        
    finally:
        try:
            turtle.bye()
        except:
            pass

if __name__ == "__main__":
    main()