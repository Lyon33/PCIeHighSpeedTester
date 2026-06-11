##########################################################################
# File Name: tests/functional/test_pcie_enum.py
# Author: Lyon
# Mail: 786208769@qq.com
# Created Time: 三  6/10 23:33:40 2026
# 🍺🍺🍺 Function is: 
#########################################################################
#!/usr/bin/env python
# coding=utf-8
import subprocess
import pytest

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, 
capture_output=True, text=True)
    return result.returncode == 0, result.stdout + 
result.stderr

def test_pcie_devices():
    """测试 PCIe 设备枚举"""""
    success, output = run_command("lspci | grep -i 'nvme|pci'")
    assert success or "No device" in output, "PCIe 设备枚举失败"
    print("PCIe 设备枚举成功")

def test_pci_config_space():
    """测试配置空间读取"""""
    success, _ = run_command("lspci -xxx | head -c 500")
    assert success, "配置空间读取失败"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

