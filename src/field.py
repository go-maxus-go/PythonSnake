# Map of the field

from src.point import *

class CellType(enumerate):
    Empty = 0
    Wall = 1

class Field:
    def __init__(self, width = 10, height = 10, data = []):
        self.__width = width
        self.__height = height
        self.__data = data
        if not data:
            self.__data = [CellType.Empty]*(width * height)
        elif len(data) != width * height:
            raise "Not enough data"

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def cell(self, point):
        if type(point) != Point2D:
            raise "Point2D type is required"
        return self.__data[point.y * self.__width + point.x]
