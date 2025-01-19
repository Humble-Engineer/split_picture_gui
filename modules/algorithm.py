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

        # 判断是在外部调用（有传参）还是末尾测试（无传参）
        if main_window is not None:

            self.rows = self.main_window.rows
            self.cols = self.main_window.cols
            self.r = self.main_window.r
            self.precision = self.main_window.precision

            image = self.main_window.origin_img.copy()

        else:
            image = cv2.imread(self.image_path)

        # print(self.rows, self.cols, self.r, self.precision)

        # 获取图像的高度和宽度
        height, width = image.shape[:2]
        
        # 计算每个小块的高度和宽度
        row_height = height // self.rows
        col_width = width // self.cols
        
        # 绘制水平切割线
        for i in range(1, self.rows):
            cv2.line(image, (0, i * row_height), (width, i * row_height), (255, 0, 0), 2)
        
        # 绘制垂直切割线
        for j in range(1, self.cols):
            cv2.line(image, (j * col_width, 0), (j * col_width, height), (255, 0, 0), 2)
        
        # 绘制每个小方格中的圆的外接正方形
        for i in range(self.rows):
            for j in range(self.cols):
                center_x = j * col_width + col_width // 2
                center_y = i * row_height + row_height // 2
                radius = int(min(row_height, col_width) * self.r)
                top_left_x = center_x - radius
                top_left_y = center_y - radius
                bottom_right_x = center_x + radius
                bottom_right_y = center_y + radius
                cv2.rectangle(image, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), 2)
        
        # 生成基于时间戳的子文件夹名称
        timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        output_folder = f'{timestamp}'

        # 创建输出子文件夹
        output_folder = os.path.join('outputs', output_folder)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # 清空数据
        self.data = []
        # 分割图像
        for i in range(self.rows):
            for j in range(self.cols):
                center_x = j * col_width + col_width // 2
                center_y = i * row_height + row_height // 2
                radius = int(min(row_height, col_width) * self.r)
                
                # 计算圆的边界
                start_row = max(center_y - radius, 0)
                end_row = min(center_y + radius, height)
                start_col = max(center_x - radius, 0)
                end_col = min(center_x + radius, width)
                
                # 裁剪图像
                sub_image = image[start_row:end_row, start_col:end_col]

                # 计算子图的平均灰度值 (R+G+B)/3
                gray_sub_image = cv2.cvtColor(sub_image, cv2.COLOR_BGR2GRAY)
                average_gray_value = cv2.mean(gray_sub_image)[0]
                average_gray_value = float(f'{average_gray_value:.{self.precision}g}')
                self.data.append(average_gray_value)
                text = f'{average_gray_value}'

                # 计算子图的加权灰度值 (a*R+b*G+c*B)/3
                # weights = np.array([0.114, 0.587, 0.299])
                # sub_image_float = sub_image.astype(np.float32)
                # weighted_gray_value = np.dot(sub_image_float[..., :3], weights)
                # average_weighted_gray_value = np.mean(weighted_gray_value)
                # text = f'{average_weighted_gray_value:.{self.precision}g}'

                # 计算子图的平均明度（v）值
                # hsv_sub_image = cv2.cvtColor(sub_image, cv2.COLOR_BGR2HSV)
                # v_channel = hsv_sub_image[:, :, 2]
                # v_channel_average = np.mean(v_channel)
                # text = f'{v_channel_average:.{self.precision}g}'
                
                # 在子图绘制文本
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 0.5
                font_color = (0, 0, 255)
                thickness = 1
                line_type = cv2.LINE_AA

                (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)

                # 计算文本的左上角位置以使其居中
                sub_height, sub_width = sub_image.shape[:2]
                text_x = (sub_width - text_width) // 2
                text_y = (sub_height + text_height) // 2

                # 设置文本位置为子图像的中心
                text_position = (text_x, text_y)

                # 绘制文本
                cv2.putText(sub_image, text, text_position, font, font_scale, font_color, thickness, line_type)

                # 保存分割后的图像
                filename = f'{i+1}-{j+1}.jpg'
                cv2.imwrite(os.path.join(output_folder, filename), sub_image)

        # 如果你需要特定的形状可以调整为：
        self.data = np.array(self.data).reshape((self.rows, self.cols))
        print(self.data)

        print("图像已保存到", output_folder)

        # 显示分割后的图像（调试模式）
        if self.image_path is not None:
            cv2.imshow('Split Image', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # 显示分割后的图像（主窗口模式）
        else:
            self.main_window.result_img = image
            self.main_window.basic.display_image(image)



if __name__ == '__main__':

    algorithm = Algorithm()

    algorithm.image_path = r'samples\plate_4x6.png'

    algorithm.count()