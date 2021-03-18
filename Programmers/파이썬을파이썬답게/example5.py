## 클래스 인스턴스 출력하기


class Coord(object):
    def __init__(self, x, y):
        self.x, self.y = x,y
    
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

point = Coord(1, 2)

print(point)


## 무엇이랑 비교해도 크다고 하는 변수

maxValue = float('inf')
if maxValue > 100000000:
    print('adwdwa')

## 음수도 가능
maxValue = float('-inf')
