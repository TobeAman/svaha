#encoding:utf-8
import subprocess
import time
import random
import cv2
import os
import shutil
import numpy
import threading
from vailes import *

#功能函数
#随机偏移坐标。p是原坐标(x, y)
def random_offset(p):
    a,b = p
    e,f = a + random.randint(-30,30), b + random.randint(-30,30)
    y = [e, f]
    return(y)
#点击
def touch(pos):
    x, y = pos
    a = "adb shell input touchscreen tap {0} {1}" .format(x, y)
    os.system(a)
#随机延迟点击延迟时间范围为【x, y】秒之间
def random_delay(x=0.1, y=0.2):
    t = random.uniform(x, y)
    time.sleep(t)

#1.手机截图到pc本地
def screenshot():
    try:
        os.makedirs(path_screenshot_pc)
        while 1:
            try:
                ts=time.time()
                p1=subprocess.Popen(do_screenshot,shell=True)
                p1.wait()
                te=time.time()
                print(int(te)-int(ts))
            except (KeyboardInterrupt,NameError) as e:
                if e==KeyboardInterrupt:
                    print("exit!!!")
                    os.exit()
                if e==NameError:
                    print("NameError!!!")
                    os.exit()
    except:
        shutil.rmtree(path_screenshot_pc)
        screenshot()

#2.加载点击图 api from:https://github.com/anywheretogo/auto_player/blob/master/auto_player.py
def load_imgs():
    imgs = {}
    treshold = accuracy
    path = wanted_path
    file_list = os.listdir(path)

    for file in file_list:
        name = file.split('.')[0]
        file_path = path + '/' + file
        a = [ cv2.imread(file_path) , treshold, name]
        imgs[name] = a
    return imgs

#3.在背景查找目标图片，以列表形式返回查找目标的中心坐标，
#screen是截屏图片，wanted是找的图片【按上面load_imgs的格式】
#api from:https://github.com/anywheretogo/auto_player/blob/master/auto_player.py
def locate(wanted):
    loc_pos = []
    wanted, treshold = wanted

    screen = cv2.imread(path_screenshot_pc+shotname)
    result = cv2.matchTemplate(screen, wanted, cv2.TM_CCOEFF_NORMED)
    location = numpy.where(result >= treshold)

    h,w = wanted.shape[:-1] 

    ex,ey = 0,0
    for pt in zip(*location[::-1]):   
        x,y = pt[0] + int(w/2), pt[1] + int(h/2)
        if (x-ex) + (y-ey) < 15:  #去掉邻近重复的点
            continue
        ex,ey = x,y

        cv2.circle(screen, (x, y), 10, (0, 0, 255), 3)
            
        x,y = int(x), int(y)
        loc_pos.append([x, y])

    return loc_pos

#4.寻找并点击,找到返回目标名，未找到返回NONE
#api from:https://github.com/anywheretogo/auto_player/blob/master/auto_player.py
def find_touch_any(target_list, tap=True):
    imgs=load_imgs()
    re = None
    for target in target_list:
        wanted = imgs[target]
        size = wanted[0].shape
        h, w , ___ = size
        pts = locate(wanted)
        if pts:
            xx = pts[0]
            xx = random_offset(xx, w, h)
            if tap:      
                touch(xx)
                random_delay()
            re = target
            break
        else:
            print('N 未找到目标', target)
    return False

#隔1秒寻找一次并点击
def timetouch(target_list):
    while True:
        find_touch_any(target_list, tap=True)
        time.sleep(1)

#线程1:
def p1(target_list):
    p_timetouch = threading.Thread(target=timetouch,args=(target_list,))
    p_timetouch.start()
    p_timetouch.join()
#线程2：
def p2():
    p_sceenshot = threading.Thread(target=screenshot)
    p_sceenshot.start()
    p_sceenshot.join()

#御魂
def yuhun():
    pone= threading.Thread(target=timetouch,args=(yuhun_list,))
    pto= threading.Thread(target=screenshot,args=())
    pto.start()
    pone.start()
    pone.join()
    pto.join()
