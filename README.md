# Stochastic Simulation & Computational Finance

独立旗舰项目，开始日期 2026-10-05。目标：提升随机过程、数值分析和软件工程能力，形成可复现 GitHub 成果，再根据实验和文献决定是否发展论文。

## 我们研究什么

在指定误差要求下，怎样可靠、高效地计算随机系统的期望量？第一阶段以期权定价为受控例子，随后比较随机数值方法和 Monte Carlo。

这是数值计算研究，不是股票走势预测系统。最初使用合成模型，不需要行情 API、付费数据或真实交易。

## 第一阶段的模型

无股息、常数利率和波动率的风险中性 geometric Brownian motion：

    dS_t = r S_t dt + sigma S_t dW_t
    S_T = S_0 exp((r - sigma²/2)T + sigma sqrt(T) Z), Z ~ N(0,1)
    V = exp(-rT) E[max(S_T-K, 0)]

初始参数：S0=100, K=100, r=0.05, sigma=0.20, T=1。这里 r 是风险中性定价的 drift；不要用历史平均收益率替换它。Black–Scholes call 公式作为价格核查：

    d1 = [ln(S0/K) + (r + sigma²/2)T] / (sigma sqrt(T))
    d2 = d1 - sigma sqrt(T)
    V = S0 Phi(d1) - K exp(-rT) Phi(d2)

范围先限制为 S0,K,T,sigma>0；退化边界随后单独实现和验证。

## 技术路线

- Python 3.12，NumPy，Matplotlib，pytest。
- 前期 CPU、float64；不依赖显卡、ROCm、CUDA 或 PyTorch。
- NumPy Generator 管理随机数；每个实验记录 seed 与参数。
- Python 先实现与验证；有 profiling 证据后再选择一个瓶颈加入 C++。
- 使用独立虚拟环境。Windows 与 Mac 各创建环境，不复制 .venv。

查看 [环境与启动说明](SETUP.md)、[项目路线](docs/PROJECT_PLAN.md)、[第一次学习任务](docs/SESSION_01.md)。

## 环境验证

Windows，在项目文件夹运行：

```powershell
.\.venv\Scripts\python.exe scripts\check_environment.py
```

Mac：

```bash
.venv/bin/python scripts/check_environment.py
```

此脚本只验证环境、随机数和无界面绘图，不是已经完成的定价实验。核心研究代码会按学习步骤逐步实现。

## 第一个可交付成果

精确 GBM 终值抽样 + European call Monte Carlo + 标准误/近似置信区间 + Black–Scholes 对照 + 多次独立重复的误差实验。

随后加入路径离散与 MLMC。GBM vanilla European call 存在精确终值抽样，公平比较时必须保留它；MLMC 不应被预设成更快的方法。路径依赖 payoff 或没有精确抽样的模型才可能体现更明确的优势。

## GitHub

项目使用私有 GitHub 仓库保存代码、文档与学习过程。虚拟环境、大型原始数据和本地缓存不提交。达到第一个可信实验后再整理 v0.1；尚未选定开源许可证。

## 长期学习日志

从[学习日志入口](docs/learning/README.md)开始。每次学习用自己的话总结，记录不理解的地方，并在之后脱离笔记复习。日志模板与代码放在同一仓库，保存学习与修正过程。

## 参考

- [Giles 的 MLMC 研究](https://people.maths.ox.ac.uk/gilesm/mlmc.html)
- [Giles 配套软件](https://people.maths.ox.ac.uk/gilesm/mlmc/)：金融 SDE 算例和多语言实现。只作参考；若采用第三方代码需遵守其许可证并明确归属。
- [Python venv 文档](https://docs.python.org/3/library/venv.html)
