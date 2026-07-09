import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

arr_1d=np.array([1, 2, 3, 4, 5])
print("一维数组：\n", arr_1d, "\n形状：", arr_1d.shape)

arr_2d=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n二维数组：\n", arr_2d, "\n形状：", arr_2d.shape)

arr_3d=np.arange(24).reshape(2, 3, 4)
print("\n三维数组：\n", arr_3d, "\n形状：", arr_3d.shape)

print("\n===== 索引切片演示 =====")
print("一维数组索引第2个元素：", arr_1d[1])
print("一维数组切片[1:4]：", arr_1d[1:4])

print("二维数组取第二行：", arr_2d[1])
print("二维数组取(0,2)位置元素：", arr_2d[0, 2])
print("二维数组前两行前两列：\n", arr_2d[:2, :2])

print("三维数组第一个块：\n", arr_3d[0])
print("\n===== 形状变换 =====")
reshape_arr=arr_1d.reshape(5, 1)
print("一维转二维reshape：\n", reshape_arr)
flatten_arr=arr_2d.flatten()
print("二维展平为一维：", flatten_arr)
transpose_arr=arr_2d.T
print("数组转置：\n", transpose_arr)

def matrix_add(mat1, mat2):
    if mat1.shape!=mat2.shape:
        raise ValueError("两个矩阵维度必须一致才能相加")
    return np.add(mat1, mat2)

def matrix_mul(mat1, mat2):
    if mat1.shape[1]!=mat2.shape[0]:
        raise ValueError("第一个矩阵列数必须等于第二个矩阵行数")
    return np.dot(mat1, mat2)

def matrix_transpose(mat):
    return mat.T

m1=np.array([[1,2],[3,4]])
m2=np.array([[5,6],[7,8]])
print("\n矩阵加法结果：\n", matrix_add(m1, m2))
print("矩阵乘法结果：\n", matrix_mul(m1, m2))
print("矩阵转置结果：\n", matrix_transpose(m1))

rand_data=np.random.normal(loc=50, scale=10, size=100)
print("\n===== 随机数据统计指标 =====")
print("均值：", np.mean(rand_data))
print("中位数：", np.median(rand_data))
print("最大值：", np.max(rand_data))
print("最小值：", np.min(rand_data))
print("方差：", np.var(rand_data))
print("标准差：", np.std(rand_data))

np.random.seed(42)
days=200
stock1=np.cumsum(np.random.randn(days)) + 100
stock2=np.cumsum(np.random.randn(days)) + 105
price_df=np.vstack([stock1, stock2]).T

returns=np.diff(price_df, axis=0) / price_df[:-1]
volatility=np.std(returns, axis=0) * np.sqrt(252)
print("\n股票1年化波动率：", round(volatility[0],4))
print("股票2年化波动率：", round(volatility[1],4))

def moving_average(price_arr, window):
    return np.convolve(price_arr, np.ones(window)/window, mode="valid")

ma5_stock1=moving_average(stock1, 5)
ma20_stock1=moving_average(stock1, 20)

cov_matrix=np.cov(returns.T)
print("\n两只股票协方差矩阵：\n", cov_matrix)
weight=np.array([0.5, 0.5])
port_variance=weight @ cov_matrix @ weight.T
port_std=np.sqrt(port_variance)
print("投资组合方差：", round(port_variance,4))
print("投资组合标准差（组合风险）：", round(port_std,4))
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(12,8))
ax1.plot(stock1, label="股票1收盘价", color="#1f77b4")
ax1.plot(np.arange(4, days), ma5_stock1, label="MA5均线", color="#ff7f0e")
ax1.plot(np.arange(19, days), ma20_stock1, label="MA20均线", color="#2ca02c")
ax1.set_title("股票价格与移动平均线")
ax1.legend()
ax1.grid(alpha=0.3)

ax2.plot(returns[:,0], label="股票1日收益率", alpha=0.7)
ax2.plot(returns[:,1], label="股票2日收益率", alpha=0.7)
ax2.set_title("两只股票日收益率走势")
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()

