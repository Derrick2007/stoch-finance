# Literature Screen and Topic Feasibility — 2026-10-07

## Decision summary

Status clarification after the project-goals discussion: this is a screened candidate, not a locked research topic. The next 4–6 weeks combine close reading, baseline implementation and targeted experiments before deciding whether to pursue it. See PROJECT_PLAN.md for deliverable and reassessment criteria.

Provisional recommendation: a bounded computational study of finite-budget control variates for a discretely monitored arithmetic Asian call under risk-neutral GBM. Start as replication and empirical analysis, not a claim of a new algorithm. Do not commit to publication or replace the roadmap before a small feasibility experiment.

Working question: When the total simulation budget includes coefficient estimation, when is an independently pilot-estimated geometric-Asian control coefficient preferable to a fixed coefficient of one?

The simpler question previously suggested (how strike and monitoring count affect plain MC versus geometric control variates) is useful but too close to established material to serve as a novelty claim. Pilot allocation is also studied already. The proposed financial case study may be valuable educationally; originality remains unverified.

## Search and reading scope

Primary sources were searched for Asian pricing, geometric controls, estimated coefficients, pilot allocation, MLMC applications, and human studies of AI scientific ideation. Relevant abstracts, introductions, method passages and experiment passages were screened. This is an initial targeted literature screen, not an exhaustive systematic review or a completed line-by-line reading of every paper. Some publisher full texts were inaccessible; those entries are explicitly limited below. Dates here are document dates, not search-engine crawl dates.

## Source-grounded reading notes

