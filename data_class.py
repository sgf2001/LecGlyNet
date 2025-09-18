import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

def normal_distribution(x, c, mu, sigma):
    return c/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2))


df = pd.read_csv('six_data.csv',header=None)

for i in range(0,df.shape[0]):
    data = df.iloc[i, :].dropna()
    x = np.linspace(min(data), max(data), 300)
    y = np.histogram(data, bins=300, density=False)[0]
    #设置初始参数
    initial_guess = [50000, 60, 100]
    params, _ = curve_fit(normal_distribution, x, y,bounds=(0,float('inf')),maxfev=float('inf'),p0= initial_guess )
    c, mu, sigma = params

    plt.figure(figsize=(8, 6))
    plt.rcParams["font.family"] = "serif"

    # 绘制直方图
    plt.hist(data, bins=x, alpha=0.5, label="Data Distribution",color='#0C4E9B', density=False)

    # 绘制拟合曲线
    x_fit = np.linspace(min(data), max(data), 1000)  # 平滑曲线的 x 值
    y_fit = normal_distribution(x_fit, c, mu, sigma)
    plt.plot(x_fit, y_fit, color='#F98F34',label="Normal Distribution")

    bounary_12 = [sigma*12,sigma*12]
    plt.plot(bounary_12, [0,30],color='red')

    plt.xlabel('RFU')
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig(f'{i}bar.svg',format='svg')
    plt.show()

