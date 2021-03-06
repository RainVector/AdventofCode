# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:22:06 2018

@author: RV
"""
import re
coveredID = set()

"""
由两个长方形，算出他们相交的区域所包含的坐标
"""
def interaction(rect1, rect2):
    coverList = set()
    # AABB of rectange 1
    (minXrect1,minYrect1,maxXrect1,maxYrect1) = [rect1[1],rect1[2],rect1[1] + rect1[3],rect1[2] + rect1[4]]
    # AABB of rectange 2
    (minXrect2,minYrect2,maxXrect2,maxYrect2) = [rect2[1],rect2[2],rect2[1] + rect2[3],rect2[2] + rect2[4]]
    #判断AABB是否相交,不考虑等于的情况，这个时候只是边重叠，并没有交叉
    if(minXrect1 > maxXrect2 or minXrect2 > maxXrect1 or minYrect1>maxYrect2 or minYrect2>maxYrect1):
        return coverList
    # 获取相交区域的坐标列表
    minXcover = max(min(minXrect1,maxXrect2),min(minXrect2,maxXrect1))
    maxXcover = min(max(minXrect1,maxXrect2),max(minXrect2,maxXrect1))
    minYcover = max(min(minYrect1,maxYrect2),min(minYrect2,maxYrect1))
    maxYcover = min(max(minYrect1,maxYrect2),max(minYrect2,maxYrect1))
    
    for i in range(minXcover,maxXcover):
        for j in range(minYcover,maxYcover):
            coverList.add((i,j))
    coveredID.add(rect1[0])
    coveredID.add(rect2[0])
    return coverList

"""
预处理文件，提取出每一行对应的信息：
#1 @ 661,227: 29x11
#id @ xPos,yPos: widthxheight
正则表达式参考：https://regexr.com/
"""
file = open("day3.txt","r")
slics = list()
for line in file:
    (boxId,xPos,yPos,width,height) = [t(s) for t,s in zip((int,int,int,int,int),re.search('^#([\d.]+) @ ([\d.]+),([\d.]+): ([\d.]+)x([\d.]+)',str(line)).groups())]
    slics.append([boxId,xPos,yPos,width,height])
file.close()

"""
长方形两两比较，算出重叠区域
"""
cover = set()
for i in range(len(slics)-1):
    for j in range(i+1,len(slics)):
        coverList = interaction(slics[i],slics[j])
        if(len(coverList) > 0):
            for pos in coverList:
                cover.add(pos)
        
print(len(cover))

"""
看看哪个一次都没有跟别的claim相交
"""
for slic in slics:
    if(slic[0] not in coveredID):
        print(slic[0])