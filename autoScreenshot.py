import time
import pyautogui


for i in range(6):
	print(5 - i)
	time.sleep(1)

screenshot = pyautogui.screenshot()
screenshot.save(f'./screenshots/0.png')
print(f'screenshot saved: 0.png')

NUM_OF_PAGES = 100

for i in range(1, NUM_OF_PAGES):
	pyautogui.click()
	time.sleep(3)
	screenshot = pyautogui.screenshot()
	screenshot.save(f'./screenshots/{i}.png')
	print(f'screenshot saved: {i}.png')
