from modelfy import BaseModel


if __name__ == '__main__':
    class Point(BaseModel):
        x: int
        y: int

    p = Point(x=1, y=2)
    print(p)

    points = [Point(x=i, y=i) for i in range(10)]
    print(points)
