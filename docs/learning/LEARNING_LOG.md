# 持续学习过程记录

由助手在每次有实质学习进展后更新。记录学习位置与证据，不代写个人理解。

## 如何一起学习

- 一轮聚焦一个概念：解释 → 小例子 → 用户尝试回答 → 反馈 → 必要时实现少量代码。
- 根据回答调整速度；尚未回答或仅听过的内容不记为已掌握。
- 每次记录讲解内容、用户反馈、代码与验证、疑问、下一步。
- 用户自己的总结写在日期日志里；工程完成情况写在 docs/PROGRESS.md。
- 每个小阶段整理一次复习，并把有意义的日志与代码变化同步到私有 GitHub。

## 当前学习位置

Exact-terminal GBM call pricing and 100-repetition validation completed. Following the user's topic discussion, next: explain path averages and build a small validated path-dependent baseline as part of provisional topic exploration. Multi-N comparison remains a useful optional baseline experiment.

## 2026-10-05 — 调整学习节奏，开始 payoff

### 已发生的背景

- 用户明确表示此前不理解项目与助手正在进行的工作；公式讲解和代码实现推进过快。
- 已介绍项目目的，创建私有 GitHub 与个人学习日志。
- Black–Scholes 参考代码已实现并测试；不代表用户已经理解公式或代码。

### 本轮讲解

European call 是到期按 K 买入标的的权利，收益为 max(S_T-K, 0)。payoff 尚未扣除购买合约时的费用，因此不同于净利润。

### 理解检查

K=100 时，分别考虑 S_T=90、100、115：到期收益是多少，是否行权？

用户反馈：“低于100肯定不买入，这个我理解，很简单，继续。”已确认理解低于执行价时放弃行权；未逐项回答其他情形，不额外推断。

### 代码与验证

本轮只更新学习文档，没有增加算法或运行新的数值实验。

### 下一步

先反馈上述答案。如果已理解，再引入一个简单离散随机变量，计算收益的期望；随后解释 Monte Carlo 的样本平均。

## 2026-10-05 — 期望与 Monte Carlo 的直觉

- 根据用户反馈继续，避免重复简单行权问题。
- 本轮讲解：假设 S_T 为 80、100、130，概率分别为 0.25、0.50、0.25。payoff 为 0、0、30，期望收益为 7.5；期望股价为 102.5。先平均股价再算 payoff 会得到 2.5，与平均 payoff 不同。
- Monte Carlo 用按指定概率生成的样本收益平均值估计期望；有限样本有抽样误差。此处概率仅为教学假设，不是现实预测或已指定的风险中性模型；7.5 是到期收益期望，不是今天的期权价格。
- 理解检查：保持同样股价情形，概率改为 0.20、0.40、0.40，计算期望 payoff。用户回复“了解，继续”，未给出数值答案；助手补充参考值 12，并按用户要求推进。
- 代码与验证：仅文档更新，没有增加算法或运行数值实验。
- 下一步：根据回答判断是否进入 NumPy 随机抽样的小段代码。

## 2026-10-06 — 第一段 Monte Carlo 学习代码

- 实现 scripts/learn_discrete_mc.py：default_rng(seed) → choice → maximum → mean。输入分布仅为教学假设，输出是期望到期收益估计，不是当前价格。
- 运行命令：.venv/Scripts/python.exe scripts/learn_discrete_mc.py。Python 3.12.14 / NumPy 2.5.3，CPU / float64；seed=20261006，N=10000，K=100，股价情形 80/100/130，概率 0.2/0.4/0.4。
- 实际输出：频率 0.1979/0.3939/0.4082，估计 12.246，精确参考 12，抽样误差 +0.246。运行成功；样本中 130 的次数为 4082，与 30*4082/10000=12.246 一致。未做性能测量或收敛实验。
- 本轮解释 seed 的可复现用途、样本数组与逐元素 payoff、有限样本频率不同于理论概率。单次偏差不说明系统性高估。
- 用户反馈“ok没问题”，并决定今天结束。解释已获用户认可；未报告独立运行或脱离笔记复述，不推断独立掌握。
- 下一步：用户运行或阅读代码，理解为何 40% 的概率不强制样本中恰好 40%；再学习抽样误差大小。

### Session close — 2026-10-06

- At the user's request, prepared an English personal journal in 2026-10-06-first-monte-carlo.md and linked it from the learning index.
- Included the learning summary, code mapping, assistant-run experiment results, remaining topics, and review questions. No independent user run or full mastery is claimed.
- Stop teaching for today. Resume with sampling error in the same discrete example next session.

## 2026-10-06 — Statistics background, Ito formula, and pricing assumptions

- The user reported AP Statistics and Math 170E background and requested moving past elementary statistics. Use SD, SE and CLT directly, adding explanation only where needed.
- Explained Brownian increments, the GBM SDE, and Ito's formula applied to log S. The user asked specifically what Ito's formula means; explained the second-order correction through Brownian quadratic variation. Independent derivation has not been checked.
- This step connects integration of log GBM to exact terminal sampling and introduces real-world measure P versus risk-neutral measure Q.
- Pricing assumptions: frictionless Black–Scholes market, no dividends, constant r and sigma, continuous trading, no arbitrage and replicability. Under Q, drift is r and discounted stock is a martingale; discounted replicable payoff expectation gives its price. This is not a forecast that actual returns equal r.
- No new code or numerical experiment in this step. Next: implement the exact-terminal GBM sampler in a small, explained step before assembling the pricing estimate.

## 2026-10-07 — User implementation and session close

- User wrote the GBM exponent, initially omitted the 1/2 correction, and corrected it after feedback; clarified that maturity T is measured in years.
- User ran exact terminal sampling, payoff calculation, discounting and SE/CI reporting, providing terminal output for two seeds.
- User refactored to estimate_call after feedback on definition order and duplicate sampling; reproduced the original seed-20261007 result.
- User skipped a manual N-scaling exercise and ran 100 fresh-batch repetitions at N=100000. Results: mean 10.456497450204715, RMSE 0.04660363215782154, mean SE 0.046571302813908415, coverage 0.96.
- Assistant reproduced the final metrics when saving. Minimal cleanup added a main guard, n >= 2 validation, metadata and loop timing; no new method or multi-N experiment.
- Saved the requested English personal journal in 2026-10-07-gbm-pricing.md. User-run evidence is recorded without asserting independent mastery of Ito derivations.
- Next session: multi-N repeated RMSE and cost table. Stop for today.

## 2026-10-07 — Project value and research goals

- User questioned whether mature literature leaves room for undergraduate research and what a non-publishable GitHub project would demonstrate.
- Clarified that established starting methods do not imply no remaining research space. The initial literature screen does not establish an original gap or rule out future contributions.
- A potential research path is faithful reading/reproduction → evidence of a limitation → exclusion of code errors and sampling noise → related-work check → analysis or improvement. Merely claiming a paper is incomplete is insufficient.
- User wants a long-term project with substantive resume/GitHub value and would prefer publication if achievable. A few scripts alone are insufficient; target a complete, reproducible computational study with conclusions, limitations and a report.
- Separate demonstrated implementation/reproduction, interpretable empirical findings, and possible original contributions. No publication promise or claim of established novelty.
- Updated the roadmap with a 4–6 week bounded exploration, deliverable criteria and reassessment rules. Asian finite-budget controls remain a candidate, not a final topic. No new experiment conducted in this discussion.
