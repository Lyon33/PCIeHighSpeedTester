#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
from datetime import datetime

def analyze_fio_results():
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)
    
    # 模拟数据（真实环境会解析 fio json）
    data = {
        'Test_Type': ['Seq_Read', 'Seq_Write', 'Rand_Read'],
        'Bandwidth_MBps': [3200, 2800, 850],
        'IOPS': [25000, 22000, 180000],
        'Latency_ms': [0.08, 0.12, 0.025]
    }
    
    df = pd.DataFrame(data)
    df.to_excel(f"{reports_dir}/performance_report.xlsx", index=False)
    
    # 生成图表
    plt.figure(figsize=(10, 6))
    df.plot(x='Test_Type', y=['Bandwidth_MBps', 'IOPS'], kind='bar')
    plt.title('PCIe/NVMe 性能基准测试 (模拟芯潮流 LSA 场景)')
    plt.ylabel('性能指标')
    plt.grid(True)
    plt.savefig(f"{reports_dir}/performance_trend.png")
    plt.close()
    
    print("✅ 数据分析报告生成完成！")
    print(df)

if __name__ == "__main__":
    analyze_fio_results()
