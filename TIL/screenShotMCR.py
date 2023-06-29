import cv2
import pyautogui
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

# 화면 캡처를 합니다.
DOWNLOAD_PATH = os.getenv("PATH") 

x, y = 385, 115

screenShot = pyautogui.screenshot(region=(x,y,100,300))
screenshot = cv2.cvtColor(np.array(screenShot), cv2.COLOR_RGB2BGR)

# 화면 캡처한 이미지를 파일로 저장합니다.
cv2.imwrite(f"{DOWNLOAD_PATH}/screenshot2.png", screenshot)

# 이미지를 화면에 보여줍니다.
cv2.imshow("Screenshot", screenshot)

# 'q' 키를 누를 때까지 기다립니다.
cv2.waitKey(0)
cv2.destroyAllWindows()

# x = pyautogui.displayMousePosition()
