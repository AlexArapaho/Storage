from Geometry import *


def run():
    r1 = rect.Rectangle(1, 2)
    r2 = rect.Rectangle(3, 4)
    s1 = sqr.Square(10)
    s2 = sqr.Square(20)
    t1 = trian.Triangle(1, 2, 3)
    t2 = trian.Triangle(4, 5, 6)
    shape = [r1, r2, s1, s2, t1, t2]
    for g in shape:
        print(g.get_perimetr())

if __name__ == '__main__':
    run()