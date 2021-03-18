## 클래스 인스턴스 출력하기


class Coord(object):
    def __init__(self, x, y):
        self.x, self.y = x,y
    
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

point = Coord(1, 2)

print(point)

