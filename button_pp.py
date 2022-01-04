#encoding:utf-8

import os
import subprocess
import time
import random

#按键位置信息数组，每个按键2个点的位置信息，斜对角线
buttons={"button1":[(1880,1020),(2010,910)],"button2":[(1035,1125),(2260,935)],"button3":[(1800,720),(2200,230)],"button4":[(2130,990),(2260,200)]}
#变换得到随机位置信息
def relogcation(buttons):
	#do someting
	buttons_random=[]
	for value in buttons.values():
		x=[]
		y=[]
		p=[]
		#print(value)
		x.append(value[0][0])
		x.append(value[1][0])
		x.sort()
		#print(x)
		y.append(value[0][1])
		y.append(value[1][1])
		y.sort()
		#print(y)
		p.append(random.randint(x[0],x[1]))
		p.append(random.randint(y[0],y[1]))
		#print(p)
		buttons_random.append(p)
		#print(buttons_random)
	#print(buttons_random)
	return buttons_random

#拼接命令
def getcmd_str(button_postion):
	#拼接cmd命令
	cmd_str = "adb shell input tap"+" "+str(button_postion[0])+" "+str(button_postion[1])
	return cmd_str

def get_cmds():
	buttons_random = relogcation(buttons)
	cmds=[]
	for point in buttons_random:
		#点击事件
		temp_str=""
		temp_str=getcmd_str(point)
		#print(temp_str)
		cmds.append(temp_str)
	return cmds

#等待时间
def get_sleep_time():
	waittime=[]
	waittime=[round(random.uniform(27.0,29.0),2),round(random.uniform(4.0,6.0),2),round(random.uniform(2.0,3.5),2)]
	#print(waittime)
	return waittime

#打印指令
def print_cmds(cmds):
	for i in range(len(cmds)):
		print("| 指令"+str(i))
		print("| "+cmds[i])
		print("|")

#打印休眠时间
def print_sleept(waittime):
    for i in range(len(waittime)):
        print("| 休眠时间"+str(i))
        print("| "+str(waittime[i]))
        print("|")

#debug info
def debug_info(cmds,waittime):
    print("==============cmds_uion_start=======================")
    print_cmds(cmds)
    print("==============cmds_uino_end=======================")
    print("==============sleep_uion_start=======================")
    print_sleept(waittime)
    print("==============sleep_uion_end=======================")

cont=0
while 1:
        cont = cont+1
        cmds1=[]
        cmds2=[]
        waittime=[]
        print("》》》》》》》》》》》》》》》》》》》》》第"+str(cont)+"轮")
        cmds1=get_cmds()
        cmds2=get_cmds()
        r1=random.randint(1,2)
        waittime=get_sleep_time()
        #debug_info(cmds1,waittime)
        print("-执行 "+cmds1[0]+"\n"+"\\")
        subprocess.Popen(cmds1[0],shell=True)
        print(" |-等待"+" "+str(waittime[0])+"秒")
        time.sleep(waittime[0])
        #debug_info(cmds2,waittime)
        print("-执行 "+str(r1)+":"+cmds2[r1]+"\n"+"\\")
        subprocess.Popen(cmds2[r1],shell=True)
        print(" |-等待"+" "+str(waittime[1])+"秒")
        time.sleep(waittime[1])
        print("-执行 "+str(3)+":"+cmds1[3]+"\n"+"\\")
        subprocess.Popen(cmds1[3],shell=True)
        print(" |-等待"+" "+str(waittime[2])+"秒")
        time.sleep(waittime[2])

