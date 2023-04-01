def drawPyramid(size=5):
    print("*" * size)
    if size > 1:
        drawPyramid(size-1)
    print("*" * size)

drawPyramid(8)