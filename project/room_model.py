import json
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

from classes import Point, Camera, Wall


START_POINT = Point(0, 0, 0)
W = 5  # x
L = 10  # y
H = 4  # z

room_to_json = {'Walls': {}, 'Cameras': {}}


camera_1 = Camera(Point(2, 0, H), angle_v=49, angle_h=64)  # Направление задано углами
camera_2 = Camera(Point(2, 0, H), Point(2.001, 4, 0))   # Направление задано точкой (вектор)
cameras = [camera_1, camera_2]

# Стены задаются точками по часовой стрелке (если смотреть из комнаты) от нижней левой до нижней правой
wall_front = Wall([Point(W, 0, 0), Point(W, 0, H), Point(0, 0, H), Point(0, 0, 0)])
wall_right = Wall([Point(W, L, 0), Point(W, L, H), Point(W, 0, H), Point(W, 0, 0)])
wall_left = Wall([Point(0, 0, 0), Point(0, 0, H), Point(0, L, H), Point(0, L, 0)])
wall_back = Wall([Point(0, L, 0), Point(0, L, H), Point(W, L, H), Point(W, L, 0)])
room = [wall_front, wall_right, wall_left, wall_back]


fig = plt.figure()
ax = Axes3D(fig)

i = 0
for wall in room:
    i += 1
    room_to_json['Walls'][str(i)] = wall.make_dict()
    X, Y, Z = wall.make_rectangle()
    ax.plot(X, Y, Z, label='parametric curve', color='k')

i = 0
for camera in cameras:
    i += 1
    room_to_json['Cameras'][str(i)] = {'point': camera.point.make_dict(), 'direction': camera.point_to.make_dict()}
    ax.plot(camera.point.x, camera.point.y, camera.point.z, 'ro')
    ax.plot([camera.point.x, camera.point_to.x],
            [camera.point.y, camera.point_to.y],
            [camera.point.z, camera.point_to.z], 'r--')

ax.set_xlim3d(0, max(H, W, L))
ax.set_ylim3d(0, max(H, W, L))
ax.set_zlim3d(0, max(H, W, L))

with open('room.json', 'w') as fp:
    json.dump(room_to_json, fp, indent='\t')

plt.show()



