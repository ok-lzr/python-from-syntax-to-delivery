# tests/test_environment.py
"""S1 环境验收测试：核对解释器版本与四个运行时依赖的锁定版本。"""

from __future__ import annotations

import importlib
import sys
from importlib.metadata import PackageNotFoundError, version

PYTHON_PIN = (3, 12, 9)
RUNTIME_PINS = {
    "numpy": "2.1.3",
    "matplotlib": "3.9.2",
    "pygame": "2.6.1",
    "requests": "2.32.3",
}


def test_python_version() -> None:
    assert sys.version_info[:3] == PYTHON_PIN, (
        f"需要 Python {'.'.join(map(str, PYTHON_PIN))}，"
        f"当前为 {'.'.join(map(str, sys.version_info[:3]))}"
    )


def test_runtime_dependencies_pinned() -> None:
    for name, expected in RUNTIME_PINS.items():
        try:
            installed = version(name)
        except PackageNotFoundError:
            raise AssertionError(
                f"未安装 {name}，请先执行 pip install -r requirements.txt"
            ) from None
        assert installed == expected, f"{name} 为 {installed}，应锁定为 {expected}"


def test_runtime_dependencies_importable() -> None:
    for name in RUNTIME_PINS:
        module = importlib.import_module(name)
        assert module is not None, f"{name} 无法导入"
