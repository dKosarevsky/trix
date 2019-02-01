
# pip install pyautogui
import pyautogui


screen = pyautogui.screenshot('screenshot.png')
print(screen)


# Если нужно сделать скриншот определенной части экрана,
# можно воспользоваться свойством region:
# pyautogui.screenshot('screenshot.png',region=(0,0, 300, 400))
