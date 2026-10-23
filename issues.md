# Issue Table — employee_payroll_system.py

Line numbers refer to the original file. Sorted by severity.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| `os.system` with string concat (B605) | Security (High) | 58 | Shell command built from `filename`; shell injection possible | Removed the shell call; use `print()` |
| Weak MD5 hash (B324) | Security (High) | 47 | MD5 is broken and unsuitable for security use | Switched to `hashlib.sha256` |
| `eval()` on caller-supplied string (B307 / W0123) | Security (Medium) | 42 | Arbitrary code execution via `deduction_expr` | `compute_net_salary` now takes a numeric `deduction_rate`; `base * (1 - rate)` |
| Hardcoded secret, printed to console | Security (not flagged by tools) | 62, 70 | Master key in source and in output | Read from `PAYROLL_MASTER_KEY` env var; only print whether it is set |
| `random` for payroll token (B311) | Security (Low) | 51 | Predictable PRNG | Use `secrets.randbelow` |
| Bare `except: pass` (B110 / W0702 / E722) | Bug / Security (Low) | 26-27 | Hides every error, including unknown employee ids | Explicit validation, return `False` and report |
| Mutable default arg `transaction_logs=[]` (W0102) | Bug | 15 | Same list shared across all calls | Default `None`; fall back to module-level `TRANSACTION_LOGS` |
| `%d` formatting of bonus | Bug (not flagged) | 19 | Truncates float bonuses (350.75 logged as 350) | f-string with `:.2f` |
| No validation of penalty | Bug (not flagged) | 23-27 | Negative penalty silently *adds* money | Reject negative penalty |
| Runs on import (`main()` at module level) | Bug / Design | 73 | Importing the module executes payroll | `if __name__ == "__main__":` guard |
| `== None` (C0121 / E711) | Style | 32 | Should use identity comparison | `is None` |
| Redundant if/else returning bool (R1703 / R1705) | Style | 34-37 | Verbose | Return the comparison directly |
| Unused variables `statutory_buffer`, `base` (W0612 / F841) | Quality | 31, 41 | Dead code | Removed / now used |
| Unused import `math` (W0611 / F401) | Quality | 6 | Dead import | Removed |
| `open()` without `with` / encoding (R1732 / W1514) | Quality | 55-57 | File may not close on error | `with open(..., encoding="utf-8")` |
| `processSalary` naming (C0103) | Style | 15 | Not snake_case | Renamed `process_salary` |
| Missing docstrings (C0116) | Style | 15-61 | No function documentation | Added docstrings |
| Line too long, 84 > 79 (E501) | Style | 19 | PEP 8 violation | Wrapped the line |
| No newline at EOF (C0304 / W292) | Style | 73 | PEP 8 violation | Added trailing newline |
