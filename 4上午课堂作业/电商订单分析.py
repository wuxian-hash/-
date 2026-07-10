import pandas as pd
import numpy as np

orders = pd.DataFrame({
    'order_id': [f'O{i}' for i in range(100, 118)],  # O100 到 O117，共18个
    'region': ['华东', '华北', '华南', '华东', '西南', '华北', '华南', '华东', '西南',
               '华北', '华南', '华东', '西南', '华北', '华南', '华东', '西南', '华北'],
    'product': ['机械键盘', '无线鼠标', '显示器', '扩展坞', '机械键盘', '显示器', '无线鼠标',
                '显示器', '扩展坞', '机械键盘', '无线鼠标', '扩展坞', '显示器', '机械键盘',
                '扩展坞', '显示器', '无线鼠标', '机械键盘'],
    'category': ['外设', '外设', '显示设备', '配件', '外设', '显示设备', '外设', '显示设备',
                 '配件', '外设', '外设', '配件', '显示设备', '外设', '配件', '显示设备', '外设', '外设'],
    'quantity': [2, 3, 1, 4, 5, 2, 6, 1, 3, 2, 8, 2, 1, 3, 5, 2, 4, 6],
    'unit_price': [289, 129, 1299, 399, 289, 1299, 1299, 1299, 1299, 289, 129, 399, 289, 399, 1299, 1299, 1299, 1298],
    'member_level': ['金卡', '普通', '银卡', '金卡', '银卡', '普通', '金卡', '银卡', '普通',
                     '金卡', '银卡', '普通', '金卡', '银卡', '普通', '金卡', '银卡', '普通'],
    'coupon_rate': [0.05, 0.00, 0.08, 0.10, 0.05, 0.00, 0.1, 2.0, 0.05, 0.00, 0.08, 0.10, 0.05, 0.00, 0.12, 0.05, 0.08, 0.00],
    'salesperson': ['小林', '小周', '小陈', '小林', '小赵', '小周', '小陈', '小林', '小赵',
                    '小周', '小林', '小陈', '小赵', '小周', '小陈', '小林', '小赵', '小周']
})

print("=" * 60)
print("【任务 1：快速理解数据】")
print("=" * 60)

print(f"行数: {orders.shape[0]}, 列数: {orders.shape[1]}")
print(f"所有列名: {list(orders.columns)}")

region_col = orders['region']
three_cols = orders[['order_id', 'product', 'quantity']]
print(f"\nregion 列类型: {type(region_col)}")
print(f"三列类型: {type(three_cols)}")

print("\n第 4~8 行、前 4 列:")
print(orders.iloc[3:8, :4])

print("\n华东地区订单:")
print(orders.loc[orders['region'] == '华东', ['order_id', 'product', 'member_level']])

print("\n为什么推荐 loc?")
print("因为 loc 使用标签索引，不依赖列的位置顺序。当业务发展需要增删列时，")
print("iloc 可能因列位置变化而取错数据，而 loc 按列名取值，代码更健壮、可读性更强。")

print("\n" + "=" * 60)
print("【任务 2：构造订单结算指标】")
print("=" * 60)

analysis = orders.copy()

analysis['gross_amount'] = analysis['quantity'] * analysis['unit_price']

analysis['member_discount'] = np.where(
    analysis['member_level'] == '金卡', 0.10,
    np.where(analysis['member_level'] == '银卡', 0.05, 0.00)
)

analysis['payable_amount'] = analysis['gross_amount'] * (1 - analysis['member_discount']) * (1 - analysis['coupon_rate'])

analysis['shipping_fee'] = np.where(analysis['payable_amount'] >= 1000, 0, 20)

analysis['final_amount'] = analysis['payable_amount'] + analysis['shipping_fee']

analysis[['gross_amount', 'payable_amount', 'final_amount']] = analysis[['gross_amount', 'payable_amount', 'final_amount']].round(2)

print("前 8 行相关字段:")
print(analysis[['order_id', 'gross_amount', 'member_discount', 'payable_amount', 'shipping_fee', 'final_amount']].head(8))

print("\n" + "=" * 60)
print("【任务 3：复杂条件筛选】")
print("=" * 60)

cond1 = analysis['region'].isin(['华东', '华南'])
cond2 = analysis['final_amount'] >= 700
cond3 = (analysis['quantity'] >= 2) | (analysis['member_level'] == '金卡')

mask = cond1 & cond2 & cond3

print("为什么 & 和 | 两侧要加括号?")
print("因为 & 和 | 的优先级高于比较运算符（如 >=、==），")
print("不加括号会导致运算顺序错误。例：'quantity >= 2 & member_level == 金卡'")
print("会被解析为 'quantity >= (2 & member_level) == 金卡'，产生错误结果。")
print("所以必须加括号：'(quantity >= 2) | (member_level == 金卡)'")

focus_orders = analysis.loc[mask, ['order_id', 'region', 'product', 'quantity', 'member_level', 'final_amount']]
focus_orders = focus_orders.sort_values('final_amount', ascending=False)
print("\n重点跟进订单:")
print(focus_orders)

print("\n" + "=" * 60)
print("【任务 4：封装可复用处理函数】")
print("=" * 60)

def add_order_level(df):
    """根据 final_amount 新增 order_level，不修改传入表"""
    df_copy = df.copy()
    df_copy['order_level'] = np.where(
        df_copy['final_amount'] >= 2000, '战略订单',
        np.where(df_copy['final_amount'] >= 1000, '重点订单', '普通订单')
    )
    return df_copy

leveled_orders = analysis.pipe(add_order_level)
print("各等级订单数:")
print(leveled_orders['order_level'].value_counts())

print("\n" + "=" * 60)
print("【任务 5：一条链完成经营汇总】")
print("=" * 60)

region_report = (
    analysis
    .pipe(add_order_level)
    .query('final_amount >= 500')
    .groupby(['region', 'order_level'])
    .agg(
        order_count=('order_id', 'count'),
        quantity_sum=('quantity', 'sum'),
        revenue_sum=('final_amount', 'sum'),
        revenue_mean=('final_amount', 'mean')
    )
    .reset_index()
    .sort_values('revenue_sum', ascending=False)
)

print("地区经营汇总报告:")
print(region_report)

print("\n" + "=" * 60)
print("【任务 6：经营诊断与表达】")
print("=" * 60)

# 1. 哪位销售人员的最终成交金额最高？
sales_total = analysis.groupby('salesperson')['final_amount'].sum()
top_sales = sales_total.idxmax()
top_sales_amount = sales_total.max()

# 2. 该销售人员成交金额最高的地区是什么？
sales_region_total = analysis[analysis['salesperson'] == top_sales].groupby('region')['final_amount'].sum()
top_region = sales_region_total.idxmax()
top_region_amount = sales_region_total.max()

# 3. 该地区金额占该销售人员总成交金额的比例是多少？
contribution = (top_region_amount / top_sales_amount) * 100

print(f"销售人员: {top_sales}")
print(f"核心地区: {top_region}")
print(f"总成交金额: {top_sales_amount:.2f}")
print(f"核心地区金额: {top_region_amount:.2f}")
print(f"地区贡献率: {contribution:.2f}%")

# 业务结论
print(f"{top_sales} 的业绩集中在 {top_region}，该地区贡献了 {contribution:.2f}% 的业绩，")
print(f"建议 {top_sales} 在巩固 {top_region} 市场的同时，将成功经验复制到其他地区。")