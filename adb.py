import time
import subprocess
import random

i = 0
sleep_time = 2 
subprocess.Popen('adb shell input tap 540 1900', shell=True)
time.sleep(sleep_time)
subprocess.Popen('adb shell input tap 431 191', shell=True)
time.sleep(10)
subprocess.Popen('adb shell input swipe 500 1750 500 80', shell=True)
time.sleep(sleep_time)
subprocess.Popen('adb shell input swipe 500 1750 500 80', shell=True)
time.sleep(sleep_time)

# 看6片文章，每篇2min
for i in range(9):
  subprocess.Popen('adb shell input tap 500 ' + str(392 + 400 * (i % 3)), shell=True)
  time.sleep(sleep_time)

  count = 60
  if i > 1:
    count = 6
  for j in range(70):
    if j % 2 and j < 10:
      subprocess.Popen('adb shell input tap 500 850', shell=True)
    time.sleep(1)
    subprocess.Popen('adb shell input swipe 500 1000 500 850', shell=True)
    time.sleep(1)
  # 收藏
  subprocess.Popen('adb shell input tap 923 1872', shell=True)
  time.sleep(2)
  # 分享
  subprocess.Popen('adb shell input tap 1020 1872', shell=True)
  time.sleep(2)
  subprocess.Popen('adb shell input tap 950 1368', shell=True)
  time.sleep(2)
  # subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
  # time.sleep(2)

  # 评论
  if i < 2:
    subprocess.Popen('adb shell input tap 166 1872', shell=True)
    time.sleep(5)

    # for i in range(40):
    #   subprocess.Popen('adb shell input keyevent 67', shell=True)
    commentKey = random.randint(1, 5)
    if commentKey == 1:
      subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "中华人民共和国万岁！"', shell=True)
    elif commentKey == 2:
      subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "富强、民主、文明、和谐"', shell=True)
    elif commentKey == 3:
      subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "中华民族崛起！"', shell=True)
    elif commentKey == 4:
      subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "坚持党的领导，人民当家作主"', shell=True)
    elif commentKey == 5:
      subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "跟着共产党走，好日子还在后头"', shell=True)
    time.sleep(2)
    subprocess.Popen('adb shell input tap 1010 1734', shell=True)
    time.sleep(5)


  subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
  time.sleep(2)
  if i == 2 or i == 4 or i == 6: 
    subprocess.Popen('adb shell input swipe 500 1700 500 700', shell=True)
    time.sleep(3)


#  进入视频

subprocess.Popen('adb shell input tap 753 1896', shell=True)
time.sleep(sleep_time)
subprocess.Popen('adb shell input tap 426 188', shell=True)
time.sleep(10)
subprocess.Popen('adb shell input swipe 500 1000 500 700', shell=True)
time.sleep(sleep_time)

# 看6个视频
for i in range(7):
  subprocess.Popen('adb shell input tap 500 ' + str(370 + 160 * (i)), shell=True)
  time.sleep(sleep_time)
  if i == 0: 
    time.sleep(1830)
  else:
    # for j in range(8):
    #   subprocess.Popen('adb shell input swipe 270 377 320 377', shell=True)
    #   time.sleep(30)
    time.sleep(240)
  subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
  time.sleep(sleep_time)
#  if i == 2 or i == 4: 
#    subprocess.Popen('adb shell input swipe 500 1500 500 800', shell=True)
#    time.sleep(sleep_time)




time.sleep(sleep_time)
