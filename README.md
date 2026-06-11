# PCIeHighSpeedTester: 面向高速接口芯片（PCIe/CXL/SerDes）的自动化驱动与固件测试框架

**副标题**：支持本地存储加速场景，集成Linux PCIe设备验证与性能回归测试

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/pytest-7%2B-green)](https://pytest.org/)

## 项目简介

PCIeHighSpeedTester 是一个端到端的自动化测试平台，专为高速接口芯片（如 PCIe 4.0/5.0、CXL、SerDes）设计，用于驱动、固件和管理软件的功能、性能、兼容性和稳定性测试。


**核心价值**：
- 自动化环境搭建与测试执行，提升测试效率 70%+
- YAML 配置驱动测试用例（易扩展）
- Python + C 混合开发
- fio 性能基准 + 数据分析报告（Excel + 图表）助力问题快速定位
- 全面覆盖 PCIe 协议关键点（配置空间、BAR、DMA、MSI-X 等）
- Github CI/CD 全自动回归测试
- 支持云端模拟模式（无硬件也可运行）

## 异常注入测试模块（核心亮点）
---
支持以下异常场景模拟（匹配 JD “问题定位”要求）：
- **热插拔模拟**：设备移除/插入场景
- **AER 错误注入**：链路错误、Corrected/Uncorrectable 错误
- **链路降速 / LTSSM 失败** 模拟
- **驱动鲁棒性验证**：错误恢复能力

**测试日志位置**：`logs/aer_errors.log`、`logs/dmesg_sim.log`

这些测试充分体现了**异常复现与定位能力**，可直接扩展到真实芯片验证。
---

## 核心工具使用

### C 语言寄存器读写工具（tools/pcie_reg_rw）

```bash
# 编译（setup_env.sh 已自动执行）
cd tools && gcc -o pcie_reg_rw pcie_reg_rw.c -O2 && cd ..

# 使用示例
./tools/pcie_reg_rw read 0xf0000000 0x100
./tools/pcie_reg_rw write 0xf0000000 0x04 0x12345678
```
> 功能：模拟芯片BAR 映射、寄存器配置验证、驱动调试

## 快速开始

### 1. 环境要求
- OS: Ubuntu 20.04/22.04 或 CentOS 7/8 (推荐 Ubuntu)
- Python 3.8+
- 硬件：NVMe SSD 或 PCIe 设备（虚拟化也可）
- 工具：lspci, nvme-cli, fio, stress-ng, pciutils

### 2. 一键部署
```bash
git clone https://github.com/Lyon33/PCIeHighSpeedTester.git
cd PCIeHighSpeedTester
bash scripts/setup_env.sh
```

### 3. 运行测试
```bash
# 功能测试
python -m pytest tests/functional/ -v --html=reports/report.html
python src/analyze_results.py

# 性能测试
bash scripts/performance_test.sh

# CXL 模拟测试
python -m pytest tests/test_cxl_simulation.py -m cxl

# Web Dashboard (可视化)
pip install streamlit
streamlit run dashboard.py
```
> 提供交互式可视化：性能图标、CXL状态、异常日志一览

## 项目架构

```
PCIeHighSpeedTester/
├── scripts/              # 部署与工具脚本
├── tests/                # 测试用例 (Pytest)
│   ├── functional/       # 功能测试
│   ├── performance/      # 性能测试
│   └── stress/           # 压力测试
├── src/                  # 核心 Python/C 模块
├── tools/                # 底层寄存器工具
├── reports/              # 测试报告输出
├── config/               # YAML 配置
├── docs/                 # 文档
├── requirements.txt      # 工具库安装列表
├── dashboard.py          # 可视化脚本
├── LICENSE
└── README.md
```

## 核心模块

### 1. 测试环境搭建
    - 自动化安装依赖
    - PCIe 设备枚举与配置验证
    - BAR 映射检查

### 2. 驱动与固件测试
    - 驱动加载/卸载
    - 寄存器读写
    - 异常注入 (热插拔模拟、错误注入)

### 3. 性能测试
    - fio / nvme-cli 基准测试
    - DMA 传输效率
    - 长时间稳定性

### 4. CXL 模拟测试
    - CXL Memory Semantics（缓存一致性）
    - CXL.io 协议模拟
    - 性能影响对比

### 5. 自动化框架
    - YAML 驱动测试用例
    - Pytest + Allure / HTML 报告
    - GitHub Actions CI/CD

### 6. 数据分析
    - pandas + matplotlib 可视化
    - 自动解析 dmesg / lspci 日志
    - Excel/PDF 报告生成

## 测试报告示例

    详见 `reports/` 目录，包含：
    - 执行总结
    - 性能趋势图
    - 错误分布分析
    - 优化建议

## 贡献与开源

    欢迎 PR！项目完全开源，旨在帮助芯片测试从业者。

