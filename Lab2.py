# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    # TODO: Implement this function
    pass  # Replace with your code
    g=9.8
    h=float(h0) - 0.5 * g * float(t) * float(t)
    return str(round(h,1))

for _ in range(3):
    h0=input("Enter initial height: ")
    t=input("Enter time: ")
    h=calculate_height(h0,t)
    print("Height of the ball at time " + t + " second = " + h + " meters")
    print()

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    pass  # Replace with your code
    speed=20.0
    distance=speed*float(time)
    return str(round(distance,1))

for _ in range (3):
    time=input("Enter time for car (in seconds): ")
    distance=calculate_car_distance(time)
    print("The car will travel " + distance + " meters in " + time + " second.")
    print()
