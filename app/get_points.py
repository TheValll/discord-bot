# Import the required libraries
import random

def get_points(real_date):

    day = real_date.day
    points = random.randint(1, 10)
    percentage = 0

    if day >= 23 :
        percentage = random.randint(1, 100)
    
    return points, percentage