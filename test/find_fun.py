import numpy as np

# y为浓度，x为灰度，先取对数log(y)=f(x)
x = np.array([3.3, 12.33, 20.20, 45, 57.73, 64.67])
y = np.array([0, 1, 2, 3, 4, 5])

coefficients = np.polyfit(x, y, 5)
print(coefficients)

# 给定一个x值，求对应的y值
x_value = 12.33
y_value = np.polyval(coefficients, x_value)

print(f"当灰度={x_value}时，浓度={10**y_value:.2f}")