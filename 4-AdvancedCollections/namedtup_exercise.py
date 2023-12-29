# Demonstrate the usage of namdtuple objects

import collections


def main():
    # create a Point namedtuple
    Point = collections.namedtuple("Point", "X Y")
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1, p2)
    print(p1.X, p2.Y)

    # use _replace to create a new instance
    p1 = p1._replace(X=100)
    print(p1)


if __name__ == "__main__":
    main()
