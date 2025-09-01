from ui.MainWindow_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QIcon

import sys
import cv2
import os
import pandas as pd

from modules.basic import Basic
# from modules.camera import Camera
from modules.algorithm import Algorithm
# from modules.draw import MplCanvas
from modules.record import DataHandler


class MainWindow(QMainWindow):
    """
    主窗口类，用于显示图像。
    """
    def __init__(self):
        """
        初始化主窗口，创建图像显示标签并加载显示用户选择的图像。
        """
        super().__init__()  # 调用父类构造函数

        self.ui = Ui_MainWindow()  # 实例化UI类
        self.ui.setupUi(self)  # 使用UI类的实例设置主窗口的界面

        self.argu_init()  # 参数初始化

        # 初始化RNA类型选项
        self.init_rna_types()

        self.basic = Basic(self)            # 图像基础操作
        # self.camera = Camera(self)          # 相机相关函数
        self.algorithm = Algorithm(self)    # 图像处理相关函数
        # self.mat = MplCanvas(self)          # Matplotlib画布
        self.handler = DataHandler(self)    # 数据存储功能

        # 设置algorithm的RNA_type为当前选中的类型
        self.algorithm.RNA_type = self.ui.type_Box.currentText()

        self.slot_bind()  # 绑定槽函数
        
        # 设置并显示开屏默认背景及标题
        background = cv2.imread('resources/icons/img1.jpeg')
        title = '微孔板阵列定量比色系统'
        font = os.path.join('resources', 'fonts', '程荣光刻楷.ttf')
        font_size = 180
        color = (0, 0, 0)
        screen = self.basic.put_chinese_text(
            background, title, font, font_size, color)

        self.basic.display_image(screen)

    def init_rna_types(self):
        """
        从curve.xlsx文件中读取RNA类型并设置为type_Box的选项
        """
        try:
            excel_path = os.path.join('arguments', 'curve.xlsx')
            if not os.path.exists(excel_path):
                raise FileNotFoundError(f"找不到Excel文件: {excel_path}")
            
            # 读取Excel文件中的所有表名
            sheet_names = pd.ExcelFile(excel_path).sheet_names
            
            # 清空现有的选项
            self.ui.type_Box.clear()
            
            # 添加表名作为选项
            self.ui.type_Box.addItems(sheet_names)
            
            # 注意：此时self.algorithm还未创建，不能设置self.algorithm.RNA_type
            
        except Exception as e:
            # 弹窗报错
            QMessageBox.critical(self, "错误", f"无法读取curve.xlsx文件中的RNA类型:\n{str(e)}")
            sys.exit(1)


    def argu_init(self):
        self.ui.rows_Slider.setValue(1)
        self.ui.cols_Slider.setValue(1)
        self.ui.r_Slider.setValue(5)
        self.ui.precision_Slider.setValue(3)

        self.argu_update_rows()
        self.argu_update_cols()
        self.argu_update_r()
        self.argu_update_precision()

    def argu_update_rows(self):
        self.rows = self.ui.rows_Slider.value()
        self.ui.rows_label.setText(str(self.rows))

    def argu_update_cols(self):
        self.cols = self.ui.cols_Slider.value()
        self.ui.cols_label.setText(str(self.cols))

    def argu_update_r(self):
        self.r = self.ui.r_Slider.value() * 5 / 100
        self.ui.r_label.setText(str(self.r))

    def argu_update_precision(self):
        self.precision = self.ui.precision_Slider.value()
        self.ui.precision_label.setText(str(self.precision))


    def slot_bind(self):
        """
        绑定按钮或菜单项的点击事件到相应的函数。
        """
        # 功能按键绑定的槽函数
        self.ui.load_button.clicked.connect(self.basic.load_image)
        self.ui.save_button.clicked.connect(self.basic.save_image)
        self.ui.reset_button.clicked.connect(self.basic.reset_image)
        
        self.ui.default_button.clicked.connect(self.argu_init)
        self.ui.count_button.clicked.connect(self.algorithm.count)

        # self.ui.capture_button.clicked.connect(self.camera.toggle_thread)

        # 滑块更新相关槽函数
        self.ui.rows_Slider.sliderReleased.connect(self.argu_update_rows)
        self.ui.rows_Slider.sliderMoved.connect(self.argu_update_rows)
        self.ui.rows_Slider.valueChanged.connect(self.argu_update_rows)

        self.ui.cols_Slider.sliderReleased.connect(self.argu_update_cols)
        self.ui.cols_Slider.sliderMoved.connect(self.argu_update_cols)
        self.ui.cols_Slider.valueChanged.connect(self.argu_update_cols)

        self.ui.r_Slider.sliderReleased.connect(self.argu_update_r)
        self.ui.r_Slider.sliderMoved.connect(self.argu_update_r)
        self.ui.r_Slider.valueChanged.connect(self.argu_update_r)

        self.ui.precision_Slider.sliderReleased.connect(self.argu_update_precision)
        self.ui.precision_Slider.sliderMoved.connect(self.argu_update_precision)
        self.ui.precision_Slider.valueChanged.connect(self.argu_update_precision)

        self.ui.type_Box.currentIndexChanged.connect(self.algorithm.argu_update_rna_type)

# ... existing code ...

if __name__ == "__main__":
    # 创建 QApplication 实例
    app = QApplication(sys.argv)
    icon = os.path.join('resources', 'icons', 'split.png')
    app.setWindowIcon(QIcon(icon))

    # 创建主窗口并显示
    main_window = MainWindow()
    main_window.show()

    # 运行应用程序
    sys.exit(app.exec())