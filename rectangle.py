from random import randint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self):
        self.start_point = Point(0,0)       # left up
        self.end_point = Point(0,0)     # right down

    def __str__(self):
        return f"### Rectangle ### " \
               f"My Width: {self.get_width()} My Height: {self.get_height()} " \
               f"My Surface: {self.get_surface()} My Perimeter: {self.get_perimeter()}"

    def get_width(self):
        return self.start_point.x - self.end_point.x

    def get_height(self):
        return self.start_point.y - self.end_point.y

    def get_surface(self):
        return self.get_width() * self.get_height()

    def get_perimeter(self):
        return 2 * self.get_height() + 2 * self.get_width()

    def randomize_start_point(self):
        self.start_point = Point(randint(1, 100), randint(1, 100))
        return self

    def randomize_end_point(self):
        self.end_point = Point(randint(1, 100), randint(1, 100))
        return self

    def filter_by_size(self, rec_list, threshold):
        ret = []
        for rec in rec_list:
            if rec.get_surface() >= threshold:
                ret.append(rec)

    def filter_by_perimeter(self, rec_list, threshold):
        ret = []
        for rec in rec_list:
            if rec.get_perimeter() >= threshold:
                ret.append(rec)

    def rand_rects(self):
        n = randint(1, 50)
        rectangles = []
        for i in range(n):
            rectangles.append(Rectangle().randomize_end_point().randomize_start_point())
        for rec in rectangles:
            if rec.get_surface() > 900 and rec.get_perimeter() > 30:
                print(rec)


def main():
    rectangle = Rectangle()
    rectangle.rand_rects()


if __name__ == '__main__':
    main()
