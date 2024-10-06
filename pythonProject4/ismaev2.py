class Figure:
    unit = "см"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, __side_length):
        super().__init__()
        self.side_length = __side_length

    def calculate_area(self):
        return self.side_length ** 2

    def info(self, square=None):
        area = self.calculate_area()
        print(f"Square side Lenght:{self.side_length}{self.unit}, area:"
              f"{area}{self.unit}.")

        # square1 = Square(5)
        # square2 = Square(3)
        # square_list = [square1, square2]

        # for square_list in square_list:
        #     square.info()


class Rectangle(Figure):
    def __init__(self, __length, __width):
        super().__init__()
        self.length = __length
        self.width = __width

    def calculate_area(self):
        return self.length * self.width

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length:{self.length}{self.unit} width:"
              f"{self.width}"f"{self.unit} area:{area}{self.unit}")

        rectangle1 = Rectangle(5, 8)
        rectangle2 = Rectangle(3, 6)
        rectangle3 = Rectangle(4, 10)
        rectangle_list = [rectangle1, rectangle2, rectangle3]

        for rectangle in rectangle_list:
            rectangle.info()
