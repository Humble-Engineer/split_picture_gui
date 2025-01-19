import matplotlib.pyplot as plt
import numpy as np
import math

def plot_line_map(data):
    # 获取行列数
    rows, cols = data.shape

    # 获取最大值和最小值
    max_value = np.max(data)
    min_value = np.min(data)

    # 生成 x 轴数据
    x = np.arange(1, cols + 1)

    # 生成图形对象 fig 和 子图对象 ax，使用约束布局避免重叠
    fig, ax = plt.subplots(constrained_layout=True)

    # 定义颜色列表
    colors = plt.cm.viridis(np.linspace(0, 1, len(data)))

    # 遍历每一行数据
    for i, row in enumerate(data):
        # 绘制每行数据的曲线
        ax.plot(x, row, marker="o", color=colors[i], label=f"row_{i+1}")

    # 设置 x 轴和 y 轴的刻度
    ax.set_xticks(x)

    vmin = math.floor(min_value)
    vmax = math.ceil(max_value)
    step = int((vmax - vmin) / 5)
    ax.set_yticks(np.arange(vmin, vmax, step))

    # 设置 x 轴和 y 轴的轴标签，加粗显示
    ax.set_xlabel("x (unit)", fontweight="bold")
    ax.set_ylabel("y (unit)", fontweight="bold")

    # 添加图例
    _ = ax.legend(frameon=False, loc=0, title="", ncol=2)

    # 显示图形
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

    plot_line_map(data)