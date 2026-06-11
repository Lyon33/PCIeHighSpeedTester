#!/bin/bash
# PCIeHighSpeedTester 环境部署脚本

set -e

echo "=== PCIeHighSpeedTester 环境一键部署 ==="

# 更新系统
sudo apt-get update -y || sudo yum update -y

# 安装基础工具
sudo apt-get install -y pciutils nvme-cli fio stress-ng python3-pip git build-essential || \
    sudo yum install -y pciutils nvme-cli fio stress-ng python3-pip git gcc make

# Python 依赖
pip3 install pytest pandas matplotlib seaborn pyyaml openpyxl pytest-html

# 创建目录
mkdir -p logs reports config tests/functional tests/performance tools

echo "=== 环境检查 ==="
lspci | grep -i nvme || echo "No NVMe device detected (virtual OK)"

echo "=== PCIe 设备枚举 ==="
lspci -vvv | head -n 50

echo "部署完成！运行 'bash scripts/run_tests.sh' 开始测试。"
echo "编译 C 寄存器工具..."
cd tools && gcc -o pcie_reg_rw pcie_reg_rw.c -O2 && cd ..
echo "✅ C 工具编译完成: tools/pcie_reg_rw"
