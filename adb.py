import time
import subprocess
import random

i = 0
sleep_time = 2 
process = subprocess.Popen('adb shell input tap 405 1398', shell=True)
time.sleep(sleep_time)
process = subprocess.Popen('adb shell input tap 323.6 149.8', shell=True)
time.sleep(10)
process = subprocess.Popen('adb shell input swipe 500 1050 500 200', shell=True)
time.sleep(10)

# 看6片文章，每篇2min
for i in range(7):
  process = subprocess.Popen('adb shell input tap 500 ' + str(280 + 300 * (i % 3)), shell=True)
  time.sleep(sleep_time)

  count = 60
  if i > 1:
    count = 6
  for j in range(70):
    process = subprocess.Popen('adb shell input tap 500 850', shell=True)
    time.sleep(1)
    process = subprocess.Popen('adb shell input swipe 500 1000 500 850', shell=True)
    time.sleep(1)
  # 收藏
  subprocess.Popen('adb shell input tap 695 1403', shell=True)
  time.sleep(2)
  # 分享
  subprocess.Popen('adb shell input tap 764 1400', shell=True)
  time.sleep(2)
  subprocess.Popen('adb shell input tap 100 1200', shell=True)
  time.sleep(2)
  # process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
  # time.sleep(2)

  # 评论
  if i < 2:
    subprocess.Popen('adb shell input tap 200 1400', shell=True)
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
    subprocess.Popen('adb shell input tap 762 1294', shell=True)
    time.sleep(5)


  process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
  time.sleep(2)
  if i == 2 or i == 4: 
    subprocess.Popen('adb shell input swipe 500 1500 500 900', shell=True)
    time.sleep(3)


#  进入视频

process = subprocess.Popen('adb shell input tap 570 1400', shell=True)
time.sleep(sleep_time)
process = subprocess.Popen('adb shell input tap 313 140', shell=True)
time.sleep(10)
process = subprocess.Popen('adb shell input swipe 500 1000 500 700', shell=True)
time.sleep(sleep_time)

# 看6个视频
for i in range(7):
  process = subprocess.Popen('adb shell input tap 500 ' + str(370 + 110 * (i - 1)), shell=True)
  time.sleep(sleep_time)
  if i == 0: 
    time.sleep(1830)
  else:
    # for j in range(8):
    #   process = subprocess.Popen('adb shell input swipe 270 377 320 377', shell=True)
    #   time.sleep(30)
    time.sleep(240)
  process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
  time.sleep(sleep_time)
#  if i == 2 or i == 4: 
#    subprocess.Popen('adb shell input swipe 500 1500 500 800', shell=True)
#    time.sleep(sleep_time)




time.sleep(sleep_time)
