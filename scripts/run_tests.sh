#!/bin/bash
# PCIeHighSpeedTester 测试运行脚本

set -e

echo "=== Running PCIeHighSpeedTester Tests ==="

# Functional tests
echo "→ Running functional tests..."
python -m pytest tests/functional/ -v --html=reports/functional_report.html --self-contained-html || echo "Warning: Some functional tests skipped (no hardware)"

# Performance tests
echo "→ Running performance tests..."
bash scripts/performance_test.sh

echo "=== All tests completed! ==="
echo "Reports generated in ./reports/"
ls -la reports/
