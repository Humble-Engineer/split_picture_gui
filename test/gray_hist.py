import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

def display_image_and_histogram(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    
    # 检查图像是否成功读取
    if image is None:
        print(f"Error: Unable to open image at {image_path}")
        return
    
    # 转换为灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 计算灰度直方图
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    hist = hist.flatten()  # 将直方图转换为一维数组
    
    # 使用 find_peaks 找到峰值
    peaks, _ = find_peaks(hist)
    
    # 筛选频率超过300的峰值
    filtered_peaks = [peak for peak in peaks if hist[peak] > 300]
    
    # 绘制灰度直方图
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("num of pixels")
    plt.plot(hist)
    
    # 标注极大值点
    plt.plot(filtered_peaks, hist[filtered_peaks], "x", label="Peaks (Frequency > 300)", color="red")
    
    # 标注极大值点
    for peak in filtered_peaks:
        plt.axvline(x=peak, color='red', linestyle='--')
    
    plt.legend()
    plt.xlim([0, 256])
    plt.show()

if __name__ == "__main__":
    # 固定路径图像
    image_path = r"F:\repos\Projects\split_picture_gui\samples\ABTS-2.png"
    display_image_and_histogram(image_path)