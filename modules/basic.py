from pathlib import Path

import cv2 as cv
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFont

from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtCore import Qt

class Basic:

    def __init__(self, main_window):
        self.main_window = main_window

    def guess_args(self, image_path):

        # 获取文件名部分
        filename = os.path.basename(image_path)
        
        # 去掉文件扩展名
        name_without_ext = os.path.splitext(filename)[0]
        
        # 查找 'x' 或 '*' 分隔符
        if '*' in name_without_ext:
            separator = '*'
        elif 'x' in name_without_ext:
            separator = 'x'
        else:
            # raise ValueError("文件名中未找到有效的行列分隔符 'x' 或 '*'")
            return None, None
        
        # 找到分隔符的位置
        sep_index = name_without_ext.index(separator)
        
        # 从前向后查找数字字符，直到遇到非数字字符
        rows_str = ''
        for char in reversed(name_without_ext[:sep_index]):
            if char.isdigit():
                rows_str = char + rows_str
            else:
                break
        
        # 从后向前查找数字字符，直到遇到非数字字符
        cols_str = ''
        for char in name_without_ext[sep_index + 1:]:
            if char.isdigit():
                cols_str += char
            else:
                break
        
        # 检查提取的行列字符串是否为空
        if not rows_str or not cols_str:
            # raise ValueError(f"文件名格式不正确，应包含行列信息，当前分割结果为: {rows_str} 和 {cols_str}")
            return None, None
        
        try:
            rows = int(rows_str)
            cols = int(cols_str)
        except ValueError:
            # raise ValueError(f"行列信息应为整数，当前分割结果为: {rows_str} 和 {cols_str}")
            return None, None

        return rows, cols
    
    def put_chinese_text(self, img, text, font_path, font_size, color):
        img_pil = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_pil)
        font = ImageFont.truetype(font_path, font_size, encoding="utf-8")
        
        # 获取文本边界框
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # 计算文本居中位置
        img_width, img_height = img_pil.size
        x = (img_width - text_width) // 2
        y = (img_height - text_height) // 2
        
        # 手动绘制粗体效果
        for dx in range(-1, 1):
            for dy in range(-1, 1):
                draw.text((x + dx, y + dy), text, font=font, fill=color)
        
        img = cv.cvtColor(np.array(img_pil), cv.COLOR_RGB2BGR)
        return img
    
    def load_image(self):
        """
        加载并显示原始图像（完整函数代码）
        """
        try:
            self.main_window.camera.stop_thread()  # 关闭实时捕获防止图像覆盖
        except Exception as e:
            pass  # 忽略摄像头模块未启用的异常

        # 文件选择对话框
        selected_file, _ = QFileDialog.getOpenFileName(
            parent=self.main_window,
            caption="选择图像",
            dir="samples",
            filter="All Images (*.png *.jpg *.jpeg *.bmp *.gif *.tif *.tiff *.webp *.ppm *.pgm *.pbm *.svg);;All Files (*)"
        )

        if selected_file:
            try:
                # 图像读取（支持中文路径）
                self.main_window.image_path = selected_file  # 直接使用原始路径
                
                # 使用二进制读取解决编码问题
                with open(self.main_window.image_path, "rb") as f:
                    img_array = np.frombuffer(f.read(), np.uint8)
                    self.main_window.origin_img = cv.imdecode(img_array, cv.IMREAD_COLOR)
                
                # 空值校验
                if self.main_window.origin_img is None:
                    raise ValueError("图像读取失败，请检查文件格式和路径")
                
                # 自动设置分割参数
                try:
                    rows, cols = self.guess_args(self.main_window.image_path)
                    if rows != None and cols!= None: 
                        self.main_window.ui.rows_Slider.setValue(rows)
                        self.main_window.ui.cols_Slider.setValue(cols)
                except Exception as e:
                    print(f"参数猜测失败: {str(e)}")
                
                # 存储图像属性
                h, w, c = self.main_window.origin_img.shape
                self.main_window.height, self.main_window.width, self.main_window.channels = h, w, c
                self.main_window.result_img = self.main_window.origin_img.copy()
                
                # 显示图像
                self.display_image(self.main_window.result_img)
                
            except Exception as e:
                print(f"图像加载错误: {str(e)}")
                self.main_window.result_img = None

    def save_image(self):
        """
        保存当前处理完成后的图像。
        """
        try:
            self.main_window.camera.stop_thread()  # 先关闭实时捕获功能防止图像被覆盖
        except Exception as e:
            # print(f"Error: {e}")
            pass

        # 获取当前处理完成的图像
        img = self.main_window.result_img

        if img is None:
            print("No image to save.")
            return

        # 将图像从 BGR 转换为 RGB 格式以适应 Qt
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        # 创建 QImage 并使用图像数据初始化
        qimg = QImage(img_rgb.data, img_rgb.shape[1], img_rgb.shape[0], QImage.Format_RGB888)
        
        # 从 QImage 创建原始 QPixmap
        pixmap = QPixmap.fromImage(qimg)

        # 弹出保存文件对话框，让用户选择保存位置和文件名
        save_path, _ = QFileDialog.getSaveFileName(
            self.main_window,  # 传递 main_window 作为父窗口
            "保存图像",
            "result.png",
            "PNG Files (*.png)",
            "",  # 添加空字符串作为 selectedFilter 参数
        )
        if not save_path:
            return
        
        # 将QPixmap保存为图像文件
        if not pixmap.save(save_path, "PNG"):
            print(f"Failed to save image to {save_path}")

    def reset_image(self):
        """
        重置图像，恢复到原始状态。
        """
        try:
            self.main_window.camera.stop_thread()  # 先关闭实时捕获功能防止图像被覆盖
        except Exception as e:
            # print(f"Error: {e}")
            pass

        self.main_window.result_img = self.main_window.origin_img
        self.display_image(self.main_window.result_img)

    def display_image(self, img):
        # 将opencv图像转换为QImage格式
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format.Format_RGB888).rgbSwapped()

        # 获取显示控件的尺寸
        label_width = self.main_window.ui.result_img.width()
        label_height = self.main_window.ui.result_img.height()

        # 计算放缩比例
        scale_width = label_width / width
        scale_height = label_height / height
        scale = min(scale_width, scale_height)

        # 计算放缩后的图像尺寸
        new_width = int(width * scale)
        new_height = int(height * scale)

        # 将QImage转换为QPixmap并放缩
        pixmap = QPixmap.fromImage(qImg).scaled(new_width, new_height, Qt.AspectRatioMode.KeepAspectRatio)

        # 显示放缩后的图像
        self.main_window.ui.result_img.setPixmap(pixmap)
        self.main_window.ui.result_img.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.main_window.ui.result_img.setAlignment(Qt.AlignmentFlag.AlignCenter)