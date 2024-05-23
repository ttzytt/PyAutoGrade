



class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def display (self):
        print('(' + str(self.x) + ', ' + str(self.y) + ')')
    def slope(self, other):
        return(self.y - other.y)/(self.x - other.x)
        




def main():
    p = Point(3,5)
    print(3,5)
    p.display()
    print(slope)
    a = Point(0,0)
    b = Point(2,1)
    print(a.slope(b))


if __name__ == "__main__":
    main()
