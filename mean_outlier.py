import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===== 新增：解决中文显示问题 =====
plt.rcParams['font.sans-serif'] = ['SimHei']    # Windows 自带黑体，用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False      # 正常显示负号（如果有）
# ================================

# 1) 取更多、跨度更大的 n
n_values = [5, 10, 20, 50, 100, 200, 500,
            1000, 2000, 5000, 10000, 20000, 50000, 100000]

res = []
for n in n_values:
    data = np.full(n, 40.0)
    data[-1] = 10_000_000.0

    mean_val = np.mean(data)
    median_val = np.median(data)
    theory_mean = (40.0 * (n - 1) + 10_000_000.0) / n

    res.append({
        '样本规模(n)': n,
        '受损均值(Mean)': mean_val,
        '受损中位数(Median)': median_val,
        '理论均值': theory_mean
    })

df = pd.DataFrame(res)
print(df.to_string(index=False))

# 2) 作图
plt.figure(figsize=(9, 5))
plt.plot(df['样本规模(n)'], df['受损均值(Mean)'],
         marker='o', label='受损均值 Mean')
plt.plot(df['样本规模(n)'], df['受损中位数(Median)'],
         marker='s', label='受损中位数 Median')
plt.axhline(40, color='gray', linestyle='--', label='真实基准值 40')

plt.xscale('log')
plt.xlabel('样本规模 n（对数刻度）')
plt.ylabel('统计量数值')
plt.title('单个千万级离群值下：均值 vs 中位数 随样本量 n 的变化')
plt.legend()
plt.grid(True, which='both', linestyle=':', alpha=0.6)
plt.show()