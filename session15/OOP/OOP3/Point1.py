import math


class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
    def __init__(self,a=0, b=0): 
        self.x= a
        self.y= b

    def __str__(self):
        return '({}, {}).'.format(self.x, self.y)

    def __add__(self, other):
        new_point = Point (self.x + other.x, self.y + other.y)
        return new_point
        
    def __sub__(self, other):
        new_point_1 = Point (self.x-other.x, self.y-other.y)
        return new_point_1
    
    def __eq__(self, other):
        return self.x== other.x, self.y== other.y
    
    def __contains__(self, value):
        return value== self.x or value== self.y


    # def print_point(self):
    #     print('({}, {}).'.format(self.x, self.y))


# def print_point(p):
#     """Print a Point object in human-readable format."""
#     print('({}, {}).'.format(p.x, p.y))


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    x_diff = p2.x - p1.x
    y_diff = p2.y - p1.y
    distance = math.sqrt(x_diff**2 + y_diff ** 2)
    return distance


def main():
    defne= Point(4,3)
    print (defne)
    # defne.print_point()
    shirley = Point (1,1)
    print (defne + shirley)
    print (defne-shirley)

    angela= Point (4,10)
    print( angela== defne)

    print (4 in angela)
    print (6 in defne)


    # my_point = Point()
    # print(Point.__doc__)
    # my_point.x = 3
    # my_point.y = 4
    # print('My point', end=' ')
    # print_point(my_point)

    # print('Is my_point an instance of Point?', isinstance(my_point, Point))
    # print('Is my_point an instance of Rectangle?',
    #       isinstance(my_point, Rectangle))
    # print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
    # print('Does my_point have an attribute z?', hasattr(my_point, 'z'))


if __name__ == '__main__':
    main()