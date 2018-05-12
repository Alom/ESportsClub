#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

names = {1:r"Ao, Lan |帅气五峰毛尖",
2:r"Qian, Junjuan |凌灵夭",
3:r"Dong, Lei |潇洒也小猪",
4:r"Ding, Weina |电竞唐嫣",
5:r"Zhu, Bo |bobzoooooo",
6:r"Yao,Zhen |Re.Jacky ",
7:r"Huang, Yue |☆Ether",
8:r"Xu, Li |Linatra",
9:r"Tian, Lang |tianlanglang",
10:r"Zhou, Haizhan |海战",
11:r"Shi, Junjie |mstr最强王者",
12:r"Li, Jia |alex123bob",
13:r"Ma, Xiao |你们别滑了",
14:r"Gao，Mengru |赵漂亮迷妹",
15:r"Liang, Fei |可达鸭呆河马",
16:r"Liu Chang |刘畅?",
17:r"曦|ufc神秘高手"
}

count = 0
namesVec = []

while (count < 10):
    r = random.randint(2, 17)
    #print r
    if (names[r] not in namesVec):
        namesVec.append(names[r])
        count = count + 1

count = 1
for name in namesVec:
    #print name
    print "Position " + str(count) + ": " + name + "\n"
    count = count + 1



