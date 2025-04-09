import cv2
import numpy as np
import os
import datetime

class Algorithm:
    def __init__(self, main_window=None):
        self.image_path = None
        self.data = []
        
        if main_window is not None:
            self.main_window = main_window
            self.rows = self.main_window.rows
            self.cols = self.main_window.cols
            self.r = self.main_window.r
            self.precision = self.main_window.precision
        else:
            self.rows = 4
            self.cols = 6
            self.r = 0.2
            self.precision = 4

    def count(self, main_window=None):
        # 初始化参数
        if main_window is not None:
            self.rows = self.main_window.rows
            self.cols = self.main_window.cols
            self.r = self.main_window.r
            self.precision = self.main_window.precision
            image = self.main_window.origin_img.copy()
        else:
            image = cv2.imread(self.image_path)

        height, width = image.shape[:2]
        row_height = height // self.rows
        col_width = width // self.cols

        # 绘制基础网格线
        for i in range(1, self.rows):
            cv2.line(image, (0, i*row_height), (width, i*row_height), (255,0,0), 2)
        for j in range(1, self.cols):
            cv2.line(image, (j*col_width, 0), (j*col_width, height), (255,0,0), 2)

        # 初始化拼接图像参数
        sub_h = int(row_height * 2 * self.r)
        sub_w = int(col_width * 2 * self.r)
        stitched_img = np.full((sub_h*self.rows, sub_w*self.cols, 3), 255, dtype=np.uint8)
        self.data = []

        for i in range(self.rows):
            for j in range(self.cols):
                # 计算中心坐标和采样区域
                cx = j*col_width + col_width//2
                cy = i*row_height + row_height//2
                radius = int(min(row_height, col_width)*self.r)
                
                # 裁剪子图
                start_row = max(cy-radius, 0)
                end_row = min(cy+radius, height)
                start_col = max(cx-radius, 0)
                end_col = min(cx+radius, width)
                sub_image = image[start_row:end_row, start_col:end_col]
                
                # 调整子图尺寸
                sub_image = cv2.resize(sub_image, (sub_w, sub_h))
                
                # 计算灰度值
                gray = cv2.cvtColor(sub_image, cv2.COLOR_BGR2GRAY)
                avg_gray = float(f"{cv2.mean(gray)[0]:.{self.precision}g}")
                self.data.append(avg_gray)
                text = f"{avg_gray}"

                # ========== 子图文本绘制 ==========
                font = cv2.FONT_HERSHEY_SIMPLEX
                thickness = 1
                
                # 动态字体计算
                base_scale = 0.004
                font_scale = min(sub_w, sub_h) * base_scale
                font_scale = max(0.3, min(font_scale, 1.0))
                
                # 自动换行处理
                (tw, th), baseline = cv2.getTextSize(text, font, font_scale, thickness)
                max_width = sub_w * 0.8
                if tw > max_width:
                    font_scale *= max_width / tw
                    font_scale = max(0.2, font_scale)
                    (tw, th), baseline = cv2.getTextSize(text, font, font_scale, thickness)
                
                # 居中定位
                tx = (sub_w - tw) // 2
                ty = (sub_h + th - baseline) // 2
                cv2.putText(sub_image, text, (tx, ty), 
                          font, font_scale, (0,0,0), thickness, cv2.LINE_AA)
                
                # 放入拼接图
                stitched_img[i*sub_h:(i+1)*sub_h, j*sub_w:(j+1)*sub_w] = sub_image

                # ========== 原始图像标注 ==========
                # 计算采样框坐标
                box_tl_x = int(cx - sub_w/2)
                box_tl_y = int(cy - sub_h/2)
                box_br_x = int(cx + sub_w/2)
                box_br_y = int(cy + sub_h/2)

                # 绘制采样框（蓝色）
                cv2.rectangle(image, (box_tl_x, box_tl_y),
                            (box_br_x, box_br_y), (0,0,255), 2)

                # 使用与子图一致的文本适配逻辑
                box_width = box_br_x - box_tl_x
                box_height = box_br_y - box_tl_y

                # 动态字体计算（基于实际文本长度）
                base_scale = 0.004  # 与子图保持相同基础比例
                text_scale = min(box_width, box_height) * base_scale
                text_scale = max(0.3, min(text_scale, 1.0))  # 字号范围与子图一致

                # 自动换行处理
                (text_w, text_h), baseline = cv2.getTextSize(text, font, text_scale, thickness)
                max_text_width = box_width * 0.8  # 保留20%边距

                # 宽度自适应调整
                if text_w > max_text_width:
                    text_scale *= max_text_width / text_w
                    text_scale = max(0.2, text_scale)  # 最小字号限制
                    (text_w, text_h), baseline = cv2.getTextSize(text, font, text_scale, thickness)

                # 高度二次验证
                max_text_height = box_height * 0.3  # 文本区域不超过框高的30%
                if (text_h + baseline) > max_text_height:
                    text_scale *= max_text_height / (text_h + baseline)
                    text_scale = max(0.2, text_scale)  # 最小字号限制
                    (text_w, text_h), baseline = cv2.getTextSize(text, font, text_scale, thickness)

                # 精确居中定位
                text_x = box_tl_x + (box_width - text_w) // 2
                text_y = box_tl_y + (box_height + text_h - baseline) // 2

                # 边界保护（保留5px安全边距）
                text_x = max(box_tl_x + 5, min(text_x, box_br_x - text_w - 5))
                text_y = min(box_br_y - baseline - 5, max(text_y, box_tl_y + text_h + 5))

                # 绘制红色文本（保持与子图相同的字体参数）
                cv2.putText(image, text, (text_x, text_y),
                        font, text_scale, (0,0,255), int(thickness*1.5), cv2.LINE_AA)

        # ========== 结果保存 ==========
        timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        output_dir = os.path.join('outputs', timestamp)
        os.makedirs(output_dir, exist_ok=True)
        
        # 保存拼接图
        cv2.imwrite(os.path.join(output_dir, 'result.jpg'), stitched_img)
        
        # 生成Excel
        try:
            from openpyxl import Workbook
            self.data = np.array(self.data).reshape((self.rows, self.cols))
            wb = Workbook()
            ws = wb.active
            for i in range(self.rows):
                for j in range(self.cols):
                    ws.cell(row=i+1, column=j+1, value=self.data[i][j])
            wb.save(os.path.join(output_dir, 'data.xlsx'))
        except Exception as e:
            print(f"Excel保存失败: {str(e)}")

        # 结果显示
        if self.image_path:
            cv2.imshow('Analysis Result', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            self.main_window.result_img = image
            self.main_window.basic.display_image(image)

if __name__ == '__main__':
    analyzer = Algorithm()
    analyzer.image_path = r'samples\tests\plate_4x6.png'
    analyzer.count()