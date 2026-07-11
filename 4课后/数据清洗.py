
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

print("="*60)
print("任务1：数据清洗与预处理")
print("="*60)
np.random.seed(42)
n = 200

data = {
    'PassengerId': np.arange(1, n+1),
    'Age': np.random.normal(30, 15, n).astype(int),
    'Fare': np.random.exponential(50, n),
    'Pclass': np.random.choice([1, 2, 3], n, p=[0.2, 0.3, 0.5]),
    'Sex': np.random.choice(['male', 'female'], n, p=[0.6, 0.4]),
    'Embarked': np.random.choice(['S', 'C', 'Q', None], n, p=[0.6, 0.2, 0.15, 0.05]),
    'Survived': np.random.choice([0, 1], n, p=[0.6, 0.4]),
}

df = pd.DataFrame(data)

# 人为添加缺失值
df.loc[np.random.choice(n, 15, replace=False), 'Age'] = np.nan
df.loc[np.random.choice(n, 10, replace=False), 'Fare'] = np.nan
df.loc[np.random.choice(n, 8, replace=False), 'Embarked'] = np.nan

# 人为添加异常值
df.loc[np.random.choice(n, 5, replace=False), 'Age'] = np.random.choice([-10, 150], 5)
df.loc[np.random.choice(n, 3, replace=False), 'Fare'] = np.random.choice([-100, 1000], 3)

# 人为添加重复记录
df_duplicated = df.iloc[:5].copy()
df_duplicated['PassengerId'] = np.arange(201, 206)
df = pd.concat([df, df_duplicated], ignore_index=True)

print(f"原始数据集形状: {df.shape}")
print(f"缺失值统计:\n{df.isnull().sum()}")
print("\n原始数据前5行:")
print(df.head())

print("\n" + "-"*40)
print("1.2 异常值处理")
print("-"*40)

def detect_outliers_iqr(series):
    """使用IQR方法检测异常值"""
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return (series < lower_bound) | (series > upper_bound)

for col in ['Age', 'Fare']:
    outliers = detect_outliers_iqr(df[col])
    print(f"{col}: 检测到 {outliers.sum()} 个异常值")

# 处理异常值：用中位数替换
for col in ['Age', 'Fare']:
    outliers = detect_outliers_iqr(df[col])
    median_val = df[col].median()
    df.loc[outliers, col] = median_val
    print(f"{col}: 异常值已用中位数 {median_val:.2f} 替换")


# 缺失值处理
print("\n" + "-"*40)
print("1.3 缺失值处理")
print("-"*40)

# 方法1：删除缺失值过多的行（阈值：缺失超过2个字段则删除）
df_clean = df.dropna(thresh=df.shape[1] - 2)
print(f"方法1 - 删除缺失过多行后: {df_clean.shape}")

# 方法2：数值列填充中位数
for col in ['Age', 'Fare']:
    df_clean[col] = df_clean[col].fillna(df_clean[col].median())
    print(f"方法2 - {col}: 缺失值已用中位数 {df_clean[col].median():.2f} 填充")

# 方法3：分类列填充众数
mode_val = df_clean['Embarked'].mode()[0]
df_clean['Embarked'] = df_clean['Embarked'].fillna(mode_val)
print(f"方法3 - Embarked: 缺失值已用众数 '{mode_val}' 填充")

# 方法4：插值法（线性插值）
age_before = df_clean['Age'].isnull().sum()
df_clean['Age'] = df_clean['Age'].interpolate(method='linear', limit_direction='both')
age_after = df_clean['Age'].isnull().sum()
print(f"方法4 - Age 插值后缺失值: {age_before} -> {age_after}")

print("\n" + "-"*40)
print("1.4 重复记录处理")
print("-"*40)

duplicates = df_clean.duplicated(subset=['Age', 'Fare', 'Pclass', 'Sex', 'Embarked'])
print(f"检测到重复记录数: {duplicates.sum()}")

df_clean = df_clean.drop_duplicates(subset=['Age', 'Fare', 'Pclass', 'Sex', 'Embarked'], keep='first')
print(f"去重后数据集形状: {df_clean.shape}")

print("\n" + "-"*40)
print("1.5 数据类型转换与格式标准化")
print("-"*40)

print("转换前数据类型:")
print(df_clean.dtypes)

df_clean['Pclass'] = df_clean['Pclass'].astype('category')
df_clean['Sex'] = df_clean['Sex'].astype('category')
df_clean['Embarked'] = df_clean['Embarked'].astype('category')
df_clean['Survived'] = df_clean['Survived'].astype('bool')

scaler = StandardScaler()
df_clean[['Age_std', 'Fare_std']] = scaler.fit_transform(df_clean[['Age', 'Fare']])

print("\n转换后数据类型:")
print(df_clean.dtypes)

print("\n标准化后的Age和Fare统计:")
print(df_clean[['Age_std', 'Fare_std']].describe())


print("\n" + "-"*40)
print("1.6 清洗结果汇总")
print("-"*40)

print(f" 最终数据集形状: {df_clean.shape}")
print("\n清洗后数据前5行:")
print(df_clean.head())

df_clean.to_csv('cleaned_data.csv', index=False)
print("\n 清洗后数据已保存为 'cleaned_data.csv'")

print("\n" + "="*60)
print(" 任务1完成！")
print("="*60)