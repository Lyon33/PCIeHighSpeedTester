# PCIeHighSpeedTester: 面向高速接口芯片（PCIe/CXL/SerDes）的自动化驱动与固件测试框架

**副标题**：支持本地存储加速场景，集成Linux PCIe设备验证与性能回归测试

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/pytest-7%2B-green)](https://pytest.org/)

## 项目简介

PCIeHighSpeedTester 是一个端到端的自动化测试平台，专为高速接口芯片（如 PCIe 4.0/5.0、CXL、SerDes）设计，用于驱动、固件和管理软件的功能、性能、兼容性和稳定性测试。

本项目高度匹配 **芯潮流科技有限公司** “软件测试工程师（高速接口芯片方向）” JD 要求，模拟本地存储加速卡（LSA）场景，支持 NVMe 虚拟化、数据传输等关键测试。

**核心价值**：
- 自动化环境搭建与测试执行，提升测试效率 70%+
- 全面覆盖 PCIe 协议关键点（配置空间、BAR、DMA、MSI-X 等）
- 集成数据分析与可视化报告，助力问题快速定位
- 支持 CI/CD 持续集成

## 快速开始

### 1. 环境要求
- OS: Ubuntu 20.04/22.04 或 CentOS 7/8 (推荐 Ubuntu)
- Python 3.8+
- 硬件：NVMe SSD 或 PCIe 设备（虚拟化也可）
- 工具：lspci, nvme-cli, fio, stress-ng, pciutils

### 2. 一键部署
```bash
git clone https://github.com/yourusername/PCIeHighSpeedTester.git
cd PCIeHighSpeedTester
bash scripts/setup_env.sh
```

### 3. 运行测试
```bash
# 功能测试
python -m pytest tests/functional/ -v --html=reports/report.html

# 性能测试
bash scripts/performance_test.sh
```

## 项目架构

```
PCIeHighSpeedTester/
├── scripts/              # 部署与工具脚本
├── tests/                # 测试用例 (Pytest)
│   ├── functional/       # 功能测试
│   ├── performance/      # 性能测试
│   └── stress/           # 压力测试
├── src/                  # 核心 Python/C 模块
├── tools/                # C 语言底层工具
├── reports/              # 测试报告输出
├── config/               # YAML 配置
├── docs/                 # 文档
├── requirements.txt
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

### 4. 自动化框架
    - YAML 驱动测试用例
    - Pytest + Allure / HTML 报告
    - GitHub Actions CI/CD

### 5. 数据分析
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

## 联系

    - GitHub Issues
    - Demo 视频： [Bilibili/YouTube 链接]

    **本项目为学习与求职作品，模拟真实企业测试场景。**
# PCIeHighSpeedTester
