# tests 测试目录

本目录存放全书共享的测试，`pytest` 从仓库根目录运行，配置见 `pyproject.toml` 的
`[tool.pytest.ini_options]`。

## 当前内容

| 文件 | 作用 |
|---|---|
| `test_environment.py` | S1 环境验收：解释器为 3.12.9，四个运行时依赖版本与锁定值一致且可导入 |

## 运行方式

```bash
pytest -q
```

## 命名约定

- 文件名 `test_*.py`，函数名 `test_*`，与 `pyproject.toml` 的 `python_files` 保持一致。
- 章内示例的测试放在对应章目录，例如 `ch06/practice/validators/test_solution.py`；
  本目录只放**跨章共享**的测试与环境验收测试。
- 测试只依赖标准库与 `requirements.txt` 中的库，不引入额外测试框架。
