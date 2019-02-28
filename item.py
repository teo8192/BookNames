class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return "{} - {}".format(self.line_number, self.name)
