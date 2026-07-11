
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

print("="*60)
print("任务2：空气质量数据分析")
print("="*60)


df = pd.read_csv('air_quality.csv')
print(f"数据加载成功！形状: {df.shape}")


df = df.dropna(subset=['pm2.5'])
df['datetime'] = pd.to_datetime(df[['year','month','day','hour']].astype(str).agg('-'.join, axis=1))
daily_data = df.groupby(df['datetime'].dt.date).agg({
    'pm2.5':'mean','pm10':'mean','so2':'mean','no2':'mean','co':'mean','o3':'mean'
}).reset_index()
daily_data.columns = ['date','pm25','pm10','so2','no2','co','o3']
daily_data['date'] = pd.to_datetime(daily_data['date'])

print(f"按天聚合后: {daily_data.shape}")


pollutants = ['pm25','pm10','so2','no2','co','o3']
print("\n描述性统计:")
print(daily_data[pollutants].describe())


print("\n相关性矩阵:")
print(daily_data[pollutants].corr())

# 可视化
fig = plt.figure(figsize=(15, 10))

# 图1：PM2.5和PM10
ax1 = plt.subplot(2,3,1)
ax1.plot(daily_data['date'], daily_data['pm25'], label='PM2.5')
ax1.plot(daily_data['date'], daily_data['pm10'], label='PM10')
ax1.set_title('PM2.5与PM10时间序列')
ax1.legend()
ax1.grid(True, alpha=0.3)

# 图2：SO2和NO2
ax2 = plt.subplot(2,3,2)
ax2.plot(daily_data['date'], daily_data['so2'], label='SO2', color='green')
ax2.plot(daily_data['date'], daily_data['no2'], label='NO2', color='orange')
ax2.set_title('SO2与NO2时间序列')
ax2.legend()
ax2.grid(True, alpha=0.3)

# 图3：热力图
ax3 = plt.subplot(2,3,3)
sns.heatmap(daily_data[pollutants].corr(), annot=True, cmap='coolwarm', ax=ax3)
ax3.set_title('相关性热力图')

# 图4：季节箱线图
ax4 = plt.subplot(2,3,4)
daily_data['season'] = daily_data['date'].dt.month.map({12:'冬季',1:'冬季',2:'冬季',3:'春季',4:'春季',5:'春季',6:'夏季',7:'夏季',8:'夏季',9:'秋季',10:'秋季',11:'秋季'})
sns.boxplot(data=daily_data, x='season', y='pm25', ax=ax4, palette='Set2')
ax4.set_title('PM2.5季节分布')
ax4.grid(True, alpha=0.3)

# 图5：散点图
ax5 = plt.subplot(2,3,5)
ax5.scatter(daily_data['pm10'], daily_data['pm25'], alpha=0.5)
ax5.set_xlabel('PM10')
ax5.set_ylabel('PM2.5')
ax5.set_title('PM2.5 vs PM10')
ax5.grid(True, alpha=0.3)

# 图6：趋势图
ax6 = plt.subplot(2,3,6)
daily_data['ma'] = daily_data['pm25'].rolling(7).mean()
ax6.plot(daily_data['date'], daily_data['pm25'], alpha=0.3, label='原始')
ax6.plot(daily_data['date'], daily_data['ma'], label='7天移动平均', color='red')
ax6.set_title('PM2.5趋势')
ax6.legend()
ax6.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('air_quality_analysis.png', dpi=300)
plt.show()

print("\n季节性平均:")
print(daily_data.groupby('season')[pollutants].mean())

print("\n✅ 完成！图表已保存为 air_quality_analysis.png")