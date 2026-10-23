# Lab 5 Report: Static Code Analysis — Employee Payroll System

**Student:** Annanya Babu (PES1UG24AM045)
**Repo:** https://github.com/SETAPESU26/L5_44_employee_payroll_system

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 5.32 / 10 (21 messages) | 10.00 / 10 |
| Bandit | 5 issues (2 High, 1 Medium, 2 Low) | 0 issues |
| Flake8 | 7 warnings | 0 warnings |

## Commits (one per tool)
1. **Bandit:** removed `eval`, `os.system`, MD5, `random`, hardcoded secret, silent `except`.
2. **Pylint:** docstrings, snake_case rename, mutable default fix, `is None`, simplified conditions, `with open`, unused code, `__main__` guard.
3. **Flake8:** wrapped the over-long line (E501).

Note: the Pylint commit also added the trailing newline and removed the unused import, so Flake8's W292/F401/E722/E711/F841 were already cleared by the earlier commits; only E501 remained for the third.

## Behavioural changes to be aware of
- `processSalary` is now `process_salary`.
- `compute_net_salary(emp_id, deduction_rate)` takes a number (e.g. `0.15`) instead of an expression string, because `eval` had to go. Output is unchanged (4122.5).
- Hash output changed from MD5 to SHA-256.
- `PAYROLL_MASTER_KEY` is read from the environment; the key itself is no longer printed.

## Issue table and reflection
See `issues.md` and `reflection.md`. Reports are in `reports/` (`*_before.txt`, `*_after.txt`).
