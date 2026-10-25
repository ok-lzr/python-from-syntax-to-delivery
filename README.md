# 《Python教程：从语法到交付》配套代码

本书面向 Python 新手，从环境安装、语法基础讲起，经模块化、面向对象、异常处理、文件操作、
标准库、类型注解、调试与测试，讲到 NumPy、Matplotlib、Pygame、Socket、Requests 五个常用库，
最后用五个可运行、可测试、可扩展的项目把知识落到交付。

本仓库是全书配套代码：示例、综合实践、项目与测试。三条硬要求：

- **代码可运行**：每个示例独立可运行，输出为 3.12.9 实测结果，不是手写。
- **规范可检查**：PEP 8、行宽 ≤ 88，`ruff`、`black`、`mypy`、`pytest` 全部纳入 CI。
- **项目可完成**：五个项目都有测试、日志、异常处理与扩展任务。

## 环境要求

| 项目 | 要求 |
|---|---|
| Python | **3.12.9**（CPython；`pyproject.toml` 限定 `>=3.12.9,<3.13`） |
| 操作系统 | Windows 10/11、macOS、Linux（CI 在三者上验证） |
| 包管理 | `pip`（随 Python 安装） |
| 编辑器 | PyCharm 社区版（推荐）、VS Code（备选） |
| Git | 2.x |

> 版本不在 3.12.9 时，先按书稿第 1 章与附录 A 卸载旧版并重装。其他 3.12.x 补丁版本可能也能运行示例，
> 但书稿输出以 3.12.9 为准，`pytest` 的环境验收会核对这一版本。

## 30 分钟快速开始

以下命令均在**仓库根目录**执行。

### 1. 获取仓库

```bash
git clone https://github.com/ok-lzr/python-from-syntax-to-delivery.git
cd python-from-syntax-to-delivery
```

### 2. 创建并激活虚拟环境

```bash
python -m venv .venv
```

Windows 命令提示符：

```cmd
.venv\Scripts\activate
```

macOS / Linux：

```bash
source .venv/bin/activate
```

Windows 的 Git Bash / PowerShell：

```bash
source .venv/Scripts/activate
```

激活后提示符前出现 `(.venv)`；退出用 `deactivate`。

### 3. 安装依赖

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

| 文件 | 内容 |
|---|---|
| `requirements.txt` | 运行时依赖：`numpy==2.1.3`、`matplotlib==3.9.2`、`pygame==2.6.1`、`requests==2.32.3` |
| `requirements-dev.txt` | 开发工具：`ruff==0.8.4`、`black==24.10.0`、`mypy==1.13.0`、`pytest==8.3.4`、`pytest-cov==6.0.0`、`pre-commit==4.0.1` |

### 4. 验证环境

```bash
python --version
python -c "print('你好，Python！')"
pytest
```

预期输出（3.12.9 实测）：

```text
Python 3.12.9
你好，Python！
3 passed
```

`pytest` 运行 `tests/test_environment.py`，逐项核对解释器版本、四个运行时依赖的锁定版本与可导入性。
出现 `3 passed` 说明环境就绪；第三方库可能附带弃用警告，不影响结果。

### 5. 跑质量门禁

```bash
ruff check .
black --check .
mypy .
pytest
```

四条命令与 GitHub Actions 中的 CI 一致，本地全绿即代表提交后 CI 大概率绿灯。

## 目录结构

```text
python-from-syntax-to-delivery/
├── .github/
│   ├── ISSUE_TEMPLATE/          # 三个反馈模板：代码失败 / 文字错误 / 版本不一致
│   └── workflows/ci.yml         # 三平台 × Python 3.12.9 的 CI
├── .gitignore                   # 排除 .venv/ 与各类缓存
├── .pre-commit-config.yaml      # 提交前自动 ruff + black
├── pyproject.toml               # 依赖范围与 ruff / black / mypy / pytest 配置
├── requirements.txt             # 运行时依赖（精确锁定）
├── requirements-dev.txt         # 开发工具（精确锁定）
├── ch01/ … ch25/                # 每章的示例、实践与测试，各含 README.md
├── appendix/                    # 附录 A–G 的配套代码
├── tests/                       # 跨章共享的测试与环境验收测试
├── LICENSE                      # MIT
└── README.md
```

