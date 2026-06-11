#!/usr/bin/env python
# coding=utf-8
import pytest
import yaml
import subprocess
import os

def load_test_cases():
    with open("config/test_cases.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        return result.returncode == 0, result.stdout + result.stderr
    except:
        return False, "Timeout or error"

@pytest.mark.parametrize("suite", load_test_cases()["test_suites"])
def test_yaml_driven(suite):
    if not suite.get("enabled", True):
        pytest.skip(f"{suite['name']} 已禁用")

    print(f"\n=== 执行测试套件: {suite['name']} ===")
    for case in suite["tests"]:
        print(f"  运行 {case['id']}: {case['name']}")
        success, output = run_command(case["command"])
        print(output[:300])  # 截断输出

        assert case["expected"] in output or success, f"{case['id']} 失败"
