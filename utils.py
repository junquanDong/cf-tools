import cv2
import numpy as np
from PIL import Image


def _convert_to_gray(image):
    # 将图像转换为灰度图像
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image
    return gray_image

# 查找图片是否存在于另一张图片中 传入path or image
def find_image_in_another(base_image, target_image):
    # 判断传入参数的类型
    if isinstance(base_image, str):
        base_image = cv2.imread(base_image)
    elif isinstance(base_image, Image.Image):
        base_image = np.array(base_image)

    if isinstance(target_image, str):
        target_image = cv2.imread(target_image)
    elif isinstance(target_image, Image.Image):
        target_image = np.array(target_image)

    # 转换为灰度图像
    base_gray = _convert_to_gray(base_image)
    target_gray = _convert_to_gray(target_image)

    # 使用模板匹配
    result = cv2.matchTemplate(base_gray, target_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 设置一个阈值，可以根据实际情况调整
    threshold = 0.8
    print('\033[92m图像匹配成功\033[92m' if max_val >= threshold else '\033[91m图像匹配失败\033[91m' , '|  匹配图像的相似度:', max_val, '|  阈值:', threshold)
    # 如果匹配度超过阈值，认为找到了目标图像
    if max_val >= threshold:
        return True
    else:
        return False
    
