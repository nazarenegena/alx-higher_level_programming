#!/usr/bin/python3
"""function defines the Pascal's Triangle function"""


def pascal_triangle(n):

    """ represents the Triangle """

    if n <= 0:
        return []

    triangles = [[1]]

    while len(triangles) != n:

        tri = triangles[-1]

        tmp_tri = [1]

        for i in range(len(tri) - 1):

            tmp_tri.append(tri[i] + tri[i + 1])

        tmp_tri.append(1)

        triangles.append(tmp_tri)

    return triangles

