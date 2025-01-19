import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.colors import LinearSegmentedColormap

def plot_heat_map(data):

    # 获取行列数
    rows, cols = data.shape

    # 获取最大值和最小值
    max_value = np.max(data)
    min_value = np.min(data)

    # 动态生成行列名称
    row_names = [f"row_{i+1}" for i in range(rows)]
    col_names = [f"col_{i+1}" for i in range(cols)]

    # 生成图形对象 fig 和 子图对象 ax，使用约束布局避免重叠
    fig, ax = plt.subplots(constrained_layout=True)
    # 设置坐标轴比例
    ax.set_aspect(aspect=1.0)
    
    # 定义自定义 colormap
    colors = ["darkviolet", "darkblue", "green", "lime"]
    custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)

    # 设置坐标轴范围
    im = ax.imshow(data, vmin=math.floor(min_value), vmax=math.ceil(max_value), cmap="viridis")
    # im = ax.imshow(data, vmin=math.floor(min_value), vmax=math.ceil(max_value), cmap=custom_cmap)

    # X轴 和 Y轴 上的标签文字
    ax.set_xticks(np.arange(len(col_names)), labels=col_names, fontweight="bold")
    ax.set_yticks(np.arange(len(row_names)), labels=row_names, fontweight="bold")

    # 添加文字注释
    for i in range(len(row_names)):
        for j in range(len(col_names)):
            text = ax.text(j, i, data[i, j], ha="center", va="center", color="w")

    # 旋转X轴标签文字
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    # 旋转Y轴标签文字
    plt.setp(ax.get_yticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # 添加颜色条
    cbar = fig.colorbar(im, ax=ax, shrink=0.92, aspect=15)
    # 设置颜色条标签
    cbar.set_label("value (unit)", fontweight="bold")

    # 保存图片
    # plt.savefig('./热度图.png', dpi=600)
    # 显示图片
    plt.show()

if __name__ == "__main__":

    # 示例调用
    data = np.array(
        [
            [0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
            [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
            [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
            [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
            [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
            [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
            [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3],
        ]
    )

    plot_heat_map(data)