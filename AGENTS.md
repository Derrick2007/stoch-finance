# Project collaboration

This is an independent stochastic simulation and computational finance project. Prioritize the user's mathematical understanding, coding ability, reproducible GitHub outputs, and a future research report. Paper publication is a possibility, not a promised outcome. UCLA lab alignment is not a requirement.

Explain mathematical assumptions and implementation choices in Chinese, preserving useful English terminology. Develop core algorithms in small, understandable steps; do not implement the entire semester plan at once. When asked to teach, explain the current step before extending implementation. Proceed with the specific requested task without repetitive confirmation.

Use README.md for scope, docs/PROJECT_PLAN.md for the roadmap, and docs/PROGRESS.md for current status. Update progress after meaningful work, distinguishing implemented, tested, and proposed work.

Use the project's .venv Python; dependencies are listed in requirements.txt and the installed snapshot in requirements-lock.txt. Start with CPU/float64, NumPy, Matplotlib, and pytest. Add dependencies or C++ components only for a concrete need.

Validate scientific correctness with known solutions and meaningful numerical/statistical checks. Distinguish sampling variance from discretization bias, risk-neutral pricing from real-world dynamics, and theoretical claims from empirical results. Retain exact GBM terminal sampling as a baseline; do not assume MLMC is superior. Record seeds, parameters, environment, timing, and reference values.

Keep virtual environments and large generated data out of Git. Respect third-party licensing and attribute borrowed code. Do not claim novelty without reviewing closely related research. No real-money trading or broker integration is within current project scope.
