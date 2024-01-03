import pyautogui
import config
import os
import utils
import time
import threading

os.environ['CUDA_VISIBLE_DEVICES'] = '1'

from pynput.mouse import Controller, Button
import easyocr

image_path = os.path.join(config.staticPath, 'gpt.png')
aa = os.path.join(config.staticPath, 'aa.png')

# def main():
#     # 获取屏幕截图
#     screenshot = pyautogui.screenshot()
#     # 图像路径为待搜索的图像文件路径
#     image_path = os.path.join(config.staticPath, 'gpt.png')
#     status = utils.find_image_in_another(screenshot, image_path)
#     # 是否匹配成功 status为True or False

# def main_thread():
#     while True:
#         sub_thread = threading.Thread(target=main)
#         sub_thread.start()
#         # 主线程等待1秒
#         time.sleep(1)

# if __name__ == "__main__":
#     main_thread = threading.Thread(target=main_thread)
#     main_thread.start()
#     # 主线程等待
#     main_thread.join()

if __name__ == "__main__":
    start_t = time.time()
    reader = easyocr.Reader(['ch_sim', 'en'])

    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    result = reader.readtext(image_data)
    print('----------')
    for detection in result:
        print(detection[1])
    print('----------')
    print(time.time() - start_t)  