章目录与书稿一一对应：`ch01`–`ch02` 准备篇，`ch03`–`ch08` 语言基础篇，`ch09`–`ch15` 进阶能力篇，
`ch16`–`ch20` 常用库篇，`ch21`–`ch25` 项目实战篇。

## 章节索引

| 章 | 标题 | 目录 |
|---|---|---|
| 1 | 安装 Python 3.12.9 与开发环境 | [ch01](ch01/README.md) |
| 2 | 第一个程序与调试入门 | [ch02](ch02/README.md) |
| 3 | 变量、对象与基本类型 | [ch03](ch03/README.md) |
| 4 | 运算符与表达式 | [ch04](ch04/README.md) |
| 5 | 条件与循环 | [ch05](ch05/README.md) |
| 6 | 函数（样章） | [ch06](ch06/README.md) |
| 7 | 容器类型 | [ch07](ch07/README.md) |
| 8 | 字符串与格式化 | [ch08](ch08/README.md) |
| 9 | 文件、路径与异常处理 | [ch09](ch09/README.md) |
| 10 | 模块、包与虚拟环境 | [ch10](ch10/README.md) |
| 11 | 面向对象编程 | [ch11](ch11/README.md) |
| 12 | 迭代器、生成器与装饰器 | [ch12](ch12/README.md) |
| 13 | 标准库精选 | [ch13](ch13/README.md) |
| 14 | 类型注解、测试与代码质量 | [ch14](ch14/README.md) |
| 15 | 并发与异步入门 | [ch15](ch15/README.md) |
| 16 | NumPy：数组与数值计算 | [ch16](ch16/README.md) |
| 17 | Matplotlib：数据可视化入门 | [ch17](ch17/README.md) |
| 18 | Pygame：2D 游戏开发入门 | [ch18](ch18/README.md) |
| 19 | Socket：网络通信基础 | [ch19](ch19/README.md) |
| 20 | Requests：HTTP 客户端入门 | [ch20](ch20/README.md) |
| 21 | 项目一：命令行记账本 | [ch21](ch21/README.md) |
| 22 | 项目二：文件整理与重复检测工具 | [ch22](ch22/README.md) |
| 23 | 项目三：NumPy 成绩分析器 | [ch23](ch23/README.md) |
| 24 | 项目四：Pygame 打砖块小游戏 | [ch24](ch24/README.md) |
| 25 | 项目五：Socket 多人聊天室 | [ch25](ch25/README.md) |
| 附录 A–G | 安装速查、PEP 8、异常排查、依赖策略、参考答案、术语表、学习路线 | [appendix](appendix/README.md) |

## 代码与文档约定

- 示例文件按 `章_节_小节.py` 命名（如 `6_1_1_def.py`），一个文件只放一个小节的最小示例，可直接运行。
- 综合实践放各章 `practice/`，每个实践含 `solution.py` 与 `test_solution.py`。
- 预期报错的示例单独成文件，文件名以 `_error.py` 结尾，顶部注释标明「预期报错」。
- 遵循 PEP 8：4 空格缩进、`snake_case` 命名、行宽 ≤ 88、必要处写类型注解。
- 代码块中的输出一律复制自实际运行结果；报错信息引用原文。
- 章节结构固定为「本节目标 / 主体 / 本节回顾与实践」，跨章引用写「详见第 X 章 X.X 节」。

## 反馈与勘误

发现问题请用对应模板开 Issue：

- [代码运行失败](.github/ISSUE_TEMPLATE/code-failure.md)：示例无法运行或输出与书稿不符。
- [文字或术语错误](.github/ISSUE_TEMPLATE/text-error.md)：正文、术语、交叉引用、标点。
- [版本行为不一致](.github/ISSUE_TEMPLATE/version-issue.md)：示例在 3.12.9 下行为与描述不符。

提交前建议先跑一遍「跑质量门禁」中的四条命令，并在 Issue 中附上 `python --version` 与操作系统。

## 当前进度

S1「环境准备」已完成：仓库骨架、虚拟环境、依赖锁定、代码质量门禁、三平台 CI、Issue 模板与
pre-commit 钩子均已就位，`pytest` 的环境验收测试通过。章节正文与示例按 S2（第 6 章样章）→
S3（其余章节初稿）的顺序陆续入库，各章状态见章目录的 `README.md`。

## 许可证

[MIT](LICENSE)
