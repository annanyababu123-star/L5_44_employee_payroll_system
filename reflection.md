# Reflection

**1. Which tool was most useful, and why?**
Bandit was the most valuable. Its two High findings (shell injection via `os.system`, MD5) and the `eval` finding were the real risks in this file. Pylint was the most thorough overall (5.32 to 10.00) and also caught the mutable default argument, a genuine bug. Flake8 was the narrowest, mostly style that Pylint also reported.

**2. Were there false positives or things the tools missed?**
No clear false positives. B311 (`random`) is arguably low risk for a non-secret token, but the token is in a payroll context so fixing it is cheap. The tools missed several real problems: the hardcoded master key that is also printed (Bandit only flags variables named like `password`/`secret`/`token`), `%d` truncating float bonuses, a negative penalty increasing salary, and `main()` running on import. Those needed reading the code and running it.

**3. How did fixing issues affect maintainability?**
Docstrings, snake_case names, the `__main__` guard and removing dead code make the module importable and testable. Replacing `eval` with a numeric rate also made `compute_net_salary` simpler and its inputs well defined. Removing the bare `except` means failures are now visible instead of silent.

**4. How would you use static analysis in a real workflow?**
Run all three in CI on every pull request and fail the build on Bandit High/Medium findings and on a Pylint score below a threshold, plus a pre-commit hook (flake8) for fast feedback locally. Static analysis complements, not replaces, unit tests and code review, since it cannot judge business logic.
