'''
this code is a demo for non maximun suppression algorithm
2018-8-6
writen by Heng Wu
'''
import cv2
import numpy as np

x = np.array([3,1,2])
# startX, startY, endX, endY
boxes = np.array([
	(12, 84, 140, 110),
	(168, 3, 259, 102),
	(36, 84, 164, 212),
	(12, 96, 140, 224),
	(24, 96, 152, 224),
	(24, 108, 152, 236)])
pick = []
x1 = boxes[:,0]
y1 = boxes[:,1]
x2 = boxes[:,2]
y2 = boxes[:,3]
area = (x2 - x1 + 1) * (y2 - y1 + 1)
idxs = np.argsort(y2)
print("boxes: ",boxes)
print("x1:",x1,end="    ")
print("x2:",x2,end="    ")
print("y1:",y1,end="    ")
print("y2:",y2)
print("area: ", area)
print("idxs:",idxs)
# print(np.argsort(x))
overlapThresh = 0.3
while len(idxs)>0:
    print("-----------------------------------------")
    last = len(idxs) -1
    print("last:",last,end="||")
    i = idxs[last]
    print(x1[i]," ",y1[i]," ",x2[i]," ",y2[i])
    print("i:",i,end="||")
    pick.append(i)
    print("pick:",pick)
    suppress = [last]
    print("suppress:",suppress)
    for pos in range(0, last):
        print("+++++++++++")
        # grab the current index
        j = idxs[pos]
        print("j:",j,end="||")
        # find the largest (x, y) coordinates for the start of
        # the bounding box and the smallest (x, y) coordinates
        # for the end of the bounding box
        print("comparing:",x1[j], " ", y1[j], " ", x2[j], " ", y2[j])
        xx1 = max(x1[i], x1[j]);print("xx1:",xx1,end="||")
        yy1 = max(y1[i], y1[j]);print("yy1:",yy1,end="||")
        xx2 = min(x2[i], x2[j]);print("xx2:",xx2,end="||")
        yy2 = min(y2[i], y2[j]);print("yy2:",yy2)

        # compute the width and height of the bounding box
        w = max(0, xx2 - xx1 + 1);print("w:",w,end="||")
        h = max(0, yy2 - yy1 + 1);print("h:",h)

        # compute the ratio of overlap between the computed
        # bounding box and the bounding box in the area list
        overlap = float(w * h) / area[j];print("overlap:",overlap)

        # if there is sufficient overlap, suppress the
        # current bounding box
        if overlap > overlapThresh:
            suppress.append(pos)
        print("suppress:",suppress)
    idxs = np.delete(idxs, suppress)

print(boxes[pick])
