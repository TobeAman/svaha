#encoding:utf-8

#截图手机路径
path_screenshot_pe="sdcard/sh.jpg"
#截图名字
shotname="/sh.jpg"
#截图电脑路径
path_screenshot_pc="./screen"
#adb命令头
adb_shell="adb shell"
adb_pull="adb pull"
adb_rm="adb rm"
#空格
blank=" "
#与
ands="&&"
#图片匹配精确度，0-1之间，默认0.85无需修改，如果匹配出错误目标则提高精度，如果要模糊匹配则降低精度
#from: https://github.com/anywheretogo/auto_player/blob/master/auto_player.py
accuracy = 0.85 
#匹配目标图片地址， 默认在./wanted文件夹
wanted_path = './wanted' 

#截图-拉取-删除命令
#截图
cmd_screenshot=adb_shell+blank+ "screencap -p"+blank+path_screenshot_pe
#拉取
cmd_pull=adb_pull+blank+path_screenshot_pe+blank+path_screenshot_pc
#删除
cmd_rm=adb_rm+blank+path_screenshot_pe
#截图-拉取-删除命令
do_screenshot=cmd_screenshot+ands+cmd_pull+ands+cmd_rm

#御魂按键
yuhun_list={}
