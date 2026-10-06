# 首个学期路线：每周 8 小时

## 工作问题

在指定均方误差目标下，SDE 数值方法、Monte Carlo 与 multilevel 方法怎样分配离散误差和抽样误差，并降低实际计算成本？此问题先作为学习与复现目标，具体原创贡献在 baseline 和文献查重后确定。

## 12 周目标

| 阶段 | 任务 | 交付与理解要求 |
|---|---|---|
| 第 1–2 周 | Brownian increments、GBM 精确抽样、Black–Scholes 与 MC | 可信价格、标准误、重复实验；能解释风险中性期望 |
| 第 3–4 周 | Euler–Maruyama、Milstein；与精确路径使用相同 Brownian increments | strong error 与 weak bias 实验，区分两者 |
| 第 5–6 周 | antithetic 与 control variate | 相同成本下比较方差；control coefficient 用独立 pilot 估计，报告 pilot 成本 |
| 第 7–9 周 | MLMC 的 telescoping identity、coupling、level allocation | fine increments 相加构造 coarse increments；测 V_l、C_l、bias 与总成本 |
| 第 10–12 周 | 一个更合适的 payoff/模型与文献收紧 | 实验报告、可复现 v0.1、选择下一研究问题 |

考试周减量，按实际累计工时推进。前期小型基础项目暂停，8 小时专注旗舰。不要同时增加 Heston、American options、真实数据、ML 和 C++ 重写。

## 学习顺序

条件期望/正态分布 → Brownian motion → Itô 公式的具体应用 → GBM → 风险中性定价 → LLN/CLT 与标准误 → SDE 离散 → MLMC。

不用先读完一本随机微积分教材，但应理解所用公式的假设。MLMC 之前必须掌握共享 Brownian path 的含义。

## 科学评估

- MSE = bias² + variance；一个置信区间只反映抽样不确定性，不能自动覆盖离散 bias。
- Monte Carlo 95% 区间是基于 CLT 的近似，单次没有覆盖解析值不自动说明代码错误。用独立重复研究 RMSE 与覆盖率。
- 准确度目标、payoff、硬件、计时、精度与随机数预算明确记录。
- 初始 GBM call 必须保留精确终值 MC；时间步方法的教学收敛价值与实际定价效率分开讨论。
- 路径依赖 payoff 的监测频率/连续监测定义必须固定，不能把离散监测和连续监测价格混为一谈。
- 每个实验记录 seed、参数、N、dt、耗时、估计、标准误、参考值、代码版本与依赖。

## 后续研究方向：只选一个

1. payoff 光滑程度怎样影响 coupling 与 MLMC 成本；相关已有研究很多，先查重。
2. 某种非线性/随机波动率模型的数值稳定性与误差预算。
3. 某种具体方差缩减方法在失配或有限 pilot 预算下的鲁棒性。

成果先是学习复现、软件和报告；没有证明原创前不宣称新方法，不保证论文发表。
