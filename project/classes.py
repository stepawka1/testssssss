import numpy as np
import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        eps = 1e-4
        return other.x - eps < self.x < other.x + eps and \
               other.y - eps < self.y < other.y + eps and \
               other.z - eps < self.z < other.z + eps

    def __copy__(self):
        return Point(self.x, self.y, self.z)

    def make_dict(self):
        return [self.x, self.y, self.z]


class Camera:
    def __init__(self, point: Point, point_to: Point = None, angle_v: float = None, angle_h: float = None):
        if not point_to and not angle_v and not angle_h:
            exit('Give point_to or angles')
        self.point = point
        if point_to:
            # dx = point.x - point_to.x
            # dy = point_to.y - point.y
            # dz = point.z - point_to.z
            # r = math.sqrt(dx**2 + dy**2)
            # self.angle_v = math.degrees(np.arctan(r/dz))
            # self.angle_h = math.degrees(np.arctan(dy/dx)) % 180
            # print(self.angle_v, self.angle_h)
            # TODO: make angles from point_to
            self.point_to = point_to
        else:
            self.angle_v = angle_v
            self.angle_h = np.mod(angle_h, 360)
            r = np.tan(math.radians(self.angle_v)) * point.z
            dx = -np.cos(np.mod(self.angle_h, 180) * np.pi / 180) * r
            dy = np.sqrt(r ** 2 - dx ** 2)
            if self.angle_h >= 180:
                dx = -dx
                dy = -dy
            self.point_to = Point(point.x + dx,
                                  point.y + dy,
                                  0)
            print(self.point_to.x, self.point_to.y)

    def __eq__(self, other):
        return self.point == other.point

    def __copy__(self):
        return Camera(self.point, self.point_to, self.angle_v, self.angle_h)

    def make_dict(self):
        # TODO: make dict from Camera to dump to json ( using point_to or angles (?) )
        pass


class Wall:
    def __init__(self, points: list):
        self.points = points

    def __copy__(self):
        return Wall(points=self.points)

    def make_dict(self):
        res = []
        for point in self.points:
            res.append(point.make_dict())
        return res

    def make_rectangle(self):
        x = []
        y = []
        z = []

        for point in self.points:
            x.append(point.x)
            y.append(point.y)
            z.append(point.z)

        x.append(self.points[0].x)
        y.append(self.points[0].y)
        z.append(self.points[0].z)

        return np.array(x), np.array(y), np.array(z)
