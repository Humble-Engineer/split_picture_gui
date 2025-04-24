import cv2
import numpy as np
import matplotlib.pyplot as plt  # 新增matplotlib导入

def detect_circles(image_path, param2=50):
    # 读取图像并检查有效性
    img = cv2.imread(image_path)
    if img is None:
        print("错误：无法读取图像文件")
        return
    
    # 预处理流程保持不变
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    
    circles = cv2.HoughCircles(
        image=gray,                # 输入灰度图像
        method=cv2.HOUGH_GRADIENT, # 检测方法（当前唯一可用）
        dp=1,                      # 累加器分辨率
        minDist=50,                # 圆心最小间距
        param1=100,                # Canny高阈值
        param2=param2,             # 圆心累加阈值
        minRadius=0,               # 最小圆半径
        maxRadius=0                # 最大圆半径
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))
        radii = circles[0, :, 2]
        min_radius = np.min(radii)
        
        # 在原始图像上绘制结果
        output_img = img.copy()
        for i in circles[0, :]:
            cv2.circle(output_img, (i[0], i[1]), min_radius, (0, 255, 0), 3)
            cv2.circle(output_img, (i[0], i[1]), 5, (0, 0, 255), 3)
        
        # 转换颜色空间用于matplotlib显示
        output_img_rgb = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)
        gray_img_rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        
        # 创建可视化子图
        plt.figure(figsize=(15, 6))
        
        # 显示原始灰度图
        plt.subplot(1, 2, 1)
        plt.imshow(gray_img_rgb)
        plt.title('Processed Gray Image')
        plt.axis('off')
        
        # 显示检测结果
        plt.subplot(1, 2, 2)
        plt.imshow(output_img_rgb)
        plt.title(f'Detected Circles (param2={param2})\nMin Radius: {min_radius}px')
        plt.axis('off')
        
        plt.tight_layout()
        plt.show()
        
    else:
        print(f"param2={param2} 未检测到圆形")

if __name__ == "__main__":
    detect_circles(r'test\find_circle\plate_4x6.png', param2=80)
    detect_circles(r'test\find_circle\real_sample.jpg', param2=50)
    # detect_circles(r'test\find_circle\hy.jpg', param2=60)