import numpy as np


def side_wall(q, pt, points, type, comp):
    if comp == 1:
        if type == 'y':
            print("Side wall in Y direction")
            print("The total number of points will be excluded are ", points)
            q_3d = np.ascontiguousarray(q[:, int(points / 2):pt - int(points / 2), :])
        elif type == 'z':
            print("Side wall in Z direction")
            print("The total number of points will be excluded are ", points)
            q_3d = np.ascontiguousarray(q[:, :, int(points / 2):pt - int(points / 2)])
    else:
        print("Components are ", comp)
        if np.shape(q)[0] != comp:
            raise ValueError(" The number of components defined in the function input is wrong")
        if type == 'y':
            q_3d = np.zeros((np.shape(q)[0], np.shape(q)[1], np.shape(q)[2] - int(points), np.shape(q)[3]))
            print("Side wall in Y direction")
            print("The total number of points will be excluded are ", points)
            for icomp in range(comp):
                q_3d[icomp, :, :, :] = np.ascontiguousarray(q[icomp, :, int(points / 2):pt - int(points / 2), :])
        elif type == 'z':
            q_3d = np.zeros((np.shape(q)[0], np.shape(q)[1], np.shape(q)[2], np.shape(q)[3] - int(points)))
            print("Side wall in Z direction")
            print("The total number of points will be excluded are ", points)
            for icomp in range(comp):
                q_3d[icomp, :, :, :] = np.ascontiguousarray(q[icomp, :, :, int(points / 2):pt - int(points / 2)])

    return q_3d
