import json
import numpy as np
import optimesh
import dmsh
import meshio



mapArray = []

mapSize = [100, 100]
radius = 30
width = 30

center = [(mapSize[0]-1)/2, (mapSize[1]-1)/2]

# print(center)

geo = dmsh.Circle([0.0, 0.0], 1.0)
X, cells = dmsh.generate(geo, 0.5)

# optionally optimize the mesh
# X, cells = optimesh.optimize_points_cells(X, cells, "CVT (full)", 1.0e-10, 100)

# visualize the mesh
# dmsh.helpers.show(X, cells, geo)


# print(X)

# and write it to a file
# meshio.Mesh(X, {"triangle": cells}).write("maps/circle.vtk")


# Point Cloud
# for x in range(0, mapSize[0]):
#     # mapArray.append([])
#     for y in range(0, mapSize[1]):
#         inCircle = 0
#         # print((x+y) ** 2)
#         if (radius ** 2) < (((x - center[0]) ** 2) + ((y - center[1]) ** 2)) < ((radius+width) ** 2):
#             # inCircle = 1
#             mapArray.append([x,y])
#         # mapArray[x].append(inCircle)

# # print(mapArray);


# json_string = json.dumps(X)

filename = "maps/maptest2.txt"

X = X * 100
X = X.round()
X.tofile(filename, ",")

with open(filename, 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write("["+content+"]")



# f = open("maps/maptest1.txt", "w")
# f.write(json_string)
# f.close()
