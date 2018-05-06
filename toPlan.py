import cv2
import numpy as np


def getpointcloud(f):
    fstr = open(f, 'rb')
    line = fstr.readline();
    linelist = line.split(" ")
    point_list = []
    while line != None and len(linelist) >= 4:
        y = int(float(linelist[2]))
        z = int(float(linelist[3]))
        x = int(float(linelist[1]))

        point_list.append([x, y, z])
        line = fstr.readline()
        linelist = line.split(" ")

    ar = np.asarray(point_list)
    return ar

def projecttolevel(point_list):
    xpts = point_list[:, 0]
    ypts = point_list[:, 1]
    minx = min(xpts)
    maxx = max(xpts)
    miny = min(ypts)
    maxy = max(ypts)
    print minx, maxx, miny, maxy
    im = np.zeros((maxx-minx, maxy-miny))
    for i in range(len(point_list)):
        x = (point_list[i, 0]-minx) -1
        y = (point_list[i, 1]-miny) -1
        im[x, y] = 1


def houghlines():
    pass


if __name__ == "__main__":
    ar = getpointcloud("reference.obj")
    projecttolevel(ar)
