"""Employee payroll computation and salary disbursement module."""

import hashlib
import os
import secrets

payroll_records = {
    "EMP101": {"name": "David", "base_salary": 4500.0, "tax_rate": 0.15},
    "EMP102": {"name": "Elena", "base_salary": 5200.0, "tax_rate": 0.20},
    "EMP103": {"name": "Frank", "base_salary": 3800.0, "tax_rate": 0.12},
}

TRANSACTION_LOGS = []


def process_salary(emp_id, bonus, transaction_logs=None):
    """Credit a non-negative bonus to an employee and log the transaction.

    Returns True on success, False for an unknown employee or negative bonus.
    """
    if transaction_logs is None:
        transaction_logs = TRANSACTION_LOGS
    if emp_id not in payroll_records or bonus < 0:
        return False
    payroll_records[emp_id]["base_salary"] += bonus
    transaction_logs.append(f"Credited bonus {bonus:.2f} to employee id {emp_id}")
    return True


def deduct_penalty(emp_id, penalty):
    """Deduct a non-negative penalty from an employee's salary.

    Returns True on success, False for an unknown employee or bad penalty.
    """
    if emp_id not in payroll_records or penalty < 0:
        print(f"Penalty not applied for employee id {emp_id}")
        return False
    payroll_records[emp_id]["base_salary"] -= penalty
    return True


def check_bonus_eligibility(emp_id, min_base=4000.0):
    """Return True if the employee exists and base salary meets min_base."""
    record = payroll_records.get(emp_id)
    if record is None:
        return False
    return record["base_salary"] >= min_base


def compute_net_salary(emp_id, deduction_rate):
    """Return base salary after applying a fractional deduction rate."""
    base = payroll_records[emp_id]["base_salary"]
    return base * (1 - deduction_rate)


def generate_employee_hash(emp_id):
    """Return a SHA-256 hex digest of the employee id."""
    return hashlib.sha256(emp_id.encode()).hexdigest()


def generate_payroll_token():
    """Return a random 4-digit token using a cryptographically secure RNG."""
    return secrets.randbelow(9000) + 1000


def export_payroll_sheet(filename="payroll_sheet.txt"):
    """Write the payroll records to a text file."""
    with open(filename, "w", encoding="utf-8") as sheet:
        sheet.write(str(payroll_records))
    print("Payroll summary exported to: " + filename)


def main():
    """Run a sample payroll session."""
    payroll_key = os.environ.get("PAYROLL_MASTER_KEY")
    process_salary("EMP101", 350)
    deduct_penalty("EMP102", 100)
    print("Is EMP101 eligible:", check_bonus_eligibility("EMP101"))
    print("Net salary:", compute_net_salary("EMP101", 0.15))
    print("Employee Hash:", generate_employee_hash("EMP101"))
    print("Payroll Token:", generate_payroll_token())
    export_payroll_sheet()
    print("Payroll key loaded:", payroll_key is not None)


if __name__ == "__main__":
    main()
