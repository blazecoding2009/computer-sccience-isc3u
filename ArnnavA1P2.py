# Name: Arnnav Kudale
# Date: October 15, 2024
# Course Code: ICS3U1-02
# Description: Selection Statements Assignment

# Figure out each vertice of the rectangle, midpoints of each side and the midpoint of the rectangle
def define_rectangle_with_midpoints_and_quadrant(x, y, width, height, Px, Py):
    # Define the individual points of the rectangle
    Ax, Ay = x, y
    Bx, By = x, (y + height)
    Cx, Cy = (x + width), (y + height)
    Dx, Dy = (x + width), y
    
    # Define the midpoints of all sides of the rectangle
    Fx, Fy = x, (y + height / 2)
    Ix, Iy = (x + width / 2), (y + height)
    Hx, Hy = (x + width), (y + height / 2)
    Gx, Gy = (x + width / 2), y
    
    # Define the midpoint of the rectangle
    Mx, My = (x + width / 2), (y + height / 2)

    # Determine the quadrant of the rectangle that point P lies in
    quadrant = None
    if (x < Px < x + width) and (y < Py < y + height):
        if Px < Mx and Py < My:
            quadrant = "Quadrant 2"
        elif Px > Mx and Py < My:
            quadrant = "Quadrant 1"
        elif Px < Mx and Py > My:
            quadrant = "Quadrant 3"
        elif Px > Mx and Py > My:
            quadrant = "Quadrant 4"

    # Output the results
    print("The rectangle has vertices A(%i, %i), B(%i, %i), C(%i, %i), and D(%i, %i)." % (Ax, Ay, Bx, By, Cx, Cy, Dx, Dy))
    print("The midpoints are: F(%i, %i), I(%i, %i), H(%i, %i), G(%i, %i), M(%i, %i)." % (Fx, Fy, Ix, Iy, Hx, Hy, Gx, Gy, Mx, My))
    if quadrant:
        print("Point P(%i, %i) lies within %s." % (Px, Py, quadrant))
    elif (Px == x or Px == x + width or Py == y or Py == y + height):
        print("Point P(%i, %i) lies on the border of the rectangle." % (Px, Py))
    else:
        print("Point P(%i, %i) is outside the rectangle." % (Px, Py))

# validate if inputs are correctly entered
def validate_input(inputV, type, positive):
    if type == "point_P":
        if not validate_coordinates(inputV):
            inputV = validate_input(input("Invalid input. Enter the point P coordinates in the form (x, y): "), type, False)
    elif (not inputV.replace("-", "").replace("+", "").isdigit() or int(inputV) <= 0) and positive:
        inputV = validate_input(input("Invalid input. Enter a positive integer for the %s: " % type), type, False)
    elif not inputV.replace("-", "").replace("+", "").isdigit():
        inputV = validate_input(input("Invalid input. Enter an integer for the %s: " % type), type, True)
    return inputV

# validate if coordinates are correctly entered (basically must have a comma and two integers)
def validate_coordinates(coord_str):
    coord_str = coord_str.replace("(", "").replace(")", "").replace(" ", "")
    if "," not in coord_str:
        return False
    x_str = coord_str[:coord_str.find(",")]
    y_str = coord_str[coord_str.find(",") + 1:]
    return x_str.isdigit() and y_str.isdigit()

# return x and y coordinates from a string
def parse_coordinates(coord_str):
    coord_str = coord_str.replace("(", "").replace(")", "").replace(" ", "")
    x = int(coord_str[:coord_str.find(",")])
    y = int(coord_str[coord_str.find(",") + 1:])
    return x, y

# User input for rectangle coordinates and dimensions
x = int(validate_input(input("Enter the x-coordinate of point A: "), "x-coordinate", False))
y = int(validate_input(input("Enter the y-coordinate of point A: "), "y-coordinate", False))
width = int(validate_input(input("Enter the width of the rectangle: "), "width", True))
height = int(validate_input(input("Enter the height of the rectangle: "), "height", True))

# User input for point P coordinates
Px, Py = parse_coordinates(validate_input(input("Enter the point P coordinates in the form (x, y): "), "point_P", False))

define_rectangle_with_midpoints_and_quadrant(x, y, width, height, Px, Py)