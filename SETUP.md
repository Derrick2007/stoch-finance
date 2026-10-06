# 环境与启动

本机项目位置：D:\Codex\stoch-finance。2026-10-05 已迁移并在 D 盘重建 .venv，环境检查通过。在 PowerShell 中先执行 cd D:\Codex\stoch-finance，再运行下面的相对路径命令。项目依赖和实验结果保存在 D 盘；基础 Python 解释器仍使用 Codex 在 C 盘的运行时。

2026-10-05 本机状态：.venv 已创建，依赖已安装。check_environment.py 和 pip check 均通过；版本记录为 Python 3.12.14、NumPy 2.5.3、Matplotlib 3.11.2、pytest 9.1.1。精确依赖见 requirements-lock.txt。当前只是环境验证，尚未完成定价实现或科学实验。

推荐 Python 3.12 + 项目独立 .venv。初期仅 NumPy、Matplotlib、pytest，不需要 PyTorch、GPU 工具链或 C++ 编译器。requirements.txt 给出兼容范围；成功安装后保存 requirements-lock.txt，正式实验使用该环境记录。

## 当前 Windows 电脑

检查发现 python 命令指向 WindowsApps 入口。Codex 自带 Python 3.12.14 可以用于本机启动，但不应将这条机器专属路径作为 GitHub 的公共安装要求。

在项目目录中，首次创建环境：

```powershell
& 'C:\Users\Derek\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts\check_environment.py
.\.venv\Scripts\python.exe -m pip freeze > requirements-lock.txt
```

如果环境已经创建，不必重复创建。这里直接调用环境中的 Python，无需修改 PowerShell 执行策略，也无需激活脚本。

若以后独立于 Codex 使用，安装标准 Python 3.12 后，用该解释器重新创建环境。不要手动编辑虚拟环境的基础解释器路径。

## MacBook 或其他标准 Python 3.12 环境

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/check_environment.py
.venv/bin/python -m pip freeze > requirements-lock.txt
```

前提是已安装 Python 3.12；没有安装时先安装标准发行版，不要用系统自带 Python 随意安装包。可使用现有编辑器；VS Code 可选，将解释器选为这个 .venv 中的 Python。

依赖锁文件记录这次安装的精确版本，跨平台仍需重新安装和验证。两台电脑之间用 Git 同步源代码，而不是同步 .venv。

## 验收

check_environment.py 应输出 Python、NumPy、Matplotlib、pytest 版本，完成固定种子随机数生成，并生成 results/environment-check.png。这验证安装与绘图；科学正确性由后续实验单独验证。
