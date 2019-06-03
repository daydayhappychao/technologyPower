import time
import subprocess
import random

i = 0
sleep_time = 2 
#用popen设置shell=True不会弹出cmd框
process = subprocess.Popen('adb shell input tap 565 1713', shell=True)
time.sleep(sleep_time)
process = subprocess.Popen('adb shell input tap 262 300', shell=True)
time.sleep(sleep_time)

# 看6片文章，每篇2min
for i in range(7):
  process = subprocess.Popen('adb shell input tap 500 ' + str(500 + 280 * (i % 3)), shell=True)
  time.sleep(sleep_time)

  count = 60
  if i > 1:
    count = 6
  for j in range(60):
    process = subprocess.Popen('adb shell input swipe 500 1000 500 950', shell=True)
    time.sleep(2)
  # 收藏
  subprocess.Popen('adb shell input tap 844 1735', shell=True)
  time.sleep(2)
  # 分享
  subprocess.Popen('adb shell input tap 980 1735', shell=True)
  time.sleep(2)
  subprocess.Popen('adb shell input tap 974 967', shell=True)
  time.sleep(2)
  process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
  time.sleep(2)

  # 评论
  if i < 2:
    subprocess.Popen('adb shell input tap 384 1750', shell=True)
    time.sleep(5)

    # for i in range(40):
    #   subprocess.Popen('adb shell input keyevent 67', shell=True)
    commentKey = random.randint(1, 5)
    if commentKey == 1:
      subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "祖国万岁！"', shell=True)
    elif commentKey == 2:
      subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "富强、民主、文明、和谐"', shell=True)
    elif commentKey == 3:
      subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "中华民族崛起！"', shell=True)
    elif commentKey == 4:
      subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "坚持党的领导，人民当家作主"', shell=True)
    elif commentKey == 5:
      subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "跟着共产党走，好日子还在后头"', shell=True)
    time.sleep(2)
    subprocess.Popen('adb shell input tap 972 1525', shell=True)
    time.sleep(5)


  process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
  time.sleep(2)
  if i == 2: 
    subprocess.Popen('adb shell input swipe 500 1500 500 950', shell=True)
    time.sleep(3)


#  进入视频

process = subprocess.Popen('adb shell input tap 755 1729', shell=True)
time.sleep(0.2)
process = subprocess.Popen('adb shell input tap 755 1729', shell=True)
time.sleep(10)
# 看6个视频
for i in range(7):
  process = subprocess.Popen('adb shell input tap 500 ' + str(1100 + 240 * (i % 3)), shell=True)
  time.sleep(sleep_time)
  for j in range(6):
    process = subprocess.Popen('adb shell input swipe 270 377 500 377', shell=True)
    time.sleep(30)
  process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
  time.sleep(2)
  if i == 2: 
    subprocess.Popen('adb shell input swipe 500 1500 500 800', shell=True)
    time.sleep(3)




time.sleep(sleep_time)
