
from ui.MainWindow_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon

import sys, cv2

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

        self.basic = Basic(self)            # 图像基础操作
        # self.camera = Camera(self)          # 相机相关函数
        self.algorithm = Algorithm(self)    # 图像处理相关函数
        # self.mat = MplCanvas(self)          # Matplotlib画布
        self.handler = DataHandler(self)    # 数据存储功能

        self.slot_bind()  # 绑定槽函数
        
        # 设置并显示开屏默认背景及标题
        background = cv2.imread(r'resources\icons\img2.jpg')
        title = '微孔板阵列定量比色系统'
        font = r'resources\fonts\程荣光刻楷.ttf'
        font_size = 160
        color = (0, 0, 0)
        screen = self.basic.put_chinese_text(
            background, title, font, font_size, color)

        self.basic.display_image(screen)
  
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

if __name__ == "__main__":
    # 创建 QApplication 实例
    app = QApplication(sys.argv)
    icon = r'resources\icons\split.png'
    app.setWindowIcon(QIcon(icon))

    # 创建主窗口并显示
    main_window = MainWindow()
    main_window.show()

    # 运行应用程序
    sys.exit(app.exec())