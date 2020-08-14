

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        a = sum(self.scores) / len(self.scores)
        if a < 40:
            return("T")
        elif (40 <= a) and (a < 55):
            return("D")
        elif (55 <= a) and (a < 70):
            return("P")
        elif (70 <= a) and (a < 80):
            return ("A")
        elif (80 <= a) and (a < 90):
            return ("E")
        elif (90 <= a) and (a <= 100):
            return("O")
        else:
            return("")
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
