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


    def __lt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches 
        return height_inches_A < height_inches_B
    
    def __eq__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches 
        return height_inches_A == height_inches_B
    
    def __le__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches 
        return height_inches_A <= height_inches_B

    def __gt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches 
        return height_inches_A > height_inches_B

    def __ge__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches 
        return height_inches_A >= height_inches_B

    def __ne__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches 
        return height_inches_A != height_inches_B


    
person_A_Height = Height(5, 10)
person_B_Height = Height(3, 9)
height_difference = person_A_Height - person_B_Height

comparison_lt = Height(4, 5) < Height(4,6)
comparison_eq = Height(4, 5) == Height(4, 5)
comparison_le = Height(4, 5) <= Height(4, 8)
comparison_gt = Height(4, 5) > Height(4, 8)
comparison_ge = Height(4, 5) >= Height(4, 8)
comparison_ne = Height(4, 5) != Height(4, 8)


# print("Difference in height: ", height_difference)
print(comparison_lt)
print(comparison_eq)
print(comparison_le)
print(comparison_gt)
print(comparison_ge)
print(comparison_ne)