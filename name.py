class Name:
    def __init__(self, name, line_number):
        self.name = name
        self.line_number = line_number

    def __str__(self):
        return "{} - {}".format(self.line_number, self.name)
