import cv2

def sort_contours(cnts, method="left-to-right"):
    reverse = False
    i = 0

    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    #计算外接矩形(boundingBoxes返回的是一个元祖，元祖当中包含4个值，xyhw)
    boundingBoxes = [cv2.boundingRect(c) for c in cnts] #用一个最小的矩形，把找到的形状包起来x,y,h,w即返回值(x，y是矩阵左上点的坐标，w，h是矩阵的宽和高)（c是一个轮廓点集合）
    #对轮廓执行一个排序操作
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))

    return cnts, boundingBoxes#返回值，返回的是轮廓cnts，boundingBoxes
def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized



