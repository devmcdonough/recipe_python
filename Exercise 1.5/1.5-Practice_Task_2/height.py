class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + " feet," + str(self.inches) + " inches"
        return output
    
    def __sub__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        difference_inches = height_A_inches - height_B_inches

        output_feet = difference_inches // 12

        output_inches = difference_inches % 12

        if output_inches < 0:
            output_feet -= 1
            output_inches += 12

        return Height(output_feet, output_inches)
    
person_A_Height = Height(5, 10)
person_B_Height = Height(3, 9)
height_difference = person_A_Height - person_B_Height

print("Difference in height: ", height_difference)