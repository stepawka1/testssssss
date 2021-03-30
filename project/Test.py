import json
from classes import Point, Camera, Wall
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

class Test(object):
    def __init__(self):
        self.W = 5  # x
        self.L = 10  # y
        self.H = 4  # z

    def test(self, angel1, angel2, point_x: float, point_y: float):
        camera_2 = Camera(Point(2, 0, self.H), angle_v=float(angel1),  angle_h=float(angel2))
        if point_x-1 < camera_2.point_to.x < point_x + 1 and point_y-1 < camera_2.point_to.y < point_y+1:
            return True
        return False