1. **Kemna and Vorst (1990), A pricing method for options based on average asset values.** [Publisher record](https://www.sciencedirect.com/science/article/pii/0378426690900395). Publisher abstract/record screened; full text not inspected. Establishes the classical average-value option pricing setting. The geometric-control attribution is corroborated in Han and Lai and Haugh below. Consequence: Asian control-variate pricing itself is established work.

2. **Martin Haugh, Simulation Efficiency and an Introduction to Variance Reduction Methods.** [Columbia course notes](https://www.columbia.edu/~mh2078/MonteCarlo/MCS_Var_Red_Basic.pdf). Method and Asian example inspected. Teaches an independent pilot for estimating a control coefficient, followed by a main simulation and CI. This is the most accessible first reading for the current skill level. It also demonstrates that estimating a coefficient with pilot data is not new.

3. **Han and Lai, Generalized Control Variate Methods for Pricing Asian Options.** [Author-hosted manuscript](https://mx.nthu.edu.tw/~chhan/gen_AAO.pdf). Abstract, introduction and selected method/conclusion passages inspected; date/version not firmly established from this copy. Discusses geometric-average controls and more general martingale controls, including MC/QMC and stochastic-volatility applications. Consequence: the literature goes well beyond the baseline proposed here. Advanced martingale controls are outside the first implementation scope.

4. **Giles (2008), Multi-level Monte Carlo path simulation.** [Author-hosted paper](https://people.maths.ox.ac.uk/gilesm/files/OPRE_2008.pdf). Method context and Asian example screened. Its Asian example uses a continuous-time average. It provides an established MLMC comparison, but does not justify conflating continuous averaging with a fixed discrete contract. Exact GBM transitions on fixed monitoring dates avoid SDE discretization bias; changing those dates changes the contract. MLMC remains a later option, not a required competitor now.

5. **Gorodetsky et al. (2020), A generalized approximate control variate framework for multifidelity uncertainty quantification.** [Author-hosted paper](https://www.alexgorodetsky.com/static/papers/gorodetsky_et_all_acv_2020.pdf). Estimated-weight experiment screened: pilot cost is included in fixed-budget comparisons. Consequence: uncertainty in fitted control weights and equal-budget evaluation are already part of related work, although its multifidelity setting differs from a known-expectation geometric control.

6. **Coons, Jivani and Huan (2025), Bayesian Covariance Uncertainty for Adaptive Pilot-Sampling Termination in Multi-fidelity Uncertainty Quantification.** [arXiv preprint](https://arxiv.org/abs/2508.18490). Abstract and author research page screened; full technical method not yet read. Addresses the trade-off between covariance accuracy and pilot cost through adaptive termination. Direct warning against presenting pilot-budget optimization as an untouched problem. This preprint is a later comparator, not a method to reproduce immediately.

7. **Si, Yang and Hashimoto (ICLR 2025), Can LLMs Generate Novel Research Ideas?** [Conference paper record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ea94957d81b1c1caf87ef5319fa6b467-Abstract-Conference.html), [author preprint](https://arxiv.org/abs/2409.04109). Abstract screened. In a study with over 100 NLP researchers, AI ideas received higher novelty ratings but somewhat weaker feasibility ratings; self-evaluation and idea diversity were limitations. These are rated proposals in NLP, not proof of successful financial research or current model performance.

8. **Radensky et al., Scideator.** [Full paper](https://arxiv.org/html/2409.14634v3). Abstract, results and limitations inspected. A 19-person CS researcher study evaluated literature-grounded idea generation; authors note small sample, short sessions and domain limits. The primary saved-idea significance depended on excluding an outlier. Supports structured human–AI assistance, not automatic certification of novelty.

## Candidate comparison — project-specific judgment

| Candidate | Fit now | Knowledge burden | Novelty assessment | Decision |
|---|---|---|---|---|
| Plain MC versus geometric Asian control across parameters | High | Low to medium | Established approach; parameter sweeps alone are insufficient | Replication baseline |
| Pilot-estimated versus fixed control at finite total budget | High after baseline | Medium | Related work exists; specific gap not verified | Provisional exploration |
| Asian MLMC with continuous averaging | Later | High | Classical examples already exist | Defer |
| Stochastic volatility, neural controls, or new adaptive algorithms | Low now | High | Requires much deeper comparison and validation | Do not expand scope |

These judgments are not results of a new computational experiment.

## Bounded experiment specification

- Contract: arithmetic Asian call, equal dates t_j=jT/m, j=1,...,m; exclude t=0. Fix this definition for every comparison.
- Model: constant-r, constant-sigma GBM under Q; exact transitions at monitoring dates, CPU/float64.
- Control: discounted geometric-average call payoff on exactly the same dates, with its exact expectation derived and validated first.
- Estimators: plain MC; fixed beta=1; beta estimated on an independent pilot and frozen for the main run.
- Cost: count pilot and main paths, normal draws, and repeated measured runtime. For estimated-beta CV, a budget B allows p pilot paths and B-p main paths; fixed-beta and plain methods can use all B. Account separately for extra control evaluation time.
- Initial scope: one maturity, one volatility, m=12, K=100. Only after validation add m=52 and K=80/120. Later pilot grids could include small fixed counts and a few fractions of B.
- Metrics: estimator variance/MSE, runtime, interval coverage, distribution of fitted beta, and zero/nearly-zero pilot control variance. Define a fallback before evaluating such cases; report its frequency.
- Validate m=1 against the European baseline and validate the geometric formula against independent repetitions. Arithmetic Asian price lacks the current Black–Scholes reference: use a separately seeded high-precision reference with reported uncertainty, or an independently validated numerical method. Reference uncertainty must be substantially below the effects being compared; do not treat a noisy reference as exact.
- Each outer repetition must regenerate both pilot and main samples. CI coverage and MSE must include the randomness of the entire procedure. Begin with fixed production N; avoid optional-stopping complications.
- Distinguish absolute error from relative error for low-price cases. Low payoff frequency may undermine normal approximations; do not add importance sampling immediately.

## Feasibility and stopping rules

Estimated learner time, not measured: 6–10 hours for exact monitoring-path sampling and contract checks; 6–10 hours for geometric pricing/control derivation; 8–12 hours for independent pilot implementation and repeated-budget comparisons; 4–8 hours for interpretation and tighter related-work reading. Total roughly 24–40 hours (3–5 weeks at 8 hours/week), with contingency for debugging. An initial go/no-go check should take about 6–10 learner hours across several sessions. No GPU, C++, external market data or new library is required.

Proceed only if validation passes and equal-cost comparisons expose a stable, explainable effect larger than experiment uncertainty. If beta=1 performs essentially as well everywhere tested, report that honestly; a reproducible negative result is still a useful project outcome. Do not inflate the parameter grid merely to find a favorable plot. If a proposed extension is already covered by related work, retain it as replication or change the question before claiming novelty.

## How AI should assist

Use AI to retrieve and compare primary sources, explain one derivation at a time, identify missing baselines, inspect code and challenge interpretations. The learner should explain the estimand, assumptions, experiment and result without the assistant. Keep a source table separating established facts, project-specific inference and untested conjectures. Seek a knowledgeable human review before calling an extension original. No claim is made that AI can guarantee a publishable topic for a novice.

## Next small learning task

Explain arithmetic versus geometric path averages, then implement one exact GBM monitoring path and inspect it. No Asian/control-variate algorithm was implemented during this literature screen. The proposed topic is provisional; the original roadmap remains available pending the go/no-go check.
