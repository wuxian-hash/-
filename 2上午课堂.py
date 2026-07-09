import numpy as np

arr = np.random.randint(0, 10, size=(3, 4))
reshaped_arr = arr.reshape(4, 3).T
filtered_arr = arr[arr > 5]
print("原始数组arr(3,4):\n", arr)
print("reshape(4,3)后转置:\n", reshaped_arr)
print("大于5的元素一维数组:", filtered_arr)


arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("原始数组:\n", arr)
row2_col1_3 = arr[1, 0:3]
all_row_col3 = arr[:, 2]
odd_rows = arr[::2, :]
print("第2行1~3列:", row2_col1_3)
print("全部行第3列:", all_row_col3)
print("奇数行:\n", odd_rows)


A = np.random.randint(1, 10, size=(2, 3))
B = np.random.randint(1, 10, size=(2, 3))
print("数组A:\n", A)
print("数组B:\n", B)
elem_mul = A * B
mat_mul = A @ B.T
print("逐元素相乘 A*B:\n", elem_mul)
print("矩阵相乘 A @ B.T:\n", mat_mul)
test_arr = np.array([[1, 2], [3, 4]])
sum_col = np.sum(test_arr, axis=0)
sum_row = np.sum(test_arr, axis=1)
print("按列求和:", sum_col)
print("按行求和:", sum_row)
float_arr = np.array([1.2, 3.5, 2.8])
mean_val = np.mean(float_arr)
std_val = np.std(float_arr)
round_arr = np.round(float_arr)
print("均值:", mean_val)
print("标准差:", std_val)
print("四舍五入结果:", round_arr)


rand_float = np.random.rand(10)
min_num = rand_float.min()
max_num = rand_float.max()
norm_arr = (rand_float - min_num) / (max_num - min_num) * 100
print("原始0~1随机数组:\n", rand_float)
print("归一化到0~100:\n", norm_arr)
sum_arr = np.cumsum(norm_arr)
max_arr = np.maximum.accumulate(norm_arr)
print("累计和sum:\n", sum_arr)
print("累计最大值max:\n", max_arr)
