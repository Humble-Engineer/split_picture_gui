该代码是基于PySide6的图形用户界面（GUI）应用程序，主要用于图像处理和分割。


# 1. 运行环境

导出环境：conda env export --name 环境名称 > environment.yml

复刻环境：conda env create -f environment.yml
环境名称在yml文件name：中修改

覆盖环境：conda env update --name 环境名称 --file environment.yml

# 2. 打包发布

pyinstaller -F -w --icon=./icons/split.png --distpath ./dist_split_gui --name split_gui main.py

pyinstaller -F -w --icon=./icons/split.png main.py
-w (–windowed / –noconsole): 对于 GUI 应用程序，隐藏控制台窗口。
--icon=FILE.ico: 指定可执行文件的图标。

# 3. 后期更新计划

1、基于正则表达式读取文件信息，获取推荐参数 （ok）
2、设置有效数字滑块，确定有效数字 （ok）

3、用hsv中的v来表示颜色深浅（而不是灰度）
4、显示模块会出现倾斜和不完全显示
