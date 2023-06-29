import cv2
import pyautogui
import numpy as np
import time
import os
from dotenv import load_dotenv

load_dotenv()

# 매크로를 실행할 횟수를 설정합니다.
DOWNLOAD_PATH = os.getenv("PATH") 
BOOK_NAME = "Do it 알고리즘 코딩테스트 with python"
num_repeats = 10

# for i in range(num_repeats):
    # (500, 500) 위치를 클릭합니다.
pyautogui.click(500, 500)

# 특정 영역을 화면을 캡처합니다.
screenshot = pyautogui.screenshot(region=(100, 100, 300, 300))
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# 캡처한 화면을 파일로 저장합니다. 파일명은 현재 시간과 인덱스로 설정합니다.
cv2.imwrite(f"/Users/yeongroksong/Desktop/screenShot_test/_screenshot_test.png", screenshot)

cv2.imshow("Screenshot", screenshot)
# # 대기시간(예를 들어 1초)
# time.sleep(1)