def CalcSize(toponym):
    poses = toponym['boundedBy']['Envelope']
    l = poses['lowerCorner']
    u = poses['upperCorner']
    xl, yl = [float(i) for i in l.split(' ')]
    xu, yu = [float(i) for i in u.split(' ')]
    sizeX = max(xu, xl) - min(xu, xl)
    sizeY = max(yu, yl) - min(yu, yl)
    return ",".join([str(sizeX), str(sizeY)])
